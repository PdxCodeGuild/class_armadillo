#this lab allows user to guesses a computer generated number between 1-10

import random
while True:
    #have the computer randomly choose a number
    computer_choice = random.randint(1, 10)
    # print(computer_choice)

    i = 1
    while i <= 10: #allows user 10 guesses
        #ask the user for their guess
        user_input = int(input('Guess a number between 1 and 10: '))
        #check if user guessed the correct answer
        if user_input == computer_choice:
            print(f'You got it right! You guessed {i} times')
            break
        #avoid printing 'try again' if the user runs out of guesses
        if i != 10:  
            print('try again')  #prints try again for each correct guess
        i += 1
    else:
        print('You lost!') #if user guesses 10 times, they lost.

    if input('Play again? Y/N') == 'n':  #if user selects 'n' break
        break           