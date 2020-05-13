import string
 
def get_rotated(char, char_set, r):
    return char_set[(char_set.index(char) + r) % len(char_set)]

def rotate_string(user_string, r_factor):
    r_factor = int(r_factor) % 26
    alphabet       = string.ascii_lowercase
    alphabet_up    = string.ascii_uppercase
    numbers        = string.digits

    rotated_string = ''
    for char in user_string:
        if char in alphabet:
            rotated_string += get_rotated(char, alphabet, r_factor)
        elif char in alphabet_up:
            rotated_string += get_rotated(char, alphabet_up, r_factor)
        elif char in numbers:
            rotated_string += get_rotated(char, numbers, r_factor)
        else:
            rotated_string += char

    return rotated_string
