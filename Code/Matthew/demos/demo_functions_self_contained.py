
import random
import string

# self-contained functions
# not referring to variables outside the function
# operating on parameters, local variables, and returning something

# if a function changes outside variables
# it can lead to unpredictable code, unexpected


n = int(input('what is the length of your password? '))

def random_password():
  password = ''
  for i in range(n): # problem 1 - referring to outside variables
    password += random.choice(string.ascii_letters + string.digits)
  print(password) # problem 2 - printing instead of returning


random_password()
random_password()










