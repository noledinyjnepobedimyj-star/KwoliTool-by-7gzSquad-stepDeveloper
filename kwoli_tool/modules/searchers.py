"""
Search modules for KWOLI TOOL
Includes IP search, phone lookup, Telegram, Discord, website, etc.
"""

import requests
import socket
import json
import time
import os
import re
from html import unescape
from pathlib import Path
from dotenv import load_dotenv
from kwoli_tool.ui.animation import (
    print_error, 
    print_success, 
    print_info, 
    print_input_field,
    loading_animation
)

# Загрузить .env из корня репозитория
_REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(_REPO_ROOT / ".env")


class IPSearcher:
    """Search information by IP address"""

    @staticmethod
    def search(ip):
        """Search IP information"""
        try:
            loading_animation(1)
            # Using free IP API
            api_url = f"https://ipapi.co/{ip}/json/"
            response = requests.get(api_url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                print_success(f"Информация найдена для IP: {ip}")
                print(f"  Страна: {data.get('country_name', 'N/A')}")
                print(f"  Город: {data.get('city', 'N/A')}")
                print(f"  Регион: {data.get('region', 'N/A')}")
                print(f"  Провайдер: {data.get('org', 'N/A')}")
                print(f"  Координаты: {data.get('latitude', 'N/A')}, {data.get('longitude', 'N/A')}")
                return data
            else:
                print_error("IP не найден или недоступен")
                return None
        except Exception as e:
            print_error(f"Ошибка при поиске: {str(e)}")
            return None


class PhoneSearcher:
    """Search information by phone number using NumVerify API"""

    @staticmethod
    def search(phone):
        """Search phone information using NumVerify API"""
        try:
            loading_animation(1)

            # Получить API ключ из переменной окружения
            api_key = os.getenv('NUMVERIFY_API_KEY')

            if not api_key:
                print_error("❌ Ошибка: NUMVERIFY_API_KEY не установлен в .env файле")
                print_info("👉 Решение: Добавьте в .env файл:")
                print("   NUMVERIFY_API_KEY=c6e9a370bcbf533b5b015ab76e6e22d5")
                print_info("📖 Или зарегистрируйтесь: https://numverify.com/")
                return None

            # URL API NumVerify
            api_url = "https://apilayer.net/api/validate"

            # Очистить номер от нежелательных символов
            phone_clean = ''.join(filter(str.isdigit, phone))

            # Определить страну по началу номера
            if phone_clean.startswith('7') and len(phone_clean) == 11:
                country_code = 'RU'
            else:
                country_code = None

            # Параметры запроса
            params = {
                'access_key': api_key,
                'number': phone_clean,
                'format': 1
            }

            if country_code:
                params['country_code'] = country_code

            # Отправить запрос
            print_info(f"🔍 Поиск информации о номере: {phone}")
            response = requests.get(api_url, params=params, timeout=5)

            if response.status_code == 200:
                data = response.json()

                if data.get('valid'):
                    print_success(f"✅ Номер ВАЛИДЕН: {phone}")
                    print(f"  📍 Страна: {data.get('country_name', 'N/A')}")
                    print(f"  🏢 Оператор: {data.get('carrier', 'N/A')}")
                    print(f"  📱 Тип: {data.get('line_type', 'N/A')}")
                    print(f"  🌍 Международный формат: {data.get('international_format', 'N/A')}")
                    print(f"  🔢 Естественный формат: {data.get('number', 'N/A')}")

                    return {
                        'valid': True,
                        'number': data.get('number'),
                        'country': data.get('country_name'),
                        'carrier': data.get('carrier'),
                        'line_type': data.get('line_type'),
                        'international_format': data.get('international_format'),
                        'price': data.get('price')
                    }
                else:
                    print_error(f"❌ Номер НЕВАЛИДЕН или не найден: {phone}")
                    print_info(f"   Введённый номер: {phone_clean}")
                    return {
                        'valid': False,
                        'number': phone_clean,
                        'error': 'Invalid or not found'
                    }
            else:
                print_error(f"❌ Ошибка API: HTTP {response.status_code}")

                # Обработка специфических ошибок
                if response.status_code == 401:
                    print_error("   API ключ невалиден или истёк")
                elif response.status_code == 429:
                    print_error("   Превышен лимит запросов (max 250/месяц на бесплатном плане)")
                elif response.status_code == 403:
                    print_error("   Доступ запрещён")

                return None

        except requests.exceptions.Timeout:
            print_error("⏱️ Превышено время ожидания подключения (timeout)")
            return None
        except requests.exceptions.ConnectionError:
            print_error("🌐 Ошибка подключения к интернету")
            return None
        except Exception as e:
            print_error(f"❌ Неизвестная ошибка при анализе: {str(e)}")
            return None


class TelegramSearcher:
    """Lookup Telegram users/chats.

    Bot API getChat works for public channels/groups/bots and for people
    who already messaged the bot. Ordinary @username of a person is not
    searchable via getChat — we fall back to the public t.me page.
    """

    _TME_HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "ru,en;q=0.9",
    }

    @staticmethod
    def _api(token, method, params=None, timeout=10):
        url = f"https://api.telegram.org/bot{token}/{method}"
        response = requests.get(url, params=params or {}, timeout=timeout)
        try:
            payload = response.json()
        except ValueError:
            response.raise_for_status()
            raise RuntimeError("Telegram API вернул не-JSON ответ")

        if not payload.get("ok"):
            description = payload.get("description", "неизвестная ошибка")
            error_code = payload.get("error_code", response.status_code)
            raise RuntimeError(f"Telegram API ({error_code}): {description}")
        return payload.get("result")

    @staticmethod
    def _normalize_query(query):
        query = (query or "").strip()
        for prefix in ("https://t.me/", "http://t.me/", "https://telegram.me/", "http://telegram.me/"):
            if query.lower().startswith(prefix):
                query = query.split("/", 3)[-1] if query.count("/") >= 3 else query
                break
        if "t.me/" in query.lower():
            query = query.split("t.me/", 1)[1]
        query = query.split("?")[0].strip("/")
        query = query.lstrip("@")
        if query.lower().startswith("s/"):
            query = query[2:]
        return query or None

    @classmethod
    def _chat_id(cls, query):
        slug = cls._normalize_query(query)
        if not slug:
            return None
        if slug.lstrip("-").isdigit():
            return slug
        return f"@{slug}"

    @staticmethod
    def _field(value, empty="не указано"):
        if value is None or value == "":
            return empty
        if isinstance(value, bool):
            return "да" if value else "нет"
        return value

    @staticmethod
    def _meta_content(html, prop):
        pattern = (
            rf'<meta[^>]+(?:property|name)=["\']{re.escape(prop)}["\'][^>]+'
            rf'content=["\']([^"\']*)["\']'
            rf'|<meta[^>]+content=["\']([^"\']*)["\'][^>]+(?:property|name)=["\']{re.escape(prop)}["\']'
        )
        match = re.search(pattern, html, re.IGNORECASE)
        if not match:
            return None
        return unescape((match.group(1) or match.group(2) or "").strip()) or None

    @staticmethod
    def _tag_text(html, class_name):
        match = re.search(
            rf'class=["\'][^"\']*{re.escape(class_name)}[^"\']*["\'][^>]*>(.*?)</(?:div|span)>',
            html,
            re.IGNORECASE | re.DOTALL,
        )
        if not match:
            return None
        text = re.sub(r"<[^>]+>", " ", match.group(1))
        text = unescape(re.sub(r"\s+", " ", text)).strip()
        return text or None

    @classmethod
    def _split_name(cls, full_name):
        if not full_name:
            return None, None
        cleaned = re.sub(r"\s+[—–-]\s+Telegram\s*$", "", full_name, flags=re.IGNORECASE).strip()
        cleaned = cleaned.strip("@")
        parts = cleaned.split()
        if not parts:
            return None, None
        if len(parts) == 1:
            return parts[0], None
        return parts[0], " ".join(parts[1:])

    @classmethod
    def _public_tme_preview(cls, slug):
        """Public preview from t.me (works for many people/channels without Bot API)."""
        if not slug or slug.lstrip("-").isdigit() or slug.startswith("+"):
            return None

        page = requests.get(
            f"https://t.me/{slug}",
            headers=cls._TME_HEADERS,
            timeout=10,
            allow_redirects=True,
        )
        html = page.text or ""
        if page.status_code == 404 or "this page isn't available" in html.lower():
            return None

        title = cls._tag_text(html, "tgme_page_title") or cls._meta_content(html, "og:title")
        extra = cls._tag_text(html, "tgme_page_extra")
        description = cls._tag_text(html, "tgme_page_description") or cls._meta_content(html, "og:description")
        image = cls._meta_content(html, "og:image")
        og_type = cls._meta_content(html, "og:type")

        if title and title.lower() in {"telegram", "telegram messenger"}:
            title = None

        first_name, last_name = cls._split_name(title)
        kind = "channel_or_group" if extra and re.search(r"subscriber|member|подписчик|участник", extra, re.I) else "user_or_bot"
        if og_type:
            kind = og_type

        looks_valid = bool(title or extra or (description and "If you have Telegram" not in (description or "")))
        if not looks_valid and not extra:
            # t.me still renders a contact card for existing usernames
            if f"@{slug}".lower() not in html.lower() and slug.lower() not in html.lower():
                return None

        return {
            "username": slug,
            "title": title,
            "first_name": first_name,
            "last_name": last_name,
            "extra": extra,
            "bio": description,
            "photo": image,
            "kind": kind,
            "url": f"https://t.me/{slug}",
        }

    @classmethod
    def _print_public_preview(cls, preview):
        print_success("Найдена публичная страница t.me (не Bot API getChat)")
        print(f"  Ссылка: {preview.get('url')}")
        print(f"  Username: @{preview.get('username')}")
        print(f"  Имя: {cls._field(preview.get('first_name'))}")
        print(f"  Фамилия: {cls._field(preview.get('last_name'))}")
        if preview.get("extra"):
            print(f"  Дополнительно: {preview['extra']}")
        print(f"  Номер телефона: недоступен (Telegram не отдаёт чужой номер боту)")
        print(f"  Группы: недоступны (бот не видит чужие чаты)")
        if preview.get("bio"):
            print(f"  Описание: {preview['bio']}")
        if preview.get("photo"):
            print(f"  Фото: {preview['photo']}")
        print_info(
            "getChat у бота работает для публичных каналов/групп/ботов и для тех, "
            "кто уже написал вашему боту. Обычный человек по @username через Bot API не ищется."
        )

    @classmethod
    def _print_bot_chat(cls, token, chat):
        chat_type = chat.get("type", "unknown")
        first_name = chat.get("first_name") or chat.get("title")
        last_name = chat.get("last_name")
        display_username = chat.get("username")
        phone = chat.get("phone_number")

        print_success("Профиль / чат найден через Telegram Bot API")
        print(f"  Тип: {cls._field(chat_type)}")
        print(f"  ID: {cls._field(chat.get('id'))}")
        print(f"  Username: @{display_username}" if display_username else "  Username: не указано")
        print(f"  Имя: {cls._field(first_name)}")
        print(f"  Фамилия: {cls._field(last_name)}")
        print(f"  Номер телефона: {cls._field(phone, 'недоступен через Bot API')}")

        bio = chat.get("bio") or chat.get("description")
        if bio:
            print(f"  Описание / bio: {bio}")
        if chat.get("is_premium") is not None:
            print(f"  Telegram Premium: {cls._field(chat.get('is_premium'))}")
        if chat.get("is_bot") is not None:
            print(f"  Это бот: {cls._field(chat.get('is_bot'))}")

        groups_note = None
        if chat_type in ("group", "supergroup", "channel"):
            member_count = None
            try:
                member_count = cls._api(token, "getChatMemberCount", {"chat_id": chat.get("id")})
            except Exception:
                member_count = None
            print(f"  Название группы/канала: {cls._field(chat.get('title'))}")
            print(f"  Участников: {cls._field(member_count)}")
            groups_note = chat.get("title")
        else:
            print("  Группы: Bot API не отдаёт список групп, в которых сидит человек.")
            print("           Бот видит только чаты, куда его уже добавили.")

        photos_count = None
        if chat_type == "private":
            try:
                photos = cls._api(
                    token,
                    "getUserProfilePhotos",
                    {"user_id": chat.get("id"), "limit": 1},
                )
                photos_count = photos.get("total_count")
                print(f"  Фото профиля: {cls._field(photos_count)}")
            except Exception:
                pass

        return {
            "id": chat.get("id"),
            "type": chat_type,
            "username": display_username,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone,
            "groups": groups_note,
            "bio": bio,
            "photos": photos_count,
            "source": "bot_api",
        }

    @classmethod
    def search(cls, username):
        """Search Telegram user or public chat by username / id / t.me link."""
        try:
            token = (os.getenv("TELEGRAM_BOT_TOKEN") or "").strip()
            if not token:
                print_error("TELEGRAM_BOT_TOKEN не задан в файле .env")
                print_info("Добавьте строку TELEGRAM_BOT_TOKEN=... (токен от @BotFather)")
                return None

            slug = cls._normalize_query(username)
            chat_id = cls._chat_id(username)
            if not chat_id:
                print_error("Введите username, числовой ID или ссылку t.me/...")
                return None

            loading_animation(1)
            print_info(f"Запрос Bot API: getChat {chat_id}")

            try:
                me = cls._api(token, "getMe")
                print_info(f"Бот: @{me.get('username', 'N/A')} ({me.get('first_name', 'N/A')})")
            except Exception as e:
                print_error(f"Токен бота не принят Telegram: {e}")
                return None

            try:
                chat = cls._api(token, "getChat", {"chat_id": chat_id})
                return cls._print_bot_chat(token, chat)
            except Exception as api_error:
                message = str(api_error)
                is_not_found = "chat not found" in message.lower() or "not found" in message.lower()
                if not is_not_found:
                    print_error(f"Ошибка при поиске: {message}")
                    return None

                print_info(
                    "Bot API: chat not found — для обычного человека getChat так и отвечает. "
                    "Пробую публичную страницу t.me..."
                )
                preview = cls._public_tme_preview(slug)
                if preview:
                    cls._print_public_preview(preview)
                    return {**preview, "source": "tme_public"}

                print_error("Аккаунт не найден ни через Bot API, ни на публичной странице t.me")
                print_info(
                    "Проверьте username без пробелов. Приватный аккаунт без публичного @ "
                    "бот найти не может, пока человек сам не напишет боту."
                )
                return None
        except requests.exceptions.Timeout:
            print_error("Превышено время ожидания Telegram API")
            return None
        except requests.exceptions.ConnectionError:
            print_error("Нет соединения с интернетом")
            return None
        except Exception as e:
            print_error(f"Ошибка при поиске: {str(e)}")
            return None


