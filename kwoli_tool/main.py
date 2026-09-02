"""
KWOLI TOOL - Advanced Search and Generation Tool
Main application file
"""

import os
import sys

# Allow `python kwoli_tool/main.py` (package imports need the repo root on sys.path)
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)


def configure_console():
    """Enable UTF-8 and ANSI colors on Windows so the ASCII logo can print."""
    if sys.platform != "win32":
        return
    try:
        os.system("chcp 65001 >nul")
    except Exception:
        pass
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    try:
        from colorama import just_fix_windows_console
        just_fix_windows_console()
    except Exception:
        try:
            from colorama import init
            init()
        except Exception:
            pass


configure_console()

from kwoli_tool.config import MENU_ITEMS, MESSAGES, Colors
from kwoli_tool.ui.animation import (
    print_animated_splash,
    print_header,
    print_menu,
    print_error,
    print_success,
    print_info,
    print_input_field,
    wait_for_enter,
    clear_screen
)

# Import all modules
from kwoli_tool.modules.searchers import (
    IPSearcher,
    PhoneSearcher,
    TelegramSearcher,
    WebsiteSearcher,
    NicknameSearcher,
    DiscordSearcher,
    RobloxSearcher,
    WebCrawler
)

from kwoli_tool.modules.generators import (
    FakePersonGenerator,
    EmailGenerator,
    PasswordGenerator,
    BanWordGenerator,
    ProxyGenerator
)

from kwoli_tool.modules.utilities import (
    AnonymityManual,
    HallOfFame,
    AnonymityTips
)


