"""
    CS 5001
    Lab 2
    Exercise 2
    Name: Alex Perkins
"""

'''
One of my favorite card games is called Hand and Foot. 
The goal of the game is to generate piles of cards of the same rank. 
Cards with different ranks have different values. For this question, 
you will implement a Hand and Foot helper that will prompt the user for a card rank 
and will output the value for the given card. The value for each rank is as follows:
Jokers = 50 points
Twos & Aces = 20 points
Nine, Ten, Jack, Queen, King = 10 points
Four, Five, Six, Seven = 5 points
Black Threes = 5 points
Red Threes = No value
Note that the value of a Three will differ based upon the color. 
Your program will prompt the user for the rank and, 
if the rank is a Three, it will need to also prompt the user for the color.
'''

def main():
    rank = input('Hi, enter the card rank: ')
    rank = rank.capitalize()
    if (rank == "Joker" or rank == "Jokers"):
        points = 50
    elif (rank == "Two" or rank == "Twos" or rank == "Ace" or rank == "Aces"):
        points = 20
    elif (rank == "Nine" or rank == "Ten" or rank == "Jack" or rank == "Queen" or rank == "King"):
        points = 10
    elif (rank == "Four" or rank == "Five" or rank == "Six" or rank == "Seven"):
        points = 5
    elif (rank == "Three" or rank == "Threes"):
        color = input("What's the color? ")
        if (color.capitalize() == "Black"):
            points = 5
        else:
            points = 0
    else:
        points = 0

    print(f'Total points is {points}')


if __name__ == '__main__':
    main()
