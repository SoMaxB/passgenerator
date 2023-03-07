import random

print("## Password Generator ##\n")

password = int(input("How many characters do you want in your password?\n"))

def generate_password():
    # Generate a list of characters that meet the requirements
    chars = []
    chars.extend(random.choice('0123456789'))
    chars.extend(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    chars.extend(random.choice('abcdefghijklmnopqrstuvwxyz'))
    chars.extend(random.choice('!@#$%^&*()_+'))

    # Fill the rest of the password with random characters
    while len(chars) < password:
        chars.extend(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+'))

    # Mix the characters
    random.shuffle(chars)

    # Join the characters in a string and return it as the password
    return ''.join(chars)


print(generate_password())
