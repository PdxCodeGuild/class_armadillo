import random


moves = ['rock', 'paper', 'scissors']


user = ''
while user != 'done':
    computer = random.choice(moves)
    user = input('Choose rock, paper, or scissors or type done when finished: ')
    
    if user == computer:
        print('tie')
    elif user == 'rock' and computer == 'paper':
        print('Computer wins')
    elif user == 'rock' and computer == 'scissors':
        print('You win')
    elif user == 'paper' and computer == 'rock':
        print('You win')
    elif user == 'paper' and computer == 'scissors':
        print('Computer wins')
    elif user == 'scissors' and computer == 'rock':
        print('You win')
    elif user == 'scissors' and computer == 'paper':
        print('You win') 
    

