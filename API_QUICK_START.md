# 🚀 БЫСТРАЯ ШПАРГАЛКА ПО API ДЛЯ KWOLI TOOL

## ⚡ Главное
- **15 функций** - 11 работают сейчас, 4 нужны API ключи
- **Бесплатные**: ipapi.co, Roblox, Telegram Bot, Discord Bot
- **Платные**: NumVerify ($4.99/мес, но есть бесплатный план на 250 запросов)

---

## 📊 Статус функций (быстро)

### ✅ Работают сейчас (БЕЗ API):
1. **IP Search** → `ipapi.co` (бесплатно)
2. **Website Search** → встроенный
3. **Nickname Search** → встроенный
4. **Roblox Search** → `api.roblox.com` (бесплатно)
5. **Web Crawler** → встроенный
6. **Proxy Generator** → встроенный
7. **Fake Person Generator** → faker (встроенный)
8. **Email Generator** → встроенный
9. **Password Generator** → встроенный
10. **Ban Word Generator** → встроенный
11. **Anonymity Manual** → встроенный
12. **Hall of Fame** → встроенный

### ⚠️ Нужны ключи (ПРОСТАЯ настройка):
| Функция | Ключ | Где взять | Время |
|---------|------|----------|-------|
| 2️⃣ **Phone Search** | NumVerify API | https://numverify.com | 5 мин |
| 3️⃣ **Telegram Search** | Bot Token | @BotFather в Telegram | 3 мин |
| 6️⃣ **Discord Search** | Bot Token | https://discord.com/developers | 5 мин |

---

## 🔑 Как получить ключи (3 способа за 10 минут)

### Способ 1: NumVerify (Phone Search) - 5 минут ⏱️

```
→ Перейти: https://numverify.com/
→ Sign Up
→ Подтвердить email
→ Скопировать API Key
→ Добавить в .env: NUMVERIFY_API_KEY=key_here
```

Бесплатный план: **250 запросов в месяц**

---

### Способ 2: Telegram Bot (Telegram Search) - 3 минуты ⏱️

```
→ Открыть Telegram
→ Найти @BotFather
→ /newbot
→ Ответить на вопросы (имя бота)
→ Скопировать TOKEN
→ Добавить в .env: TELEGRAM_BOT_TOKEN=token_here
```

**Бесплатно, неограниченно**

---

### Способ 3: Discord Bot (Discord Search) - 5 минут ⏱️

```
→ Перейти: https://discord.com/developers/applications
→ Войти
→ New Application
→ + Add Bot
→ Copy Token
→ Добавить в .env: DISCORD_BOT_TOKEN=token_here
```

**Бесплатно, достаточно для использования**

---

## 📝 Установка (копировать-вставить)

### Шаг 1: Зависимости

```bash
pip install -r kwoli_tool/requirements.txt
pip install python-dotenv
```

### Шаг 2: Создать .env файл

```bash
# Скопировать это в файл .env в корне проекта
NUMVERIFY_API_KEY=your_key
TELEGRAM_BOT_TOKEN=your_token
DISCORD_BOT_TOKEN=your_token
```

### Шаг 3: Защита

```bash
echo ".env" >> .gitignore
```

### Шаг 4: Тест

```bash
python run.py
```

---

## 🔗 Прямые ссылки

| Что нужно | Ссылка |
|----------|--------|
| NumVerify API | https://numverify.com/auth/sign-up |
| Telegram BotFather | https://t.me/botfather |
| Discord Developer | https://discord.com/developers/applications |
| ipapi.co | https://ipapi.co/ |
| Roblox API | https://api.roblox.com |

---

## 💡 Примеры кода

### NumVerify (Phone Search)

```python
import requests
import os

api_key = os.getenv('NUMVERIFY_API_KEY')
phone = "+79991234567"

response = requests.get(
	"https://apilayer.net/api/validate",
	params={
		'access_key': api_key,
		'number': phone,
		'format': 1
	}
)

data = response.json()
print(f"Валиден: {data['valid']}")
print(f"Оператор: {data['carrier']}")
```