class WebsiteSearcher:
    """Search information by website URL"""

    @staticmethod
    def search(url):
        """Search website information"""
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            loading_animation(1)
            response = requests.head(url, timeout=5, allow_redirects=True)

            print_success(f"Сайт найден: {url}")
            print(f"  HTTP Status: {response.status_code}")
            print(f"  Content-Type: {response.headers.get('Content-Type', 'N/A')}")
            print(f"  Server: {response.headers.get('Server', 'N/A')}")
            print(f"  Last-Modified: {response.headers.get('Last-Modified', 'N/A')}")

            return {"url": url, "status": response.status_code}
        except requests.exceptions.Timeout:
            print_error("Превышено время ожидания подключения")
            return None
        except Exception as e:
            print_error(f"Ошибка при поиске: {str(e)}")
            return None


class NicknameSearcher:
    """Search information by nickname across platforms"""

    @staticmethod
    def search(nickname):
        """Search nickname"""
        try:
            loading_animation(1)
            # Mock search across multiple platforms
            platforms = [
                ('GitHub', f"https://github.com/{nickname}"),
                ('Twitter', f"https://twitter.com/{nickname}"),
                ('Reddit', f"https://reddit.com/user/{nickname}"),
                ('Instagram', f"https://instagram.com/{nickname}"),
            ]

            print_success(f"Поиск никнейма: {nickname}")
            found_count = 0

            for platform, url in platforms:
                try:
                    response = requests.head(url, timeout=3)
                    if response.status_code != 404:
                        print(f"  ✓ {platform}: {url}")
                        found_count += 1
                except:
                    pass

            if found_count == 0:
                print_info("Никнейм не найден на проверенных платформах")

            return {"nickname": nickname, "found": found_count}
        except Exception as e:
            print_error(f"Ошибка при поиске: {str(e)}")
            return None


