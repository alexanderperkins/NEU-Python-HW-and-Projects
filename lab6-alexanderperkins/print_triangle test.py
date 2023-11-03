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

# def print_triangle2(n, current):
        # Print the current row
        # print(" " * (n - current) + " ".join(map(str, range(current + 1))))

        # Recursively call the function to print the next row
        # print_triangle(number, current + 1)

        # Print the current row again (for decreasing part)
        # print(" " * (n - current) + " ".join(map(str, range(current, -1, -1))))

def print_triangle(n, current=0): ##, spaces=None):
    ## if spaces is None:
        ## spaces = n

    if current <= n:
        ## Print spaces
        ## print(" " * spaces, end="")

        # Print the numbers in the current row
        print_numbers(0, current)

        # Go to the next line
        print()

        # Recursively call the function to print the next row
        print_triangle(n, current + 1) ##, spaces - 1)

        # Print the current row again (for decreasing part)
        if current > 0:
            ## print(" " * spaces, end="")
            print_numbers(current, 0)
            print()

def print_numbers(start, end):
    if start <= end:
        print(start, end=" ")
        print_numbers(start + 1, end)

def main():
    length_of_longest_row = int(input("Enter a integer: "))
    print_triangle(length_of_longest_row)
    # print_nums_recursive(number)
    # a = 0
    # print_triangle(number, a)
    a = range(length_of_longest_row)
    a = list(a)
    print(a[0:length_of_longest_row:2])

if __name__ == '__main__':
    main()