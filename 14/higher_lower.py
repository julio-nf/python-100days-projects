# Day 14
# -----
# Project: Higher Lower Game


import os
import random
from art import logo, vs
from game_data import data

def compare_followers(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'a'
    else:
        return 'b'

def pick_famous(data, seen):
    while True:
        famous = random.choice(data)

        if famous['name'] not in seen:
            seen.append(famous)
            return famous

def play_game(data):
    should_continue = True
    seen = []
    score = 0
    previous = pick_famous(data, seen)

    while should_continue:
        print(logo)

        if len(seen) == len(data):
            print('You win!!')
            return

        if score > 0:
            print(f'You\'re right! Current score: {score}')

        a = previous

        while True:
            b = pick_famous(data, seen)
            if b['name'] != a['name']:
                break

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

        user_answer = input('Who has more followers? Type "A" or "B": ').lower()
        answer = compare_followers(a, b)

        if user_answer == answer:
            score += 1
            previous = b
        else:
            print(f'Sorry, that\'s wrong. Final score: {score}')
            return

        os.system('clear')

play_game(data)
