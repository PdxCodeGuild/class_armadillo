



import random
import string

# self-contained functions
# not referring to variables outside the function
# operating on parameters, local variables, and returning something

# if a function changes outside variables
# it can lead to unpredictable code, unexpected

def random_password(n):
  password = ''
  for i in range(n):
    password += random.choice(string.ascii_letters + string.digits)
  return password


if __name__ == '__main__':
  n = int(input('what is the length of your password? '))
  print(random_password(n))









