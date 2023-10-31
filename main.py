profit = 0


resources = {
    "water": 500,
    "milk": 300,
    "coffee": 250,
}


Menu = {
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

def enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f" Sorry we are low on {item} , choose another item please .")
            return False
        return True

def coins():
    print(" Please insert coins .")
    total = int (input("How many quarters ? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total

def transaction_test(payment , drink_cost):
    if payment > drink_cost :
        change = payment - drink_cost
        print(f"Transaction successful , here is your change : {change} ")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"sorry that is not enough money . Money refunded ... ")
        return False


def make_Coffee (drink_name , order_ingredients):
    for item in order_ingredients :
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True
while is_on :
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = Menu[choice]
        if enough_resources(drink["ingredients"]):
            payment = coins()
            if transaction_test(payment , drink["cost"]) :
                make_Coffee(choice , drink["ingredients"])

