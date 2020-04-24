#this lab allows user to guess pre generate number between 1-10.  Tells user if their guesses is high or low.

import random

#have the computer randomly choose aa number
computer_choice = random.randint(1, 10)
# print(computer_choice)

i = 1  #start at 1
while True:
    #ask the user for their guess
    user_input = int(input('Guess a number between 1 and 10: '))
    #check if user guessed the correct answer
    if user_input == computer_choice:
        print(f'You got it right! You guessed {i} times')  #shows user how many guesses they took
        break
    elif user_input > computer_choice:  #if user input higher than random choice: return too high
        print("too high,", end=" ")  
    else:
        print("too low,", end=" ")     
    print('try again') #end= "" places try again on same line as too low or too high
    
    i += 1 #adds guess to tally