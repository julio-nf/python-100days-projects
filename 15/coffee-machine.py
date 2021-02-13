# Day 15
# -----
# Project: Coffee Machine


# Project initial code
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# My code
def print_report(resources, money):
    for key in resources:
        unit = ''
        if key == 'water' or key == 'milk':
            unit = 'ml'
        elif key == 'coffee':
            unit = 'g'
        print(f'{key.capitalize()}: {resources[key]}{unit}')
    print(f'Money: ${money}')

def insert_coins():
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))

    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

def check_resources(resources, option):
    print(resources, option)
    option_ingredients = MENU[option]['ingredients']

    for key in resources:
        if key == 'milk' and option == 'espresso':
            pass
        elif resources[key] < option_ingredients[key]:
            print(f'Sorry, there is not enough {key}.')
            return False
    return True

def reduce_resources(resources, option):
    option_ingredients = MENU[option]['ingredients']
    new_resources = resources

    for key in new_resources:
        if key == 'milk' and option == 'espresso':
            pass
        else:
            new_resources[key] -= option_ingredients[key]

    return new_resources

def check_cost(option, money):
    option_cost = MENU[option]["cost"]
    if money < option_cost:
        print('Sorry that\'s not enough money. Money refunded.')
        return False
    return True

def calculate_change(option, money):
    option_cost = MENU[option]["cost"]

    change = money - option_cost
    print(f'Here is ${change} in change.')
    return change

def start_machine(resources, money):
    option = input('What would you like? (espresso/latte/cappuccino): ')
    if option == 'report':
        print_report(resources, money)
    else:
        if check_resources(resources, option):
            money_inserted = insert_coins()
            money += money_inserted

            if check_cost(option, money):
                resources = reduce_resources(resources, option)
                money = calculate_change(option, money)
                print(f'Here is your {option} ☕️... Enjoy!')
            else:
                money -= money_inserted

    new_resources = {
        "resources": resources,
        "money": money
    }
    return new_resources

my_resources = {
    "resources": resources,
    "money":  0
}
while True:
    resources = my_resources['resources']
    money = my_resources['money']

    my_resources = start_machine(resources, money)
