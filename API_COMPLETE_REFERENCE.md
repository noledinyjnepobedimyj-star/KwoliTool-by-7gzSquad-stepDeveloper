# 📚 ПОЛНЫЙ СПРАВОЧНИК API ДЛЯ KWOLI TOOL

## 🎯 СВОДНАЯ ТАБЛИЦА ПО ФУНКЦИЯМ

```
ФУНКЦИЯ                  СТАТУС    API/БИБЛИОТЕКА        ТИП          ЛИМИТ
────────────────────────────────────────────────────────────────────────────
1. IP Search             ✅        ipapi.co              Бесплатный   30K/мес
2. Phone Search          ⚠️        NumVerify             Платный      250/мес*
3. Telegram Search       ⚠️        Bot API               Бесплатный   ∞
4. Website Search        ✅        requests (встроенный) Бесплатный   ∞
5. Nickname Search       ✅        requests (встроенный) Бесплатный   ∞
6. Discord Search        ⚠️        Discord Bot API       Бесплатный   ∞
7. Roblox Search         ✅        api.roblox.com        Бесплатный   ∞
8. Web Crawler           ✅        requests (встроенный) Бесплатный   ∞
9. Proxy Generator       ✅        встроенный            Бесплатный   ∞
10. Fake Person          ✅        faker (установлена)   Бесплатный   ∞
11. Email Generator      ✅        встроенный            Бесплатный   ∞
12. Password Generator   ✅        встроенный            Бесплатный   ∞
13. Ban Word Generator   ✅        встроенный            Бесплатный   ∞
14. Anonymity Manual     ✅        встроенный            Бесплатный   ∞
15. Hall of Fame         ✅        встроенный            Бесплатный   ∞
────────────────────────────────────────────────────────────────────────────
* 250 запросов в месяц бесплатно (есть платные планы от $4.99/мес)
```

---

## 🔴 СРОЧНЫЕ ТРЕБОВАНИЯ (ДЛЯ ПОЛНОЙ РАБОТЫ)

### ⚙️ ОБЯЗАТЕЛЬНО установить Python пакеты:

| Пакет | Версия | Команда | Статус |
|-------|--------|---------|--------|
| requests | >=2.31.0 | `pip install requests` | ✅ Установлен |
| colorama | >=0.4.6 | `pip install colorama` | ✅ Установлен |
| faker | >=15.0.0 | `pip install faker` | ✅ Установлен |
| python-dotenv | >=1.0.0 | `pip install python-dotenv` | ❌ Требуется |

### 🔐 ОПЦИОНАЛЬНО для расширенной функциональности:

| Пакет | Для чего | Команда |
|-------|----------|---------|
| beautifulsoup4 | Лучший парсинг HTML | `pip install beautifulsoup4` |
| lxml | Парсер для BS4 | `pip install lxml` |
| pyrogram | Полноценный Telegram поиск | `pip install pyrogram` |
| discord.py | Полноценный Discord API | `pip install discord.py` |
| telethon | Альтернатива Pyrogram | `pip install telethon` |

---

## 📌 ДЕТАЛЬНЫЕ ДАННЫЕ ПО КАЖДОМУ API

### 1️⃣ ipapi.co - IP Search

```
┌─ Название: ipapi.co
├─ Сайт: https://ipapi.co/
├─ Документация: https://ipapi.co/api/
├─ Метод: GET HTTPS
├─ Бесплатно: ДА
├─ Регистрация: НЕ требуется
├─ API Key: НЕ требуется
├─ Лимиты: 30,000 запросов/месяц
├─ Задержка: обычно < 100 мс
├─ Тип данных: JSON
└─ Информация: страна, город, регион, провайдер, координаты

Пример URL:
https://ipapi.co/1.1.1.1/json/

Ответ (JSON):
{
  "ip": "1.1.1.1",
  "version": "IPv4",
  "city": "Los Angeles",
  "region": "California",
  "region_code": "CA",
  "country_name": "United States",
  "country_code": "US",
  "continent_name": "North America",
  "continent_code": "NA",
  "latitude": 34.0522,
  "longitude": -118.2437,
  "asn": "AS13335",
  "postal": "90001",
  "calling_code": "1",
  "gmt_offset": "-07:00",
  "timezone": "America/Los_Angeles",
  "isp": "Cloudflare",
  "org": "CLOUDFLARENET",
  "is_vpn": false
}

Текущее состояние: ✅ РАБОТАЕТ
```

