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

def print_string(string: str, index, x_counter, new_word):
    """
    Implement a recursive function that takes as input a str and prints
    the characters of the str one per line *without using a loop*.
    """
    if index >= len(string):
        print(new_word + 'x' * x_counter)
        return
    elif string[index] == 'x':
        #print(string[index])
        new_word += ''
        x_counter += 1
    else:
        new_word += string[index]
        #print(new_word)
    index += 1
    print_string(string, index, x_counter, new_word)

def main():
    user_string = input("Enter a string to check if lowercase x's will be moved to the end: ")
    index = 0
    x_counter = 0
    new_word = ''
    print_string(user_string, index, x_counter, new_word)


if __name__ == '__main__':
    main()