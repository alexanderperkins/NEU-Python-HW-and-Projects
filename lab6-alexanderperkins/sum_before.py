"""
    CS 5001
    Lab 6
    Exercise 3
    Name: Alex Perkins
"""

'''
    Write a recursive Python function that takes as input a number_list
     of integers and returns True if there is a number in the number_list
     that equals the numbers_sum of all numbers before it in the number_list and
     False otherwise.
'''


def if_numbers_sum_exists(number_list, index, numbers_sum):
    """
    Implement a recursive function that returns true if a number in a list matches
    the sum of preceding numbers in the list *without using a loop*.
    """
    if number_list == '':
        return number_list
    if index < len(number_list):
        if 1 < index < len(number_list) and int(number_list[index]) == numbers_sum:
            return True
        elif index == len(number_list) - 1 and int(number_list[index]) != numbers_sum:
            return False
        else:
            numbers_sum += int(number_list[index])
            index += 1
            return if_numbers_sum_exists(number_list, index, numbers_sum)

def main():
    number_number_list = input("Enter a number_list of integers: ").split()
    # print(number_number_list)
    index = 0
    numbers_sum = 0
    print(if_numbers_sum_exists(number_number_list, index, numbers_sum))


if __name__ == '__main__':
    main()
