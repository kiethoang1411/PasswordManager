import string

rule_upper = {
    'A': 'ZY', 'B': 'YX', 'C': 'XV', 'D': 'VT', 'E': 'TS',
    'F': 'SR', 'G': 'RQ', 'H': 'QP', 'I': 'PO', 'J': 'ON',
    'K': 'NM', 'L': 'ML', 'M': 'LK', 'N': 'KJ', 'O': 'JI',
    'P': 'IH', 'Q': 'HG', 'R': 'GF', 'S': 'FE', 'T': 'ED',
    'U': 'DC', 'V': 'CB', 'W': 'BA', 'X': 'AZ', 'Y': 'ZA',
    'Z': 'AB'
}

rule_lower = {
    'a': 'zy', 'b': 'yx', 'c': 'xv', 'd': 'vt', 'e': 'ts',
    'f': 'sr', 'g': 'rq', 'h': 'qp', 'i': 'po', 'j': 'on',
    'k': 'nm', 'l': 'ml', 'm': 'lk', 'n': 'kj', 'o': 'ji',
    'p': 'ih', 'q': 'hg', 'r': 'gf', 's': 'fe', 't': 'ed',
    'u': 'dc', 'v': 'cb', 'w': 'ba', 'x': 'az'
}

def encode_letter(letter):
    if letter in rule_upper:
        return rule_upper[letter]
    elif letter in rule_lower:
        return rule_lower[letter]
    else:
        return letter

def rot5(text):
    rot5_trans = str.maketrans(string.digits, '5678901234')
    return text.translate(rot5_trans)

def encode_text(text):
    encoded_text = ''
    for char in text:
        if char.isdigit():  # Use ROT5 for numbers
            encoded_text += rot5(char)
        elif char.isalpha():  # Use encode_letter for alphabetic characters
            encoded_text += encode_letter(char)
        else:
            encoded_text += char
    return encoded_text

def decode_text(encoded_text):
    decoded_text = ''
    i = 0
    while i < len(encoded_text):
        char = encoded_text[i]
        if char.isdigit():  # Use ROT5 for numbers
            decoded_text += rot5(char)
            i += 1
        elif char.isalpha():  # Combine two letters and compare with dictionaries
            combined_letters = encoded_text[i:i + 2]
            i += 2
            for rule_dict in [rule_upper, rule_lower]:
                for key, value in rule_dict.items():
                    if value == combined_letters:
                        decoded_text += key
                        break
        else:
            decoded_text += char
            i += 1
    return decoded_text

user_input = input("Enter a string: ")
encoded_result = encode_text(user_input)
print("Encoded Result:", encoded_result)
decoded_result = decode_text(encoded_result)
print("Decoded Result:", decoded_result)
