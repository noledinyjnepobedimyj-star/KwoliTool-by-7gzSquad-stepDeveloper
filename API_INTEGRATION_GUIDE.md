# 🔧 Интеграция API - Практические примеры кода

Полные примеры для подключения каждого API к вашему приложению.

---

## 1. Phone Search - NumVerify API

### Шаг 1: Регистрация и получение ключа

```
1. Перейдите: https://numverify.com/
2. Нажмите "Sign Up"
3. Заполните форму
4. Подтвердите email
5. В личном кабинете скопируйте API Key
```

### Шаг 2: Установка зависимостей

```bash
pip install python-dotenv
```

### Шаг 3: Создание файла .env

```bash
# Создайте файл .env в корне проекта
echo NUMVERIFY_API_KEY=your_key_here > .env
```

### Шаг 4: Обновление кода в kwoli_tool/modules/searchers.py

```python
import os
from dotenv import load_dotenv

load_dotenv()

class PhoneSearcher:
	"""Search information by phone number"""

	@staticmethod
	def search(phone):
		"""Search phone information using NumVerify API"""
		try:
			loading_animation(1)

			# Получить API ключ из переменной окружения
			api_key = os.getenv('NUMVERIFY_API_KEY')

			if not api_key:
				print_error("⚠️ API KEY не настроен в .env файле")
				print_info("📖 Инструкции: смотри API_REQUIREMENTS.md")
				return None

			# URL API NumVerify
			api_url = "https://apilayer.net/api/validate"

			# Параметры запроса
			params = {
				'access_key': api_key,
				'number': phone,
				'country_code': 'RU',  # Россия по умолчанию
				'format': 1
			}

			# Отправить запрос
			response = requests.get(api_url, params=params, timeout=5)

			if response.status_code == 200:
				data = response.json()

				if data.get('valid'):
					print_success(f"✓ Номер валиден: {phone}")
					print(f"  Страна: {data.get('country_name', 'N/A')}")
					print(f"  Оператор: {data.get('carrier', 'N/A')}")
					print(f"  Тип: {data.get('line_type', 'N/A')}")
					print(f"  Международный формат: {data.get('international_format', 'N/A')}")

					return {
						'valid': True,
						'number': data.get('number'),
						'country': data.get('country_name'),
						'carrier': data.get('carrier'),
						'line_type': data.get('line_type'),
						'international_format': data.get('international_format')
					}
				else:
					print_error(f"✗ Номер невалиден: {phone}")
					return {
						'valid': False,
						'number': phone
					}
			else:
				print_error(f"Ошибка API: {response.status_code}")
				return None

		except requests.exceptions.Timeout:
			print_error("Превышено время ожидания подключения")
			return None
		except Exception as e:
			print_error(f"Ошибка при анализе: {str(e)}")
			return None
```

### Шаг 5: Обновление файла requirements.txt

```bash
# Добавить в kwoli_tool/requirements.txt
python-dotenv>=1.0.0
```

### Пример использования

```bash
# В CLI
python run.py
# Выбрать опцию 2 (Phone Search)
# Ввести номер: +7 (495) 123-45-67
```

### Ценовая информация NumVerify

| План | Стоимость | Запросы | Регистрация |
|------|----------|---------|-------------|
| Бесплатный | $0 | 250/месяц | Да |
| Starter | $4.99/мес | 10K/месяц | Да |
| Basic | $9.99/мес | 50K/месяц | Да |
| Professional | $24.99/мес | 250K/месяц | Да |
| Enterprise | Custom | Unlimited | Да |

---

## 2. Telegram Search - Bot API + Client API

### Способ 1: Использование Bot Token (простой, но ограниченный)

```python
import requests

class TelegramSearcher:
	"""Search information by Telegram username using Bot API"""

	@staticmethod
	def search(username):
		"""Search Telegram user"""
		try:
			loading_animation(1)

			bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

			if not bot_token:
				print_error("⚠️ TELEGRAM_BOT_TOKEN не настроен в .env файле")
				print_info("📖 Инструкции:")
				print("  1. Найдите @BotFather в Telegram")
				print("  2. Отправьте /newbot")
				print("  3. Следуйте инструкциям")
				return None

			# Bot API не может напрямую искать пользователей по username
			# Можно только проверить группы/каналы

			api_url = f"https://api.telegram.org/bot{bot_token}"

			# Попытка получить информацию о боте
			response = requests.get(f"{api_url}/getMe", timeout=5)

			if response.status_code == 200:
				bot_info = response.json()
				print_success("✓ Бот подключен")
				print(f"  Username: @{bot_info['result']['username']}")
				print(f"  ID: {bot_info['result']['id']}")
				print(f"  Примечание: Для поиска пользователей нужен Client API")
				return True
			else:
				print_error("Невалидный Bot Token")
				return None

		except Exception as e:
			print_error(f"Ошибка: {str(e)}")
			return None
```

