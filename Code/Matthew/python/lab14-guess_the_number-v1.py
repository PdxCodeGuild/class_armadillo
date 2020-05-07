
import random

# have the computer randomly choose a number
computer_choice = random.randint(1, 10)
# print(computer_choice)

i = 1
# loop 10 times
while i <= 10:
  # ask the user for their guess
  user_input = int(input('Guess a number between 1 and 10: '))
  # check if the user guessed the correct number
  if user_input == computer_choice:
    print(f'You got it right! You guessed {i} times')
    break
  # avoid printing 'try again' if the user runs out of guesses
  if i != 10:
    print('try again')
  i += 1
else: # this will run if we finish the loop without breaking
  print('You lost!')

# if i >= 10:
#   print('You lost!')












