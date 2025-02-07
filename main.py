import random
import string
import pyperclip

def generate_password(length, upper, lower, digits, special):
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character must be selected!")
    
    return ''.join(random.choice(characters) for _ in range (length))

def main():
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    special = input("Include punctuation? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, upper, lower, digits, special)
        print(f"Generated Password: {password}")
        pyperclip.copy(password)
        print("Password copied to clipboard!")
    except ValueError as e:
        print(e)


main()