### Способ 2: Использование Pyrogram (полнофункциональный)

```bash
# Установка
pip install pyrogram
```

```python
from pyrogram import Client
import os
from dotenv import load_dotenv

load_dotenv()

class TelegramSearcher:
	"""Search information by Telegram username using Pyrogram"""

	@staticmethod
	def search(username):
		"""Search Telegram user using Pyrogram"""
		try:
			loading_animation(1)

			# Получить учетные данные
			api_id = os.getenv('TELEGRAM_API_ID')
			api_hash = os.getenv('TELEGRAM_API_HASH')
			phone = os.getenv('TELEGRAM_PHONE')

			if not all([api_id, api_hash, phone]):
				print_error("⚠️ Telegram учетные данные не настроены в .env файле")
				print_info("Получите их здесь: https://my.telegram.org/apps")
				return None

			# Создать клиент
			app = Client(
				"kwoli_session",
				api_id=int(api_id),
				api_hash=api_hash
			)

			async def get_user_info():
				async with app:
					try:
						# Получить пользователя по username
						user = await app.get_users(username)

						print_success(f"✓ Пользователь найден: {username}")
						print(f"  ID: {user.id}")
						print(f"  Name: {user.first_name} {user.last_name or ''}")
						print(f"  Username: @{user.username}")
						print(f"  Bio: {user.bio or 'N/A'}")
						print(f"  Verified: {'Да' if user.is_verified else 'Нет'}")

						return {
							'id': user.id,
							'first_name': user.first_name,
							'last_name': user.last_name,
							'username': user.username,
							'bio': user.bio,
							'verified': user.is_verified
						}
					except Exception as e:
						print_error(f"User not found: {username}")
						return None

			# Запустить асинхронный поиск
			import asyncio
			return asyncio.run(get_user_info())

		except Exception as e:
			print_error(f"Ошибка: {str(e)}")
			return None
```

### Получение Telegram API ID и Hash

```
1. Перейдите: https://my.telegram.org/apps
2. Войдите со своим номером телефона
3. Скопируйте API ID и API Hash
4. Добавьте в .env:
   TELEGRAM_API_ID=your_id
   TELEGRAM_API_HASH=your_hash
   TELEGRAM_PHONE=+7XXXXXXXXXX
```

---

## 3. Discord Search - Discord API + discord.py

### Установка

```bash
pip install discord.py
```

### Получение Bot Token

```
1. Перейдите: https://discord.com/developers/applications
2. Log In with Discord
3. Нажмите "New Application"
4. Введите имя приложения
5. Перейдите на вкладку "Bot"
6. Нажмите "Add Bot"
7. Под TOKEN нажмите "Copy"
8. Добавьте в .env:
   DISCORD_BOT_TOKEN=your_token_here
```

### Код интеграции

```python
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

class DiscordSearcher:
	"""Search information by Discord username"""

	@staticmethod
	def search(username):
		"""Search Discord user"""
		try:
			loading_animation(1)

			bot_token = os.getenv('DISCORD_BOT_TOKEN')

			if not bot_token:
				print_error("⚠️ DISCORD_BOT_TOKEN не настроен в .env файле")
				print_info("📖 Инструкции: https://discord.com/developers/applications")
				return None

			# Создать простой клиент
			intents = discord.Intents.default()
			client = discord.Client(intents=intents)

			async def get_user():
				async with client:
					await client.login(bot_token)
					try:
						# Discord не имеет встроенного поиска по username через API
						# Это требует скана серверов или использования неофициального API

						print_info(f"Поиск пользователя: {username}")
						print_error("⚠️ Discord Bot API не поддерживает прямой поиск по username")
						print_info("Альтернативы:")
						print("  1. Использовать ID пользователя")
						print("  2. Подключить бота к своему серверу для скана")
						print("  3. Использовать unofficial API (не рекомендуется)")

						return None
					except Exception as e:
						print_error(f"Error: {str(e)}")
						return None

			import asyncio
			return asyncio.run(get_user())

		except Exception as e:
			print_error(f"Ошибка: {str(e)}")
			return None
```

