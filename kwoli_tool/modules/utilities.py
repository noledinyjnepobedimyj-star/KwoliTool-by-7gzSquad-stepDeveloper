"""
Utility modules for KWOLI TOOL
Includes anonymity manual and hall of fame
"""

from kwoli_tool.ui.animation import print_info, print_success
from kwoli_tool.config import Colors


class AnonymityManual:
    """Manual for staying anonymous online"""

    TIPS = {
        '1. VPN и прокси': [
            '• Используйте надежный VPN (ExpressVPN, NordVPN, ProtonVPN)',
            '• Проверяйте утечки IP через ipleak.net',
            '• Используйте SOCKS5 прокси для дополнительной защиты',
            '• Не доверяйте бесплатным VPN'
        ],
        '2. Браузеры': [
            '• Используйте Tor Browser для максимальной анонимности',
            '• Firefox с расширениями uBlock Origin и NoScript',
            '• Отключайте JavaScript в небезопасных сетях',
            '• Используйте режим приватного браузера'
        ],
        '3. Операционная система': [
            '• Linux более безопасна для анонимности',
            '• Используйте Tails или Whonix для полной анонимности',
            '• Отключайте геолокацию и смарт-функции',
            '• Регулярно обновляйте ОС'
        ],
        '4. Сетевая безопасность': [
            '• Используйте HTTPS везде где возможно',
            '• Проверяйте SSL сертификаты',
            '• Отключайте Wi-Fi и Bluetooth при неиспользовании',
            '• Используйте VPN даже в домашней сети'
        ],
        '5. Учетные записи': [
            '• Используйте разные пароли для каждого сервиса',
            '• Включайте двухфакторную аутентификацию',
            '• Не привязывайте номер телефона к реальным данным',
            '• Используйте временные почты вместо основной'
        ],
        '6. Мессенджеры': [
            '• Signal для защищенного мессинджа',
            '• Wire для видеозвонков',
            '• Session для анонимного чата',
            '• Не используйте WhatsApp без VPN'
        ]
    }

    @staticmethod
    def display():
        """Display anonymity manual"""
        print_success("Мануал по анонимности в интернете")
        print()

        for topic, tips in AnonymityManual.TIPS.items():
            print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}{topic}{Colors.RESET}")
            for tip in tips:
                print(f"{Colors.GREEN}{tip}{Colors.RESET}")
            print()


class HallOfFame:
    """Links to useful applications and tools"""

    APPS = {
        'VPN & Прокси': {
            'ExpressVPN': 'https://www.expressvpn.com',
            'NordVPN': 'https://nordvpn.com',
            'ProtonVPN': 'https://protonvpn.com',
            'Tor Browser': 'https://www.torproject.org'
        },
        'Мессенджеры': {
            'Signal': 'https://signal.org',
            'Wire': 'https://wire.com',
            'Session': 'https://getsession.org',
            'Ricochet': 'https://ricochet.im'
        },
        'ОС & Системы': {
            'Tails': 'https://tails.boum.org',
            'Whonix': 'https://www.whonix.org',
            'Qubes OS': 'https://www.qubes-os.org',
            'Kali Linux': 'https://www.kali.org'
        },
        'Инструменты безопасности': {
            'KeePass': 'https://keepass.info',
            'VeraCrypt': 'https://www.veracrypt.fr',
            'Tor Browser Bundle': 'https://www.torproject.org/download',
            'Torsocks': 'https://torsocks.rocks'
        },
        'Анализ безопасности': {
            'Shodan': 'https://www.shodan.io',
            'Have I Been Pwned': 'https://haveibeenpwned.com',
            'Censys': 'https://censys.io',
            'ZoomEye': 'https://www.zoomeye.org'
        },
        'Генераторы & Утилиты': {
            'Password Generator': 'https://www.passwordgenerator.com',
            'Temp Mail': 'https://temp-mail.org',
            'DuckDuckGo': 'https://duckduckgo.com',
            'ProtonMail': 'https://proton.me/mail'
        }
    }

    @staticmethod
    def display():
        """Display hall of fame"""
        print_success("Зал славы - Полезные приложения и ссылки")
        print()

        for category, apps in HallOfFame.APPS.items():
            print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}{category}{Colors.RESET}")
            for app_name, link in apps.items():
                print(f"{Colors.CYAN}  • {app_name}{Colors.RESET}")
                print(f"{Colors.WHITE}    🔗 {link}{Colors.RESET}")
            print()


class AnonymityTips:
    """Quick anonymity tips"""

    QUICK_TIPS = [
        "✓ Никогда не используйте реальное имя в интернете",
        "✓ Всегда используйте VPN на общественных Wi-Fi",
        "✓ Проверяйте утечки DNS и IP регулярно",
        "✓ Используйте разные браузеры для разных личностей",
        "✓ Очищайте куки и историю браузера регулярно",
        "✓ Не совмещайте разные личности в одной сессии",
        "✓ Используйте средства от отслеживания (uBlock Origin, Privacy Badger)",
        "✓ Отключайте WebRTC в браузере для защиты IP",
        "✓ Используйте HTTPS везде где возможно",
        "✓ Не передавайте личные данные в интернете"
    ]

    @staticmethod
    def display():
        """Display quick tips"""
        print_info("Быстрые советы по анонимности:")
        for tip in AnonymityTips.QUICK_TIPS:
            print(f"{Colors.GREEN}{tip}{Colors.RESET}")


# Email Providers
EMAIL_PROVIDERS = {
    'ProtonMail': 'https://proton.me/mail',
    'Temp-Mail': 'https://temp-mail.org',
    '10MinuteMail': 'https://10minutemail.com',
    'Guerrilla Mail': 'https://www.guerrillamail.com',
    'Mailinator': 'https://www.mailinator.com',
    'Throwaway Email': 'https://www.throwaway.email'
}

# VPN Providers
VPN_PROVIDERS = {
    'ExpressVPN': 'https://www.expressvpn.com',
    'NordVPN': 'https://nordvpn.com',
    'ProtonVPN': 'https://protonvpn.com',
    'Windscribe': 'https://windscribe.com',
    'CyberGhost': 'https://www.cyberghostvpn.com',
    'Surfshark': 'https://surfshark.com'
}