### Telegram Bot (Check token)

```python
import requests
import os

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

response = requests.get(
	f"https://api.telegram.org/bot{bot_token}/getMe"
)

if response.status_code == 200:
	print("✓ Token работает")
else:
	print("✗ Token не работает")
```

### Discord Bot (Check token)

```python
import discord

class Client(discord.Client):
	async def on_ready(self):
		print(f'✓ Bot {self.user} работает')
		await self.close()

client = Client()
client.run(os.getenv('DISCORD_BOT_TOKEN'))
```

---

## ❓ FAQ

**Q: NumVerify бесплатный?**  
A: Да, 250 запросов/месяц бесплатно

**Q: Telegram/Discord требуют платежные системы?**  
A: Нет, полностью бесплатно

**Q: Нужно ли настраивать все 4 ключа?**  
A: Нет, можно использовать функции без них (будут работать 11 других)

**Q: Где хранить ключи?**  
A: В файле .env, не коммитьте в Git!

**Q: Работает ли приложение без ключей?**  
A: Да! 11 функций будут работать без ключей

**Q: Можно ли использовать чужие ключи?**  
A: Не рекомендуется (опасность и лимиты)

---

## 🛡️ Безопасность (ВАЖНО!)

❌ **НИКОГДА не делайте:**
- Не коммитьте .env в Git
- Не давайте ключи друзьям
- Не выкладывайте ключи в интернет
- Не добавляйте в код напрямую

✅ **ВСЕГДА делайте:**
- Используйте .env файл
- Добавьте .env в .gitignore
- Регенерируйте ключи если утекли
- Проверяйте использование в личном кабинете

---

## 🧪 Проверка (3 способа)

### Способ 1: Встроенный тест

```bash
python test_api_integration.py
```

### Способ 2: Через приложение

```bash
python run.py
# Выбрать функцию и попробовать
```

### Способ 3: Вручную

```python
import requests
from dotenv import load_dotenv

load_dotenv()

# Тест ApiAPI.co
print(requests.get("https://ipapi.co/1.1.1.1/json/").status_code)

# Тест NumVerify
print(requests.get("https://apilayer.net/api/validate", 
	params={'access_key': api_key, 'number': '12015550123', 'format': 1}
).status_code)

# Тест Telegram
print(requests.get(f"https://api.telegram.org/bot{token}/getMe").status_code)
```

---

## 📈 После настройки

**Что будет работать:**
- ✅ 11 функций работают сейчас
- ✅ +1 функция (Phone Search) с NumVerify
- ✅ +1 функция (Telegram) улучшится с Bot API
- ✅ +1 функция (Discord) улучшится с Bot Token
- ✅ = **ПОЛНЫЕ 15 ФУНКЦИЙ** 🚀

---

## 📞 Поддержка

| Проблема | Решение |
|----------|---------|
| Token не работает | Проверить скопировал полностью? Перегенерировать |
| Лимит исчерпан | Ждать конца месяца или обновить план |
| .env не видна | Проверить расширение файла (.env, не .txt) |
| Import Error | Установить зависимости: pip install -r requirements.txt |

---

## 🎯 Рекомендуемый путь

```
День 1:
├─ pip install requirements.txt + python-dotenv
├─ Создать .env
└─ Запустить python run.py (работает 11 функций)

День 2 (опционально):
├─ Добавить NumVerify Key (Phone Search)
├─ Добавить Telegram Token (@BotFather)
└─ Добавить Discord Token (devportal)

День 3:
└─ Наслаждаться ВСЕМИ 15 ФУНКЦИЯМИ! 🎉
```

---

*Версия: 1.0*  
*KWOLI TOOL*  
*Для вопросов см: API_REQUIREMENTS.md & API_INTEGRATION_GUIDE.md*
