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
password_list = []
password = ''

for i in range(num_letters):
    password_list.append(random.choice(letters))

for i in range(num_symbols):
    password_list.append(random.choice(symbols))

for i in range(num_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

for char in password_list:
    password += char

print(f'Order randomized: {password}')
