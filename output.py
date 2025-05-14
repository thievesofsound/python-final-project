import time
import modules
from rich.text import Text
from rich.console import Console, Group
from rich import get_console
from rich.table import Table
from rich.panel import Panel
import rich
from rich.progress import Progress, TextColumn, BarColumn
from rich.pretty import pprint
from operator import attrgetter
from dataclasses import dataclass
from rich.columns import Columns
from rich.align import Align
import shutil
import os
import sys

def move_cursor(row: int, col: int):
    # ANSI escape code to move the cursor
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()

def slow_print(text: str, delay: float = 0.05):
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



def OptionPrompt(options_list: list, question: str, prompt_text: str, player):
    """Generate and ask prompt for option"""
    console = Console()
    console.clear()
    console.print(
        option_layout_data(options_list, question, prompt_text, player),
        justify="center"
    )
    while True:
        try:
            prompt = input("Enter an Option: ")
            if int(prompt) - 1 not in [i for i in range(0, len(options_list))]:
                raise ValueError
        except:
            console.clear()
            slow_print("Invalid input")
            time.sleep(1)
            console.clear()
            console.print(
                option_layout_data(options_list, question, prompt_text, player),
                justify="center"
            )
        else:
            return options_list[int(prompt) - 1]


def CheckpointMessage(description_text: str):
    slow_print(description_text)


def OptionMessage(message, return_value=True):
    slow_print(message)
    return return_value



def default_layout(player, chicken_wings):
    """ """
    table = Table.grid()
    table.add_column()
    table.add_column(max_width=40)
    table.add_row(
        chicken_wings, Group(inventory_output(player.inventory.items), progress(player))
    )
    return Panel(table)


def progress(player):
    p = Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    p.add_task("Weariness:", total=100, completed=player.weariness)
    return p


def option_layout_data(options_list: list, question: str, prompt_text: str, player) -> Table:
    """
    This function creates a layout for the options
    Args:
        listofoptions: a ListOfOptions instance
    Returns:
        A grid object
    """

    return default_layout(player, print_list_options(options_list, question, prompt_text))


def print_list_options(listofoptions, question, prompt):
    text = ""
    for index, option in enumerate(listofoptions, 1):
        text += f"\n{index}. {option.description}"
    return Panel(
        Group(
            Text(question),
            Text(prompt),
            Text(text),
        )
    )


def selection_menu():
    pass


def expanded_inventory_output(item_list):
    # Uses attrgetter for efficient extraction of specified attributes from InventoryItem objects.
    unpack = attrgetter("name", "description", "quantity")

    # Generates a rich.Table to display the contents of the inventory.
    table = Table(title="Inventory List")
    table.add_column("Name")
    table.add_column("Description")
    table.add_column("Quantity")
    for item in item_list:
        item_unpacked = map(lambda x: str(x), unpack(item))
        table.add_row(*item_unpacked)
    return table


def inventory_output(item_list):
    # Uses attrgetter for efficient extraction of specified attributes from InventoryItem objects.
    unpack = attrgetter("name", "quantity")

    # Generates a rich.Table to display the contents of the inventory.
    table = Table(title="Inventory List")
    table.add_column("Name")
    table.add_column("Quantity")
    for item in item_list:
        item_unpacked = map(lambda x: str(x), unpack(item))
        table.add_row(*item_unpacked)
    return table
