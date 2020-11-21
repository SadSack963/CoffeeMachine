from data import MENU, resources, choices, error_codes


def user_selection():
    """Validates and returns user selection as an index to the item in choices[]"""
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
        print(error_codes[error_code])
        return "", error_code


result = user_selection()
selection = result[0]
error = result[1]
