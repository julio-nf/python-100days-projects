# Day 11
# -----
# Project: Blackjack Game


import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_score(cards):
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def pick_remaining_cards(cards):
    while get_score(cards) < 17:
        cards.append(random.choice(cards))

    return cards

def finalize_game(my_cards, computer_cards):
    my_score = get_score(my_cards)
    computer_score = get_score(computer_cards)

    print(f'    Your final hand: {my_cards}, final score: {my_score}')
    print(f'    Your final hand: {computer_cards}, final score: {computer_score}')

    if my_score == 21 and len(my_cards) == 2:
        print('Win with a Blackjack 😎')
    elif computer_score == 21 and len(computer_cards) == 2:
        print('Lose, opponent has Blackjack 😱')
    elif my_score == computer_score:
        print('Draw 🤨')
    elif my_score > 21:
        print('You went over. You lose 😭')
    elif computer_score > 21:
        print('Opponent went over. You win 🥳')
    elif computer_score > my_score:
        print('You lose 😤')
    else:
        print('You win 🤩')

def play_blackjack():
    print(logo)

    my_cards = random.choices(population=cards, k=2)
    computer_cards = random.choices(population=cards, k=2)

    should_continue = True
    while should_continue:
        print(f'    Your cards: {my_cards}, current score: {get_score(my_cards)}')
        print(f'    Computer\'s first card: {computer_cards[0]}')

        if get_score(my_cards) >= 21 or get_score(computer_cards) >= 21:
            should_continue = False
            finalize_game(my_cards, computer_cards)
        elif input('Type "y" to get another card, type "n" to pass: ') == 'n':
            should_continue = False
            computer_cards = pick_remaining_cards(computer_cards)
            finalize_game(my_cards, computer_cards)
        else:
            my_cards.append(random.choice(cards))

while input('Do you want to play a game of Blackjack? Type "y" or "n": ') == 'y':
    os.system('clear')
    play_blackjack()
