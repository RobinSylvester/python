from details import MENU

resources = {
    "Milk" : 1000,
    "Water" : 2000,
    "Coffee" : 500,
    "Money" : 0
}
# TODO 4: Check Money
def check_money(coffee_type):
    print("Please insert coins !")
    quarters = int(input("How many quarters ? "))
    dimes = int(input("How many dimes ? "))
    nickels = int(input("How many nickels ? "))
    cents = int(input("How many cents ? "))
    sum_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (cents * 0.01)
    if sum_amount > MENU[coffee_type]['cost']:
        print(f"Here is your change: ${round(sum_amount - MENU[coffee_type]['cost'], 2)}")
    elif sum_amount < MENU[coffee_type]['cost']:
        print(f"You are ${round(MENU[coffee_type]['cost'] - sum_amount, 2)} short of money. Money refunded.")
        return -1

    resources['Money'] += MENU[coffee_type]['cost']

# TODO 3: Prepare Coffee
def prepare_coffee(coffee_type):
    milk_needed = 0
    water_needed = MENU[coffee_type]["ingredients"]["water"]
    coffee_needed = MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type != "espresso":
        milk_needed = MENU[coffee_type]["ingredients"]["milk"]
        if (resources['Milk'] - milk_needed) < 0:
            print("Not enough Milk. Money refunded")
            return
        else:
            resources['Milk'] -= milk_needed
    if (resources['Water'] - water_needed) < 0:
        print("Not enough Water. Money refunded")
        return
    else:
        resources['Water'] -= water_needed

    if (resources['Coffee'] - coffee_needed) < 0:
        print("Not enough Coffee. Money refunded")
        return
    else:
        resources['Coffee'] -= coffee_needed

    print(f"Here is your {coffee_type} ☕. Enjoy!")



# TODO 2: Respond based on choice
def respond_to_choice(choice):
    if choice == "off":
        #off
        return
    elif choice == "report":
        #print report
        print(f"Milk: {resources['Milk']}ml\nWater: {resources['Water']}ml\nCoffee: {resources['Coffee']}g\nMoney: ${resources['Money']}")
        prompt_user()
    elif choice == "espresso":
        #make espresso
        flag = check_money("espresso")
        if(flag != -1):
            prepare_coffee("espresso")
        prompt_user()
    elif choice == "latte":
        #make latte
        flag = check_money("latte")
        if (flag != -1):
            prepare_coffee("latte")
        prompt_user()
    elif choice == "cappuccino":
        #make cappuccino
        flag = check_money("cappuccino")
        if (flag != -1):
            prepare_coffee("cappuccino")
        prompt_user()
    else:
        print("Invalid Option")
        prompt_user()


# TODO 1: Ask user what they want
def prompt_user():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    respond_to_choice(user_choice)

prompt_user()
