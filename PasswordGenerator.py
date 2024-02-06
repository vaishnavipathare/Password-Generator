import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example: Generate a password with default length (12 characters)
password = generate_password()
print("Generated Password:", password)