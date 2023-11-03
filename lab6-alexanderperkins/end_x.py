"""
    CS 5001
    Lab 6
    Exercise 2
    Name: Alex Perkins
"""

'''
    Write a recursive Python function that takes as input a string
     and recursively computes a new string where all the lowercase
     'x' chars have been moved to the end of the string. The function
     should take only one parameter and not use any loops.
'''

def print_string(string: str):
    """
    Implement a recursive function that takes as input a str and prints
    the characters of the str while moving x's to the end *without using a loop*.
    """
    if string == '':
        return string
    if string[0] == 'x':
        print_string(string[1:])
        return print_string(string[1:]) + 'x'
    else:
        return string[0] + print_string(string[1:])

def main():
    user_string = input("Enter a string to check if lowercase x's will be moved to the end: ")
    print(print_string(user_string))


if __name__ == '__main__':
    main()