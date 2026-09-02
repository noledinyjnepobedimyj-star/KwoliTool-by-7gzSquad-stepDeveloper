"""
Configuration file for KWOLI TOOL
Contains colors, settings, and constants
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Загрузить .env из корня репозитория (не зависит от текущей папки)
_REPO_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_REPO_ROOT / ".env")

# ===== API KEYS (из переменных окружения) =====
NUMVERIFY_API_KEY = os.getenv('NUMVERIFY_API_KEY', '')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN', '')

# ===== ANSI Color Codes =====
class Colors:
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Background colors
    BG_GREEN = '\033[42m'
    BG_BLUE = '\033[44m'
    BG_CYAN = '\033[46m'

    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'

    # Reset
    RESET = '\033[0m'

    # Gradient simulation (green to blue gradient)
    GRADIENT_GREEN_BLUE = [
        '\033[32m',      # Green
        '\033[32;94m',   # Green-Blue
        '\033[36m',      # Cyan
        '\033[96m',      # Bright Cyan
        '\033[34m',      # Blue
        '\033[94m',      # Bright Blue
    ]

# ===== ASCII Art Logo =====
ASCII_LOGO = [
    "██ ▄█▀ █     █░ ▒█████   ██▓     ██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓",
    " ██▄█▒ ▓█░ █ ░█░▒██▒  ██▒▓██▒    ▓██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒",
    "▓███▄░ ▒█░ █ ░█ ▒██░  ██▒▒██░    ▒██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░",
    "▓██ █▄ ░█░ █ ░█ ▒██   ██░▒██░    ░██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░",
    "▒██▒ █▄░░██▒██▓ ░ ████▓▒░░██████▒░██░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒",
    "▒ ▒▒ ▓▒░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░▓  ░░▓       ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░",
    "░ ░▒ ▒░  ▒ ░ ░    ░ ▒ ▒░ ░ ░ ▒  ░ ▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░",
    "░ ░░ ░   ░   ░  ░ ░ ░ ▒    ░ ░    ▒ ░     ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░",
    "░  ░       ░        ░ ░      ░  ░ ░                  ░ ░      ░ ░      ░  ░",
]

# ===== Menu Items =====
MENU_ITEMS = [
    "🔍 Поиск по IP адресу",
    "📱 Поиск по номеру телефона",
    "✈️  Поиск по Telegram",
    "🌐 Поиск по веб-сайту",
    "👤 Поиск по никнейму",
    "🎮 Поиск по Discord",
    "🎯 Поиск по Roblox",
    "🕷️  WebCrawler",
    "🔁 Создание прокси",
    "🎭 Генератор вымышленной личности",
    "📧 Генератор временной почты",
    "🔐 Генератор паролей",
    "🏦 Генератор BAN-слова",
    "🛡️  Мануал по анонимности",
    "⭐ Зал славы (полезные приложения)",
]

# ===== UI Settings =====
ANIMATION_SPEED = 0.1  # seconds between animation frames
APP_NAME = "KWOLI TOOL"
APP_VERSION = "1.0.0"

# ===== External APIs =====
# (These are just defaults - will be used in respective modules)
API_CONFIGS = {
    'ip_api': 'https://ipapi.co',
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# ===== Messages =====
MESSAGES = {
    'welcome': 'Добро пожаловать в KWOLI TOOL',
    'press_enter': 'Нажмите ENTER чтобы продолжить',
    'select_option': 'Выберите опцию (1-15) или Q для выхода: ',
    'invalid_input': 'Неверный ввод. Попробуйте снова.',
    'going_back': 'Возврат в главное меню...',
}
