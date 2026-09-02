"""
Color utilities and gradient generation for KWOLI TOOL
"""

from kwoli_tool.config import Colors

def apply_gradient(text, gradient_colors=None):
    """
    Apply gradient coloring to text character by character

    Args:
        text: The text to colorize
        gradient_colors: List of color codes to cycle through

    Returns:
        Gradient-colored text string
    """
    if gradient_colors is None:
        gradient_colors = Colors.GRADIENT_GREEN_BLUE

    result = ""
    for i, char in enumerate(text):
        color = gradient_colors[i % len(gradient_colors)]
        result += f"{color}{char}"

    result += Colors.RESET
    return result


def create_animated_gradient(text, frame_num, max_frames=6):
    """
    Create animated gradient effect by shifting colors

    Args:
        text: The text to animate
        frame_num: Current frame number
        max_frames: Total number of frames for animation

    Returns:
        Gradient-colored text string
    """
    gradient = Colors.GRADIENT_GREEN_BLUE
    shifted_gradient = gradient[frame_num % len(gradient):] + gradient[:frame_num % len(gradient)]
    return apply_gradient(text, shifted_gradient)


def colorize(text, color_code):
    """
    Apply a single color to text

    Args:
        text: The text to colorize
        color_code: ANSI color code

    Returns:
        Colored text string
    """
    return f"{color_code}{text}{Colors.RESET}"


def bold_gradient(text):
    """
    Apply bold gradient to text
    """
    result = f"{Colors.BOLD}"
    result += apply_gradient(text)
    return result


def center_text(text, width=None):
    """
    Center text in terminal (approximate)

    Args:
        text: Text to center
        width: Terminal width (default: 80)

    Returns:
        Centered text
    """
    if width is None:
        width = 80

    # Count only printable characters (excluding ANSI codes)
    printable_len = len(remove_ansi_codes(text))
    padding = (width - printable_len) // 2
    return " " * padding + text


def remove_ansi_codes(text):
    """
    Remove ANSI color codes from text for length calculation

    Args:
        text: Text with ANSI codes

    Returns:
        Clean text without ANSI codes
    """
    import re
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def print_centered(text, color=None, bold=False):
    """
    Print text centered in terminal

    Args:
        text: Text to print
        color: Optional color code
        bold: Whether to make text bold
    """
    if color:
        text = colorize(text, color)
    if bold:
        text = f"{Colors.BOLD}{text}"

    centered = center_text(text)
    print(centered)
