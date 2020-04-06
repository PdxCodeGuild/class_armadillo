"""
Lab 6: generate a random password
"""

import random
import string

# alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJK@$%#^'
#
# n = int(input('how long should the password be?'))
#
# password = ''
# i = 0
# while i < n:
#     password += random.choice(alphabet)
#     i = i + 1
# print(password)

# alternatively, use a for-loop instead of a while-loop
# for i in range(n):
#     password += random.choice(alphabet)
# print(password

n_lowercase = int(input('how many lowercase characters? '))
n_uppercase = int(input('how many uppercase characters? '))
n_numbers = int(input('how many numerical characters? '))
n_special = int(input('how many special characters? '))


password = []
for i in range(n_lowercase):
    password.append(random.choice(string.ascii_lowercase))

for i in range(n_uppercase):
    password.append(random.choice(string.ascii_uppercase))

for i in range(n_numbers):
    password.append(random.choice(string.digits))

for i in range(n_special):
    password.append(random.choice('~`!@#$%^&*()-_=+[{]}\\|;:\'"<,>.?/'))

print(password)
random.shuffle(password)
password = ''.join(password)
print('-'*10 + 'YOUR PASSWORD IS' + '-'*10)
print(password)













