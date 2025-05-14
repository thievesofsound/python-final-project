import random
import time
import modules
from output import *
def print_delay(text, delay=1):
    print(text)
    time.sleep(delay)

def pharaoh_battle():
    player_health = 200
    pharaoh_health = 500
    pharoah_medallion = ""

    print_delay("PHARAOH: THE EVIL ENFORCER")
    print_delay("After stealing the briefcase and making your way, you believe you are home free...")
    print_delay("But wait! Who is that formulating in that massive sand storm?")
    print_delay("Low and behold, it is THE MIGHTY PHARAOH and he wants to take your money AND your life!")
    print_delay(f"Your Health: {player_health} | PHARAOH'S Health: {pharaoh_health}\n")

    # First move
    print("What move would you like to use first?")
    print("1. Double Kick (-75 boss health, you lose 50)")
    print("2. Vacuum Wave (-50 boss health, you lose 25)")
    choice1 = input("Enter 1 or 2: ")
    if choice1 == "1":
        pharaoh_health -= 75
        player_health -= 50
        print_delay("You used Double Kick! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Supersonic!")
    else:
        pharaoh_health -= 50
        player_health -= 25
        print_delay("You used Vacuum Wave! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Smelling Salts!")

    print(f"Your Health: {player_health} | PHARAOH'S Health: {pharaoh_health}\n")

    # Second move
    print("What move would you like to do second?")
    print("1. Mach Punch (-75 boss health, you lose 25)")
    print("2. Combat Torque (-100 boss health, you lose 75)")
    choice2 = input("Enter 1 or 2: ")
    if choice2 == "1":
        pharaoh_health -= 75
        player_health -= 25
        print_delay("You used Mach Punch! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Egg Bomb!")
    else:
        pharaoh_health -= 100
        player_health -= 75
        print_delay("You used Combat Torque! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Facade!")

    print(f"Your Health: {player_health} | PHARAOH'S Health: {pharaoh_health}\n")

    # Third move
    print("What move would you like to do third?")
    print("3. Jump Kick (-150 boss health, you lose 50)")
    print("4. Flying Press (-75 boss health, you lose 25)")
    choice3 = input("Enter 3 or 4: ")
    if choice3 == "3":
        pharaoh_health -= 150
        player_health -= 50
        print_delay("You used Jump Kick! It was devastating!")
        print_delay("THE MIGHTY PHARAOH used Sand Attack!")
    else:
        pharaoh_health -= 75
        player_health -= 25
        print_delay("You used Flying Press! It was effective!")
        print_delay("THE MIGHTY PHARAOH used Echoed Voice!")

    print(f"Your Health: {player_health} | PHARAOH'S Health: {pharaoh_health}\n")

    # Final move
    print("What move would you like to do last?")
    print("5. Focus (-250 boss health, you lose 25)")
    print("6. Collision Curse (-200 boss health, you lose 25)")
    choice4 = input("Enter 5 or 6: ")
    if choice4 == "5":
        pharaoh_health -= 250
        player_health -= 25
        print_delay("You used Focus! A finishing blow!")
        print_delay("THE MIGHTY PHARAOH used Mega Kick!")
    else:
        pharaoh_health -= 200
        player_health -= 25
        print_delay("You used Collision Curse! Dark energy erupts!")
        print_delay("THE MIGHTY PHARAOH used Smelling Salts!")

    print(f"Your Final Health: {player_health} | PHARAOH'S Final Health: {pharaoh_health}\n")

    # Outcome
    if pharaoh_health <= 0 and player_health > 0:
        print_delay("THE MIGHTY PHARAOH HAS BEEN DEFEATED!")
        chance = random.random()
        if chance < 0.15:
            print_delay("You feel a strange energy surround you...")
            print_delay("You have inherited the PHARAOH'S lifestyle: opulence, power, and respect.")
            print_delay("Your stats increase drastically. You are now a living legend.")
            print("** RICHNESS OPULENCE ENDING UNLOCKED **")
            #**PHAROAH_MEDALLION ADDED INTO INVENTORY 
        else:
            print_delay("Though the PHARAOH is defeated, his curse fades into the wind...")
            print("You walk away victorious, but the sands keep their secrets.")
            return modules.change_state.CONTINUE
    elif player_health <= 0:
        print_delay("You collapse before THE MIGHTY PHARAOH.")
        print_delay("Your journey ends here...")
        return modules.change_state.CHECKPOINT
    else:
        print_delay("Both you and PHARAOH collapse... the storm consumes you.")
        print("** DOUBLE K.O. ENDING **")


