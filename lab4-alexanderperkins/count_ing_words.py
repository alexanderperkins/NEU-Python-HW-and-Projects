"""
    CS 5001
    Lab 4
    Exercise 1
    Name: Alex Perkins
"""

'''
Write a Python program that uses a while loop to read words from the user until the user enters 'quit'. 
Print the number of words the user entered that ended with the characters 'ing'.

Requirements and Hints:

    Your solution must be case insensitive. The function lower() can be used on a string to convert all 
      of the characters to lower case.
    You will need to use another string function that we have not discussed in class. Refer to the String 
      Methods portion of the Python documentation: https://docs.python.org/3/library/stdtypes.html 

    Links to an external site.
    Sample output is as follows. Make sure to test thoroughly!

srollins@ada lab4 % python count_ing_words.py
Enter next word -- use 'quit' to end input: waiting
Enter next word -- use 'quit' to end input: enjoy
Enter next word -- use 'quit' to end input: happy
Enter next word -- use 'quit' to end input: working
Enter next word -- use 'quit' to end input: flying
Enter next word -- use 'quit' to end input: quit
You entered 3 words ending with 'ing'.
'''

def ing_word_counter():
    counter = 0     # counter used in while loop to count words entered by user
    ing_counter = 0     # counter used in while loop to count words ending with 'ing'
    read_word = ""      # defining or initiating user's input string
    suffix = "ing"      # suffix we're matching user's input for to count
    while read_word != "quit":      # condition for loop to continue while user does not enter 'quit'
        read_word = input("Enter a word -- use 'quit' to end input: ")      # user's input word
        counter += 1        # adding 1 to word count after user's entry above
        if read_word.endswith(suffix):      # condition for separating user's input for matching suffix
            ing_counter += 1        # adding 1 to words entered by user ending with 'ing'
    return ing_counter      # sending back number of words ending with matching suffix

def main():
    ing_word_count = ing_word_counter()     # storing returned value from matching suffix word count function
    print(f'You entered {ing_word_count} words ending with "ing"')      # showing number of user words ending 'ing'


if __name__ == '__main__':
    main()
