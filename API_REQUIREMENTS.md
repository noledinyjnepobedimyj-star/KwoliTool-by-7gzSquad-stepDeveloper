# 🔌 KWOLI TOOL - Требования к API

Полный список API, необходимых для функционирования всех 15 функций приложения.

---

## 📋 Таблица функций и API

| № | Функция | Текущий статус | Требуемый API | Тип | Примечание |
|---|---------|---|---|---|---|
| 1 | **IP Search** (Поиск по IP) | ✅ Работает | `ipapi.co` | Бесплатный | Бесплатный, без регистрации |
| 2 | **Phone Search** (Пробив по номеру) | ⚠️ Частично | `NumVerify`, `PhoneNumberLookup` | Платный | Требует API ключ |
| 3 | **Telegram Search** | ⚠️ Требует настройки | `Telegram Bot API` | Бесплатный* | Требует Bot Token |
| 4 | **Website Search** (Информация о сайте) | ✅ Работает | Встроенный `requests` | Бесплатный | Встроенная функция |
| 5 | **Nickname Search** (Поиск по никнейму) | ✅ Работает | Встроенный | Бесплатный | Проверка доступности профилей |
| 6 | **Discord Search** | ⚠️ Требует настройки | `Discord API` | Бесплатный* | Требует Bot Token |
| 7 | **Roblox Search** | ✅ Работает | `api.roblox.com` | Бесплатный | Встроенный в Roblox |
| 8 | **Web Crawler** (Краулер сайтов) | ✅ Работает | Встроенный `requests` | Бесплатный | Встроенная функция |
| 9 | **Proxy Generator** | ✅ Работает | Встроенный | Бесплатный | Встроенная генерация |
| 10 | **Fake Person Generator** | ✅ Работает | `faker` | Бесплатный | Установлен в зависимостях |
| 11 | **Email Generator** | ✅ Работает | Встроенный | Бесплатный | Встроенная генерация |
| 12 | **Password Generator** | ✅ Работает | Встроенный | Бесплатный | Встроенная генерация |
| 13 | **Ban Word Generator** | ✅ Работает | Встроенный | Бесплатный | Встроенная генерация |
| 14 | **Anonymity Manual** | ✅ Работает | Встроенный | Бесплатный | Статическая информация |
| 15 | **Hall of Fame** | ✅ Работает | Встроенный | Бесплатный | Статическая информация |

---

## 🔍 Детальное описание по функциям

### 1️⃣ IP Search (Поиск по IP адресу)

**Статус:** ✅ **Полностью рабочее**

**API:** `ipapi.co`
- **URL:** `https://ipapi.co/{ip}/json/`
- **Метод:** GET
- **Параметры:** IP адрес (путь)
- **Результат:** JSON с данными о стране, городе, регионе, провайдере, координатах
- **Лимиты:** 30,000 запросов/месяц (бесплатно)
- **Регистрация:** НЕ требуется
- **Пример:** 
  ```
  https://ipapi.co/1.1.1.1/json/
  ```

```python
# Текущая реализация в searchers.py - РАБОТАЕТ
api_url = f"https://ipapi.co/{ip}/json/"
response = requests.get(api_url, timeout=5)
```

---

### 2️⃣ Phone Search (Пробив по номеру телефона) ⚠️

**Статус:** ⚠️ **ТРЕБУЕТ ДОРАБОТКИ**

**Текущая ситуация:** 
- Код содержит только базовую валидацию формата
- Возвращает mock-данные
- Не подключен никакой API

**Требуемые API (выбрать один):**

#### Вариант 1: NumVerify (РЕКОМЕНДУЕТСЯ)
- **Сайт:** https://numverify.com/
- **Тип лицензии:** Платный (от $4.99/месяц)
- **Бесплатный план:** Да (250 запросов/месяц)
- **API Key:** Требуется регистрация
- **URL:** `https://apilayer.net/api/validate`
- **Параметры:**
  ```
  ?access_key={API_KEY}
  &number={PHONE_NUMBER}
  &country_code={CODE} (опционально)
  &format=1
  ```
