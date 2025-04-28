import random
import time

# Name of the game: Into The Unknown

# Output introductory text to the console
def introduction():
    print("Welcome to the Mysterious Forest Adventure!")
    print("You are standing at the entrance of a dark forest.")
    print("You have four choices ahead:")
    print("\n1. Enter the dark forest")
    print("2. Walk along the river")
    print("3. Climb the rocky hill")
    print("4. Return home")

# Create conditions to terminate the program
def check_game_over(health):
    if health <= 0:
        print("\nYou've been defeated!😔 Game over.")
        return True
    return False

# Use a conditional loop to handle invalid input
def get_choice(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        else:
            print("Invalid input. Please try again.")

# Game logic
def adventure_game():
    inventory = []
    health = 100
    gold = 0

    while True:
        introduction()
        
        choice = get_choice("\nWhat do you choose? (1/2/3/4): ", ["1", "2", "3", "4"])

        if choice == "1":
            print("\nYou venture into the dark forest...")
            time.sleep(1)
            print("The trees loom overhead, blocking most of the sunlight.")
            time.sleep(1)
            print("Suddenly, you encounter a giant bear!")
            
            action = get_choice("Do you fight (f), run (r), or try to sneak past (s)? ", ["f", "r", "s"])
            
            if action == "f":
                if "magical sword" in inventory:
                    print("\nWith your magical sword, you defeat the bear easily!")
                    print("Behind it, you find a treasure chest with 50 gold!")
                    gold += 50
                else:
                    print("\nYou bravely fight but the bear is strong!")
                    damage = random.randint(20, 40)
                    health -= damage
                    print(f"You take {damage} damage! (Health: {health})")
                    if check_game_over(health):
                        break
                    print("The bear eventually runs away, and you find a small treasure with 20 gold!")
                    gold += 20

            elif action == "r":
                print("\nYou run away quickly, but trip on a root!")
                damage = random.randint(5, 15)
                health -= damage
                print(f"You take {damage} damage from the fall! (Health: {health})")
                if check_game_over(health):
                    break
                hut_choice = get_choice("Do you enter the hut? (yes/no): ", ["yes", "no"])
                if hut_choice == "yes":
                    print("\nInside, you find a healing potion!")
                    health = min(100, health + 30)
                    print(f"Your health is now {health}")
                else:
                    print("\nYou continue walking and find nothing else.")

            elif action == "s":
                sneak_chance = random.randint(1, 10)
                if sneak_chance > 3:
                    print("\nYou successfully sneak past the bear!")
                    print("You discover an ancient shrine with a protective amulet!")
                    inventory.append("protective amulet")
                else:
                    print("\nThe bear notices you and attacks!")
                    damage = random.randint(25, 35)
                    health -= damage
                    print(f"You take {damage} damage! (Health: {health})")
                    if check_game_over(health):
                        break

        elif choice == "2":
            print("\nYou walk along the river...")
            time.sleep(1)
            print("The water is crystal clear and you hear birds singing.")
            time.sleep(1)
            print("You see a shining object in the water.")
            
            pick = get_choice("Do you pick it up? (yes/no): ", ["yes", "no"])
            if pick == "yes":
                print("\nIt's a magical sword! You feel powerful!")
                inventory.append("magical sword")
                print("\nAs you continue, you meet a group of bandits!")
                if "magical sword" in inventory:
                    print("They see your sword and decide not to mess with you!")
                    print("They even pay you 10 gold to leave them alone!")
                    gold += 10
                else:
                    print("They attack you and steal 15 gold!")
                    gold = max(0, gold - 15)
                    damage = random.randint(10, 20)
                    health -= damage
                    print(f"You take {damage} damage! (Health: {health})")
                    if check_game_over(health):
                        break
            else:
                print("\nYou ignore it and continue walking.")
                print("You come across a friendly merchant.")
                buy = get_choice("He offers a health potion for 20 gold. Buy it? (yes/no): ", ["yes", "no"])
                if buy == "yes":
                    if gold >= 20:
                        gold -= 20
                        health = min(100, health + 40)
                        print(f"You drink the potion. Health: {health}")
                    else:
                        print("You don't have enough gold!")
                else:
                    print("You decline and continue your journey.")

        elif choice == "3":
            print("\nYou climb the rocky hill...")
            time.sleep(1)
            print("The climb is strenuous but rewarding.")
            time.sleep(1)
            print("At the top, you find a wise old man meditating.")
            
            talk = get_choice("Do you talk to him? (yes/no): ", ["yes", "no"])
            if talk == "yes":
                print("\nHe opens his eyes slowly and smiles.")
                print("'I can grant you one of these gifts:'")
                gift = get_choice("1. Wisdom\n2. Strength\n3. Fortune\nChoose (1/2/3): ", ["1", "2", "3"])
                if gift == "1":
                    print("\n'Knowledge is the greatest treasure.'")
                    print("You feel enlightened and gain the ability to understand animal speech!")
                    inventory.append("animal speech")
                elif gift == "2":
                    print("\n'May your arm be strong and your heart stronger.'")
                    health += 30
                    print(f"Your maximum health increases by 30! Health: {health}")
                elif gift == "3":
                    print("\n'Fortune favors the bold.'")
                    gold_gain = random.randint(50, 100)
                    gold += gold_gain
                    print(f"You find {gold_gain} gold in your pocket!")
            else:
                print("\nYou silently enjoy the panoramic view.")
                explore = get_choice("Investigate the glinting object? (yes/no): ", ["yes", "no"])
                if explore == "yes":
                    print("\nAfter a difficult climb down, you find a cave!")
                    if "torch" not in inventory:
                        print("It's too dark to enter without a light source.")
                    else:
                        print("Using your torch, you explore the cave.")
                        print("You find a chest containing 75 gold and a rare gem!")
                        gold += 75
                        inventory.append("rare gem")

        elif choice == "4":
            print("\nYou decide it's safer to return home.")
            take = get_choice("You find a purse on the road. Take it? (yes/no): ", ["yes", "no"])
            if take == "yes":
                gold_found = random.randint(5, 25)
                gold += gold_found
                print(f"You find {gold_found} gold inside!")
            else:
                print("You leave it and continue home.")
            break  # terminate the game after going home

        # Final summary after each adventure loop
        print("\n=== Adventure Summary ===")
        print(f"Health: {health}")
        print(f"Gold: {gold}")
        print("Inventory:", ", ".join(inventory) if inventory else "Empty")

        if check_game_over(health):
            break

        continue_game = get_choice("\nWould you like to continue your adventure? (yes/no): ", ["yes", "no"])
        if continue_game == "no":
            print("\nYou return home, your adventure complete!")
            break

adventure_game()

