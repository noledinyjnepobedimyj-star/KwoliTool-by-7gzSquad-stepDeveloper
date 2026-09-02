"""
Animation utilities for KWOLI TOOL splash screen
"""

import os
import sys
import time
from kwoli_tool.config import Colors, ANIMATION_SPEED, MESSAGES
from kwoli_tool.ui.colors import (
    create_animated_gradient, 
    center_text, 
    remove_ansi_codes,
    bold_gradient,
    apply_gradient
)


def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_animated_splash():
    """
    Print animated splash screen with KWOLI ASCII art logo
    """
    clear_screen()

    # ASCII Art Logo with gradient
    ascii_logo = [
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

    max_frames = 8

    # Animation loop
    for frame in range(max_frames * 3):  # Run animation multiple times
        clear_screen()

        print("\n" * 3)

        # Apply gradient to each line of ASCII art
        for i, line in enumerate(ascii_logo):
            # Shift the gradient for animation effect
            gradient_colors = [
                Colors.GREEN,
                Colors.BRIGHT_GREEN,
                Colors.CYAN,
                Colors.BRIGHT_CYAN,
                Colors.BLUE,
                Colors.BRIGHT_BLUE,
            ]

            # Rotate colors based on frame and line
            shifted_colors = gradient_colors[(i + frame) % len(gradient_colors):]
            shifted_colors += gradient_colors[:(i + frame) % len(gradient_colors)]

            # Apply color to line
            colored_line = ""
            for char_idx, char in enumerate(line):
                color = shifted_colors[char_idx % len(shifted_colors)]
                colored_line += f"{color}{char}"
            colored_line += Colors.RESET

            # Center and print
            centered = center_text(colored_line, width=120)
            print(centered)

        # Print subtitle
        subtitle = f"{Colors.MAGENTA}{Colors.BOLD}⭐ Advanced Search & Generation Tool ⭐{Colors.RESET}"
        centered_subtitle = center_text(subtitle, width=120)
        print("\n" * 2)
        print(centered_subtitle)

        # Print instruction at bottom
        instruction = f"{Colors.YELLOW}{Colors.BOLD}{MESSAGES['press_enter']}{Colors.RESET}"
        centered_instruction = center_text(instruction, width=120)
        print("\n" * 3)
        print(centered_instruction)

        time.sleep(ANIMATION_SPEED)

    # Wait for user to press Enter
    input()


def print_header():
    """
    Print static header with KWOLI ASCII art at the top of main menu
    """
    clear_screen()

    # Compact version of ASCII art for header
    ascii_header = [
        "██ ▄█▀ █     █░ ▒█████   ██▓     ██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓",
        " ██▄█▒ ▓█░ █ ░█░▒██▒  ██▒▓██▒    ▓██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒",
        "▓███▄░ ▒█░ █ ░█ ▒██░  ██▒▒██░    ▒██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░",
        "▓██ █▄ ░█░ █ ░█ ▒██   ██░▒██░    ░██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░",
        "▒██▒ █▄░░██▒██▓ ░ ████▓▒░░██████▒░██░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒",
        "▒ ▒▒ ▓▒░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░▓  ░░▓       ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░",
        "░ ░▒ ▒░  ▒ ░ ░    ░ ▒ ▒░ ░ ░ ▒  ░ ▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░",
        "░ ░░ ░   ░   ░  ░ ░ ░ ▒    ░ ░    ▒ ░     ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░",
        "░  ░       ░        ░ ░      ░  ░ ░                  ░ ░      ░ ░      ░  ░",
        "",
        "made by 7GZ SQUAD & @stepDeveloper",
        "ни в коем случае не несу за твои действия ответственность",
        "проект написан в учебных и познавательских намерениях",
        ]
    print("\n")

    # Print header with gradient colors
    for line in ascii_header:
        # Apply green-cyan-blue gradient
        gradient_colors = [
            Colors.BRIGHT_GREEN,
            Colors.BRIGHT_CYAN,
            Colors.BRIGHT_BLUE,
        ]

        colored_line = ""
        for char_idx, char in enumerate(line):
            color = gradient_colors[char_idx % len(gradient_colors)]
            colored_line += f"{color}{char}"
        colored_line += Colors.RESET

        centered = center_text(colored_line, width=120)
        print(centered)

    print(f"\n{Colors.BRIGHT_CYAN}{'=' * 80}{Colors.RESET}".center(120))
    print()


def print_menu(items):
    """
    Print menu items

    Args:
        items: List of menu items to display
    """
    for i, item in enumerate(items, 1):
        print(f"{Colors.BRIGHT_CYAN}{i:2d}. {Colors.RESET}{Colors.WHITE}{item}{Colors.RESET}")

    print()
    print(f"{Colors.RED}{'Q'}. Выход{Colors.RESET}")
    print()


def print_separator():
    """Print a decorative separator"""
    separator = f"{Colors.CYAN}{'=' * 60}{Colors.RESET}"
    print(separator)


def print_error(message):
    """
    Print error message

    Args:
        message: Error message to display
    """
    print(f"\n{Colors.RED}{Colors.BOLD}❌ Ошибка: {message}{Colors.RESET}\n")


def print_success(message):
    """
    Print success message

    Args:
        message: Success message to display
    """
    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ {message}{Colors.RESET}\n")


def print_info(message):
    """
    Print info message

    Args:
        message: Info message to display
    """
    print(f"\n{Colors.BRIGHT_CYAN}ℹ️  {message}{Colors.RESET}\n")


def print_input_field(prompt):
    """
    Print input field with styling

    Args:
        prompt: Input prompt text

    Returns:
        User input
    """
    styled_prompt = f"{Colors.BRIGHT_GREEN}➜ {prompt}{Colors.RESET}: "
    return input(styled_prompt)


def loading_animation(duration=2):
    """
    Show loading animation

    Args:
        duration: Duration of loading animation in seconds
    """
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    start_time = time.time()
    frame_idx = 0

    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Colors.CYAN}{frames[frame_idx % len(frames)]} Загрузка...{Colors.RESET}")
        sys.stdout.flush()
        frame_idx += 1
        time.sleep(0.1)

    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()


def wait_for_enter(message="Нажмите ENTER для продолжения..."):
    """
    Wait for user to press Enter

    Args:
        message: Message to display
    """
    input(f"\n{Colors.YELLOW}{message}{Colors.RESET}")
