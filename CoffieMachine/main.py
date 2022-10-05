from machine_data import MENU
from machine_data import resources


def reduce_res(coffees, machine):
    """This function reduce machine supply"""
    machine['water'] -= MENU[f'{coffees}']['ingredients']['water']
    machine['coffee'] -= MENU[f'{coffees}']['ingredients']['coffee']
    if coffees == "latte" or coffees == "cappuccino":
        machine['milk'] -= MENU[f'{coffees}']['ingredients']['milk']


def enough_res(order_drink):
    for item in order_drink['ingredients']:
        if order_drink['ingredients'][item] >= resources[item]:
            print(f"Sorry there is not enough {item} to prepare your coffee")
            return False
    return True

def process_wallet():
    print("Please insert coin")
    # TODO3 Po wybraniu kawy wypisać poszczególne monety
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


machine_wallet = 0


def coffee_machine(wallet):
    still_ask = True
    while still_ask:

#       TODO1 Zapytać usera jaki typ kawy wybiera
        user_coffee = input("What type of coffee do you want? (espresso\latte\cappuccino): ").lower()
#       TODO2 Pokazać zapasy i konto maszyny
        if user_coffee == "report":
            for i in resources:
                print(f"{i}: {resources[i]}")
            print(f"Money: ${wallet}")
        elif user_coffee == 'off':
            print("Shutting down.")
            still_ask = False
        else:
            drink = MENU[user_coffee]
            if enough_res(drink):
                user_wallet = process_wallet()
                if user_wallet >= drink['cost']:
                    print("Pleas wait a moment. Enjoy your coffee.")
                    wallet += drink["cost"]
                    back_money = round(user_wallet - drink["cost"], 2)
                    print(f"Your change is ${back_money}. Enjoy your coffee.")
                    reduce_res(user_coffee, resources)

                else:
                    print("Sorry that's not enough to buy coffee. Money refund")
                    user_wallet = 0
    return wallet


coffee_machine(machine_wallet)
