import random
import time
# name of my game: (Into The Unknown)
def adventure_game():
    print("Welcome to the Mysterious Forest Adventure!")
    print("You are standing at the entrance of a dark forest.")
    print("You have four choices ahead:")

    print("\n1. Enter the dark forest")
    print("2. Walk along the river")
    print("3. Climb the rocky hill")
    print("4. Return home")

    inventory = []
    health = 100
    gold = 0

    choice = input("\nWhat do you choose? (1/2/3/4): ")

    if choice == "1":
        print("\nYou venture into the dark forest...")
        time.sleep(1)
        print("The trees loom overhead, blocking most of the sunlight.")
        time.sleep(1)
        print("Suddenly, you encounter a giant bear!")
        
        action = input("Do you fight (f), run (r), or try to sneak past (s)? ")
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
                if health > 0:
                    print("The bear eventually runs away, and you find a small treasure with 20 gold!")
                    gold += 20
                else:
                    print("You've been defeated!😔 Game over.")
                    return
        elif action == "r":
            print("\nYou run away quickly, but trip on a root!")
            damage = random.randint(5, 15)
            health -= damage
            print(f"You take {damage} damage from the fall! (Health: {health})")
            if health > 0:
                print("You find a hidden path that leads to a small hut.")
                hut_choice = input("Do you enter the hut? (yes/no): ")
                if hut_choice.lower() == "yes":
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
                if health <= 0:
                    print("You've been defeated!😔 Game over.")
                    return
    
    elif choice == "2":
        print("\nYou walk along the river...")
        time.sleep(1)
        print("The water is crystal clear and you hear birds singing.")
        time.sleep(1)
        print("You see a shining object in the water.")
        
        pick = input("Do you pick it up? (yes/no): ")
        if pick.lower() == "yes":
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
                if health <= 0:
                    print("You've been defeated!😔 Game over.")
                    return
        else:
            print("\nYou ignore it and continue walking.")
            print("You come across a friendly merchant.")
            buy = input("He offers a health potion for 20 gold. Buy it? (yes/no): ")
            if buy.lower() == "yes" and gold >= 20:
                gold -= 20
                health = min(100, health + 40)
                print(f"You drink the potion. Health: {health}")
            elif buy.lower() == "yes":
                print("You don't have enough gold!")
            else:
                print("You decline and continue your journey.")
    
    elif choice == "3":
        print("\nYou climb the rocky hill...")
        time.sleep(1)
        print("The climb is strenuous but rewarding.")
        time.sleep(1)
        print("At the top, you find a wise old man meditating.")
        
        talk = input("Do you talk to him? (yes/no): ")
        if talk.lower() == "yes":
            print("\nHe opens his eyes slowly and smiles.")
            print("'I can grant you one of these gifts:'")
            gift = input("1. Wisdom\n2. Strength\n3. Fortune\nChoose (1/2/3): ")
            
            if gift == "1":
                print("\n'Knowledge is the greatest treasure.'")
                print("You feel enlightened and gain the ability to understand animal speech!")
                inventory.append("animal speech")
            elif gift == "2":
                print("\n'May your arm be strong and your heart stronger.'")
                print("Your maximum health increases by 30!")
                health += 30
                print(f"Health: {health}")
            elif gift == "3":
                print("\n'Fortune favors the bold.'")
                gold_gain = random.randint(50, 100)
                gold += gold_gain
                print(f"You find {gold_gain} gold in your pocket!")
            else:
                print("\nThe old man sighs at your indecision and vanishes.")
        else:
            print("\nYou silently enjoy the panoramic view.")
            print("You notice something glinting in the distance...")
            explore = input("Investigate? (yes/no): ")
            if explore.lower() == "yes":
                print("\nAfter a difficult climb down, you find a cave!")
                if "torch" not in inventory:
                    print("It's too dark to enter without a light source.")
                else:
                    print("Using your torch, you explore the cave.")
                    print("You find a chest containing 75 gold and a rare gem!")
                    gold += 75
                    inventory.append("rare gem")
            else:
                print("\nYou return home without discovering what it was.")
    
    elif choice == "4":
        print("\nYou decide it's safer to return home.")
        print("As you walk back, you find a purse on the road!")
        take = input("Do you take it? (yes/no): ")
        if take.lower() == "yes":
            gold_found = random.randint(5, 25)
            gold += gold_found
            print(f"You find {gold_found} gold inside!")
        else:
            print("You leave it where it is and continue home.")
    
    else:
        print("\nThat's not a valid choice. Please restart the game.")
        return
    
    print("\n=== Adventure Summary ===")
    print(f"Health: {health}")
    print(f"Gold: {gold}")
    print("Inventory:", ", ".join(inventory) if inventory else "Empty")
    
    if health <= 0:
        print("\nYour adventure ends here...")
    else:
        print("\nWould you like to continue your adventure?")
        continue_game = input("There might be more to discover! (yes/no): ")
        if continue_game.lower() == "yes":
            print("\nYou set out once more into the unknown...")
            adventure_game()
        else:
            print("\nYou return home, your adventure complete!")

adventure_game()
