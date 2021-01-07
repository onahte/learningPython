MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

menu_print = """-----------------------------------------------
       A       |      B      |        C
   espresso    |    latte    |    cappuccino
     $1.50     |    $2.50    |      $3.00
-----------------------------------------------
"""
from time import sleep
import os

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os. system('cls')
# TODO 1. Turn on/off
on = 'True'
print("If you would like some cofee, please turn on the machine.")
status = input("Would you like to turn on the coffee machine? 'y' or 'n' ")
if status == 'n':
    on = 'False'
while on == 'True':

# TODO 2. Request selection
    print(menu_print)
    selection = input('Please type in your selection from the menu. ').lower()

# TODO 3. Check resources.
    cont = 'True'
    water_needed = MENU[selection]['ingredients']['water']
    coffee_needed = MENU[selection]['ingredients']['coffee']
    milk_needed = MENU[selection]['ingredients']['milk']
    if resources['water'] - water_needed < 0:
        print('There is not enough resources to make your drink. Sorry.')
        cont = 'False'
    elif resources['coffee'] - coffee_needed < 0:
        print('There is not enough resources to make your drink. Sorry.')
        cont = 'False'
    elif resources['milk'] - milk_needed < 0:
        print('There is not enough resources to make your drink. Sorry.')
        cont = 'False'
    if cont == 'True':

# TODO 4. Process payment
        price = MENU[selection]['cost']
        print(f'The cost is {price}. Please insert coins.')
        quarter = int(input('How many quarters? '))
        dime = int(input('How many dimes? '))
        nickel = int(input('How many nickels? '))
        penny = int(input('How many pennies? '))
        def coin_total(q, d, n, p):
            q = q * .25
            d = d * .1
            n = n * .05
            p = p * .01
            return q, d, n, p
        def change(price, q, d, n, p):
            total = sum(coin_total(q, d, n, p))
            print(f'Thank you. You have inserted ${total}.')
            change_back = round(total - price, 2)
            not_enough = round(price - total, 2)
            while change_back < 0:
                print('You have not inserted sufficient coins for this purchase.')
                print(f'You will need ${not_enough} more to make this purchase.')
                more = input('Would you like to insert more coins? y or n : ').lower()
                if more == 'y':
                    q = int(input('How many quarters? '))
                    d = int(input('How many dimes? '))
                    n = int(input('How many nickels? '))
                    p = int(input('How many pennies? '))
                    total += sum(coin_total(q, d, n, p))
                    change_back = total - price
            print(f'Your change is ${change_back}.')
            return change_back
        change(price, quarter, dime, nickel, penny)

# TODO 5. Make coffee.
        resources['water'] -= water_needed
        resources['coffee'] -= coffee_needed
        resources['milk'] -= milk_needed
        print('Your drink is being made.')
        sleep(2)
        print('Your drink is ready!')
        print('Your resources remaining: ', list(map(lambda r : r + " " + str(resources.get(r)), ['water', 'milk', 'coffee'])))
        finish = input('Would you like to turn off the machine? y or n ')
        if finish == 'y':
            on = 'False'
        clear_screen()