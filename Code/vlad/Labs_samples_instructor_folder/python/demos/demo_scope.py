

# scope - range of code in which a variable is visible


p = 10
def add(a, b):
  print(p)
  return a + b
print(add(5, 2))

exit()



# functions limit the scope of a variable

def add(a, b):
  c = 10
  print(c) # totally fine
  return a + b
print(c) # crash - c is undefined
print(add(5, 2))


# this code works but is ambiguous and a little dangerous
temperature = 65
if temperature < 60:
  message = 'cold'
elif temperature < 80:
  message = 'warm'
else:
  message = 'hot'
print(message)

# this code crashes under certain conditions
# because message is not defined

import random
temperature = random.randint(50, 100)
if temperature < 60:
  ...
elif temperature < 80:
  message = 'warm'
else:
  ...
print(message)


# more clear way of writing the above
# declaring message outside the if statements tells the reader you'll use it
# it also prevents this code from crashing

temperature = 65
message = ''
if temperature < 60:
  message = 'cold'
elif temperature < 80:
  message = 'warm'
else:
  message = 'hot'
print(message)



# variable scope extends beyond loops too

# crash
# while False:
#   z = 10
# print(z)

for i in range(10):
  z = 10
print(z)
print(i)


x = input('enter a message: ')
if x: # ambiguous
  ...
if x != '': # better
  ...