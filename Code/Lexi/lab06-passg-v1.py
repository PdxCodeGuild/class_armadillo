# #https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/labs/lab06-random_password.md

# Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters, e.g. a62xB95. Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

# Concepts Covered
# input, print
# looping
# random.choice
# the 'sting builder pattern'
# Version 2
# Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string.

# Version 3 (optional)
# Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. You do not want the pieces in order (e.g. 3 lowercase letters followed by 3 uppercase letters...). You can use list(password_string) or password_string.split('') to convert the string to a list, random.shuffle(password_list) to shuffle it, and then ''.join(password_list) to turn it back into a string.
import string
import random

i = 0
while i < 2:
    i += 1
    code = print(input("Would you like a password generated?"))
    lil = string.ascii_letters + string.ascii_uppercase + string.punctuation
    if code != 'no':
        print("++loading++")
        break

max = int(input("how many characters do you want your password to be? "))

p = "".join(random.sample(lil, max))
print(p)
# for i in range(max):
#     print(lil)
# import string
# import random
# https://www.practicepython.org/solution/2014/06/06/16-passw
# 
# ord-generator-solutions.html

# def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
# 	return ''.join(random.choice(chars) for _ in range(size))

# print(pw_gen(int(input('How many characters in your password?'))))