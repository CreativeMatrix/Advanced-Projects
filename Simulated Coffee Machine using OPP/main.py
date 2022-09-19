from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

money_machine.report()
coffee_maker.report()
menu.get_items()

coffeemaker_is_on = True
while coffeemaker_is_on:
    user_choice = input(f"What would you like?({menu.get_items()}): ")
    if user_choice == 'off':
        coffeemaker_is_on = False
    elif user_choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            
         
       