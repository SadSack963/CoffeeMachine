from data import MENU, resources, choices, error_codes
import functions

# START
# =====

money: float = 0.0

# Get user selection
result = functions.user_selection()
selection = result[0]
error = result[1]
# TODO: if error then restart back at prompt

# Take action to perform user selection
if selection == 3:
    functions.switch_off()

elif selection == 4:
    functions.print_report(money)

else:
    # Check sufficient ingredients to make the drink
    result = functions.check_ingredients(selection)
    sufficient = result[0]
    error = result[1]

    if sufficient:
        # Sufficient ingredients to make the drink
        # Ask for payment
        result = functions.get_payment(selection, money)
        paid = result[0]
        money = result[1]
        error = result[2]

        if paid:
            # Drink paid for
            # Make the drink
            result = functions.make_drink(selection)
            success = result[0]
            error = result[1]

# TODO: Restart back at prompt