- **Результат:** JSON с информацией об операторе, стране, типе номера

#### Вариант 2: TwilioLookup API
- **Сайт:** https://www.twilio.com/
- **Платно:** Да (от $0.005 за запрос)
- **API Key:** Требуется регистрация + платежный метод
- **Документация:** https://www.twilio.com/docs/lookup/api

#### Вариант 3: HLR Lookups
- **Сайт:** https://hlr-lookups.com/
- **Платно:** Да
- **Проверка:** Статус активности номера

**Рекомендуемое решение:**
```python
# Использовать NumVerify (бесплатный план есть)
import requests

def search_phone(phone_number):
	api_key = "YOUR_NUMVERIFY_API_KEY"
	url = "https://apilayer.net/api/validate"

	params = {
		'access_key': api_key,
		'number': phone_number,
		'format': 1
	}

	response = requests.get(url, params=params)
	data = response.json()

	return {
		'valid': data.get('valid'),
		'country': data.get('country_name'),
		'carrier': data.get('carrier'),
		'line_type': data.get('line_type')
	}
```

---

### 3️⃣ Telegram Search ⚠️

**Статус:** ⚠️ **ТРЕБУЕТ КОНФИГУРАЦИИ**

**Текущая ситуация:** 
- Код содержит функцию поиска
- Требует Telegram Bot Token
- Не подключен API

**Требуемые данные:**

#### Telegram Bot API
- **Документация:** https://core.telegram.org/bots/api
- **Как получить Bot Token:**
  1. Найти в Telegram: `@BotFather`
  2. Команда: `/newbot`
  3. Выполнить инструкции
  4. Получить TOKEN вида: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`

- **URL базовый:** `https://api.telegram.org/bot{TOKEN}/`
- **Методы:**
  - `getMe` - получить информацию о боте
  - `getUser` - получить информацию о пользователе (требует ID)
  - `searchPublicChat` - поиск по username (доступно через Client API)

**Примечание:** 
- Для полнофункционального поиска требуется **Telegram Client API** (не Bot API)
- Client API требует номер телефона и коды подтверждения
- Это сложнее, чем Bot API

**Рекомендуемое решение (с Bot API):**
```python
import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_me():
	response = requests.get(f"{BASE_URL}/getMe")
	return response.json()

# Для поиска нужен Telegram Client API (pyrogram, telethon)
```

---

### 4️⃣ Website Search (Информация о сайте)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Встроенное решение:**
- Использует обычный `requests.head()`
- Получает HTTP заголовки
- Не требует API ключей

```python
# Текущая реализация - РАБОТАЕТ
response = requests.head(url, timeout=5, allow_redirects=True)
# Возвращает: статус, тип контента, сервер, время модификации
```

---

### 5️⃣ Nickname Search (Поиск по никнейму)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Встроенное решение:**
- Проверка наличия профилей на популярных сайтах:
  - GitHub
  - Twitter
  - Reddit
  - Instagram
- Использует обычные HEAD запросы
- Не требует API ключей

```python
# Текущая реализация - РАБОТАЕТ
platforms = [
	('GitHub', f'https://github.com/{nickname}'),
	('Twitter', f'https://twitter.com/{nickname}'),
	# ...
]
```

---

### 6️⃣ Discord Search ⚠️

**Статус:** ⚠️ **ТРЕБУЕТ КОНФИГУРАЦИИ**

**Текущая ситуация:** 
- Код содержит функцию поиска
- Требует Discord Bot Token
- Только информационное сообщение

**Требуемые данные:**

#### Discord API
- **Документация:** https://discord.com/developers/docs/intro
- **Как получить Bot Token:**
  1. Перейти на https://discord.com/developers/applications
  2. Нажать "New Application"
  3. Перейти на вкладку "Bot"
  4. Нажать "Add Bot"
  5. Скопировать TOKEN

- **Основные endpoints:**
  - `GET /users/@me` - информация о боте
  - `GET /users/{user_id}` - информация о пользователе
  - `GET /users/{user_id}/profile` - профиль пользователя