class DiscordSearcher:
    """Search information by Discord username"""

    @staticmethod
    def search(username):
        """Search Discord user"""
        try:
            loading_animation(1)
            print_info(f"Поиск пользователя Discord: {username}")
            print(f"  Примечание: Полный поиск требует Discord Bot Token")
            print(f"  Вы можете использовать Discord API для этого")

            return {"username": username, "status": "requires_bot_token"}
        except Exception as e:
            print_error(f"Ошибка при поиске: {str(e)}")
            return None


class RobloxSearcher:
    """Search information by Roblox username"""

    @staticmethod
    def search(username):
        """Search Roblox user"""
        try:
            loading_animation(1)
            # Roblox API endpoint
            api_url = f"https://api.roblox.com/users/get-by-username?username={username}"
            response = requests.get(api_url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                if 'Id' in data:
                    print_success(f"Пользователь Roblox найден: {username}")
                    print(f"  ID: {data.get('Id')}")
                    print(f"  Username: {data.get('Username')}")
                    return data
                else:
                    print_error("Пользователь не найден")
            else:
                print_error("Пользователь не найден")

            return None
        except Exception as e:
            print_error(f"Ошибка при поиске: {str(e)}")
            return None


class WebCrawler:
    """Simple web crawler functionality"""

    @staticmethod
    def crawl(url, depth=1):
        """Crawl website"""
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            loading_animation(1)
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                print_success(f"Краулинг начат для: {url}")
                print(f"  Размер содержимого: {len(response.content)} байт")

                # Simple link extraction
                import re
                links = re.findall(r'href=[\'"]?([^\'" >]+)', response.text)
                links = list(set(links))[:10]  # First 10 unique links

                print(f"  Найдено ссылок: {len(links)}")
                for link in links[:5]:
                    print(f"    - {link}")

                return {"url": url, "links_found": len(links)}
            else:
                print_error("Не удалось подключиться к сайту")

            return None
        except Exception as e:
            print_error(f"Ошибка при краулинге: {str(e)}")
            return None
