import string
import random

def password_generator():
    while True:
        try:
            password_length = int(input("Enter the length of the password (minimum length is 8): "))
            if password_length >= 8:
                break
            else:
                print("Password length must be at least 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print("Enter the types of characters to include in the password:")
    print("1. Lowercase")
    print("2. Uppercase")
    print("3. Numbers")
    print("4. Special characters")
    
    character_types = []
    while True:
        option = int(input("Choose an option (1-4), or enter 0 when done: "))
        if option == 0:
            break
        elif option not in [1, 2, 3, 4]:
            print("Invalid option. Please choose a number between 1 and 4.")
        else:
            if option not in character_types:
                character_types.append(option)
    
    characters = ""
    if 1 in character_types:
        characters += string.ascii_lowercase
    if 2 in character_types:
        characters += string.ascii_uppercase
    if 3 in character_types:
        characters += string.digits
    if 4 in character_types:
        characters += string.punctuation
    
    password = "".join(random.choice(characters) for _ in range(password_length))
    
    print(f"Your generated password is: {password}")

password_generator()
