"""
    CS 5001
    Lab 4
    Exercise 3
    Name: Alex Perkins
"""

'''
Write a Python program that uses a function find_greater_than to determine the number
 of values in a list of integers that are greater than a value specified by the user.
 The function will take as input a list of integers and a single int provided by the
 user. It will return the number of values in the list that exceed the user's number.
'''

def find_greater_than():
    number_list = input('Enter a list of integers separated by space \n')
    number_list = number_list.split()
    base_number = input('Enter the base number to compare against \n')
    counter = 0
    higher_value_counter = 0
    while counter < len(number_list):
        if int(number_list[counter]) > int(base_number):
            higher_value_counter += 1
        counter += 1
    return higher_value_counter

def main():
    larger_values_count = find_greater_than()
    print(f"Number of listed values higher than user's base number is: {larger_values_count}")


if __name__ == '__main__':
    main()
