import random

choice_list = ['rock', 'paper','scissors']

print('WELCOME TO ROCK, PAPER, SCISSORS!!!\n')

user_choice = input('Rock, paper, or scissors? ')


computer = random.choice(choice_list)
print("\nLooks like your Rival chooses. . . " + computer + "\n")



if user_choice == 'rock' and computer == 'rock' or user_choice == 'paper' and computer == 'paper' or user_choice == 'scissors' and computer == 'scissors':
    print('You tied!!!')
elif user_choice == 'rock' and computer == 'paper' or user_choice == 'paper' and computer == 'scissors' or user_choice == 'scissors' and computer == 'rock':
    print('You LOSE!!!')
elif user_choice == 'rock' and computer == 'scissors' or user_choice == 'paper' and computer == 'rock' or user_choice == 'scissors' and computer == 'paper':
    print('You WIN!!!')