### 2️⃣ NumVerify - Phone Search

```
┌─ Название: NumVerify
├─ Сайт: https://numverify.com/
├─ Документация: https://numverify.com/documentation
├─ Метод: GET/POST HTTPS
├─ Бесплатно: ДА (250/месяц)
├─ Регистрация: ТРЕБУЕТСЯ (email)
├─ API Key: ТРЕБУЕТСЯ (получите на сайте)
├─ Платные планы: от $4.99/месяц до $499.99/месяц
├─ Упор на валидацию и операторов мобильных сетей
├─ Тип данных: JSON
└─ Информация: валидность, страна, оператор, тип (мобильный/стационарный)

Регистрация:
1. https://numverify.com/auth/sign-up
2. Заполнить форму (email, пароль)
3. Подтвердить email
4. Войти в аккаунт
5. Скопировать API Key из личного кабинета

Пример запроса:
GET https://apilayer.net/api/validate?access_key=YOUR_KEY&number=12015550123&format=1

Параметры:
- access_key: ваш API ключ (обязательно)
- number: номер телефона (обязательно)
- country_code: код страны ISO (опционально)
- format: 1 для JSON (опционально)

Ответ (JSON):
{
  "valid": true,
  "format": "+1 201-555-0123",
  "international_format": "+12015550123",
  "country_prefix": "+1",
  "country_name": "United States",
  "country_code": "US",
  "carrier": "Verizon",
  "line_type": "mobile",
  "error": false
}

Ценовая таблица:
╔════════════════╦═════════╦═════════════╗
║ План           ║ Цена    ║ Запросы     ║
╠════════════════╬═════════╬═════════════╣
║ Бесплатный     ║ $0      ║ 250/месяц   ║
║ Starter        ║ $4.99   ║ 10K/месяц   ║
║ Basic          ║ $9.99   ║ 50K/месяц   ║
║ Professional   ║ $24.99  ║ 250K/месяц  ║
║ Enterprise     ║ Custom  ║ Unlimited   ║
╚════════════════╩═════════╩═════════════╝

Текущее состояние: ⚠️ НЕ ИНТЕГРИРОВАНО
Требуется: API ключ + код интеграции
```

### 3️⃣ Telegram Bot API

```
┌─ Название: Telegram Bot API
├─ Сайт: https://core.telegram.org/bots
├─ Документация: https://core.telegram.org/bots/api
├─ Метод: GET/POST HTTPS
├─ Бесплатно: ДА
├─ Регистрация: ТРЕБУЕТСЯ (номер телефона)
├─ Bot Token: ТРЕБУЕТСЯ (@BotFather)
├─ Лимиты: ~30-50 запросов в секунду
├─ Тип данных: JSON
└─ Информация: информация о боте, сообщения, файлы

Как получить Bot Token:
1. Открыть Telegram
2. Найти пользователя: @BotFather
3. Отправить: /newbot
4. Следовать инструкциям (название, username)
5. Получить TOKEN вида: 123456789:ABCDEFGHIJKLMNOPQRSTUVWxyz123456789

Пример Token:
5368145236:AAEQTWr-BTp3z4_mKZdBvZjBwP9K5nM1Z9E

Основные endpoints:
GET /getMe - информация о боте
GET /getUpdates - получить сообщения
POST /sendMessage - отправить сообщение
GET /getUserProfilePhotos - фото профиля пользователя
GET /getFile - получить файл

Пример использования:
https://api.telegram.org/bot{BOT_TOKEN}/getMe

Ответ:
{
  "ok": true,
  "result": {
	"id": 123456789,
	"is_bot": true,
	"first_name": "MyBot",
	"username": "mybotusername",
	"can_join_groups": true,
	"can_read_all_group_messages": false
  }
}

Ограничения Bot API:
- Не может искать пользователей по username
- Не может получать все сообщения из группы
- Видит только сообщения, адресованные боту
- Требует явного добавления в группу

Для полноты нужен Client API (Pyrogram/Telethon):
pip install pyrogram
pip install telethon

Текущее состояние: ⚠️ ЧАСТИЧНО ИНТЕГРИРОВАНО
Требуется: Bot Token + Client API для поиска
```

