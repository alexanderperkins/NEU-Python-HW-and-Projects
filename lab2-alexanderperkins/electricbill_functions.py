"""
    CS 5001
    Lab 2
    Exercise 4
    Name: Alex Perkins
"""

'''
Modify your solution to Question 1 so that it uses a function to perform the calculation. 
The function must take as input the base rate and the number of kWh used. 
It will return the total bill. This function will be called from your main function.
'''

def calculation(base_rate, used_monthly):
    bill = used_monthly // 1000 * base_rate * 1000 + used_monthly % 1000 * (base_rate * 1.25)
    return bill

def main():
    base_rate = float(input('Hi, enter the base kilowatt hour (kWh) rate: '))
    used_monthly = int(input('How much kWh have you used in a month? '))
    bill = calculation(base_rate, used_monthly)
    print(f'Total due is ${bill}')


if __name__ == '__main__':
    main()
