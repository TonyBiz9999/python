from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    option = input("What would you like? (espresso/latte/cappuccino):")
    if option == "off":
        is_on = False
    elif option == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(option)
        is_payment_sucessfull = money_machine.make_payment(drink.cost)
        is_enought_resource = coffee_maker.is_resource_sufficient(drink)
        if is_payment_sucessfull and is_enought_resource:
            coffee_maker.make_coffee(drink)
