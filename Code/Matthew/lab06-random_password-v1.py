


# cases
# this_is_snake_case
# thisIsCamelCase
# ThisIsPascalCaseOrTitleCase
# this-is-kebab-case

import string
import random

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabet += alphabet.upper()

alphabet = string.ascii_letters + string.digits + string.punctuation

password_length = int(input('how many characters should the password be? '))
password = ''
for i in range(password_length):
    # print(random.choice(alphabet), end='')
    password += random.choice(alphabet)
print(password)

# s = ''
# for i in range(10):
#     # s += str(i) # s = s + str(i)
#     s = str(i) + s
#     print(s)
# print(s)
















