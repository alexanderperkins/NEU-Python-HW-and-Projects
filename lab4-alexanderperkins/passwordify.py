"""
    CS 5001
    Lab 4
    Exercise 2
    Name: Alex Perkins
"""

'''
Write a Python program that uses a function passwordify to convert a phrase to a version of the 
 phrase that you might use as a password. The function will take as input the original phrase and 
 will return the passwordified phrase as output. The rules for passwordification are as follows:

    All instances of the character 's' or 'S' will be replaced with '$'
    All instances of the character 'l' or 'L' will be replaced with 1.
    All spaces will be replaced with '-'.
    The words 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', and 
    'ten' will be replaced by their numerical equivalent no matter where they appear in the phrase.

Example:

    input = ""sleeping in a tent"
    output = "$1eeping-in-a-10t"

'''
def passwordify():
    counter = 0
    password = ''
    phrase = input('Enter a phrase to convert to password: ')
    while counter < len(phrase):
        if phrase[counter] == 's' or phrase[counter] == 'S':
            password += '$'
        elif phrase[counter] == 'l' or phrase[counter] == 'L':
            password += '1'
        elif phrase[counter] == ' ':
            password += '-'
        else:
            password += phrase[counter]
        counter += 1
    password = password.replace('one', '1')
    password = password.replace('two', '2')
    password = password.replace('three', '3')
    password = password.replace('four', '4')
    password = password.replace('five', '5')
    password = password.replace('six', '6')
    password = password.replace('seven', '7')
    password = password.replace('eight', '8')
    password = password.replace('nine', '9')
    password = password.replace('ten', '10')
    return phrase, password

def main():
    phrase, password = passwordify()
    print(f'You entered the phrase: \n{phrase}')
    print(f'It was converted to: \n{password}')


if __name__ == '__main__':
    main()
