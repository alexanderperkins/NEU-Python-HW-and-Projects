"""
    CS 5001
    Lab 6
    Exercise 1
    Name: Alex Perkins
"""

'''
    Write a recursive Python program that prints the following output. 
    You will implement a function print_triangle that takes as input the
     length of the longest row, in this case 5. You may use one or more
     helper methods. For full credit, your solution may not use any loops.
'''

def print_triangle(number, current, start):
    """
    Takes helper function from given 0 and adds 1 to range while less than user's
     number. Then repeats back the full range and reduces it back down by 1 until 0.
    """
    if current >= number:
        print_nums_helper(start, number)
        if number <= start:
            return
        print_bottom_triangle(number - 1, start)
    if current < number:
        print_nums_helper(start, current)
        print_triangle(number, current + 1, start)

def print_bottom_triangle(number: int, start):
    """
    Implement print_nums_iterative from Sami's example without using a loop.
    Takes helper function for initial full range of numbers and then repeats
     back the range after reducing the entered value by 1 for each iteration.
    """
    print_nums_helper(start, number)
    if number <= start:
       return
    print_bottom_triangle(number-1, start)

def print_nums_helper(current: int, n: int):
    '''
    Puts numbers in a row up to user's entered number.
    '''
    if current == n:
        print(current)
        return
    print(current, end=" ")
    print_nums_helper(current+1, n)

def main():
    number = int(input("Enter a integer: "))
    current = 0
    start = 0
    print_triangle(number, current, start)


if __name__ == '__main__':
    main()