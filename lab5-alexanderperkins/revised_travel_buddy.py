"""
    CS 5001
    Lab 5
    Exercise 1
    Name: Alex Perkins
"""

'''
For this assignment, you will revise your travel buddy solution as follows:

    If the user enters an invalid currency for either cost or money on hand use a loop to print an error 
     message and request that the user enter a valid currency.
    Use a loop to allow the user to continue to perform conversions for additional items until they wish
     to quit.
    Make sure to fix any outstanding bugs from your original solution.
'''


def purchase_request():
    souvenir = input("What would you like to purchase? ")
    return souvenir


def listed_currencies():
    listed_currency = ['USD', 'KRONE', 'YUAN', 'EUR']
    return listed_currency


def get_item_price(souvenir, listed_currency):
    item_price = float(input(f"How much does the {souvenir} cost? "))
    while (type(item_price) != int and type(item_price) != float):
        print("**Invalid cost!**")
        item_price = input(f"Please state how much the {souvenir} costs. ")
        if (type(item_price) == int or type(item_price) == float):
            item_price = float(item_price)
            break
    currency = input("In what currency? (USD, KRONE, YUAN, EUR) ")
    currency = currency.upper()
    while (currency not in listed_currency):
        print("**Invalid currency!**")
        currency = input("Please choose either USD, KRONE, YUAN, or EUR. ")
        currency = currency.upper()
        if currency in listed_currency:
            break
    return item_price, currency


def get_customer_money(currencies):
    customer_money = input("How much money do you have? ")
    customer_currency = input("In what currency? (USD, KRONE, YUAN, or EUR) ")
    customer_currency = customer_currency.upper()
    while (customer_currency not in currencies):
        print("**Invalid currency!**")
        customer_currency = input("Please choose either USD, KRONE, YUAN, or EUR. ")
        customer_currency = customer_currency.upper()
        if customer_currency in currencies:
            break
    return customer_money, customer_currency


def display_user_currency_cost(item, local_cost, user_cost):
    print(f'The {item} costs {local_cost[0]} in {local_cost[1]} or {user_cost[0]} in {user_cost[1]}')


def display_amount_sufficiency(item, local_cost, user_money, converted_money):
    converted_cost, user_currency = converted_money[0]
    converted_budget, local_currency = converted_money[1]
    user_amount = float(user_money[0])
    local_amount = float(local_cost[0])
    converted_cost = float(converted_cost)
    converted_budget = float(converted_budget)
    print(f'You have {user_amount} in {user_currency} or {converted_budget} in {local_currency}')
    if converted_cost > user_amount or local_amount > converted_budget:
        converted_short = converted_cost - user_amount
        local_short = local_amount - converted_budget
        print(f"You don't have enough money. You're short by {local_short} in {local_currency}")
        print(f"or {converted_short} in {user_currency} for the {item}")
    else:
        print(f'You have enough for the {item}. Thank you!')


def currency_conversion(item, user):
    item_cost = float(item[0])
    item_currency = item[1]
    budget = float(user[0])
    user_currency = user[1]
    if item_currency == "USD":
        if (user_currency == "KRONE"):
            item_cost = 1356.54 * item_cost
            budget = 0.00074 * budget
        elif (user_currency == "YUAN"):
            item_cost = 7.30 * item_cost
            budget = 0.14 * budget
        elif (user_currency == "EUR"):
            item_cost = 0.95 * item_cost
            budget = 1.05 * budget
    elif item_currency == "KRONE":
        if (user_currency == "USD"):
            item_cost = 0.00074 * item_cost
            budget = 1356.54 * budget
        elif (user_currency == "YUAN"):
            item_cost = 0.0054 * item_cost
            budget = 185.53 * budget
        elif (user_currency == "EUR"):
            item_cost = 0.00070 * item_cost
            budget = 1428.66 * budget
    elif item_currency == "YUAN":
        if (user_currency == "USD"):
            item_cost = 0.14 * item_cost
            budget = 7.30 * budget
        elif (user_currency == "KRONE"):
            item_cost = 185.53 * item_cost
            budget = 0.0054 * budget
        elif (user_currency == "EUR"):
            item_cost = 0.13 * item_cost
            budget = 7.56 * budget
    elif item_currency == "EUR":
        if (user_currency == "USD"):
            item_cost = 1.05 * item_cost
            budget = 0.95 * budget
        elif (user_currency == "KRONE"):
            item_cost = 1428.66 * item_cost
            budget = 0.00070 * budget
        elif (user_currency == "YUAN"):
            item_cost = 7.56 * item_cost
            budget = 0.13 * budget
    converted_item = [item_cost, user_currency]
    converted_budget = [budget, item_currency]
    return converted_item, converted_budget


def repeat():
    item = purchase_request()
    currencies = listed_currencies()
    item_cost = get_item_price(item, currencies)
    customer_money = get_customer_money(currencies)
    converted_currencies = currency_conversion(item_cost, customer_money)
    display_user_currency_cost(item, item_cost, converted_currencies[0])
    display_amount_sufficiency(item, item_cost, customer_money, converted_currencies)

def main():
    print("Welcome to Travel Buddy!")
    continue_purchase = "Y"
    while continue_purchase == "Y" or continue_purchase == "YES":
        repeat()
        continue_purchase = input("Would you like to continue with a purchase request (Y/N)? ")
        continue_purchase = continue_purchase.upper()
        if continue_purchase == "N" or continue_purchase == "NO" or continue_purchase == "quit":
            print("Have a nice day!")
            quit()


if __name__ == '__main__':
    main()
