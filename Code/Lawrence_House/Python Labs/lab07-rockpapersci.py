import random

#   Version 1  Regular Rock paper scissors

choice_list = ['rock', 'paper','scissors']

print('WELCOME TO ROCK, PAPER, SCISSORS!!!\n')

user_choice = input('Rock, paper, or scissors? ')


computer = random.choice(choice_list)
print("\nLooks like your Rival chooses. . . " + computer + "\n")


if user_choice == 'rock' and computer == 'rock':
    print('You tied!!!')
elif user_choice == 'paper' and computer == 'paper':
    print('You tied!!!')
elif user_choice == 'scissors' and computer == 'scissors':
    print('You tied!!!')
elif user_choice == 'rock' and computer == 'paper':
    print('You LOSE!!!')
elif user_choice == 'paper' and computer == 'scissors':
    print('You LOSE!!!')
elif user_choice == 'scissors' and computer == 'rock':
    print('You LOSE!!!')
elif user_choice == 'rock' and computer == 'scissors':
    print('You WIN!!!')
elif user_choice == 'paper' and computer == 'rock':
    print('You WIN!!!')
elif user_choice == 'scissors' and computer == 'paper':
    print('You WIN!!!')