# Day 9
# -----
# Project: The Secret Auction


import os
from art import logo

print(logo)
print('Welcome to the secret auction program.')

is_running = True
bidders = {}

while is_running:
    name = input('What\'s your name?: ')
    bid = int(input('What\'s your bid?: $'))

    bidders[name] = bid

    has_another_bidder = input('Are there any other bidders? Type "yes" or "no". ')

    if has_another_bidder == 'no':
        is_running = False

    os.system('clear')

winner = {
    name: '',
    bid: 0
}
for key in bidders:
    if bidders[key] > winner[bid]:
        winner[name] = key
        winner[bid] = bidders[key]

print(f'The winner is {winner[name]} with a bid of ${winner[bid]}.')
