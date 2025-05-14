# Project Description: 
In this project, you'll create a text adventure game where the player makes choices that affect the outcome of the game. 
The game should be designed to be fun and engaging, and can be set in any world or environment that you choose.

## Project Requirements:

The game should have a clear storyline with multiple choices that affect the outcome of the game.
The game should include different characters with unique personalities and attributes.
The game should include a variety of challenges and obstacles that the player must overcome to reach the end of the game.
The game should be designed to be fun and engaging, encouraging the player to keep playing and exploring different outcomes.
Include mini-games and puzzles that the player must solve to progress in the game.
Add a scoring system that rewards players for making good choices and penalizes them for making bad choices.
Add Easter eggs or secret areas that can only be discovered by exploring and making certain choices.
---

# Project Plan

Gameplay:
- Starts with chooser
- choose specific game
    - play option
        - right option moves forward
        - wrong option moves backward
    - play till checkpoint
        - checkpoint appears
        - then game starts
            - if won move forward, else start game again
    - repeat till end is reached
- easter eggs:
    - weariness: this stat will tell you about nothing: but u can't access the program till for 20 real minutes
        - will use the inside clock timer and check with real time, so turning it off won't help you
    - sign out: this stat will shutdown the computer immediately
game is seperated into 3 things: 
- Game Layout
    - a consistent layout, stores the outputs and prints them out
    - least complex layout (The One I am doing)
        - 1 box: contains all the items needed
        - when needed: it'll turn into a box for other things
- Game Data:
    - Storage of Game
        - Game Dialogue: Story
        - Story state = Passage
        - Minigame
            - create each file for the minigame
            - data print
            - all that 
        - Player
            - plays game
            - has weariness
            - inventory