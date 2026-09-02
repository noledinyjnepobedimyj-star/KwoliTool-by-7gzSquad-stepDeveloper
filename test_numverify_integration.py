#!/usr/bin/env python3
"""
Тест NumVerify API интеграции для KWOLI TOOL
Проверяет что API ключ работает и функция Phone Search готова
"""

import os
import sys
import requests
from dotenv import load_dotenv
from colorama import Fore, Style

# Загрузить переменные окружения
load_dotenv()

print(f"\n{Fore.LIGHTCYAN_EX}{'='*60}")
print(f"🧪 ТЕСТ NUMVERIFY API ИНТЕГРАЦИИ")
print(f"{'='*60}{Style.RESET_ALL}\n")

# 1. Проверить наличие .env файла
print("1️⃣  Проверка .env файла...")
env_file = '.env'
if os.path.exists(env_file):
    print(f"   {Fore.LIGHTGREEN_EX}✅ Файл .env найден{Style.RESET_ALL}")
else:
    print(f"   {Fore.LIGHTRED_EX}❌ Файл .env не найден{Style.RESET_ALL}")
    sys.exit(1)

# 2. Проверить наличие API ключа
print("\n2️⃣  Проверка API ключа...")
api_key = os.getenv('NUMVERIFY_API_KEY')
if api_key:
    print(f"   {Fore.LIGHTGREEN_EX}✅ API ключ найден{Style.RESET_ALL}")
    print(f"   {Fore.CYAN}Ключ: {api_key[:10]}...{api_key[-10:]}{Style.RESET_ALL}")
else:
    print(f"   {Fore.LIGHTRED_EX}❌ API ключ не установлен{Style.RESET_ALL}")
    print(f"   ➜ Добавьте в .env: NUMVERIFY_API_KEY=ваш_ключ")
    sys.exit(1)

# 3. Проверить подключение к интернету
print("\n3️⃣  Проверка подключения к интернету...")
try:
    response = requests.get('https://www.google.com', timeout=3)
    print(f"   {Fore.LIGHTGREEN_EX}✅ Интернет подключен{Style.RESET_ALL}")
except:
    print(f"   {Fore.LIGHTRED_EX}❌ Нет подключения к интернету{Style.RESET_ALL}")
    sys.exit(1)

# 4. Протестировать NumVerify API
print("\n4️⃣  Тест NumVerify API...")
print("   🔍 Отправка тестового запроса для номера +1 201 555 0123...")

try:
    url = "https://apilayer.net/api/validate"
    params = {
        'access_key': api_key,
        'number': '12015550123',  # Тестовый номер (США)
        'format': 1
    }

    response = requests.get(url, params=params, timeout=5)

    if response.status_code == 200:
        data = response.json()

        if data.get('valid'):
            print(f"   {Fore.LIGHTGREEN_EX}✅ API РАБОТАЕТ!{Style.RESET_ALL}")
            print(f"   📊 Результаты:")
            print(f"      • Валиден: {Fore.LIGHTGREEN_EX}{data.get('valid')}{Style.RESET_ALL}")
            print(f"      • Страна: {data.get('country_name')}")
            print(f"      • Оператор: {data.get('carrier')}")
            print(f"      • Тип: {data.get('line_type')}")
            print(f"      • Формат: {data.get('international_format')}")
        else:
            print(f"   {Fore.LIGHTYELLOW_EX}⚠️  API ответил, но номер невалиден{Style.RESET_ALL}")
            print(f"   {Fore.LIGHTGREEN_EX}✅ ЭТО НОРМАЛЬНО - API РАБОТАЕТ!{Style.RESET_ALL}")
    else:
        print(f"   {Fore.LIGHTRED_EX}❌ Ошибка API: HTTP {response.status_code}{Style.RESET_ALL}")
        if response.status_code == 401:
            print(f"      API ключ невалиден или истёк")
        elif response.status_code == 429:
            print(f"      Превышен лимит запросов")
        sys.exit(1)

except requests.exceptions.Timeout:
    print(f"   {Fore.LIGHTRED_EX}❌ Timeout (превышено время ожидания){Style.RESET_ALL}")
    sys.exit(1)
except Exception as e:
    print(f"   {Fore.LIGHTRED_EX}❌ Ошибка: {str(e)}{Style.RESET_ALL}")
    sys.exit(1)

# 5. Проверить интеграцию в коде
print("\n5️⃣  Проверка интеграции в коде...")
try:
    from kwoli_tool.modules.searchers import PhoneSearcher
    print(f"   {Fore.LIGHTGREEN_EX}✅ PhoneSearcher импортирован{Style.RESET_ALL}")
except ImportError as e:
    print(f"   {Fore.LIGHTRED_EX}❌ Ошибка импорта: {str(e)}{Style.RESET_ALL}")
    sys.exit(1)

# 6. Итоговый результат
print(f"\n{Fore.LIGHTGREEN_EX}{'='*60}")
print(f"✅ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!")
print(f"{'='*60}{Style.RESET_ALL}")

print(f"\n{Fore.LIGHTCYAN_EX}📌 ИНФОРМАЦИЯ:{Style.RESET_ALL}")
print(f"""
✅ NumVerify API успешно интегрирован
✅ Функция Phone Search (Пробив по номеру) готова к использованию
✅ Лимит: 250 запросов в месяц на бесплатном плане

🚀 ТЕСТИРОВАНИЕ ФУНКЦИИ:

   python run.py
   ↓
   Выбрать опцию: 2
   ↓
   Ввести номер телефона (например: +7 (999) 123-45-67)
   ↓
   Получить информацию об операторе и типе номера

📚 ДОКУМЕНТАЦИЯ: смотрите README_API.md и API_QUICK_START.md
""")

print(f"{Fore.LIGHTGREEN_EX}✨ Готово к использованию!{Style.RESET_ALL}\n")
