import random
import string

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
#print(alphabet)
num = int(input('How many characters would you like your password to have? (1 - 10) '))
print('Okay, here\'s your password: ')
password = ''

for int in range(num):
    print(random.choice(alphabet))
length = num 
password = ''
for i in range(num):     
    password += random.choice(alphabet)

    print(password)

