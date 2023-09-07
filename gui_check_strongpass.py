def check_password_strength(password: str) -> int:
    # Set initial password strength to 0
    strength = 0
    
    # Check password length
    if len(password) < 8:
        return strength
    
    # Check for lowercase letters
    has_lowercase = any(char.islower() for char in password)
    
    # Check for uppercase letters
    has_uppercase = any(char.isupper() for char in password)
    
    # Check for digits
    has_digits = any(char.isdigit() for char in password)
    
    # Check for special characters
    has_special = any(char in '!@#$%^&*()_+-=[]{}|;:,.<>/?' for char in password)

    # Check for spaces
    has_spaces = any(char.isspace() for char in password)
    
    # Update strength based on criteria
    if has_lowercase or has_uppercase:
        strength = 1
    if (has_lowercase and has_digits) or (has_uppercase and has_digits):
        strength = 2
    if has_lowercase and has_uppercase and has_digits:
        strength = 3
    if has_lowercase and has_uppercase and has_digits and has_special:
        strength = 4
    if has_lowercase and has_uppercase and has_digits and has_special and has_spaces:
        strength = 5
    return strength

