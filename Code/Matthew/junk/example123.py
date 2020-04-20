


import random
import string


def generate_password(n=10):
  password = ''
  for i in range(n):
    password += random.choice(string.ascii_letters + string.digits)
  return password


n = 45
password = generate_password(n)
print(password)


