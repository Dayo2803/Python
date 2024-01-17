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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sufficient_resources(order_ingredient):
    """Returns the list of ingredients available"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True
    
def process_coins():
    """Returns the total value calculated"""
    print("Please insert coins. ")
    total = int(input("How many Quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def transaction(money_received, drink_cost):
    """Retrns True or False to confirm payemnet"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} your change")
        global profit
        profit +=drink_cost
        return True
    else:
        print("Sorry that's not enough Money. Money refunded")


def make_coffee(drink_name, order_ingredient):
    """Subtract ingredients from resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}")

machine_on = True
while machine_on:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "off":
        machine_on = False
    elif coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(coffee, drink["ingredients"])