### 4️⃣ Discord Bot API

```
┌─ Название: Discord Bot API
├─ Сайт: https://discord.com/developers/applications
├─ Документация: https://discord.com/developers/docs
├─ Метод: GET/POST HTTPS (WebSocket для real-time)
├─ Бесплатно: ДА
├─ Регистрация: ТРЕБУЕТСЯ (Discord аккаунт)
├─ Bot Token: ТРЕБУЕТСЯ (создается в devportal)
├─ Лимиты: различные в зависимости от endpoint
├─ Тип данных: JSON
└─ Информация: пользователи, серверы, сообщения

Как получить Bot Token:
1. Перейти: https://discord.com/developers/applications
2. Войти (Discord login)
3. Нажать "New Application"
4. Дать имя приложению
5. Перейти на вкладку "Bot"
6. Нажать "Add Bot"
7. Нажать "Copy" под Token
8. Сохранить токен надежно

Пример Token:
MTk4NjIyNzk3MzIwODI1Nzky.Clwa7A.7a6KfJz9FMjMbFI1z_z8DWjR0cc

Основные endpoints:
GET /users/@me - информация о боте
GET /users/{id} - информация о пользователе
GET /users/{id}/profile - профиль пользователя
GET /guilds/{id} - информация о сервере
GET /channels/{id} - информация о канале

Ограничения:
- Не может искать пользователей по username напрямую
- Нужно быть добавленным на сервер для доступа
- Rate limiting строгие (100 запросов в 1.41 минуты)
- Требует intent permissions для некоторых операций

Установка discord.py:
pip install discord.py

Интеграция требует:
- Bot Token
- discord.py библиотека
- Интенты (Intent permissions)

Текущее состояние: ⚠️ ТРЕБУЕТ ИНТЕГРАЦИИ
Требуется: Bot Token + discord.py
```

### 5️⃣ Roblox API

```
┌─ Название: Roblox Users API
├─ Сайт: https://roblox.com/
├─ API: https://api.roblox.com
├─ Документация: https://wiki.roblox.com/index.php?title=API:_Reference
├─ Метод: GET HTTPS
├─ Бесплатно: ДА
├─ Регистрация: НЕ требуется
├─ API Key: НЕ требуется
├─ Лимиты: ~200 запросов в минуту
├─ Тип данных: JSON
└─ Информация: ID, username, статус, друзья

Основные endpoints:
GET /users/get-by-username?username={username} - получить пользователя
GET /users/{id} - информация о пользователе
GET /users/{id}/friends - друзья пользователя
GET /users/{id}/followers - подписчики

Пример запроса:
https://api.roblox.com/users/get-by-username?username=Builderman

Ответ:
{
  "success": true,
  "message": "Success.",
  "data": {
	"userId": 1,
	"username": "Builderman",
	"displayName": "david.baszucki"
  }
}

Или (более новый API):
GET /users/{id}

Ответ:
{
  "description": "Creator of Roblox",
  "created": "2006-02-27T18:41:26.96Z",
  "isBanned": false,
  "id": 1,
  "name": "Builderman",
  "displayName": "david.baszucki"
}

Текущее состояние: ✅ РАБОТАЕТ
Не требует настройки
```

### 6️⃣ Встроенные функции (requests, faker, etc)

