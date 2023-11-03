"""
    CS 5001
    Lab 2
    Exercise 1
    Name: Alex Perkins
"""

'''
Write a program to calculate the amount of money the user must pay for their electric bill. 
Your program will prompt the user for 
(1) their base kilowatt hour (kWh) rate and 
(2) the number of kWh they have used in a month. 

Your program will calculate and print as output the the total amount due. 
Your program will appropriately calculate overage as follows: 
up to 1,000 kWh are charged at the base rate, and 
any kWh used in excess of 1,000 kWh are charged at 125% of the base rate. 
For example, if the user used 1,250 kWh at $0.14 per kWh the total due would be (1000*.14)+(250*(.14*1.25)). 
'''

def main():
    base_rate = float(input('Hi, enter the base kilowatt hour (kWh) rate: '))
    used_monthly = int(input('How much kWh have you used in a month? '))
    bill = used_monthly // 1000 * base_rate * 1000 + used_monthly % 1000 * (base_rate * 1.25)
    print(f'Total due is ${bill}')


if __name__ == '__main__':
    main()
