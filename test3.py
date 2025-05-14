from rich.console import Console
import time
import shutil
import os
import sys


def move_cursor(row: int, col: int):
    # ANSI escape code to move the cursor
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()

def typewriter_centered_multiline(text: str, delay: float = 0.05):
    console = Console()
    lines = text.split('\n')
    term_width = shutil.get_terminal_size().columns
    term_height = shutil.get_terminal_size().lines

    # Calculate vertical starting position to center the block
    start_line = (term_height - len(lines)) // 2

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    for i, line in enumerate(lines):
        buffer = ""
        for j, char in enumerate(line):
            buffer += char
            # Calculate centered horizontal position
            x = (term_width - len(buffer)) // 2 + 1  # ANSI columns start at 1
            y = start_line + i + 1                   # ANSI rows start at 1
            move_cursor(y, x)
            console.print(buffer, end='', highlight=False, soft_wrap=True)
            time.sleep(delay)

    print()  # Final line break after animation

# Example usage
multi_line_text = """\
Welcome to the System
Loading environment...
Ready to launch."""

typewriter_centered_multiline(multi_line_text, delay=0.05)
