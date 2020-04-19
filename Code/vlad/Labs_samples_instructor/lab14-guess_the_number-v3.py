#lab14-guess_the_number-v3 sample by the instructor: 

# def print(*values, sep=' ', end='\n')


# print('apples', 'bananas')
# print('apples', 'bananas', 'pears')
# print('apples', 'bananas', 'pears', sep='__')

# print('apples', end='')
# print('bananas', end='')
# print('pears', end='')

# for i in range(10):
#   print('x', end='')





import random

# have the computer randomly choose a number
computer_choice = random.randint(1, 10)
# print(computer_choice)

i = 1
# loop 10 times
while True:
  # ask the user for their guess
  user_input = int(input('Guess a number between 1 and 10: '))
  # check if the user guessed the correct number
  if user_input == computer_choice:
    print(f'You got it right! You guessed {i} times')
    break
  elif user_input > computer_choice:
    print('Your guess was too high, try again')
  else:
    print('Your guess was too low, try again')
  
  i += 1


# 1 2 3 4 (5) 6 7 8 9 10
#     3
#       4 - closer
#                 8 - further
