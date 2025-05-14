import modules
from output import *
import dill
from rich import get_console
from rich.console import Console
from easter_eggs import wearinessTimeOut, shutdownComputer
from minigames import pharaoh_battle, storm_navigation
import random
import time
import rich
import datetime
import atexit

getting_on_flight = modules.ListOfOptions(
    [
        modules.Option(
            lambda: OptionMessage(
                (
                    "You are lucky enough to have hot wiring skills, as this allows you to take their car.\nThey do notice as their car alarm sirens wake them up.\nYou are able to make it to the airport and board your plane with no issues."
                ),
                modules.change_state.CONTINUE,
            ),
            "Steal your neighbor’s car and drive to the airport.",
        ),
        modules.Option(
            lambda: OptionMessage(
                "The earliest bus that arrives is at 9:30AM. You think nothing of it. \nThe bus comes and arrives. \nUnfortunately, the driver is drunk, and 10 minutes later, you face a head-on collision. \nEverybody except you dies. \nYou are now in the hospital suffering from internal decapitation, fractured skull, broken ribs, and every time you breathe it hurts. \nYou do your best to recover.",
                modules.change_state.CHECKPOINT,
            ),
            "Take the bus to the airport.",
        ),
    ],
    "Astana, Kazakhstan is a country located in Asia and is known for its modernistic and futuristic architecture.\nThough its beauty is undeniable, the state of living is struggling,\nas anti-government militias are on the rise in Kazakhstan and placing various cities under strict rule. \nAstana is one of them. To escape, you must hitch a plane to Egypt.\n\n\n",
    "The only available flight to Egypt is at 10:32AM.\nYou have no money, as most of your available funds went to the plane ticket. \nYou have no transportation to get to the airport other than yourself. What do you do?"
)

egypt = modules.ListOfOptions(
    [
        modules.Option(
            lambda: OptionMessage(
                "You slip into the alley’s shadows and time your approach. \nOne man lights a cigarette. The other turns away to count change.\nYou lunge, grab the briefcase, and sprint like your life depends on it. \nShouts echo behind you, but you vanish into a nearby rug shop. \nInside the briefcase is exactly $2,500 USD—you now have half your goal. \nWith quick thinking and street hustle, you flip it into $5,000 USD through clever exchanges and small trades. You’re ready for Morocco.",
                modules.change_state.CONTINUE,
            ),
            "Steal the briefcase while they're distracted",
        ),
        modules.Option(
            lambda: OptionMessage(
                "You approach humbly, explaining your situation and offering to help carry their goods for some cash.\nThey laugh, but agree to bring you along—for a “small task.”\nThat task turns out to be a drug run across downtown Cairo.\nOn the delivery, police storm the location. You’re arrested along with the gang.\nLabeled as a smuggler, you're now sitting in an Egyptian prison, with your journey at a dead stop.",
                modules.change_state.CHECKPOINT,
            ),
            "Ask the men for a cut of the money in exchange for labor",
        ),
    ],
    "You have arrived in Egypt! You relish in the grand landscape, and are anticipating greatness. \nBut then you realize, I have no money! You need at least $5000 to begin your next venture.  \nAs you wander through a marketplace, you overhear two men exchanging $2,500 USD for E£128,000 in a dim alley behind a spice vendor. \nTheir briefcase is open. No guards. No cameras. You consider your next move:",
)
pharoah_checkpoint = modules.Checkpoint(
    "Placeholder",
    "After stealing the briefcase and making your way, you believe you are home free.\nBut wait! Who is that formulating in that massive sand storm?\nLow and behold, it is THE MIGHTY PHARAOH and he wants to take your money AND your life!",
    lambda: (pharoah_checkpoint(player))
)
morocco = modules.ListOfOptions(
            [
                modules.Option(
                    lambda: OptionMessage("You slip inside a crate at night.\nMid-voyage, authorities inspect the cargo.\nYou are found, arrested, and deported back to Morocco. \n Your face is now flagged in international databases.", modules.change_state.CHECKPOINT), #TODO: Change these to actual data
                    "Hide in a shipping crate heading to Cádiz",
                ),
                modules.Option(
                    lambda: OptionMessage("You pay Samir and sneak onto a packed fishing boat.\n The waves are rough, but by sunrise, you reach Spain alive, wet, but free.\nYou move forward to Portugal, planning your next move.", modules.change_state.CONTINUE), "Board the smuggler's boat at midnight" #TODO: change these to actual data
                ),
            ],
            "After surviving Egypt, you’ve now made it to Tangier, Morocco—a gateway city between Africa and Europe.\nThe Atlantic Ocean glimmers to the west, and the Strait of Gibraltar lies to the north. \nYour goal is clear: find passage to Europe. The options are limited, and time is critical. \nImmigration authorities are cracking down on undocumented travelers, and you can feel eyes watching your every move.\n\n",
            "A shady contact at the harbor tells you that two ways exist to cross into Spain: by boarding a smuggler’s boat at midnight or hiding in a shipping crate bound for Cádiz. You weigh your options:"
        )