**Рекомендуемое решение:**
```python
import discord

# Использовать discord.py библиотеку
client = discord.Client()

async def search_user(username):
	user = await client.fetch_user_by_username(username)
	return {
		'id': user.id,
		'username': user.name,
		'avatar': user.avatar.url if user.avatar else None,
		'created_at': user.created_at
	}
```

---

### 7️⃣ Roblox Search

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**API:** `api.roblox.com`
- **URL:** `https://api.roblox.com/users/get-by-username?username={username}`
- **Метод:** GET
- **Параметры:** username
- **Результат:** JSON с ID и информацией пользователя
- **Лимиты:** Свободные
- **Регистрация:** НЕ требуется
- **Пример:** 
  ```
  https://api.roblox.com/users/get-by-username?username=Builderman
  ```

```python
# Текущая реализация в searchers.py - РАБОТАЕТ
api_url = f"https://api.roblox.com/users/get-by-username?username={username}"
response = requests.get(api_url, timeout=5)
```

---

### 8️⃣ Web Crawler (Краулер сайтов)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Встроенное решение:**
- Загружает содержимое страницы
- Парсит HTML регулярными выражениями
- Извлекает ссылки
- Не требует API ключей

```python
# Текущая реализация - РАБОТАЕТ
response = requests.get(url, timeout=5)
links = re.findall(r'href=[\'"]?([^\'" >]+)', response.text)
```

---

### 9️⃣ Proxy Generator (Генератор прокси)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Встроенное решение:**
- Встроенная генерация IP адресов
- Встроенная генерация портов
- Не требует API ключей

```python
# Генерируется локально, без API
```

---

### 🔟 Fake Person Generator (Генератор фейк-персон)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Библиотека:** `faker`
- **Установлена в:** requirements.txt
- **Документация:** https://faker.readthedocs.io/
- **Регистрация:** НЕ требуется

```python
from faker import Faker
fake = Faker('ru_RU')  # Русская локаль

# Генерирует:
# - Полные имена
# - Адреса
# - Номера телефонов
# - Email
# - Работу
# - И многое другое
```

---

### 1️⃣1️⃣ Email Generator (Генератор почт)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Встроенное решение:**
- Встроенная генерация случайных email адресов
- Использует встроенную Faker библиотеку
- Не требует API ключей

```python
# Генерируется локально
from faker import Faker
fake = Faker()
email = fake.email()
```

---

### 1️⃣2️⃣ Password Generator (Генератор паролей)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Встроенное решение:**
- Встроенная генерация мощных паролей
- Использует `secrets` и `string` модули Python
- Не требует API ключей

```python
# Генерируется локально
import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(16))
```

---

### 1️⃣3️⃣ Ban Word Generator (Генератор BAN-слов)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Встроенное решение:**
- Встроенный список "плохих" слов
- Локальная генерация
- Не требует API ключей

---

### 1️⃣4️⃣ Anonymity Manual (Руководство по анонимности)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Встроенное решение:**
- Статический контент
- Не требует API ключей

---

### 1️⃣5️⃣ Hall of Fame (Доска почета)

**Статус:** ✅ **ПОЛНОСТЬЮ РАБОЧЕЕ**

**Встроенное решение:**
- Статический контент
- Не требует API ключей

---

## 📊 Резюме требований

### ✅ Уже работает (11 функций)
1. IP Search - `ipapi.co`
2. Website Search - встроенный
3. Nickname Search - встроенный
4. Roblox Search - `api.roblox.com`
5. Web Crawler - встроенный
6. Proxy Generator - встроенный
7. Fake Person Generator - встроенный (faker)
8. Email Generator - встроенный
9. Password Generator - встроенный
10. Ban Word Generator - встроенный
11. Anonymity Manual - встроенный
12. Hall of Fame - встроенный

### ⚠️ Требует доработки (4 функции)

| Функция | Требует | Тип | Стоимость |
|---------|---------|---|---|
| Phone Search | NumVerify API | Платный* | $4.99/месяц (есть бесплатный) |
| Telegram Search | Bot Token + Client API | Бесплатный | Бесплатно |
| Discord Search | Bot Token + discord.py | Бесплатный | Бесплатно |
| - | - | - | - |

