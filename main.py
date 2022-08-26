menu = {
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

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

water = []
milk = []
coffee = []
should_continue = True

for value in menu:
    water.append(menu[value]["ingredients"]["water"])
    coffee.append(menu[value]["ingredients"]["coffee"])
    milk.append(menu[value]["ingredients"]["milk"])


def choose_one(option_value, number):
    if option_value == "report":
        print(resources)

    elif resources["water"] >= water[number] or resources["milk"] >= milk[number] and \
            resources["coffee"] >= coffee[number]:
        print("Please insert the coins")
        q_quarters = float(input("How many quarters?: "))
        q_dimes = float(input("How many dimes?: "))
        q_nickles = float(input("How many nickles?: "))
        q_pennies = float(input("How many pennies?: "))
        total = (quarters * q_quarters) + (dimes * q_dimes) + (nickles * q_nickles) + (q_pennies * pennies)
        if total == menu[option_value]["cost"]:
            print("Here is your latte☕. Thank yo u for choosing our service. ")
        elif total > menu[option_value]["cost"]:
            balance = total - (menu[option_value]["cost"])
            balance = round(balance, 2)
            print(f"Here is {balance} in change.")
            print("Here is your latte☕. Thank yo u for choosing our service. ")
            resources["water"] = resources["water"] - water[number]
            resources["milk"] = resources["milk"] - milk[number]
            resources["coffee"] = resources["coffee"] - coffee[number]
            print(f"Balance resources are {resources}")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry there is a shortage of ingredients.")


while should_continue:
    def quest_func():
        question = input("What would you like?(espresso/latte,cappuccino): ")

        num = 0
        if question == "espresso":
            num += 0
        elif question == "latte":
            num += 1
        else:
            num += 2
        choose_one(option_value=question, number=num)
    quest_func()
    if input("Do you want next drink?(y/n)") == "y":
        quest_func()
    else:
        should_continue = False
        print("Good bye")
