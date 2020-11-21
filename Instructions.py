# TODO 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​”
# a. Check the user’s input to decide what to do next.
# TODO 1b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

# TODO 2. Turn off the Coffee Machine by entering “​off​” to the prompt.
# TODO 2a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens

# TODO 3. Print report.
# TODO 3a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
#   Water: 100ml 
#   Milk: 50ml 
#   Coffee: 76g 
#   Money: $2.5 

# TODO 4. Check resources sufficient?
# TODO 4a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# TODO 4b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “​Sorry there is not enough water.​”
# TODO 4c. The same should happen if another resource is depleted, e.g. milk or coffee.

# TODO 5. Process coins.
# TODO 5a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# TODO 5b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# TODO 5c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO 6. Check transaction successful?
# TODO 6a. Check that the user has inserted enough money to purchase the drink they selected.
#   E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “​Sorry that's not enough money. Money refunded.​”.
# TODO 6b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#   Water: 100ml 
#   Milk: 50ml 
#   Coffee: 76g 
#   Money: $2.5
# TODO 6c. If the user has inserted too much money, the machine should offer change.
#   E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

# TODO 7. Make Coffee.
# TODO 7a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
#   E.g. report before purchasing latte:
#   Water: 300ml
#   Milk: 200ml
#   Coffee: 100g
#   Money: $0
#   Report after purchasing latte:
#   Water: 100ml 
#   Milk: 50ml 
#   Coffee: 76g 
#   Money: $2.5
#
# TODO 7b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.



