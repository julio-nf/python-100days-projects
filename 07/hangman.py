# Day 7
# -----
# Project: Hangman


import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for char in chosen_word:
    if not char == ' ':
        display += '_'
    else:
        display += ' '

while not end_of_game:
    guess = input("Escolha uma letra: ").lower()

    os.system('clear')

    if guess in display:
        print(f'Você já tentou essa letra: {guess}.')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'Essa letra não está na palavra: {guess}')

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Você perdeu. 😔😭")

    print(stages[lives])

    print(f"{' '.join(display)}\n")

    if "_" not in display:
        end_of_game = True
        print("Você venceu! 😃🥳🎉")
