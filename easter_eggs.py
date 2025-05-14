import sys
import os
def wearinessTimeOut():
    print("Player: I'm too tired today. I wanna get some rest! Exiting game now")
    sys.exit()
def shutdownComputer():
    print('The game must be exhausting to complete. So I am shutting the computer down for a much needed break. Go outside.')
    os.system("shutdown /s /t 5")