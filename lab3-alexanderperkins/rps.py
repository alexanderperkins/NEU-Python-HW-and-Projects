import random
"""
    CS 5001
    Lab 3
    Exercise 3
    Name: Alex Perkins
"""

'''
Write a Python program that uses functions to play the game rock, paper, scissors. Play will proceed as follows:

    A random number will be selected to represent the computer choice. A 1 will be "rock"; a 2 will be "paper";
     and a 3 will be "scissors".
    The user will be prompted to enter a choice of rock, paper, or scissors.
    If the user choice is valid the computer choice and user choice will be compared and a winner will be declared.
        paper beats rock 
        rock beats scissors
        scissors beats paper
    If the user choice is not valid then play will end.

Hints:

    Grading will primarily depend upon how you decompose your program into functions. Consider the steps listed
     above as you think about which functions to implement.
    You must validate the user input to confirm that it is either rock, paper, or scissors. 
'''

def computer_choice():
    random_number = random.randint(1, 3)
    computer = ""
    if (random_number == 1):
        computer = "ROCK"
    elif (random_number == 2):
        computer = "PAPER"
    elif (random_number == 3):
        computer = "SCISSORS"
    return computer

def user_choice():
    choice = input("Select rock, paper, or scissors: ")
    choice = choice.upper()
    if (choice != "ROCK" and choice != "PAPER" and choice != "SCISSORS"):
        print(f'Invalid choice. Play will end. {quit}')
        quit()
    while (choice == "ROCK" or choice == "PAPER" or choice == "SCISSORS"):
        validate = input(f'You chose {choice}, correct (Y/N)? ')
        validate = validate.upper()
        if (validate == "Y" or validate == "YES"):
            break
        elif (validate == "N" or validate == "NO"):
            choice = input("Select rock, paper, or scissors: ")
            choice = choice.upper()
            if (choice != "ROCK" and choice != "PAPER" and choice != "SCISSORS"):
                print(f'Invalid choice. Play will end. {quit}')
                quit()
    return choice

def declare_winner(computer, user):
    winner = ""
    if (user == computer):
        winner = "No one"
    elif (user == "ROCK"):
        if (computer == "PAPER"):
            winner = "Computer"
        elif (computer == "SCISSORS"):
            winner = "User"
    elif (user == "PAPER"):
        if (computer == "ROCK"):
            winner = "User"
        elif (computer == "SCISSORS"):
            winner = "Computer"
    elif (user == "SCISSORS"):
        if (computer == "ROCK"):
            winner = "Computer"
        elif (computer == "PAPER"):
            winner = "User"
    return winner

def main():
    print("Let's play rock, paper, scissors!")
    computer = computer_choice()
    user = user_choice()
    print(f'Computer chose {computer}')
    winner = declare_winner(computer, user)
    while (winner == "No one"):
        print("Tie game. Try again.")
        computer = ""
        user = ""
        ''' 
        For some odd reason (recall if tie, user == computer), if I don't clear computer and user choices,
        Tie consistently continues after validating Y/yes, but would break out of tie after saying N/no.
        This happens even though user and computer choices are restated to blank in each of their functions
        individually or one by one. As such, restated to clear them again in the main function and it works.
        No more never ending ties after 1st tie.
        '''
        computer = computer_choice()
        user = user_choice()
        print(f'Computer chose {computer}')
        winner = declare_winner(computer, user)
        if (winner == "Computer" or winner == "User"):
            break
    print(f'Winner is {winner}')
    if (winner == "User"):
        print("You won!")
    elif (winner == "Computer"):
        print("You lose!")


if __name__ == '__main__':
    main()