def storm_navigation():
    print("\n--- Step III: Storm Navigation ---")
    print("A violent sandstorm howls around you.")
    print("You must choose a direction to navigate through it.")
    print("Only one direction leads to safety. The others will cost you health!")

    health = 100
    directions = ['north', 'south', 'east', 'west']

    for step in range(1, 6):
        correct_path = random.choice(directions)
        print(f"\nStep {step}: Choose a direction (north, south, east, west)")
        choice = input("Your choice: ").lower()

        if choice == correct_path:
            print("You move cautiously and find safe ground.")
        elif choice in directions:
            health -= 25
            print("You stumble through harsh winds and burning sand!")
            print(f"-25 Health | Current Health: {health}")
        else:
            print("Invalid direction! You hesitate and the storm punishes you!")
            health -= 50
            print(f"-25 Health | Current Health: {health}")

        if health <= 0:
            print("\nThe storm overwhelms you. You collapsed under the weight of the desert.")
            print("** GAME OVER **")
            return change_state.WAIT

    print("\nYou've made it through the storm with your life.")
    print(f"Final Health: {health}")
    print("** STORM SURVIVED **")


import random

def obstacle_navigation():
    print("\n--- Step IV: Obstacle Navigation ---")
    print("You face a series of deadly obstacles in the desert.")
    print("Roll the dice to navigate through them.")
    print("1-2 = Safe | 3-4 = Not Safe | 5-6 = Injured")

    safe_count = 0
    injured = False

    while True:
        input("\nPress Enter to roll the dice...")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}.")

        if roll in [1, 2]:
            safe_count += 1
            print(f"Safe! ({safe_count} safe roll(s))")
        elif roll in [5, 6]:
            injured = True
            print("You were injured!")
        else:
            print("Not safe! Try again.")

        # Check win conditions
        if safe_count >= 3:
            print("\nYou've safely navigated the obstacles!")
            print("*OBSTACLE CLEARED*")
            break
        elif injured and safe_count >= 2:
            print("\nDespite injury, you've managed to get through!")
            print("*OBSTACLE CLEARED*")
            break

### Puzzle | Played if User picks rob option | Step 3 - Story III
import random

def puzzle_minigame1():
    print("\n--- Step II: Bomb Disable ---")
    print("On your stolen item, there is a ticking time bomb")
    print("To prevent your death, you must enter the correct 3-digit code.")
    print("You only get 3 tries before the bomb explodes!")

    # Generate random 3-digit code as a string
    code = random.randint(100, 110)
    attempts = 3

    while attempts > 0:
        guess = int(input(f"\nEnter 3-digit code ({attempts} attempt(s) left): "))

        if guess == code:
            print("Code accepted. Wealth unlocked!")
            print("** SUCCESS **")
            return
        else:
            print("Incorrect code.")
            attempts -= 1

    print("\nALARM SOUNDING! The Russians are coming!")
    print("** GAME OVER **")

###Puzzle | Played at Step 3 - StoryIII
import random

