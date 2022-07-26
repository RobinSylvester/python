from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
is_on = True
while is_on :
    user_choice = input(f"What would you like to have ? {menu.get_items()}: ").lower()

    if user_choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif user_choice == "off":
        print("Switching off the machine . . .")
        is_on = False
    else:
        order = menu.find_drink(user_choice)


        if order is not None:
            if coffeeMaker.is_resource_sufficient(order):
                # Make coffee

                if moneyMachine.make_payment(order.cost):
                    coffeeMaker.make_coffee(order)