```
┌─ Встроенные HTTP запросы (requests)
├─ Website Search: HEAD запрос на URL
├─ Nickname Search: проверка доступности профилей
├─ Web Crawler: GET запрос и парсинг HTML
├─ Лимиты: нет (зависит от сайта)
└─ Статус: ✅ РАБОТАЕТ

┌─ Faker (генератор фейк-данных)
├─ Fake Person Generator
├─ Email Generator
├─ Статус: ✅ РАБОТАЕТ
└─ Установлена версия: 15.0.0+

┌─ Встроенные генераторы
├─ Proxy Generator: встроенная генерация IP:PORT
├─ Password Generator: секретные ключи для генерации паролей
├─ Ban Word Generator: встроенный список слов
├─ Anonymity Manual: статический контент
├─ Hall of Fame: статический контент
└─ Статус: ✅ ВСЕ РАБОТАЮТ

Текущее состояние: ✅ ВСЕ РАБОТАЮТ БЕЗ ДОППРОМЕЖИУМА
```

---

## 🛠️ УСТАНОВКА И КОНФИГУРАЦИЯ

### Шаг 1: Установить базовые пакеты

```bash
cd C:\Users\zavoe\source\repos\kwoliTOOL
pip install -r kwoli_tool/requirements.txt
pip install python-dotenv
```

### Шаг 2: Создать файл .env

```bash
# Позиция: C:\Users\zavoe\source\repos\kwoliTOOL\.env

NUMVERIFY_API_KEY=
TELEGRAM_BOT_TOKEN=
DISCORD_BOT_TOKEN=
```

### Шаг 3: Получить API ключи (опционально)

#### NumVerify (Phone Search)
```
1. https://numverify.com/auth/sign-up
2. Создать аккаунт
3. Скопировать API Key
4. Вставить в .env: NUMVERIFY_API_KEY=key
```

#### Telegram Bot Token
```
1. Telegram > @BotFather
2. /newbot
3. Следовать инструкциям
4. Скопировать token
5. Вставить в .env: TELEGRAM_BOT_TOKEN=token
```

#### Discord Bot Token
```
1. https://discord.com/developers/applications
2. Log In
3. New Application
4. Add Bot
5. Copy Token
6. Вставить в .env: DISCORD_BOT_TOKEN=token
```

### Шаг 4: Добавить .env в .gitignore

```bash
echo .env >> .gitignore
```

### Шаг 5: Проверить работу

```bash
python run.py
```

---

## 🔐 ТАБЛИЦА БЕЗОПАСНОСТИ

```
╔═══════════════════════╦═════════════════════════════════════════════╗
║ Действие              ║ Безопасность                                ║
╠═══════════════════════╬═════════════════════════════════════════════╣
║ Хранить в .env        ║ ✅ БЕЗОПАСНО                                ║
║ Хранить в коде        ║ ❌ ОПАСНО - утечка при commit                ║
║ Коммитить .env        ║ ❌ ОПАСНО - утечка на GitHub/Git            ║
║ Использовать переменные ║✅ БЕЗОПАСНО - рекомендуется             ║
║ Делиться ключами      ║ ❌ ОПАСНО - нарушение лимитов/взлом         ║
║ Регенерировать ключи  ║ ✅ ОБЯЗАТЕЛЬНО если утекли                 ║
║ Azure/AWS Vault       ║ ✅ ИДЕАЛЬНО для production                  ║
╚═══════════════════════╩═════════════════════════════════════════════╝
```

---

## 📊 СРАВНИТЕЛЬНАЯ ТАБЛИЦА API

```
╔────────────┬──────────┬──────────┬─────────┬──────────────╦════════════╗
║ API        ║ Тип      ║ Платно   ║ Регист. ║ Лимит        ║ Сложность  ║
╠════════════╬══════════╬══════════╬═════════╬══════════════╬════════════╣
║ ipapi.co   ║ Поиск IP ║ Нет      ║ Нет     ║ 30K/мес     ║ ⭐ Very easy║
║ NumVerify  ║ Телефон  ║ Да*      ║ Да      ║ 250/мес*    ║ ⭐ Easy     ║
║ Telegram   ║ Чат      ║ Нет      ║ Да      ║ ∞           ║ ⭐⭐ Medium  ║
║ Discord    ║ Чат      ║ Нет      ║ Да      ║ ∞           ║ ⭐⭐ Medium  ║
║ Roblox     ║ Игра     ║ Нет      ║ Нет     ║ ~200/мин    ║ ⭐ Easy     ║
║ Built-in   ║ Разное   ║ Нет      ║ Нет     ║ ∞           ║ ⭐ Easy     ║
╚════════════╩══════════╩══════════╩═════════╩══════════════╩════════════╝

* NumVerify имеет бесплатный план на 250 запросов
```

