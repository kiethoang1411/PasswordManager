import string

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def encode_letter(letter):
    rule_upper = {
        'ZY': 'A', 'YX': 'B', 'XV': 'C', 'VT': 'D', 'TS': 'E',
        'SR': 'F', 'RQ': 'G', 'QP': 'H', 'PO': 'I', 'ON': 'J',
        'NM': 'K', 'ML': 'L', 'LK': 'M', 'KJ': 'N', 'JI': 'O',
        'IH': 'P', 'HG': 'Q', 'GF': 'R', 'FE': 'S', 'ED': 'T',
        'DC': 'U', 'CB': 'V', 'BA': 'W', 'AZ': 'X', 'ZA': 'Y',
        'AB': 'Z'
    }

    rule_lower = {
        'a': 'zy', 'b': 'yx', 'c': 'xv', 'd': 'vt', 'e': 'ts',
        'f': 'sr', 'g': 'rq', 'h': 'qp', 'i': 'po', 'j': 'on',
        'k': 'nm', 'l': 'ml', 'm': 'lk', 'n': 'kj', 'o': 'ji',
        'p': 'ih', 'q': 'hg', 'r': 'gf', 's': 'fe', 't': 'ed',
        'u': 'dc', 'v': 'cb', 'w': 'ba', 'x': 'az'
    }

    if letter in rule_upper:
        return rule_upper[letter]
    elif letter in rule_lower:
        return rule_lower[letter]
    else:
        return letter

def rot5(text):
    rot5_trans = str.maketrans(string.digits, '5678901234')
    return text.translate(rot5_trans)

def rotate_special_characters(text, rotation=3):
    encoded_text = ''
    for char in text:
        if '!' <= char <= '~':  # Check if the character is a printable ASCII character
            encoded_char = chr(((ord(char) - 33 + rotation) % 95) + 33)  # Use modulo 95
        else:
            encoded_char = char
        encoded_text += encoded_char
    return encoded_text

def encode_text(text):
    encoded_text = ''
    for i, char in enumerate(text):
        if is_prime(i + 1):
            if encoded_text and encoded_text[-1] != '=':
                encoded_text += '='  # Insert '=' if the previous character is not '='
            encoded_text += encode_letter(char) + '='
        elif char.isdigit():  # Use ROT5 for numbers
            encoded_text += rot5(char)
        elif char.isalpha():  # Use ROT13 for alphabetic characters
            encoded_text += encode_letter(char)
        else:  # Use rotate_special_characters for special characters
            if encoded_text and encoded_text[-1] != '-':
                encoded_text += '-'  # Insert '-' if the previous character is not '-'
            encoded_text += rotate_special_characters(char)
    return encoded_text


def decode_text(encoded_text):
    decoded_text = ''
    prime_index = False  # To keep track of whether the current index is prime
    combined_char = ''   # To store the character at prime index for combining
    for i, char in enumerate(encoded_text):
        if is_prime(i + 1):
            prime_index = True
            combined_char = char  # Store the current character
        elif prime_index:
            prime_index = False
            combined_char += char
        else:
            decoded_text += encode_letter(combined_char)  # Decode the combined characters
            combined_char = ''  # Reset combined_char
            if char.isdigit():  # Use ROT5 for numbers
                decoded_text += rot5(char)
            elif char.isalpha():  # Use ROT13 for alphabetic characters
                decoded_text += encode_letter(char)
            else:  # Use rotate_special_characters for special characters
                decoded_text += rotate_special_characters(char, -3)  # Rotate in the opposite direction when decoding

    if prime_index:  # Check if there's a character at the end of the string
        decoded_text += encode_letter(combined_char)

    return decoded_text



user_input = input("Enter a string: ")
encoded_result = encode_text(user_input)
print("Encoded Result:", encoded_result)
decoded_result = decode_text(encoded_result)
print("Decoded Result:", decoded_result)
