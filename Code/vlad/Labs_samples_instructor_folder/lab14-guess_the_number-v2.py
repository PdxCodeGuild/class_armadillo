#lab14-guess_the_number-v2 sample by the instructor: 

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
  # avoid printing 'try again' if the user runs out of guesses
  print('try again')
  i += 1


