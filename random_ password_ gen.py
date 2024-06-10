import random
import string

# Create randon password function

def create_random_password():
    print_title()
    num_1, letter_1, letter_2, special, length = collect_user_input()
    char_set = combine_characters(num_1, letter_1, letter_2, special)
    password = generate_password(char_set, length)
    print("Generated Password:", password)

# Print the name of the program

def print_title():
    print("Random Password Generator")
    print("")

# Get user input for each variable (number, letter (upper, lower) and symbol) and validate.

def collect_user_input():
    num_1 = validate_input("Include numbers (0-9)? (Y) or (N) ")
    letter_1 = validate_input("Include uppercase letters? (Y) or (N) ")
    letter_2 = validate_input("Include lowercase letters? (Y) or (N) ")
    special = validate_input("Include special characters? (Y) or (N) ")
    length = validate_length("Password length (8-30)? ")
    return num_1, letter_1, letter_2, special, length

def validate_input(prompt):
    while True:
        response = input(prompt)
        if response.upper() in ('Y', 'N'):
            return response.upper()
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def validate_length(prompt):
    while True:
        length = input(prompt)
        if length.isdigit() and 8 <= int(length) <= 30:
            return int(length)
        else:
            print("Invalid length. Please enter a number between 8 and 30.")

# Combine characters

def combine_characters(num_1, letter_1, letter_2, special):
    char_set = ""
    if num_1.upper() == 'Y':
        char_set += string.digits
    if letter_1.upper() == 'Y':
        char_set += string.ascii_uppercase
    if letter_2.upper() == 'Y':
        char_set += string.ascii_lowercase
    if special.upper() == 'Y':
        char_set += string.punctuation
    return char_set
    
# Create a random string based on user input

def generate_password(char_set, length):
    return''.join(random.choice(char_set) for _ in range(length))

# Call the random password function

create_random_password()