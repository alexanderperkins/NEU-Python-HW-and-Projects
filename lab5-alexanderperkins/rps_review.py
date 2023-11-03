"""
    CS 5001
    Lab 5
    Exercise 2
    Name: Alex Perkins
    Reviewing Lutubulla's RPS
"""

'''
For this question, you will do a code review of an existing Python program that implements
 Rock/Paper/Scissors. Your code review must include at least five substantive comments about the code. 

Option 1: For option 1 you will work with a partner and each review the other person's solution.

Option 2:  For option 2 you will search the web for a Python Rock/Paper Scissors solution and submit
 a review of that solution.

Format: Your code review will be implemented as comments embedded in the code itself. So, you will
 download the program and insert block comments with your feedback.

Code Review Guidelines:

    You are encouraged to search the web for guidelines for doing a code review; however, be aware
     that many web pages will have information that does not apply in our context. 
    The Summary section at the bottom of this page is a good starting point:
     https://google.github.io/eng-practices/review/reviewer/looking-for.html 

Links to an external site. Consider questions such as the following:

    What good design practices does the code use? Are there any ways you would improve the design
     (e.g., how the program is broken into functions)?
    Are variables and functions named appropriately?
    Is the program documented well? Does it include comments that appropriately describe the design
     and functionality?
    Does the logic make sense? Could it be implemented in a way that would be easier to read?
    Are there any obvious errors you see in the program?
'''
import random

def get_random_choice():
	choice_number=random.randint(1,3)
	if choice_number==1:
		return 'rock'
	elif choice_number==2:
		return 'paper'
	else:
		return 'scissors'
	# short way to draft function and get random computer choice. For easier readability,
	# I think I'd rename or specify the get_random_choice to note it's the computer's choice
	# for the function. I'd also add spaces between defining the variables with their values.
	# PyCharm keeps telling me warnings listed for missing whitespace around the operators.

def get_user_choice():
	user_choice=input('Enter your choice with lower case only (rock, paper, or scissors): ')
	return user_choice
	# Simple function. Again, I'd add the space between the variable and assigned value for readability.

def compare(user_choice, computer_choice):
	print('Computer choice: ', computer_choice)
	if computer_choice==user_choice:
		print('Equal: same choices')
	else:
		if user_choice=='rock' :
			if computer_choice=='scissors':
				print('You won!')
			else:
				print('You lost!')
		elif user_choice=='paper':
			if computer_choice=='rock':
				print('You won!')
			else:
				print('You lost!')
		elif user_choice=='scissors':
			if computer_choice=='paper':
				print('You won!')
			else:
				print('You lost!')
	# Easy to follow. Would just add spaces. Looks like there's a typo for unneccessary space between 'rock' :
	# but it doesn't seem to impact anything other than stand out.

def main():
	computer_choice=get_random_choice()
	user_choice=get_user_choice()
	if user_choice !='rock' and user_choice!='paper' and user_choice!='scissors':
				print('Invalid choice. Game over.')
	else:
		compare(user_choice, computer_choice)
	# Overall design looks great. Each of the functions specialize in one purpose e.g. getting the
	# computer's choice using randint, retrieving input for user's choice, and comparing the choices
	# to declare a winner (or tie). One thing I'd do differently for design is have the user choice validation
	# in the get_user_choice function rather than in the main function.

	# Variables and functions are named adequately though I think the get_random_choice could be improved as
	# stated back in the function.

	# The program is not documented so that would help ease the understanding for someone who didn't know
	# what this was for unless they reviewed the exercise or ran it.

	# The logic makes sense, especially the compare function. It was much easier to read and follow than the
	# way I did my comparison function by stating exactly who won the way it'd be read or said in English.

	# No obvious that I can see here. Only the warnings about whitespaces seem to exist.

if __name__ == '__main__':
	main()