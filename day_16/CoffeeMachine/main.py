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

coffee_map = {
    'e': "espresso",
    'l': "latte",
    'c': "cappuccino"
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def prompt_user():
    prompt = "What would you like? (espresso/latte/cappuccino): "
    """Prompt user and validate command"""
    cmd = input(prompt)
    while cmd.lower()[0] not in 'elcro':
        print(f"Invalid entry: {cmd}")
        cmd = input(prompt)
    return cmd.lower()[0]

def run_report():
    """Print resources report"""
    #   a. When the user enters “report” to the prompt, a report should be generated that shows
    #   the current resource values. e.g.
    #     Water: 100ml
    #     Milk: 50ml
    #     Coffee: 76g
    #     Money: $2.5
    for resource in ['water', 'milk', 'coffee', 'money']:
        resource_format = f"{resources[resource]}ml"
        if resource == 'coffee':
            resource_format = f"{resources[resource]}g"
        if resource == 'money':
            resource_format = f"${resources[resource]:.2f}"
        print(f"{resource.title()}: {resource_format}")

def check_resources(selection):
    """verify that resources are sufficient to make selection"""
    #   b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    #   not continue to make the drink but print: “Sorry there is not enough water.​ ”
    #   c. The same should happen if another resource is depleted, e.g. milk or coffee.
    sufficient = True
    ingredients = MENU[selection]['ingredients']
    for ingredient, qty in ingredients.items():
        if resources[ingredient] < qty:
            print(f"Sorry there is not enough {ingredient}.")
            sufficient = False
    return sufficient

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
    "pennies": 0.01
}

def collect_coins():
    """collect coins and return amount"""
    #   b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    #   c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    #   pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    total = 0
    print("Please insert coins.")
    for coin, value in coins.items():
        current = -1
        while current < 0:
            coin_count = input(f"How many {coin}? ")
            try:
                current = int(coin_count) * value
            except ValueError:
                print(f"Invalid input: {coin_count}")
            if current  < 0:
                print(f"Please enter a positive number.")
        total += current
    return total

def make_coffee(selection):
    """make coffee and deduct resources"""
    #  then the ingredients to make the drink should be deducted from the
    #  coffee machine resources.
    ingredients = MENU[selection]['ingredients']
    for ingredient, qty in ingredients.items():
        resources[ingredient] -= qty
    #  b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    #  latte was their choice of drink.
    print(f"Here is your {selection}. Enjoy!")

def main():
    shutdown = False
    while not shutdown:
        command = prompt_user()
        if command == 'o':
            #   a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
            #   the machine. Your code should end execution when this happens.
            shutdown = True
            continue
        if command == 'r':
            run_report()
        if command in 'elc':
            coffee = coffee_map[command]
            #   a. When the user chooses a drink, the program should check if there are enough
            #   resources to make that drink.
            if not check_resources(coffee):
                continue
            #   a. If there are sufficient resources to make the drink selected, then the program should
            #   prompt the user to insert coins.
            money_in = collect_coins()
            #   a. Check that the user has inserted enough money to purchase the drink they selected.
            #   E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
            #   program should say “Sorry that's not enough money. Money refunded.​ ”.
            if money_in < MENU[coffee]['cost']:
                print("Sorry that's not enough money. Money refunded.")
                continue
            #   b. But if the user has inserted enough money, then the cost of the drink gets added to the
            #   machine as the profit and this will be reflected the next time “report” is triggered.
            resources['money'] += MENU[coffee]['cost']
            #   c. If the user has inserted too much money, the machine should offer change.
            #   E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
            #   places.
            if money_in > MENU[coffee]['cost']:
                print(f"Here is ${money_in - MENU[coffee]['cost']:.2f} dollars in change.")
            #   a. If the transaction is successful and there are enough resources to make the drink the
            #   user selected,
            make_coffee(coffee)

if __name__ == "__main__":
    main()