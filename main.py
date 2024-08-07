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

money = 0

def check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def user_selection():
    user_choice = input("What drink do you want? (cappuccino/latte/espresso): ").lower()
    if user_choice in MENU:
        print(f'{user_choice} and the price is ${MENU[user_choice]["cost"]}')
        return user_choice
    else:
        print("Sorry, invalid choice or unavailable drink.")
        return None

def process_coins():
    try:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        return quarters + dimes + nickels + pennies
    except ValueError:
        print("Invalid input. Please enter valid coin amounts.")
        return 0

def transaction_process(drink, received_money):
    cost = MENU[drink]["cost"]
    if received_money >= cost:
        change = round(received_money - cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += cost
        ingredients = MENU[drink]['ingredients']
        for ingredient in ingredients:
            resources[ingredient] -= ingredients[ingredient]
        print(f"Here is your {drink}. Enjoy!")
    else:
        print(f"Sorry, that's not enough money. Money refunded.")

def coffee_machine():
    while True:
        drink = user_selection()
        if drink:
            if check_resources(drink):
                received_money = process_coins()
                if received_money > 0:
                    transaction_process(drink, received_money)

coffee_machine()