---

## 📈 ГРАФИК ВНЕДРЕНИЯ

```
ДЕНЬ 1 - БАЗОВАЯ УСТАНОВКА
├─ pip install requirements
├─ pip install python-dotenv
├─ Создать .env файл
└─ python run.py (11 функций работают)
   ✅ Готово! Можно использовать

ДЕНЬ 2 - ОПЦИОНАЛЬНАЯ РАСШИРЕННАЯ НАСТРОЙКА
├─ NumVerify регистрация (5 мин)
├─ Telegram @BotFather (3 мин)
├─ Discord devportal (5 мин)
├─ Добавить в .env
└─ python run.py (15 функций работают)
   ✅ ВСЕ ФУНКЦИИ РАБОТАЮТ!

ДЕНЬ 3 - ДОПОЛНИТЕЛЬНЫЕ БИБЛИОТЕКИ (опционально)
├─ pip install beautifulsoup4 lxml (парсинг)
├─ pip install pyrogram (Telegram Client API)
├─ pip install discord.py (Discord расширения)
└─ python run.py (улучшенная функциональность)
   ✅ ПРЕМИУМ РЕЖИМ!
```

---

## 🎯 МИНИМАЛЬНЫЕ ТРЕБОВАНИЯ

Для работы минимум 11 функций:
- ✅ Python 3.7+
- ✅ requests (установлен)
- ✅ colorama (установлен)
- ✅ faker (установлен)

Для работы ВСЕх 15 функций добавить:
- ⚠️ python-dotenv
- ⚠️ NumVerify API ключ (опционально)
- ⚠️ Telegram Bot Token (опционально)
- ⚠️ Discord Bot Token (опционально)

---

## ✅ ФИНАЛЬНЫЙ ЧЕК-ЛИСТ

```
ПОДГОТОВКА:
☐ Прочитал API_QUICK_START.md
☐ Прочитал API_REQUIREMENTS.md
☐ Прочитал этот файл

УСТАНОВКА:
☐ pip install -r kwoli_tool/requirements.txt
☐ pip install python-dotenv
☐ Создал файл .env
☐ Добавил .env в .gitignore

КЛЮЧИ (выбрать нужные):
☐ NumVerify API Key (http://numverify.com)
☐ Telegram Bot Token (@BotFather)
☐ Discord Bot Token (devportal)

ТЕСТИРОВАНИЕ:
☐ python run.py
☐ Протестировал функцию 1 (IP Search)
☐ Протестировал функцию 4 (Website Search)
☐ Протестировал функцию 7 (Roblox)
☐ Протестировал функцию 9 (Proxy Generator)

ОПЦИОНАЛЬНО:
☐ python test_api_integration.py
☐ pip install beautifulsoup4 lxml
☐ pip install pyrogram
☐ pip install discord.py

ГОТОВО:
☐ ВСЕ ФУНКЦИИ РАБОТАЮТ!
☐ Приложение готово к использованию
☐ Я счастлив(а) 🎉
```

---

## 📞 КОНТАКТЫ ПОДДЕРЖКИ

| Сервис | Email | Чат | GitHub |
|--------|-------|-----|--------|
| ipapi.co | support@ipapi.co | - | - |
| NumVerify | support@numverify.com | - | - |
| Telegram | @BotSupport | Telegram | - |
| Discord | support@discord.com | Help | - |
| Roblox | appeals@roblox.com | - | - |

---

**Документация создана: 2024**  
**Версия: 1.0**  
**KWOLI TOOL - Полные API требования**
