# Day 5
# -----
# Project: Password Generator


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('Welcome to the PyPassword Generator!')

num_letters = int(input('How many letters would you like in your password? '))
num_symbols = int(input('How many symbols would you like? '))
num_numbers = int(input('How many numbers would you like? '))

# Order not randomized
password = ''

for i in range(num_letters):
    password += random.choice(letters)

for i in range(num_symbols):
    password += random.choice(symbols)

for i in range(num_numbers):
    password += random.choice(numbers)

print(f'Order not randomized: {password}')


# Order randomized
password = ''

total = num_letters + num_symbols + num_numbers
counter_letters = 0
counter_symbols = 0
counter_numbers = 0

while total > 0:
    rand = random.randint(0, 3)
    total -= 1

    if rand == 0 and counter_letters < num_letters:
        password += random.choice(letters)
        counter_letters += 1
    elif rand == 1 and counter_symbols < num_symbols:
        password += random.choice(symbols)
        counter_symbols += 1
    elif rand == 2 and counter_numbers < num_numbers:
        password += random.choice(numbers)
        counter_numbers += 1
    else:
        total += 1

print(f'Order randomized: {password}')
