import requests
import hashlib

# Function to get the first 5 characters of the SHA-1 hash
def get_hash_prefix(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    return sha1_hash[:5]

# Function to check if the password has been pwned
def check_password_pwned(password):
    # Get the first 5 characters of the hash
    hash_prefix = get_hash_prefix(password)

    # Make a GET request to the "Have I Been Pwned" API
    api_url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    response = requests.get(api_url)

    # Check if the response status code is OK (200)
    if response.status_code == 200:
        # Split the response by line and check if the full hash appears
        hashes = response.text.split('\n')
        full_hash = hashlib.sha1(password.encode()).hexdigest().upper()[5:]
        for h in hashes:
            if h.startswith(full_hash):
                return f"The password '{password}' has been pwned {h.split(':')[1]} times."
        return f"The password '{password}' has not been pwned."
    else:
        return "Failed to check the password."

# Get user input for the password
password = input("Enter the password to check: ")

# Check if the password has been pwned
result = check_password_pwned(password)
print(result)
