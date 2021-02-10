# Day 4
# -----
# Project: Rock Paper Scissors


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_images = [rock, paper, scissors]

choice = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if choice > 3 or choice < 0:
    print('Invalid number. You lose.')
else:
    print(choices_images[choice])

    computer_choice = random.randint(0, 2)
    print('Computer chose:')
    print(choices_images[computer_choice])

    game = [[-1, -1, -1], [-1, -1, -1]]
    game[0][choice] = choice
    game[1][computer_choice] = computer_choice

    if game[1][choice - 1] != -1:
        print('You win')
    elif game[1][choice] != -1:
        print('Draw')
    else:
        print('You lose')
