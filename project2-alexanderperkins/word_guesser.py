"""
    CS 5001
    Project 2
    Name: Alex Perkins
"""

import random  # library required to randomly choose a secret word

def get_secret_word() -> str:
	"""
	Returns a randomly generated secret word.
	Uses the list of words in the public domain retrieved from:
	https://www-cs-faculty.stanford.edu/~knuth/sgb.html
	Requires a text file called words.txt.
	"""
	with open('words.txt') as f:
		words = f.read().splitlines()
		word = random.choice(words)
	return word

def get_user_guess():
	"""
	Returns user's guessed word. Error check loop to make user repeat until word is only 5 letters.
	"""
	guess = input("Guess the 5 letter word: ")
	while len(guess) != 5:
		print("***Error***")
		guess = input("You did not enter a 5 letter word. Please enter a 5 letter word only: ")
	return guess

def match_letters(secret_word, guess, unmatched_letters):
	"""
	Compares letters in user's guess word against those in random word in two ways. First,
	 checks by indexed position to return 'G' for matches. Second, it checks if the letter
	  exists in any position in the random word and returns 'Y' for matches. If it doesn't
	  exist, shows the unmatched letters for reference.
	"""
	index = 0
	matches = ''
	guess_attempt = ''
	position_matches = ''
	for character in guess:
		if character == secret_word[index]:
			guess_attempt += character
			matches += 'G'
			position_matches += character
			# position_matches is to track 'G' or matching letters and positions for 'Y' for loop below
		else:
			guess_attempt += '_'
			matches += '_'
		index += 1
	index = 0
	for character in guess:
		guess_attempt = list(guess_attempt)
		matches = list(matches)
		# putting guessed letters and matches into a list to edit them due to immutable string error
		if character == secret_word[index]:
			guess_attempt[index] = character
			# for each position, keeping matched letters
		elif character in secret_word:
			max_character_matches = secret_word.count(character) - position_matches.count(character) - 1
			# gives limit of what maximum matched letters excluding those matched for index/position 'Y' can be.
			# needed to subtract out position matches that are already noted as 'G' above loop for length minus 1
			# print(max_character_matches) # keeping note for check reference of y's not in g
			#  or matched letters not in same index/position
			guessed_character_matches = guess_attempt.count(character)
			# need comparison of matching characters from guess in random/secret word
			# print(guessed_character_matches) # keeping here for testing purposes for reference
			if guessed_character_matches > max_character_matches:
				guess_attempt[index] = '_'
			else:
				guess_attempt[index] = character
				matches[index] = 'Y'
		# Needed to determine number of those matched characters not in the same position e.g. if user
		# includes 'e' 3 times, but random word only includes it 2 times, will only match 2.
		else:
			guess_attempt[index] = '_'
			matches[index] = '_'
			if character not in unmatched_letters:
				unmatched_letters += character + ' '
		guess_attempt = "".join(guess_attempt)
		matches = "".join(matches)
		# need to join the lists back together to put into string (undoing original list)
		index += 1
	print(guess_attempt)
	print(matches)
	print(unmatched_letters)
	return guess_attempt, matches, unmatched_letters

def guess_attempts(secret):
	"""
	Allows user to make or repeat up to 6 guesses to match the random word.
	Let's user know how many more attempts they have if they don't get the right word.
	"""
	user_guesses = 0
	max_guesses = 6
	unmatched_letters = ''
	while max_guesses > user_guesses:
		guess = get_user_guess()
		attempt, match, unmatched_letters = match_letters(secret, guess, unmatched_letters)
		user_guesses += 1
		if guess == secret:
			break
		print(f'Nice try! You have {max_guesses - user_guesses} guesses left.')
	return user_guesses, attempt, match

def game_result(attempts, guess, secret, wins, losses):
	"""
	Tells the user if they won or not. If they didn't win, shows the random word.
	Also, returns +1 to wins or losses to help track record for later function.
	"""
	if guess == secret:
		print(f'You won! It took you {attempts} tries.')
		wins += 1
	else:
		print("You lose. Better luck next time! Secret word was: ", secret)
		losses += 1
	return wins, losses

def play_game():
	"""
	Enables user to play again or quit with error checking if user doesn't answer yes or no.
	"""
	wins = 0
	losses = 0
	play = 'Y'
	while play == 'Y' or play == 'YES':
		random_word = get_secret_word()
		# print(random_word)  # keeping for testing purposes to track secret/random word & compare
		guesses, guess_result, matches = guess_attempts(random_word)
		wins, losses = game_result(guesses, guess_result, random_word, wins, losses)
		play = input("Want to play again (Y/N)? ")
		play = play.upper()
		while play != 'Y' and play != 'YES' and play != 'N' and play != 'NO':
			print("***Error*** \n You did not choose a valid response!")
			play = input("Want to play again (Y/N)? ")
			play = play.upper()
	game_wins_losses(wins, losses)

def game_wins_losses(wins, losses):
	"""
	Shows record of wins and losses.
	"""
	print(f'You won {wins} times and lost {losses} times!')
	return

def main():
	play_game()


if __name__ == '__main__':
	main()
