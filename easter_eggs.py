import sys
import os
def wearinessTimeOut():
    print("Player: I'm too tired today. I wanna get some rest! Exiting game now")
    sys.exit()
def shutdownComputer():
    print("Now that the game is finished, I can peacefully sleep")
    os.system("shutdown /s /t 1")