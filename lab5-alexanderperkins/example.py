'''
Practice with for loops!
'''

def fun_with_for_loops():
	# Remember to call this function :)
	list = ["hello", "there", "cs", "5001", "class"]
	# i = 0
	# while i < len(list):
	# 	item = list[i]
	# 	print(f'{i} {item}')
	# 	i += 1

	# 15
	# 0 5 10 15

	# Iterating over a list is easier with a for loop!
	# string = 'hello class'
	# for item in list:
	# 	print(item)

	# Accessing the index using range()
	# for i in range(1, len(list), 2):
	# 	item = list[i]
	# 	print(f'{i} {item}')

	# Accessing the index using enumerate
	# for value in enumerate(list):
	# 	print(value)
	# for i, item in enumerate(list):
	# 	print(f'{i} --- {item}')

	# Using zip to iterate over two lists at once
	first_names = ['joe', 'jane', 'julio']
	last_names = ['berket', 'saberi', 'vega']

	for first, last in zip(first_names, last_names):
		print(f'First: {first} Last: {last}')


def multiples_of_5(number: int):
	'''
	A function that takes as input a positive integer and
	uses a for loop to print the multiples of 5 that are
	less than or equal to the number that was entered.
	'''
	for i in range(0, number+1, 5):
		# if i % 5 == 0:
		# 	print(i)
		print(i)

def is_vowel(char):
	vowel = ('a', 'e', 'i', 'o', 'u')
	char = char.lower()
	return char in vowel

def count_vowels(sentence: str) -> int:
	'''
	A function that takes as input a string and returns the number
	of vowels (a, e, i, o, u) that are found in the sentence.
	'''
	count = 0
	for char in sentence:
		if is_vowel(char):
			count += 1
	return count


def generate_user_names(first_names: list[str], last_names: list[str]) -> list[str]:
	for first, last in zip(first_names, last_names):
		first_initial = first[0]
		last_part = last[:7]
		username = first_initial + last_part
		usernames.append(username) #pycharm doesn't have append??
		#print(f'{first[0]}{last[0:7]}')

	'''
	A function that takes as input a list of strings
	representing first names and a list of strings representing
	last names and returns a list of usernames where the ith username
	is the first initial of the first name stored at the ith position
	of the first_names list concatenated with the first 7 characters
	of the last name stored at the ith position of the last_names
	list.
	'''
	return usernames


def nested_loops():
	pass

def main():
	# fun_with_for_loops()

	#sentence = input('Enter sentence: ')
	#count = count_vowels(sentence)
	#print(count)

	first_names = ['joe', 'jane', 'sally']
	last_names = ['ortega', 'saberi', 'berketrollins']
	# [jortega, jsaberi, sberketr]

	generate_user_names(first_names, last_names)


# result = count_vowels('hello')
# print(f'result: {result} expected result: 2')

# result = count_vowels('hello hello')
# print(f'result: {result} expected result: 4')

# result = count_vowels('hEllo hellO')
# print(f'result: {result} expected result: 4')


if __name__ == '__main__':
	main()
