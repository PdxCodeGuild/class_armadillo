#lab06-random_password-v3 sample by instructor: 

# fruits = 'apples, bananas, pears'
# print(fruits)
# fruits = fruits.split(', ')
# print(fruits)
# fruits = ' - '.join(fruits)
# print(fruits)
# exit()

# cases
# this_is_snake_case
# thisIsCamelCase
# ThisIsPascalCaseOrTitleCase
# this-is-kebab-case

import string
import random
import time

excluded = ['|', '!', ';']

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabet += alphabet.upper()

# alphabet = string.ascii_letters + string.digits + string.punctuation

length_lowercase = int(input('how many lowercase letters? '))
length_uppercase = int(input('how many uppercase letters? '))
length_digits = int(input('how many digits? '))
length_special = int(input('how many special characters? '))

# seed = int(round(time.time() * 1000))
seed = 1586383252162
print(f'the seed is {seed}')
random.seed(seed)

password = ''
for i in range(length_lowercase):
    while True:
        character = random.choice(string.ascii_lowercase)
        if character not in excluded:
            password += character
            break
for i in range(length_uppercase):
    password += random.choice(string.ascii_uppercase)
for i in range(length_digits):
    password += random.choice(string.digits)
for i in range(length_special):
    password += random.choice(string.punctuation)


print(password)
password = list(password)
print(password)
random.shuffle(password)
print(password)
password = ''.join(password)
print(password)

# s = ''
# for i in range(10):
#     # s += str(i) # s = s + str(i)
#     s = str(i) + s
#     print(s)
# print(s)