def p_dice():
    print("\n--- Step III: Police Dodge---")
    print("After blowing up the drone outpost, guards take aim at you")
    print("You must dodge their shots, unaware of where they come from.")
    print("1-2 = Headshot (FAIL)")
    print("3-4 = Stomach Shot (INJURED but safe)")
    print("5-6 = Missed")

    safe_steps = 0
    injured = False

    while True:
        input("Type 'Enter' to roll a dice and make your move")
        roll = random.randint(1, 6)
        print(f"You moved {roll} steps.")

        if roll in [1, 2]:
            print("HEADSHOT! You died")
            print("** GAME OVER **")
            break
        elif roll in [3, 4]:
            injured = True
            print("The stomach shot does a number on you, but you persevere.")
        elif roll in [5, 6]:
            safe_steps += 1
            print(f"Safe step! ({safe_steps} safe step(s))")

        # moves on if user meets conditions
        if safe_steps >= 1:
            print("\nYou safely escape the bullet fire!")
            print("** BULLET DICE CLEARED **")
            break
        elif injured and safe_steps >= 2:
            print("\nDespite the injury, you've made it!")
            print("** BULLET DICE CLEARED **")
            break


# New minigame for health regeneration
def health_regen_minigame():
    print_delay("\n--- Regeneration Minigame ---")
    number = random.randint(10, 13)
    print_delay("Guess the secret number between 10 and 13. You have 3 tries!")

    for i in range(3):
        try:
            guess = int(input(f"Attempt {i + 1}: "))
            if guess == number:
                print_delay("Correct! You've regained your strength.")
                return True
            else:
                print_delay("Wrong guess.")
        except ValueError:
            print_delay("Please enter a number.")

    print_delay("You failed to guess the number.")
    return False

# Handles the health 
def health_check(player):
    player.reduce_health(10)
    if player.health <= 0:
        print_delay("\nYou're too weak to continue.")
        if health_regen_minigame():
            player.restore_health()
        else:
            print_delay("You failed to regenerate. Game Over.")
            ask_retry()
            return False
    return True

def get_choice_input(options):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice-1
        except:
            print("Invalid input. Please enter a number in the options.")

#user must pick random 3 digit number in 3 tries, only used when user picks bad option
def puzzle_minigame():
    print_delay("\n--- Return Minigame: Puzzle Minigame ---")
    code = random.randint(100, 103)
    print_delay("You must guess the 3-digit access code between 100 and 103. You have 3 attempts!")

    for attempt in range(3):
        guess = input(f"Attempt {attempt + 1}: Enter a 3-digit code: ")
        if guess.isdigit() and len(guess) == 3:
            if int(guess) == code:
                print_delay("Correct! You bypassed the alarm.\n")
                return modules.change_state.CONTINUE
            else:
                print_delay("Incorrect code.")
        else:
            print_delay("Invalid input. Enter 3 digits.")

    print_delay("\nAlarm triggered! You have been captured.\n--- Game Over ---\n")
    return modules.change_state.CHECKPOINT

