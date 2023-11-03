"""
    CS 5001
    Lab 2
    Exercise 5
    Name: Alex Perkins
"""

'''
Write a program that uses a function called is_close to determine whether a number provided as input is 
within 10% of 100 or within 20% of 200. The function will be defined as follows:
def is_close(number: int) -> bool
Your main function will (1) prompt the user for a number; 
(2) call the function is_close and store the result; 
(3) print the result returned by the function.
'''

def is_close(number: int) -> bool:
    if (number <= 0.10 * 100):
        print("Number is within 10% of 100")
        approximate = True
    elif (number <= 0.20 * 200):
        print("Number is within 20% of 200")
        approximate = True
    else:
        print("Number is not within 10% of 100 or 20% of 200")
        approximate = False
    return approximate

def main():
    number = int(input('Hi, enter a number: '))
    result = is_close(number)
    print(f'The result is close? {result}')


if __name__ == '__main__':
    main()
