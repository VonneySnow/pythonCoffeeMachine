MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
machine_on = True
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def report():
    # water = resources["water"]
    # milk = resources["milk"]
    # coffee = resources["coffe
    # money = 0
    print(
        f"water : {water}ml\n"
        f"milk : {milk} ml\n"
        f"coffee : {coffee}g\n"
        f"money : $ {money}"
    )


def modifying_report():
    global water, milk, coffee, money
    water -= MENU[coffee_choice]["ingredients"]["water"]
    milk -= MENU[coffee_choice]["ingredients"]["milk"]
    coffee -= MENU[coffee_choice]["ingredients"]["coffee"]
    money += MENU[coffee_choice]["cost"]
    # if water<= 0 or milk <= 0 or coffee <= 0:
    #     machine_on = False
    #     print ("Sorry, the machine is out of resources")
    #     return


def resources_sufficient():
    global machine_on
    if water < MENU[coffee_choice]["ingredients"]["water"]:
        machine_on = False
        return "Sorry, there's not enough water"

    elif milk < MENU[coffee_choice]["ingredients"]["milk"]:
        machine_on = False
        return "Sorry, there's not enough milk"

    elif coffee < MENU[coffee_choice]["ingredients"]["coffee"]:
        machine_on = False
        return "Sorry, there's not enough coffee"
    else:
        return True


def process_coins():
    global quarters, dimes, nickles, pennies
    print("Please insert coins.")
    total_quarters = int(input("how many quarters?$ \n"))
    total_quarter_value = total_quarters * quarters
    total_dimes = int(input("how many dimes?$ \n"))
    total_dimes_value = total_dimes * dimes
    total_nickles = int(input("how many nickles?$ \n"))
    total_nickles_value = total_nickles * nickles
    total_pennies = int(input("how many pennies?$ \n"))
    total_pennies_value = total_pennies * pennies
    total_cash_entered = total_quarter_value + total_dimes_value + total_nickles_value + total_pennies_value
    change = total_cash_entered - MENU[coffee_choice]["cost"]
    if total_cash_entered >= MENU[coffee_choice]["cost"]:
        print(f"Here is ${change} in change.")
        return True
    elif total_cash_entered < MENU[coffee_choice]["cost"]:
        print("Sorry, not enough money. Money refunded.")
        return


while machine_on:
    coffee_choice = input("What would you like?(espresso/latte/cappuccino): \n").lower()
    if coffee_choice in MENU:
        if resources_sufficient() is True:
            modifying_report()
            process_coins()
            print(f"Here is your {coffee_choice}. Enjoy!")
            # report()
        else:
            print(resources_sufficient())
    elif coffee_choice == "report":
        report()
    else:
        print("invalid choice!")
