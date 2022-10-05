from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
wallet = MoneyMachine()
main_menu = Menu()
still_run = True


while still_run:
    user_order = input(f"What you want to order? ({main_menu.get_items()}): ")
    if user_order == "off":
        still_run = False
        print("Shutting down")
    elif user_order == "report":
        machine.report()
        wallet.report()
    else:
        drink = main_menu.find_drink(user_order)
        if machine.is_resource_sufficient(drink):
            if wallet.make_payment(drink.cost):
                machine.make_coffee(drink)
