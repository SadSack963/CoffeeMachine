from data import MENU, resources, choices, error_codes


def print_error(error_code):
    print(f"{error_codes[error_code]}")


def user_selection():
    """Validates the user selection.
    Returns: index to the function in choices[], and an error code"""
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
        return choices.index(choice), error_code
    else:
        error_code = 1
        print_error(error_code)
        return "", error_code


def print_report(money):
    """Prints the Coffee Machine resources.
    Requires: total of money in machine"""
    print("Report\n======")
    for x in resources:
        print(f"{x}: {resources[x]['quantity']}{resources[x]['unit']}")
    print(f"Money: ${money:.2f}")


def switch_off():
    print("The Coffee Machine is now switched Off!")
    quit()


def check_ingredients(index):
    """Check sufficient ingredients to make the selected beverage
    Required: index to the beverage in choices[].
    Returns: True if enough, False otherwise, and an error code"""
    error_code = 0
    sufficient = True
    drink = choices[index]
    recipe = MENU[drink]
    for ingredient in recipe["ingredients"]:
        if recipe["ingredients"][ingredient] > resources[ingredient]["quantity"]:
            error_code = 2
            print_error(error_code)
            sufficient = False
    return sufficient, error_code


def get_payment(selection, money):
    """Request coins to pay for the selected drink.
    Required: index to the beverage in choices[].
    Returns: True if enough, False otherwise, new money total, and an error code"""
    error_code = 0
    paid = False
    change = 0
    cost = MENU[selection]["cost"]
    print(f"Your drink costs ${cost}\nPlease insert coins.")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))
    total = quarters * 0.25 + dimes * 10 + nickles * 5 + pennies
    if total < cost:
        error_code = 3
        print_error(error_code)
    elif total > cost:
        paid = True
        money += cost
        change = total - cost
        print(f"Here is ${change} in change.")
    else:
        paid = True
        money += cost
    return paid, money, error_code


def make_drink(selection):
    """Perform actions to make the selected drink.
    Required: index to the beverage in choices[].
    Returns: True if enough, False otherwise"""
    print("Thank you. Your drink is on the way.")

