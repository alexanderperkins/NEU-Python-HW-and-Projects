"""
    CS 5001
    Lab 2
    Exercise 6
    Name: Alex Perkins
"""

'''
For this exercise you will write a program to calculate the total of a user's shopping cart 
and the amount of change he/she is owed given the amount they wish to pay.

Requirements:

    Your store will offer at least three items. 
    Your program will prompt the user to enter the number of each item they wish to purchase.
    At least one of the items must have a price that is not a whole number.
    Your program will display for the user the total amount owed.
    Your program will prompt the user to enter the amount of payment.
    If the payment is less than the amount owed, your program will tell the user they are short and exit.
    If the payment is more than the amount owed, your program will calculate the user's change. 
    You will display for the user the number of $20, $10, $5, $1, 
    quarters, nickels, dimes, and pennies to be returned.

Your store may offer any three (or more) items. 
'''
def charges(item_1, item_2, item_3):
    charge = item_1 * 5.00 + item_2 * 10.00 + item_3 * 12.50
    return charge

def change(payment, bill):
    returned20 = int((payment - bill) // 20)
    returned10 = int((payment - bill - returned20 * 20) // 10)
    returned5 = int((payment - bill - returned20 * 20 - returned10 * 10) // 5)
    returned1 = int((payment - bill - returned20 * 20 - returned10 * 10 - returned5 * 5) // 1)
    returned = (payment - bill - returned20 * 20 - returned10 * 10 - returned5 * 5 - returned1 * 1)
    # calculation got too long so storing portion of calculation to meet style standards
    returned_quarters = int(returned // 0.25)
    returned_dimes = int((returned - returned_quarters * 0.25) // 0.10)
    returned_pennies = int((returned - returned_quarters * 0.25 - returned_dimes * 0.1) // 0.01)
    return returned20, returned10, returned5, returned1, returned_quarters, returned_dimes, returned_pennies
    # forgot or got stuck using for loop. Went the long route instead

def main():
    item_1 = int(input('Hi, how many produce would you like? '))
    item_2 = int(input('How many toiletries? '))
    item_3 = int(input('How many meat? '))
    bill = charges(item_1, item_2, item_3)
    print(f'Total due is ${bill}')

    payment = float(input(f'How much will you pay? $'))
    if (payment < bill):
        print("Your payment is short")
        # Given we're exiting after declaring payment is short of bill, no need to include in a loop
    else:
        returned = change(payment, bill)
        returned20, returned10, returned5, returned1, returned_quarters, returned_dimes, returned_pennies = returned

        print('Your change is $', payment - bill)
        print(f'Here is the breakout: \n{returned20} $20 bills')
        print(f'{returned10} $10 bills')
        print(f'{returned5} $5 bills')
        print(f'{returned1} $1 bills')
        print(f'{returned_quarters} quarters')
        print(f'{returned_dimes} dimes')
        print(f'{returned_pennies} pennies')


if __name__ == '__main__':
    main()
