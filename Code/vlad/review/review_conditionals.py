#review_conditionals.py

# == != < <= > >= ==================================

temperature = 67
is_hot = temperature > 80 # comparison operators yield booleans!
print(is_hot)

if temperature > 80:
  print('hot')
elif temperature > 60:
  print('warm')
else:
  print('cold')


# everything is truthy except None, 0, '', [], {}
values = [0, -1, 1, 'hi', '', [], ['hi'], {}, {'apples': 5.0}]
for value in values:
  print(value, 'is', bool(value))

# prices = {'apples': 5.0}
# if prices:

# while True:
#   name = input('enter your name: ')
#   if name != '':
#     break
# print(name)


# while not name: # keep looping while name is a ''
#   name = input('enter your name: ')
# print(name)

# keep_going = 'yes'
# while keep_going == 'yes':
#   keep_going = input('should I keep going? yes/no ')



# and, or, not ==================================


raining = False
lazy = False
go_outside = not raining and not lazy
go_outside = raining == False and lazy == False


# "a and b" is true if a is true and b is true
# "a or b" is true if a is true or b is true

# if grade > 80 and grade < 90
