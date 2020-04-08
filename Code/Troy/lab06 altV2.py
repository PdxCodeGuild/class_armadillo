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
