#!/usr/bin/env python3
"""
Демонстрация ASCII логотипа KWOLI TOOL
"""

import sys
import os
import time

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from kwoli_tool.config import Colors, ASCII_LOGO
from kwoli_tool.ui.colors import center_text

def demo_logo_animation():
    """Демонстрация анимированного логотипа"""

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n" * 3)
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}".center(120))
    print("Демонстрация ASCII ART логотипа KWOLI TOOL".center(120))
    print(f"{Colors.RESET}\n")

    # Gradient colors
    gradient_colors = [
        Colors.BRIGHT_GREEN,
        Colors.GREEN,
        Colors.CYAN,
        Colors.BRIGHT_CYAN,
        Colors.BLUE,
        Colors.BRIGHT_BLUE,
    ]

    # Animation demo
    for frame in range(6):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" * 2)

        # Print animated logo
        for line_idx, line in enumerate(ASCII_LOGO):
            colored_line = ""
            for char_idx, char in enumerate(line):
                # Change color based on frame and position
                color_idx = (char_idx + frame + line_idx) % len(gradient_colors)
                color = gradient_colors[color_idx]
                colored_line += f"{color}{char}"
            colored_line += Colors.RESET

            centered = center_text(colored_line, width=120)
            print(centered)

        # Info
        print(f"\n{Colors.CYAN}⭐ Advanced Search & Generation Tool ⭐{Colors.RESET}".center(120))
        print(f"\n{Colors.YELLOW}Frame: {frame + 1}/6{Colors.RESET}".center(120))

        time.sleep(0.5)

    print(f"\n\n{Colors.GREEN}✓ Демонстрация завершена!{Colors.RESET}".center(120))
    print(f"\n{Colors.BRIGHT_CYAN}Запустите приложение: python run.py{Colors.RESET}".center(120))
    print()


if __name__ == "__main__":
    try:
        demo_logo_animation()
    except KeyboardInterrupt:
        print("\n\nОтмена.")
        sys.exit(0)