### Получение информации по ID (работает)

```python
# Если есть ID пользователя
async def get_user_by_id(user_id):
	user = await client.fetch_user(int(user_id))
	return {
		'id': user.id,
		'name': user.name,
		'discriminator': user.discriminator,
		'avatar_url': str(user.avatar.url) if user.avatar else None,
		'created_at': user.created_at,
		'bot': user.bot
	}
```

---

## 4. Файл .env - Пример конфигурации

```env
# NumVerify API (Phone Search)
NUMVERIFY_API_KEY=your_numverify_key_here

# Telegram Bot API
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11

# Telegram Client API (для Pyrogram)
TELEGRAM_API_ID=123456789
TELEGRAM_API_HASH=0123456789abcdef0123456789abcdef
TELEGRAM_PHONE=+79991234567

# Discord Bot API
DISCORD_BOT_TOKEN=your_discord_bot_token_here

# Debug режим (опционально)
DEBUG=False
LOG_LEVEL=INFO
```

### Защита .env файла

```bash
# 1. Создать .gitignore (если не существует)
echo ".env" >> .gitignore
echo ".env.local" >> .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore

# 2. Убедиться, что файл не закоммичен
git rm --cached .env

# 3. Для боевого сервера использовать менеджер секретов
# - AWS Secrets Manager
# - Azure Key Vault
# - HashiCorp Vault
# - Docker Secrets
```

---

## 5. Обновление config.py

```python
# kwoli_tool/config.py

import os
from dotenv import load_dotenv
from colorama import Fore, Style

# Загрузить переменные окружения
load_dotenv()

# API Keys (из переменных окружения)
NUMVERIFY_API_KEY = os.getenv('NUMVERIFY_API_KEY', '')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID', '')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH', '')
TELEGRAM_PHONE = os.getenv('TELEGRAM_PHONE', '')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN', '')

# Debug режим
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# ASCII Logo
ASCII_LOGO = """
[... логотип ...]
"""

# Меню
MENU_ITEMS = [
	"🔍 Поиск по IP",
	"📞 Пробив по номеру (требует NumVerify API)",
	"✈️ Поиск Telegram (требует Bot Token)",
	"🌐 Информация о сайте",
	"🔎 Поиск по никнейму",
	"🎮 Поиск Discord (требует Bot Token)",
	"🎮 Поиск Roblox",
	"🕷️ Краулер сайтов",
	"🔐 Генератор прокси",
	"👤 Генератор фейк-персон",
	"📧 Генератор почт",
	"🔐 Генератор паролей",
	"🚫 Генератор BAN-слов",
	"📚 Руководство по анонимности",
	"🏆 Доска почета",
]

# Сообщения
MESSAGES = {
	'welcome': 'Добро пожаловать в KWOLI TOOL',
	'exit': 'Спасибо за использование KWOLI TOOL!',
}

# Цвета
class Colors:
	GREEN = Fore.GREEN
	RED = Fore.RED
	YELLOW = Fore.YELLOW
	CYAN = Fore.CYAN
	WHITE = Fore.WHITE
	BRIGHT_GREEN = Fore.LIGHTGREEN_EX
	BRIGHT_CYAN = Fore.LIGHTCYAN_EX
	BRIGHT_RED = Fore.LIGHTRED_EX
	BOLD = Style.BRIGHT
	RESET = Style.RESET_ALL
```

---

## 6. Тестирование интеграции

### Скрипт для проверки всех API