class KWOLITool:
    """Main KWOLI TOOL application class"""

    def __init__(self):
        self.running = True

    def show_splash_screen(self):
        """Show animated splash screen"""
        print_animated_splash()

    def show_main_menu(self):
        """Show main menu and handle user input"""
        while self.running:
            print_header()

            print(f"{Colors.WHITE}Выберите функцию:{Colors.RESET}\n")
            print_menu(MENU_ITEMS)

            choice = input(f"{Colors.BRIGHT_GREEN}➜ Выбор{Colors.RESET}: ").strip().upper()

            if choice == 'Q':
                self.exit_app()
                break

            try:
                choice_num = int(choice)
                if 1 <= choice_num <= len(MENU_ITEMS):
                    self.handle_menu_choice(choice_num)
                else:
                    print_error(f"Выберите число от 1 до {len(MENU_ITEMS)}")
                    wait_for_enter()
            except ValueError:
                print_error("Пожалуйста введите число или Q для выхода")
                wait_for_enter()

    def handle_menu_choice(self, choice_num):
        """Handle menu choice"""
        clear_screen()

        # 1. IP Search
        if choice_num == 1:
            ip = print_input_field("Введите IP адрес")
            if ip:
                IPSearcher.search(ip)
            wait_for_enter()

        # 2. Phone Search
        elif choice_num == 2:
            phone = print_input_field("Введите номер телефона")
            if phone:
                PhoneSearcher.search(phone)
            wait_for_enter()

        # 3. Telegram Search
        elif choice_num == 3:
            username = print_input_field("Введите Telegram username, ID или ссылку t.me")
            if username:
                TelegramSearcher.search(username)
            wait_for_enter()

        # 4. Website Search
        elif choice_num == 4:
            url = print_input_field("Введите URL сайта")
            if url:
                WebsiteSearcher.search(url)
            wait_for_enter()

        # 5. Nickname Search
        elif choice_num == 5:
            nickname = print_input_field("Введите никнейм")
            if nickname:
                NicknameSearcher.search(nickname)
            wait_for_enter()

        # 6. Discord Search
        elif choice_num == 6:
            username = print_input_field("Введите Discord username")
            if username:
                DiscordSearcher.search(username)
            wait_for_enter()

        # 7. Roblox Search
        elif choice_num == 7:
            username = print_input_field("Введите Roblox username")
            if username:
                RobloxSearcher.search(username)
            wait_for_enter()

        # 8. WebCrawler
        elif choice_num == 8:
            url = print_input_field("Введите URL для краулинга")
            if url:
                depth = input(f"{Colors.BRIGHT_GREEN}➜ Глубина краулинга (1-3){Colors.RESET}: ").strip()
                try:
                    depth = min(3, max(1, int(depth)))
                except:
                    depth = 1
                WebCrawler.crawl(url, depth)
            wait_for_enter()

        # 9. Proxy Generator
        elif choice_num == 9:
            print_info("Генерирование прокси конфигурации...")
            ProxyGenerator.generate()
            wait_for_enter()

        # 10. Fake Person Generator
        elif choice_num == 10:
            person = FakePersonGenerator.generate()
            print()
            # Also generate email for this person
            email_data = EmailGenerator.generate()
            wait_for_enter()

        # 11. Email Generator
        elif choice_num == 11:
            count_input = input(f"{Colors.BRIGHT_GREEN}➜ Количество почт (1-10){Colors.RESET}: ").strip()
            try:
                count = min(10, max(1, int(count_input)))
            except:
                count = 1

            if count == 1:
                EmailGenerator.generate()
            else:
                EmailGenerator.generate_bulk(count)
            wait_for_enter()

        # 12. Password Generator
        elif choice_num == 12:
            print_info("Выберите тип пароля:")
            print(f"{Colors.CYAN}1. Обычный пароль (16 символов){Colors.RESET}")
            print(f"{Colors.CYAN}2. Длинный пароль (32 символа){Colors.RESET}")
            print(f"{Colors.CYAN}3. Парольная фраза{Colors.RESET}")

            pwd_choice = input(f"{Colors.BRIGHT_GREEN}➜ Выбор{Colors.RESET}: ").strip()

            if pwd_choice == '1':
                PasswordGenerator.generate(16)
            elif pwd_choice == '2':
                PasswordGenerator.generate(32)
            elif pwd_choice == '3':
                PasswordGenerator.generate_passphrase()
            else:
                PasswordGenerator.generate(16)

            wait_for_enter()

        # 13. Ban Word Generator
        elif choice_num == 13:
            print_info("Выберите количество BAN-слов:")
            print(f"{Colors.CYAN}1. Одно слово{Colors.RESET}")
            print(f"{Colors.CYAN}2. Пять слов{Colors.RESET}")
            print(f"{Colors.CYAN}3. Десять слов{Colors.RESET}")

            bw_choice = input(f"{Colors.BRIGHT_GREEN}➜ Выбор{Colors.RESET}: ").strip()

            if bw_choice == '1':
                BanWordGenerator.generate()
            elif bw_choice == '2':
                BanWordGenerator.generate_multiple(5)
            elif bw_choice == '3':
                BanWordGenerator.generate_multiple(10)
            else:
                BanWordGenerator.generate()

            wait_for_enter()

        # 14. Anonymity Manual
        elif choice_num == 14:
            clear_screen()
            print(f"\n{Colors.BOLD}{Colors.BRIGHT_CYAN}📖 Мануал по анонимности{Colors.RESET}\n")
            AnonymityManual.display()
            print()
            AnonymityTips.display()
            wait_for_enter()

        # 15. Hall of Fame
        elif choice_num == 15:
            clear_screen()
            print()
            HallOfFame.display()
            wait_for_enter()

    def exit_app(self):
        """Exit application"""
        clear_screen()
        goodbye = f"{Colors.BRIGHT_CYAN}Спасибо за использование KWOLI TOOL!{Colors.RESET}"
        print()
        print(goodbye.center(120))
        print()
        print(f"{Colors.GREEN}До свидания! 👋{Colors.RESET}".center(120))
        print()
        self.running = False

    def run(self):
        """Run application"""
        self.show_splash_screen()
        self.show_main_menu()


def main():
    """Main entry point"""
    try:
        app = KWOLITool()
        app.run()
    except KeyboardInterrupt:
        print()
        print_error("Приложение прервано пользователем")
        sys.exit(0)
    except Exception as e:
        try:
            print_error(f"Критическая ошибка: {str(e)}")
        except Exception:
            print(f"Critical error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
