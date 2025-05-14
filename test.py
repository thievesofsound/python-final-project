import os
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

console = Console()

# Game state
game_text = "You are in a forest. There's a path to the north."
stats_text = "Health: 100\nMana: 40\nInventory:\n- Sword\n- Potion"
user_input = ""

# Custom prompt style
prompt_style = Style.from_dict({
    "": "#ffffff bg:#333333",  # Default text style
    "prompt": "ansigreen",  # Prompt text style (green)
    "input": "ansicyan",    # Input text style (cyan)
    "border": "ansired",    # Border text style (red)
})

def clear_console():
    # Clear the console screen (cross-platform)
    os.system('cls' if os.name == 'nt' else 'clear')

def make_layout(game_text: str, stats_text: str) -> Layout:
    layout = Layout()

    # Split the screen into top and bottom boxes
    layout.split(
        Layout(name="top"),
    )

    # Split top into two columns: left (game), right (stats)
    layout["top"].split_row(
        Layout(Panel(game_text, title="Game"), name="game", ratio=4),
        Layout(Panel(stats_text, title="Stats & Inventory"), name="sidebar",ratio=1)
    )

    return layout

def print_game():
    # Clear the console and print the layout
    clear_console()

    # Make the layout with game and stats
    layout = make_layout(game_text, stats_text)

    # Print the layout to the console
    console.print(layout)

def main():
    global game_text
    global user_input

    while True:
        # Print the game UI with boxes
        print_game()

        # Get user input
        user_input = prompt("> ", style=prompt_style)

        # Process user input
        if user_input.lower() == "quit":
            break
        elif "north" in user_input.lower():
            game_text = "You walk north and arrive at a mysterious ruin."
        else:
            game_text = f"You said: {user_input}"

if __name__ == "__main__":
    main()
