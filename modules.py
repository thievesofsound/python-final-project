from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
import rich
from rich.progress import Progress, TextColumn, BarColumn
from rich.pretty import pprint
from operator import attrgetter
from dataclasses import dataclass
from rich.columns import Columns
from output import *
from enum import Enum, auto
from datetime import datetime
import dill

try:
    import msvcrt as getch
except:
    import getch

# Import necessary modules from the rich library for terminal formatting and display.
# Also imports `attrgetter` for efficient attribute access and `dataclass` for creating simple data classes.


class change_state(Enum):
    CONTINUE = auto()
    CHECKPOINT = auto()


class Option:
    """
    Class for creating option:
    - Options cotain:
        -action -> what they are going to do
        - Description -> the string based output
    """

    def __init__(self, action, description):
        # Initializes an Option object with an action (what happens when chosen) and a description (how it's displayed).
        self.action = action
        self.description = description

    def __str__(self):
        # Defines the string representation of an Option, which is its description.
        return self.description

    def action(self):
        # Placeholder method for the action to be performed.
        pass


class Checkpoint:
    # create a checkpoint that can be used to save the game to a file(txt), also contains a minigame
    def __init__(self, name, description, minigame):
        # Initializes a Checkpoint object with a name, description, and associated minigame.
        self.name = name
        self.description = description
        self.minigame = minigame


class Start:
    def __init__(self, action):
        self.action = action

    # create a start that can be used to start the game(checkpoint without game), and set the seed of the game(also setup player)


# Placeholder class for the game's starting point.


class End:
    # create a end that can be used to end the game(brings back to main menu(not implemented yet))
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # Initializes an End object with a name and description.
    def action(self):
        pass


# Placeholder class for the game's ending point.


class ListOfOptions:
    """
    Chooses Option For Us(list with question, and prompt):
    - options
    - question
    - prompt
    """

    def __init__(self, options, question, prompt="Here are your options"):
        # Initializes with a list of options, a question, and an optional prompt.
        self.options = options
        self.question = question
        self.prompt = prompt
        self.options.append(
            Option(exit_game, "Exit the game and save progress")
        )


def exit_game():
    """Exits the game."""
    sys.exit()


class Story:
    # Simple class to represent a story with a path (presumably a list of story nodes or checkpoints).
    def __init__(self, path):
        self.path = path

def import_inventory(items):
    try:
        with open("inventory.p", "rb") as f:
            inventory = dill.load(f)
    except FileNotFoundError:
        inventory = Inventory(items)
    return inventory

# Class to represent the player character.
class Player:
    def __init__(self, name, items=[]):
        self.name = name
        self.current_story = ["blank story"]
        self.state = self.current_story[0]
        self.checkpoint = None
        self.DateTime = None

        self.inventory = import_inventory(items)
        self.weariness = 100
        self.health = 100

    def play(self, story):
        # Sets the player's current story and initial state/checkpoint.
        self.current_story = story
        self.checkpoint = self.current_story.path[0]
        self.state = self.current_story.path[0]


@dataclass
class InventoryItem:
    # Dataclass to represent an item in the player's inventory.
    name: str
    description: str
    quantity: int


# Class to manage the player's inventory.
class Inventory:
    # Initializes the inventory with an optional list of starting items.
    def __init__(self, items=[]):
        self.items = items

    def clear_null_entries(self):
        self.items = list(filter(filter_condition, self.items))
    
    def filter_condition(self, item):
        def filter(item):
            return True if item.quantity > 0 else False
        return filter
    def add_item(self, item):
        for index, inventory_item in self.items:
            # Checks if the item already exists in the inventory and increments the quantity if it does.
            if inventory_item.name == item.name:
                inventory_item.quantity += 1
                break
        else:
            self.items.append(item)
    
    def save_inventory(self):
        dill.dump(self, open("inventory.p", "wb"))
    def remove_item(self, item_to_remove):
        self.clear_null_entries()
        # Removes an item from the inventory by decrementing its quantity, ensuring quantity doesn't go below zero.

        for index, item in enumerate(self.items()):
            if item_to_remove.name == item:
                item_to_remove.quantity -= 1 if item_to_remove.quantity > 0 else 0


def quit_loop():
    while True:
        char = getch.getch()  # User input, but not displayed on the screen
        if char == "q":
            return True

def import_game_state():
    try:
        with open("direct.p", "rb") as f:
            player = dill.load(f)
    except FileNotFoundError:
        player = modules.Player("name")
    
    return player