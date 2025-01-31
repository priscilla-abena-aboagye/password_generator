import secrets
import string

def generate_password():
    # All the characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all the characters
    all_characters = letters + digits + symbols