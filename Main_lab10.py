from Player_lab10 import Player
import random

# Pokemon like game where you are P1 and P2 is a CPU that choses options by itself.
# turn number evens == p2
turn_number = 0


# CPU coding, Main coding below the object comment
# player2 cpu turn moves based on counts, odd numbs
def cpu(option):
    if option % 2 == 0:  # even numbers, CPU attacks P1
        x1 = random.randint(0, 100)
        if x1 % 2 == 0:
            print()
            print(f'{p2.name} attacks you!')
            p1.take_damage(p2.attack())
            print(p1)
            print(p2)
            print()
        elif x1 == 1 or 49 or 97:
            # try to escape
            y1 = random.randint(0, 20)
            if y1 % 2 == 0:  # even numbs, CPU fails to quit game!
                print()
                print(f'{p2.name} can not escape! You damage {p2.name}!')
                p2.take_damage(p1.strength)
                print(p1)
                print(p2)
                print()
            else:  # odd numbs, CPU attempts to exit the game!
                print()
                print(f'{p2.name} has successfully escaped!')
                print("The Results are:")
                print(p1)
                print(p2)
                exit()
        else:
            # heal itself, CPU heal itself!
            print()
            print(f'{p2.name} has healed itself!')
            p2.heal()
            print(p1)
            print(p2)
            print()
    else:
        pass


# objects
p1 = Player("Pikachu", 100, 30)
p2 = Player("Charizard", 100, 25)
print(p1)
print(p2)
print()
print(f"Your are ambushed by {p2.name}! What do you do?")

# You are P1 with options, Main code starts here.
while True:
    print(f'1: Attacks, 2: Heals, 3: Escape, 4: quit game')
    u = int(input("Enter Option: "))
    if u == 1:
        print()
        print(f'You attack {p2.name}!')
        p2.take_damage(p1.attack())
        turn_number += 2
        print(p1)
        print(p2)
        cpu(turn_number)
        print()
    elif u == 2:
        print()
        print("You have healed.")
        p1.heal()
        print(p1)
        print(p2)
        print()
    elif u == 3:
        x = random.randint(0, 99)
        if x % 2 == 0:  # even numbs
            print()
            print(f"You can not escape, you take damage from {p2.name}!")
            p1.take_damage(p2.strength)
            print(p1)
            print(p2)
            print()
        else:  # odd numbs
            print("You have successfully escaped!")
            print("The Results are:")
            print(p1)
            print(p2)
            break
    elif u == 4:
        print(f'You have quit the game!')
        break
