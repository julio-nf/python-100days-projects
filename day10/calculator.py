# Day 10
# -----
# Project: Calculator


import os
from art import logo

print(logo)

# Operations functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Operations dict
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    x = float(input('What\'s the first number?: '))

    for operation in operations:
        print(operation)

    keep_calculating = True
    while keep_calculating:
        operation_chosen = input('Pick an operation: ')

        y = float(input('What\'s the next number?: '))

        calculation_function = operations[operation_chosen]
        answer = calculation_function(x, y)

        print(f'{x} {operation_chosen} {y} = {answer}')

        if input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation: ') == 'y':
            x = answer
        else:
            keep_calculating = False
            os.system('clear')
            calculator()

calculator()
