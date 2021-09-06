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
machine_on = True
money = 0
r_water = resources["water"]
r_milk = resources["milk"]
r_coffee = resources["coffee"]


def resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(money_reciev, price):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_reciev >= price:
        change = money_reciev - price
        print(f"Here is change : {change}")
        return True
    else:
        print("Sorry ! Not enought money ! Here is refund")


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while machine_on:
    # TODO : promt user by asking :
    choice = input("What would you like (Espresso, Latte or Capuchino)? \n").lower()
    # TODO : turn off power with serect key "off"
    if choice == "off":
        machine_on = False
    # TODO 3 : print report
    elif choice == "report":
        print(f"Water : {r_water} ml \n")
        print(f"Milk : {r_milk} ml \n")
        print(f"Coffe : {r_coffee} g \n")
        print(f"Money : $ {money}  \n")
    # TODO 4: Check resource sufficient , make coffee
    else:
        drink = MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])


