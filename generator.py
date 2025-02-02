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
                (nums, r"[0-9]"),
                (lowercase, r"[a-z]"),
                (uppercase, r"[A-Z]")
                (special_chars, r"")
                ]   

    return password

new_password = generate_password(8)

# Alternate code
# pattern = re.compile("a")
# quote = "Frank and Ben are my brothers"
# print(pattern.search(quote))


pattern = r"\."
quote = "Frank and Ben are my brothers"
print(re.findall(pattern, quote))