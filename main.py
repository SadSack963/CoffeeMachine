import functions
import os
from time import sleep


def cls():
    """Cross-platform clear screen"""
    # os.system(command) is used to run operating system commands
    # This works in a terminal, but NOT in the PyCharm Run pane
    os.system('cls' if os.name == 'nt' else 'clear')


# START
# =====

money: float = 0.0

while True:
    # Get user selection
    selection = functions.user_selection()
    if selection == "":
        continue

    # Take action to perform user selection
    elif selection == 3:
        functions.switch_off()

    elif selection == 4:
        functions.print_report(money)

    else:
        # Check sufficient ingredients to make the drink
        sufficient = functions.check_ingredients(selection)
        if not sufficient:
            print("Maintenance required")

        if sufficient:
            # Sufficient ingredients to make the drink
            # Ask for payment
            result = functions.get_payment(selection, money)
            paid = result[0]
            money = result[1]

            if paid:
                # Drink paid for
                # Make the drink
                functions.print_report(money)
                functions.make_drink(selection)
                functions.print_report(money)

    sleep(5)  # Allows checking of output before clearing the screen
    cls()  # Doesn't work in PyCharm Run pane
    print()  # Print a blank line because cls() doesn't work