storm_navigate_checkpoint = modules.Checkpoint(
            "Placeholder",
            "",
            lambda: (storm_navigation()),
        )
spain = modules.ListOfOptions(
            [
                modules.Option(
                    lambda: OptionMessage(
                        "On your hitchhiking journey, a trucker spots you and offers you a trip to Vancouver. You are immensely grateful, but know that you need at least two more rides to reach the US Border.\n 2 hours later you arrive at the border.",
                        modules.change_state.CONTINUE,
                    ),
                    "1. Hitchhike down through Canada and into the U.S.",
                ),
                modules.Option(
                    lambda: OptionMessage(
                        "You are somehow hired, and create excuses for the lack of an id and SSN card.\nYou work this job and don't make a lot of money, and on top of that, a rumor spreads around your workplace hinting at your immigration status.\nUnfortunately, immigration agents raid the vessel, and you are identified as an illegal immigrant. \nYou are now among the detention center with thousands of others who have been caught in the US.",
                        modules.change_state.CHECKPOINT,
                    ),
                    "2. Take a job on a fishing vessel to fund a bus trip south",
                ),
            ],
            "You arrive in Lisbon, Portugal, hunted and desperate.\nYou don't have enough money to fly directly to the US.\nYou need a way to the U.S.",
            """
You meet two figures:
    Nadia Ben Amara – A passport forger who offers you a new identity—for a price.
    Elías Navarro – A rogue pilot who can fly you to California if you carry a sealed briefcase.
You agree to carry a sealed briefcase. During the trip, you feel a sudden urge to open the briefcase.
            """
        )
games = modules.Story(
    [
        modules.Start(lambda: OptionMessage("<<start game>>")),
        # beginning of Story I
        getting_on_flight,
        egypt,
        pharoah_checkpoint,
        morocco,
        storm_navigate_checkpoint,
        spain,
        modules.End(
            lambda x: slow_print("You have finished! Good work getting this far."),
            "Placeholder",
        ),
    ]
)


def exitGame(player):
    def func():
        dill.dump(player, open("egypt.p", "wb"))
        print("Files have been saved, press q to fully exit.")
        while True:
            if modules.quit_loop() == True:
                break

    return func


player = modules.Player("pranav")
player.play(games)

atexit.register(exitGame(player))

while True:
    match player.state:
        case modules.ListOfOptions():
            prompt = OptionPrompt(player.state, player)
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
                    slow_print("Moving Back to Last Checkpoint. You become more weary.\nPress q to start checkpoint.")
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
            os.system("rm save.p")
            shutdownComputer()
        case modules.Start():
            player.state.action()
            player.state = games.path[games.path.index(player.state) + 1]
    if player.weariness <= 0:
        wearinessTimeout()
        break
