#lab14-guess_the_number-v4 sample by instructor: 

# 1 2 3 4 (5) 6 7 8 9 10
#     3
#       4 - closer
#                 8 - further



import random

# have the computer randomly choose a number
computer_choice = random.randint(1, 10)
# print(computer_choice)

last_guess = 0

i = 1
# loop 10 times
while True:
  
  # ask the user for their guess
  user_input = int(input('Guess a number between 1 and 10: '))
  # check if the user guessed the correct number
  if user_input == computer_choice:
    print(f'You got it right! You guessed {i} times')
    break
  if last_guess != 0:
    d1 = abs(user_input-computer_choice)
    d2 = abs(last_guess-computer_choice)
    if d1 < d2:
      print('Warmer')
    elif d1 > d2:
      print('Colder')
    else:
      print('just as far away')
  last_guess = user_input
  i += 1