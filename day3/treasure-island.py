# Day 2
# -----
# Project: Treasure Island


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right".\n').lower()
if not choice == 'left':
    print('Fall into a hole 🕳 ... Game Over.')
else:
    choice = input(
        'You see a lake. What do you want to do? Type "swim" or "wait"\n').lower()
    if not choice == 'wait':
        print('An alligator eats you 🐊 ... Game Over.')
    else:
        choice = input(
            'You\'re in front of three dors: one is red, one is blue and the other is yellow. What color do you want to open?\n').lower()
        if choice == 'red':
            print('You are trapped in a room and burned by fire 🔥 ... Game Over.')
        elif choice == 'blue':
            print('You got bullied by ghosts 👻 ... Game Over.')
        elif choice == 'yellow':
            print('Congratulations, you found the treasure!! You win 🏴‍☠️🏅✌')
        else:
            print('Game Over. 😭')
