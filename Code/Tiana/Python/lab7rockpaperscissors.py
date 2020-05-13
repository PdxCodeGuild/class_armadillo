#Rock Paper Scissors

import random

print('Let\'s play Rock Paper Scissors!!' )



while True:
    #ask the user for their choice rock, paper, scissors
    choice = input('Choose rock, paper or scissors: ')

    #computer will randomly choose rock, paper, scissors
    computer = [ 'rock', 'paper', 'scissors' ]
    ran_computer = random.choice(computer)
    print(f" The computer chose {ran_computer}. ")



    if ran_computer == choice:
        print('Its a tie!! ')
        
    elif choice == 'rock' and ran_computer == 'paper':
        print('The computer won! ')                         #Determine who won and tell the user
    elif choice == 'rock' and ran_computer == 'scissors':
        print('You won! ')
    elif choice == 'paper' and ran_computer == 'rock':
        print('You won! ')
    elif choice == 'paper' and ran_computer == 'scissors':
        print('The computer won! ')
    elif choice == 'scissors' and ran_computer == 'rock':
        print('The computer won! ')
    elif choice == 'scissors' and ran_computer == 'paper':
        print('You won! ')


#Ask the user if they would like to play again, loop until they do not say yes.
    question = input('Would you like to play again? ')

    if question != 'yes':
        print('Thanks for playing!! ')
        break
    else:
        continue