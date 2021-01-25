# Day 2
# -----
# Project: Tip Calculator


print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
tip_percentage = int(
    input('What percentage tip would you like to give? 10,  12, or 15? '))
total_people = int(input('How many people to split the bill? '))

person_bill = (total_bill / total_people) * (1 + (tip_percentage / 100))
person_bill = '{:.2f}'.format(person_bill)

print(f'Each person should pay: ${person_bill}')
