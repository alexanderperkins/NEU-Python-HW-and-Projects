"""
--------------------------
Midterm Substitution Cipher
--------------------------
STUDENT: Alex Perkins
SEMESTER: Spring 2023
"""
import sys
from string import digits, ascii_letters, punctuation
from random import sample

# use this for your original alphabet string. Excludes punctuation
ALL_LETTERS_DIGITS = " " + digits + ascii_letters
# use this random key if none is provided, try printing it out to see what it is
RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))
# use this for alphabet string plus punctuation
ALL_ASCII_PUNC = " " + digits + ascii_letters + punctuation
# use this random key to generate with punctuation
RANDOM_KEY_PUNC = "".join(sample(list(ALL_ASCII_PUNC), len(ALL_ASCII_PUNC)))


# add your functions here. Includes function for encrypting message without punctuation
def encrypt(m, c1, k, c2):
    for letter in m:
        index = c1.index(letter)
        c2 += k[index]
    return c2


# Decrypts encrypted message to revert to original message and check it matches
def decrypt(c1, c2, k):
    m = ""
    for letter in c1:
        index = k.index(letter)
        m += c2[index]
    return m


# Checks if message has punctuation
def contains_punctuation(string_to_verify):
    return any(p in string_to_verify for p in punctuation)


# Do not modify the arguments for main, we will call it directly
def main(action: str, msg: str, key: str):
    """ Starting point of your program. You must start here."""
    cipher = ''
    if msg == "":
        msg = input("Message is blank. Insert message: \n")
    else:
        print("Your message is: ", msg)

    if action == "":
        action = input("Action is blank. Type encrypt or decrypt: \n")

    if action == "encrypt":
        # if contains punctuation
        if contains_punctuation(msg):
            if key == "":
                key = RANDOM_KEY_PUNC
            cipher = encrypt(msg, ALL_ASCII_PUNC, key, cipher)
        else:
            if key == "":
                key = RANDOM_KEY
            cipher = encrypt(msg, ALL_LETTERS_DIGITS, key, cipher)
        print(f"Encrypted={cipher}\n"
              f"Key={key}")
    elif action == "decrypt":
        if not key:
            raise Exception("Key was not provided.")
        if contains_punctuation(msg):
            cipher = encrypt(msg, ALL_ASCII_PUNC, key, cipher)
            cipher = decrypt(cipher, ALL_ASCII_PUNC, key)
        else:
            cipher = encrypt(msg, ALL_LETTERS_DIGITS, key, cipher)
            cipher = decrypt(cipher, ALL_LETTERS_DIGITS, key)
        print(f"Decrypted message is: {cipher}")
    else:
        print("Incorrect action chosen \n")
        cipher = ""
        print(cipher)


# The following allows us to run various features from the command line
# do not modify.
# If you wish to run the program from the command line
# You could do the following
# python subcipher.py "Aloha, World"
# that will encrypt this is my message and return both message and key
# you can decrypt by adding -d or --decrypt as the first argument, and then a key after the message
# python subcipher.py -d "9HUqv, VUEHQ" "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO"
if __name__ == "__main__":
    # check to see if there are command line arguments
    _action = 'encrypt'
    _msg = ''
    _key = ''
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
            _action = 'decrypt'
            remainder = sys.argv[2:]
        else:
            remainder = sys.argv[1:]
        if len(remainder) > 0:
            _msg = remainder[0]
            if len(remainder) > 1:
                _key = remainder[1]
    main(_action, _msg, _key)
