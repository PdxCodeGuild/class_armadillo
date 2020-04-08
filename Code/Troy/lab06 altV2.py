# import string
# import random

# def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
# 	return ''.join(random.choice(chars) for _ in range(size))

# print(pw_gen(int(input('How many characters in your password?'))))



import random
import string

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

number = input('Number of passwords? - ')
number = int(number)

length = input('Password length? - ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password = random.choice(alphabet)
        print(password, end= '')
