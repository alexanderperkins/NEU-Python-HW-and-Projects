"""
    CS 5001
    Lab 2
    Exercise 3
    Name: Alex Perkins
"""

'''
Implement a program that will prompt the user for the following three pieces of information 
(1) the amount of a restaurant bill; 
(2) the quality of service; and 
(3) the number of diners. 
The program will add a tip to the bill amount and will output the amount each diner owes. 
Requirements:
    1. The quality of service will be specified as fair, good, or excellent. 
    The corresponding tip amounts will be 18%, 20%, and 25% respectively.
    2. The program will print an error message and exit if the quality of service  
    entered is not one of fair/good/excellent.
    3. If the total amount owed for the bill + tip does not divide evenly among
    the diners then you may round up or down. Either is acceptable.
'''

def main():
    bill = float(input("Hi, what's the bill amount? $"))
    service_quality = input("How was the quality i.e. fair, good, or excellent? ")
    tip = float(1)
    while service_quality not in ['fair', 'good', 'excellent']:
        service_quality = input("**Error**\n Please choose quality from these options only: fair, good, or excellent: ")
        if service_quality == 'fair' or service_quality == 'good' or service_quality == 'excellent':
            break
    if (service_quality == 'fair'):
        tip = 1.18
    elif (service_quality == 'good'):
        tip = 1.2
    elif (service_quality == 'excellent'):
        tip = 1.25

    diners = int(input("How many diners were there? "))

    total_amount = bill * tip
    if (total_amount % diners == 0):
        amount_due = total_amount / diners
    else:
        amount_due = round(total_amount / diners)
    print(f"Total due for each diner is ${amount_due}")


if __name__ == '__main__':
    main()