---

## 🛠️ Инструкции установки

### 1. Установка зависимостей

```bash
pip install -r kwoli_tool/requirements.txt
```

Текущие зависимости:
```
requests>=2.31.0
colorama>=0.4.6
faker>=15.0.0
```

### 2. Настройка Phone Search (NumVerify)

```bash
# 1. Зарегистрироваться на https://numverify.com/
# 2. Получить бесплатный API ключ (250 запросов/месяц)
# 3. Добавить в kwoli_tool/config.py:

NUMVERIFY_API_KEY = "YOUR_API_KEY_HERE"
```

### 3. Настройка Telegram Search

```bash
# 1. Найти @BotFather в Telegram
# 2. Команда /newbot
# 3. Следовать инструкциям
# 4. Добавить в kwoli_tool/config.py:

TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

### 4. Настройка Discord Search

```bash
# 1. Перейти на https://discord.com/developers/applications
# 2. Create Application
# 3. Add Bot
# 4. Copy Token
# 5. Добавить в kwoli_tool/config.py:

DISCORD_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

### 5. Установка дополнительных библиотек (опционально)

Для полноты функционала рекомендуется установить:

```bash
# Для Telegram (клиентский API)
pip install pyrogram  # или telethon

# Для Discord
pip install discord.py

# Для более полного парсинга веб-страниц
pip install beautifulsoup4
pip install lxml
```

---

## 🔐 Безопасность API ключей

### ВАЖНО:
- ❌ НЕ коммитьте API ключи в Git!
- ❌ НЕ делитесь ключами с другими!
- ✅ Используйте переменные окружения

### Пример с переменными окружения:

```python
import os
from dotenv import load_dotenv

load_dotenv()

NUMVERIFY_API_KEY = os.getenv('NUMVERIFY_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
```

### Создать файл .env:

```
NUMVERIFY_API_KEY=your_key_here
TELEGRAM_BOT_TOKEN=your_token_here
DISCORD_BOT_TOKEN=your_token_here
```

### Добавить в .gitignore:

```
.env
.env.local
.env.*.local
```

---

## 📞 Контакты поддержки API

| Сервис | Поддержка | Лимиты | Docs |
|--------|----------|--------|------|
| ipapi.co | Email | 30K/месяц | https://ipapi.co/api/ |
| NumVerify | Email/Chat | 250/месяц (free) | https://numverify.com/documentation |
| Telegram | Community | Неограниченно | https://core.telegram.org/bots/api |
| Discord | Community | Достаточно | https://discord.com/developers/docs |
| Roblox | Community | Достаточно | https://api.roblox.com |

---

## 📝 Чек-лист для полной функциональности

- [ ] `requests` - установлена (для всех HTTP запросов)
- [ ] `colorama` - установлена (для цветов)
- [ ] `faker` - установлена (для фейк-данных)
- [ ] `NumVerify API Key` - получен (для Phone Search)
- [ ] `Telegram Bot Token` - получен (для Telegram Search)
- [ ] `Discord Bot Token` - получен (для Discord Search)
- [ ] `.env` файл - создан с ключами
- [ ] `.gitignore` - обновлен

---

## 🎯 Итоговая рекомендация

Для максимальной функциональности рекомендуем:

1. **Сразу установить:**
   ```bash
   pip install -r kwoli_tool/requirements.txt
   ```

2. **Обязательно настроить (бесплатно):**
   - ✅ Telegram Bot Token (@BotFather)
   - ✅ Discord Bot Token (devportal)

3. **Опционально (платно, но есть бесплатный план):**
   - NumVerify API Key (для phone search)

4. **Опционально (для лучшего парсинга):**
   - BeautifulSoup4 + lxml
   - Pyrogram (для Telegram)
   - discord.py (для Discord)

После этого все 15 функций будут работать на полную мощность! 🚀

---

*Последнее обновление: 2024*
*KWOLI TOOL v1.*
