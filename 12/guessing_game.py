# Day 12
# -----
# Project: Guessing Game


import random
from typing import NoReturn
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty():
    if input('Choose a difficulty. Type "easy" or "hard": ') == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def compare_answer(guess, answer, attempts):
    if guess == answer:
        print('You win!!')
        return None
    elif guess > answer:
        print('Too high.')
    else:
        print('Too low')

    return attempts - 1

def guessing_game():
    print(logo)

    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    answer = random.randint(1,101)

    attempts = set_difficulty()

    guess = 0
    while guess != answer:
        print(f'You have {attempts} remaining to guess the number.')

        guess = int(input('Make a guess: '))
        attempts = compare_answer(guess, answer, attempts)

        if attempts == 0:
            print('You\'ve run out of guesses, you lose.')
            return

guessing_game()
