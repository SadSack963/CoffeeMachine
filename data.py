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
    "water": {"quantity": 300, "unit": "ml"},
    "milk": {"quantity": 200, "unit": "ml"},
    "coffee": {"quantity": 100, "unit": "g"},
}

choices = [
    "espresso",
    "latte",
    "cappuccino",
    "off",
    "report"
]

error_codes = {
    1: "Invalid selection!",
    2: "Sorry there is not enough {ingredient}.",
    3: "Sorry that's not enough money. Money refunded.",
}

