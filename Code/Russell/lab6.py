import string
import random

letters = string.ascii_letters + string.punctuation + string.digits

user = int(input('How many characters would you like in the random password?: '))
word = ""
for letter in range(user):
    word += random.choice(letters)
    
print(word)