#epic pokemon battle
def battle_minigame(player):
    print_delay("\n--- Checkpoint: Wailord Battle ---")
    player_health = 100
    wailord_health = 300
    special_moves = []

    print_delay("Wailord appears! You must beat him in 3 moves or perish.")

    print_delay("\nYou find two items beneath the cargo ship:")
    print_delay("1. Electric Beam\n2. Bamboo Stick")

    move1 = get_choice_input(["Electric Beam", "Bamboo Stick"])

    if move1 == 0:
        damage = random.randint(90, 110)
        wailord_health -= damage
        player_health -= 40
        special_moves.append(damage)
        print_delay(f"You used Electric Beam! Wailord loses {damage} HP.")
        print_delay("Wailord smashes you with his tail. You lose 40 HP.")
    else:
        damage = random.randint(45, 55)
        wailord_health -= damage
        player_health -= 25
        print_delay(f"You used Bamboo Stick! Wailord loses {damage} HP.")
        print_delay("Wailord splashes you with water. You lose 25 HP.")

    print_delay("\nIn the chaos, you spot more items:")
    print_delay("1. Electroweb\n2. Syrup Bomb")

    move2 = get_choice_input(["Electroweb", "Syrup Bomb"])

    if move2 == 0:
        wailord_health -= 25
        player_health -= 50
        print_delay("You used Electroweb. It was weak. Wailord loses 25 HP.")
        print_delay("Wailord eats and spits you out. You lose 50 HP.")
    else:
        wailord_health -= 150
        special_moves.append(150)
        print_delay("You used Syrup Bomb. Very effective! Wailord loses 150 HP.")

    print_delay("\nFinally, you find two more items:")
    print_delay("1. Mushrooms\n2. Plasma Gloves")

    move3 = get_choice_input(["Mushrooms", "Plasma Gloves"])

    if move3 == 0:
        wailord_health -= 20
        player_health -= 20
        print_delay("You used Mushrooms. Both you and Wailord lose 20 HP.")
    else:
        wailord_health -= 125
        special_moves.append(125)
        print_delay("You used Plasma Gloves. Super effective! Wailord loses 125 HP.")

    print_delay(f"\nFinal Health: You = {player_health} | Wailord = {wailord_health}")

    if player_health <= 0:
        print_delay("\nYou have died. Wailord wins!\n--- Game Over ---")
        ask_retry()
        return modules.change_state.CHECKPOINT

    if wailord_health <= 0:
        print_delay("\nYou defeated Wailord!")
        if any(move >= 100 for move in special_moves):
            print_delay("You achieved the SPECIAL POKEMON ENDING!")
            print_delay("You get 1 passport of any citizenship")
            player.inventory.items.append(modules.InventoryItem("passport", "A universal passport that modifies for the user to enter any country.", 1))
        else:
            print_delay("You move forward to Alaska.")
        player.health = player_health
        return modules.change_state.CONTINUE
        
    else:
        print_delay("\nWailord finishes you off as he still stands!\n--- Game Over ---")


#Immigration checkpoint for final
def immigration_gaurds(player):

    print("\n--- Checkpoint: immigration ---")
    print("Due to recent events, every person in the US is subject to ID checks.")
    print("Conveniently though, there has been a veteran who was buried recently with all of his possessions, including his passport.")
    print("One issue though; becuase he was a high ranking gneral , his gravesite is gaurded 24/7")

    row1 = [4,5]
    row1_choice = random.choice(row1)
    if any(item.name == "passport" for item in player.inventory.items):
        slow_print("You already have a passport. You don't need another one.")
        return modules.change_state.CONTINUE
    else:
        while True:
            try:
                guess1 = int(input("\nEnter a number 1-7 to move up: "))
                if guess1 > row1_choice and guess1 > 0 and guess1 < 8:
                    print_delay("Congrats, You have moved up to row 2")
                else:
                    print_delay("You have been captured and beaten to death.")
                    print_delay("Prompt to retry")
                    break
                row2_choice = random.choice(row1)
                guess1 = int(input("\nEnter a number 1-7 to move up: "))
                if guess1 < row2_choice and guess1 > 0 and guess1 < 8:
                    print_delay("Congrats, You have moved up to row 3")
                else:
                    print_delay("You have been captured and beaten to death.")
                    print_delay("Prompt to retry")
                    break
                row3_choice = random.choice(row1)
                guess1 = int(input("\nEnter a number 1-7 to move up: "))
                if guess1 < row3_choice and guess1 > 0 and guess1 < 8:
                    print_delay("Congrats, You have moved up to row 4")
                else:
                    print_delay("You have been captured and beaten to death.")
                    print_delay("Prompt to retry")
                    break
                row4_choice = random.choice(row1)
                guess1 = int(input("\nEnter a number 1-7 to move up: "))
                if guess1 < row4_choice and guess1 > 0 and guess1 < 8:
                    print_delay("Congrats, You have moved up to row 5")
                else:
                    print_delay("You have been captured and beaten to death.")
                    print_delay("Prompt to retry")
                    break
                row5_choice = random.choice(row1)
                guess1 = int(input("\nEnter a number 1-7 to move up: "))
                if guess1 > row5_choice and guess1 > 0 and guess1 < 8:
                    print_delay("Congrats, You have escaped the gaurds!")
                    return modules.change_state.CONTINUE
                else:
                    print_delay("You have been captured and beaten to death.")
                    print_delay("Prompt to retry")
                    break
            except Exception:
                print_delay("Enter a number please.")
