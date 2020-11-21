from data import MENU, resources, choices, error_codes
from time import sleep


def print_error(error_code):
    """Prints an error message
    Requires: error code"""
    print(f"{error_codes[error_code]}")


def user_selection():
    """Validates the user selection.
    Returns: index to the function in choices[]"""
    error_code: int = 0
    choice_text = ""
    for x in choices:
        if x.lower() != "off" and x.lower() != "report":
            if choice_text == "":
                choice_text += x
            else:
                choice_text += " / " + x
    choice = input(f"What would you like? ({choice_text}): ").lower()
    if choice in choices:
        return choices.index(choice)
    else:
        error_code = 1
        print_error(error_code)
        return ""


def print_report(money):
    """Prints the Coffee Machine resources.
    Requires: total of money in machine"""
    print("Report\n======")
    for x in resources:
        print(f"{x}: {resources[x]['quantity']}{resources[x]['unit']}")
    print(f"Money: ${money:.2f}")


def switch_off():
    print("The Coffee Machine is now switched Off!")
    quit()  # use os.system("exit") in terminal ?


def check_ingredients(index):
    """Check sufficient ingredients to make the selected beverage.
    Required: index to the beverage in choices[].
    Returns: True if enough, False otherwise"""
    error_code = 0
    drink = choices[index]
    recipe = MENU[drink]
    for ingredient in recipe["ingredients"]:
        if recipe["ingredients"][ingredient] > resources[ingredient]["quantity"]:
            error_code = 2
            print_error(error_code)
            return False
    return True


def get_payment(index, money):
    """Request coins to pay for the selected drink.
    Required: index to the beverage in choices[].
    Returns: True if enough, False otherwise, new money total"""
    error_code = 0
    paid = False
    change = 0
    drink = choices[index]
    cost = MENU[drink]["cost"]
    print(f"Your drink costs ${cost:.2f}\nPlease insert coins.")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))
    total = (quarters * 25 + dimes * 10 + nickles * 5 + pennies) / 100  # in dollars
    if total < cost:
        error_code = 3
        print_error(error_code)
    elif total > cost:
        paid = True
        money += cost
        change = total - cost
        print(f"Here is ${change:.2f} in change.")
    else:
        paid = True
        money += cost
    return paid, money


def make_drink(index):
    """Perform actions to make the selected drink.
    Required: index to the beverage in choices[]."""
    print("Thank you. Your drink is on the way.")
    sleep(5)  # Pause for 5 seconds

    drink = choices[index]
    recipe = MENU[drink]
    for ingredient in recipe["ingredients"]:
        resources[ingredient]["quantity"] -= recipe["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy!")
