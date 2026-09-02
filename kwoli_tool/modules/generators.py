"""
Generator modules for KWOLI TOOL
Includes fake person, email, password, and ban word generators
"""

import random
import string
import secrets
from datetime import datetime, timedelta
from kwoli_tool.ui.animation import (
    print_success, 
    print_info,
    loading_animation
)


class FakePersonGenerator:
    """Generate fake person data"""

    FIRST_NAMES_RU = [
        'Иван', 'Петр', 'Сергей', 'Артем', 'Дмитрий',
        'Анна', 'Мария', 'Елена', 'Оксана', 'Наталья'
    ]

    LAST_NAMES_RU = [
        'Иванов', 'Петров', 'Сидоров', 'Федоров', 'Волков',
        'Соколов', 'Леонов', 'Павлов', 'Морозов', 'Козлов'
    ]

    JOBS = [
        'Программист', 'Дизайнер', 'Менеджер', 'Инженер',
        'Учитель', 'Врач', 'Адвокат', 'Бухгалтер'
    ]

    COUNTRIES = ['Россия', 'Украина', 'Беларусь', 'Казахстан', 'Киргизия']

    @staticmethod
    def generate():
        """Generate fake person data"""
        loading_animation(1)

        person = {
            'first_name': random.choice(FakePersonGenerator.FIRST_NAMES_RU),
            'last_name': random.choice(FakePersonGenerator.LAST_NAMES_RU),
            'age': random.randint(18, 80),
            'job': random.choice(FakePersonGenerator.JOBS),
            'country': random.choice(FakePersonGenerator.COUNTRIES),
            'phone': FakePersonGenerator._generate_phone(),
            'email': None,  # Will be generated separately
        }

        print_success("Сгенерирована вымышленная личность:")
        print(f"  Имя: {person['first_name']} {person['last_name']}")
        print(f"  Возраст: {person['age']}")
        print(f"  Профессия: {person['job']}")
        print(f"  Страна: {person['country']}")
        print(f"  Телефон: {person['phone']}")

        return person

    @staticmethod
    def _generate_phone():
        """Generate fake Russian phone number"""
        return f"+7 ({random.randint(900, 999)}) {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"


class EmailGenerator:
    """Generate temporary email addresses"""

    DOMAINS = [
        'tempmail.com', 'mailinator.com', '10minutemail.com',
        'throwaway.email', 'temp-mail.org', 'guerrillamail.com'
    ]

    @staticmethod
    def generate():
        """Generate temporary email"""
        loading_animation(1)

        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(EmailGenerator.DOMAINS)
        email = f"{username}@{domain}"

        print_success(f"Сгенерирована временная почта:")
        print(f"  Email: {email}")

        # Generate password for this email
        password = PasswordGenerator.generate(print_result=False)
        print(f"  Пароль: {password}")

        # Calculate expiration
        expiration = datetime.now() + timedelta(minutes=10)
        print(f"  Истекает: {expiration.strftime('%H:%M:%S')}")

        return {'email': email, 'password': password, 'expires': expiration}

    @staticmethod
    def generate_bulk(count=5):
        """Generate multiple temporary emails"""
        print_info(f"Генерирование {count} временных почт...")
        emails = []
        for _ in range(count):
            emails.append(EmailGenerator.generate())
        return emails


class PasswordGenerator:
    """Generate secure passwords"""

    @staticmethod
    def generate(length=16, include_special=True, print_result=True):
        """
        Generate random password

        Args:
            length: Password length
            include_special: Include special characters
            print_result: Print result to console

        Returns:
            Generated password
        """
        loading_animation(1)

        characters = string.ascii_letters + string.digits
        if include_special:
            characters += "!@#$%^&*_+-="

        password = ''.join(secrets.choice(characters) for _ in range(length))

        if print_result:
            print_success(f"Сгенерирован пароль:")
            print(f"  Пароль: {password}")
            print(f"  Длина: {len(password)}")
            print(f"  Сложность: {'HIGH' if include_special else 'MEDIUM'}")

        return password

    @staticmethod
    def generate_passphrase():
        """Generate password from words"""
        words = [
            'красивый', 'быстрый', 'сильный', 'золотой', 'умный',
            'верный', 'смелый', 'добрый', 'честный', 'светлый',
            'гром', 'волк', 'лев', 'орел', 'сокол',
            'луна', 'солнце', 'звезда', 'огонь', 'вода'
        ]

        loading_animation(1)

        passphrase = '-'.join(random.choices(words, k=4))

        print_success(f"Сгенерирована парольная фраза:")
        print(f"  Фраза: {passphrase}")
        print(f"  Длина: {len(passphrase)}")

        return passphrase


class BanWordGenerator:
    """Generate ban words for various services"""

    PREFIXES = ['super', 'mega', 'ultra', 'hyper', 'cyber', 'neo']
    ROOTS = ['vortex', 'nexus', 'phoenix', 'dragon', 'shadow', 'phantom', 'specter']
    SUFFIXES = ['_elite', '_pro', '_ultra', '_force', '_master']

    @staticmethod
    def generate():
        """Generate ban word"""
        loading_animation(1)

        ban_word = (
            random.choice(BanWordGenerator.PREFIXES) +
            random.choice(BanWordGenerator.ROOTS) +
            random.choice(BanWordGenerator.SUFFIXES)
        )

        print_success(f"Сгенерировано BAN-слово:")
        print(f"  Слово: {ban_word}")

        return ban_word

    @staticmethod
    def generate_multiple(count=5):
        """Generate multiple ban words"""
        print_info(f"Генерирование {count} BAN-слов...")
        words = []
        for _ in range(count):
            word = (
                random.choice(BanWordGenerator.PREFIXES) +
                random.choice(BanWordGenerator.ROOTS) +
                random.choice(BanWordGenerator.SUFFIXES)
            )
            words.append(word)

        for word in words:
            print(f"  - {word}")

        return words


class ProxyGenerator:
    """Generate proxy server configurations"""

    PROXY_TYPES = ['HTTP', 'HTTPS', 'SOCKS5', 'SOCKS4']

    @staticmethod
    def generate():
        """Generate proxy configuration"""
        loading_animation(1)

        proxy_type = random.choice(ProxyGenerator.PROXY_TYPES)
        host = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        port = random.choice([3128, 8080, 9090, 1080, 8888])

        # Generate credentials
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        password = PasswordGenerator.generate(length=12, print_result=False)

        proxy_config = {
            'type': proxy_type,
            'host': host,
            'port': port,
            'username': username,
            'password': password
        }

        print_success(f"Сгенерирована конфигурация прокси:")
        print(f"  Тип: {proxy_type}")
        print(f"  Host: {host}")
        print(f"  Port: {port}")
        print(f"  Username: {username}")
        print(f"  Password: {password}")

        return proxy_config

    @staticmethod
    def generate_multiple(count=5):
        """Generate multiple proxy configurations"""
        print_info(f"Генерирование {count} прокси конфигураций...")
        proxies = []
        for _ in range(count):
            proxies.append(ProxyGenerator.generate())
        return proxies
