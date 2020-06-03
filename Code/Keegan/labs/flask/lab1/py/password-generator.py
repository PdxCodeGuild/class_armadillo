import string
from random import choice, shuffle

def get_chars(n, char_set):
    return ''.join([choice(char_set) for i in range(n)])

def generate_password(letters, digits, special):
    
    password = ''
    password += get_chars(letters, string.ascii_letters)
    password += get_chars(digits, string.digits)
    password += get_chars(special, '!@#$%&*')

    password = list(password)
    shuffle(password)    
    
    return ''.join(password)


