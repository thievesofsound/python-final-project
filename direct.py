import modules
from output import *
import dill
from rich import get_console
from rich.console import Console
from easter_eggs import wearinessTimeOut, shutdownComputer
from minigames import puzzle_minigame, battle_minigame, immigration_gaurds
import random
import time
import rich
import datetime
import atexit

getting_on_train = modules.ListOfOptions(
    [
        modules.Option(
            lambda: OptionMessage(
                (
                    "Choosing this option proves risky, but is efficient.\n"
                    "You exit your front door and tiptoe to avoid being seen.\n\n"
                    "The cops does see you but you are able to hide in some bushes a few blocks down.\n"
                    "After they left, you start your journey to the train station and arrive at 8:52AM\n"
                    "This decision has given you some time before the train arrives.\n"
                    "You decide to sleep a little before the train arrives\n"
                    "Some time passes and it's 9:00 AM, and true to word, the train arrives and with that, your adventure begins.\n"
                ),
                modules.change_state.CONTINUE,
            ),
            "Try to sneak around surrounding officers on the block to walk to the train ",
        ),
        modules.Option(
            lambda: OptionMessage(
                "Diversion does not work as the officers still capture you. You are in prison.",
                modules.change_state.CHECKPOINT,
            ),
            "Create a diversion outside  ",
        ),
        modules.Option(
            lambda: OptionMessage(
                "Officers leave and you are able to make it to the train station with 5 minutes to spare.",
                modules.change_state.CONTINUE,
            ),
            "Wait until rush hour for them to leave",
        ),
    ],
    "Astana, Kazakhstan is a country located in Asia and is known for its modernistic and futuristic architecture.\nThough its beauty is undeniable, the state of living is struggling,\nas anti-government militias are on the rise in Kazakhstan and placing various cities under strict rule. \nAstana is one of them. To escape, you must hitch a train to the US in the morning to avoid forced labor.\n\n\n",
    "It is 6:32 AM. Walking to a train station will take 2 hours on foot and the last train to the US before hell breaks loose is 9:00AM.\nPeople are scrambling to escape, but rush hour is at 7:30AM.\nYou can make time. What do you do?"
)

siberia = modules.ListOfOptions(
    [
        modules.Option(
            lambda: OptionMessage(
                "You follow the path, and are able to evade Russian capture and hide out in an abandoned cabin near the Russian border",
                modules.change_state.CONTINUE,
            ),
            "1. Follow the abandoned rail tunnels at night",
        ),
        modules.Option(
            lambda: OptionMessage(
                "As you travel, a blizzard hits you. The blizzard leaves you incapacitated for weeks and are unable to move on. This is your fate.",
                modules.change_state.CHECKPOINT,
            ),
            "2. Travel through the snowy forests on foot",
        ),
    ],
    (
        "The train from Astana only takes you so far—it ends at Novosibirsk, deep in Siberia. \n"
        "From here, you’ll need to traverse thousands of kilometers through ice, forests, and secret rail lines to reach the Russian Far East."
    ),
    "It’s -12 degrees. Supplies are scarce. A map offers two possible routes forward:",
)
games = modules.Story(
    [
        modules.Start(
            lambda: OptionMessage("<<start game>>")
        ),
        # beginning of Story I
        getting_on_train,
        siberia,
        modules.Checkpoint(
            "Placeholder",
            "This minigame will involve a randomly generated code to move on to the next path\nYou are given 3 tries. If you fail, the alarm will ‘sound’ and the game is over.",
            puzzle_minigame,
        ),
        modules.ListOfOptions(
            [
                modules.Option(
                    lambda: OptionMessage("R bozo", modules.change_state.CHECKPOINT), #TODO: Change these to actual data
                    "1. Attempt to cross the ice at night",
                ),
                modules.Option(
                    lambda: OptionMessage("L Bozo", modules.change_state.CONTINUE), "2. Sneak onto a docked cargo ship" #TODO: change these to actual data
                ),
            ],
            "After the battle, you are left with no choice but to find a way to get to the U.S.",
        ),
        modules.Checkpoint(
            "Placeholder",
            "On the cargo ship, you spot something underneath the water circling your ship\nIt’s Wailord! The biggest water type Pokemon ever and he is angry.\nHe has 300 health, and in this battle, your health is regenerated to 100. Beat him in 3 moves or perish",
            lambda: (battle_minigame(player)),
        ),
        modules.ListOfOptions(
            [
                modules.Option(
                    lambda: OptionMessage("On your hitchhiking journey, a trucker spots you and offers you a trip to Vancouver.\nYou are immensely grateful, but know that you need at least two more rides to reach the US Border.\n 2 hours later you arrive at the border.",modules.change_state.CONTINUE), "1. Hitchhike down through Canada and into the U.S."
                ),
                modules.Option(
                    lambda: OptionMessage("You are somehow hired, and create excuses for the lack of an id and SSN card.\nYou work this job and don't make a lot of money, and on top of that, a rumor spreads around your workplace hinting at your immigration status.\nUnfortunately, immigration agents raid the vessel, and you are identified as an illegal immigrant. \nYou are now among the detention center with thousands of others who have been caught in the US.",modules.change_state.CHECKPOINT),
                    "2. Take a job on a fishing vessel to fund a bus trip south",
                ),
            ],
            "Alaska is cold and suspicious. You have no ID, no money, no allies. The U.S. may be free—but it’s not easy. Your goal is California. How do you get there?",
        ),
        modules.Checkpoint(
            "Placeholder",
            (
                "Due to recent events, every person in the US is subject to ID checks.\n"
                "Conveniently though, there has been a veteran who was buried recently with all of his possessions, including his empty passport.\n"
                "One issue tho, b/c he was a high ranking general, his gravesite is guarded 24/7 and you must make your way across the graveyard.\n"
            ),
            lambda: immigration_gaurds(player),
        ),
        # End of story I
        modules.End(lambda x: slow_print("You have finished! Good work getting this far."), "Placeholder")
    ]
)


def exitGame(player):
    def func():
        dill.dump(player, open("direct.p", "wb"))
        print("Files have been saved, press q to fully exit.")
        while True:
            if modules.quit_loop() == True:
                break

    return func



player = modules.import_game_state()
player.play(games)

atexit.register(exitGame(player))

while True:
    match player.state:
        case modules.ListOfOptions():
            prompt = OptionPrompt(player.state.options, player.state.question, player.state.prompt, player)
            result = prompt.action()
            console = get_console()
            console.print("[bold red]Press Q to move forward.", justify="center")
            while True:
                if modules.quit_loop() == True:
                    break
            match result:
                case modules.change_state.CONTINUE:
                    player.state = games.path[games.path.index(player.state) + 1]
                case modules.change_state.CHECKPOINT:
                    slow_print("Moving Back to Last Checkpoint.You become more weary.\nPress q to start checkpoint.")
                    while True:
                        if modules.quit_loop() == True:
                            break
                    player.weariness -= 10
                    player.state = player.checkpoint
        case modules.Checkpoint():
            player.checkpoint = player.state
            CheckpointMessage(player.state)
            result = player.state.minigame()
            match result:
                case modules.change_state.CONTINUE:
                    player.state = games.path[games.path.index(player.state) + 1]
                case modules.change_state.CHECKPOINT:
                    player.state = player.checkpoint
        case modules.End():
            player.state.action()
            os.system("rm direct.p")
            shutdownComputer()
        case modules.Start():
            player.state.action()
            player.state = games.path[games.path.index(player.state) + 1]
    if player.weariness <= 0:
        wearinessTimeout()
        break