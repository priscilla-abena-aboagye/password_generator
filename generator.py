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
                (nums, "[0123456789]")
                ]

    return password

new_password = generate_password(8)

pattern = re.compile("a")
quote = "Frank and Ben are my brothers"
print(pattern.search(quote))

# Alternate code
# pattern = "r[aos]"
# quote = "Frank and Ben are my brothers"
# print(re.findall(pattern, quote))