```python
# test_api_integration.py

import os
from dotenv import load_dotenv
import requests

load_dotenv()

def test_api_keys():
	"""Test all configured API keys"""

	tests = []

	# 1. Test NumVerify
	print("🧪 Проверка NumVerify API...")
	numverify_key = os.getenv('NUMVERIFY_API_KEY')
	if numverify_key:
		try:
			response = requests.get(
				"https://apilayer.net/api/validate",
				params={
					'access_key': numverify_key,
					'number': '12015550123',
					'format': 1
				},
				timeout=5
			)
			if response.status_code == 200:
				print("  ✓ NumVerify API работает")
				tests.append(True)
			else:
				print("  ✗ NumVerify API ошибка")
				tests.append(False)
		except Exception as e:
			print(f"  ✗ NumVerify Error: {e}")
			tests.append(False)
	else:
		print("  ⚠️ NumVerify API KEY не установлен")
		tests.append(False)

	# 2. Test Telegram Bot
	print("\n🧪 Проверка Telegram Bot API...")
	telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
	if telegram_token:
		try:
			response = requests.get(
				f"https://api.telegram.org/bot{telegram_token}/getMe",
				timeout=5
			)
			if response.status_code == 200:
				print("  ✓ Telegram Bot Token работает")
				tests.append(True)
			else:
				print("  ✗ Telegram Bot Token ошибка")
				tests.append(False)
		except Exception as e:
			print(f"  ✗ Telegram Error: {e}")
			tests.append(False)
	else:
		print("  ⚠️ Telegram Bot Token не установлен")
		tests.append(False)

	# 3. Test ipapi.co (всегда должен работать)
	print("\n🧪 Проверка ipapi.co...")
	try:
		response = requests.get(
			"https://ipapi.co/1.1.1.1/json/",
			timeout=5
		)
		if response.status_code == 200:
			print("  ✓ ipapi.co работает")
			tests.append(True)
		else:
			print("  ✗ ipapi.co ошибка")
			tests.append(False)
	except Exception as e:
		print(f"  ✗ ipapi.co Error: {e}")
		tests.append(False)

	# Результаты
	print("\n" + "="*50)
	passed = sum(tests)
	total = len(tests)
	print(f"Результат: {passed}/{total} API работают ✓")
	print("="*50)

	if passed == total:
		print("🎉 Все API настроены корректно!")
	else:
		print("⚠️ Некоторые API требуют настройки, см. API_REQUIREMENTS.md")

if __name__ == "__main__":
	test_api_keys()
```

### Запуск теста

```bash
python test_api_integration.py
```

---

## 7. Обработка ошибок API

### Стандартные HTTP коды ошибок

```python
def handle_api_error(status_code):
	"""Handle common API errors"""

	errors = {
		400: "Неверные параметры запроса",
		401: "Неавторизированный доступ (ошибка API ключа)",
		403: "Доступ запрещен",
		404: "Ресурс не найден",
		429: "Превышен лимит запросов (rate limit)",
		500: "Внутренняя ошибка сервера",
		502: "Bad Gateway",
		503: "Сервис недоступен",
	}

	return errors.get(status_code, f"Неизвестная ошибка: {status_code}")
```

### Обработка лимитов запросов

```python
import time

class RateLimiter:
	def __init__(self, calls_per_minute=30):
		self.calls_per_minute = calls_per_minute
		self.calls = []

	def wait_if_needed(self):
		now = time.time()
		# Удалить старые вызовы (старше 1 минуты)
		self.calls = [c for c in self.calls if c > now - 60]

		if len(self.calls) >= self.calls_per_minute:
			wait_time = 60 - (now - self.calls[0])
			if wait_time > 0:
				print(f"⏳ Ожидание {wait_time:.1f}с из-за лимита API...")
				time.sleep(wait_time)

		self.calls.append(now)

# Использование
limiter = RateLimiter(calls_per_minute=30)
limiter.wait_if_needed()
response = requests.get(url)
```

---

## 📝 Итоговый чек-лист интеграции

- [ ] Установить зависимости: `pip install -r kwoli_tool/requirements.txt`
- [ ] Установить python-dotenv: `pip install python-dotenv`
- [ ] Создать файл `.env` в корне проекта
- [ ] Получить NumVerify API Key (опционально, для Phone Search)
- [ ] Получить Telegram Bot Token (опционально, для Telegram)
- [ ] Получить Discord Bot Token (опционально, для Discord)
- [ ] Добавить ключи в `.env` файл
- [ ] Добавить `.env` в `.gitignore`
- [ ] Обновить `kwoli_tool/config.py`
- [ ] Обновить `kwoli_tool/modules/searchers.py`
- [ ] Запустить тест: `python test_api_integration.py`
- [ ] Протестировать каждую функцию: `python run.py`

---

## 🔗 Полезные ссылки

| Сервис | Ссылка |
|--------|--------|
| NumVerify | https://numverify.com/ |
| Telegram Bot | https://core.telegram.org/bots |
| Discord Developer | https://discord.com/developers/applications |
| ipapi.co | https://ipapi.co/ |
| Roblox API | https://api.roblox.com |
| Pyrogram | https://docs.pyrogram.org/ |
| discord.py | https://discordpy.readthedocs.io/ |
| python-dotenv | https://github.com/theskumar/python-dotenv |

---

*Справочник по интеграции API для KWOLI TOOL*  
*Версия 1.0*  
*Последнее обновление: 2024*
