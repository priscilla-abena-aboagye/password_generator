import re
import secrets
import string

def generate_password(length, nums, special_chars, lowercase, uppercase):
    # All the characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all the characters
    all_characters = letters + digits + symbols
    

    while True:
        password = ""
        # Generate a password
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [
                (nums, r"\d"),
                (lowercase, r"[a-z]"),
                (uppercase, r"[A-Z]"),
                (special_chars, fr"[{symbols}]")
                ] 
        count = 0  
        
        if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints):
            count == 4
            break

    return password

new_password = generate_password(8)
