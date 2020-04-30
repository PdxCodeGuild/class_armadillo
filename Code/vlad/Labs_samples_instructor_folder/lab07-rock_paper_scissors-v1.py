#lab07-rock_paper_scissors-v1 sample by the instructor: 

import random

rps = ['rock', 'paper', 'scissors']

human_score = 0
computer_score = 0

while True:  # main game loop

    print(f'Human score {human_score}')
    print(f'Computer score {computer_score}')

    computer_choice = random.choice(rps)

    while True:  # get valid user input
        human_choice = input('Rock, paper, scissors or quit? ').lower().strip()
        if human_choice in ['q', 'quit', 'exit']:
            quit()
        if human_choice in rps:
            break
        print('please enter a valid option')

    # human_choice = None
    # while human_choice not in rps:
    #     human_choice = input('Rock, paper, or scissors? ').lower().strip()

    print('human chose ' + human_choice)
    print('computer chose ' + computer_choice)

    if human_choice == computer_choice:
        print('tie')
    elif human_choice == 'rock' and computer_choice == 'paper':
        print('computer wins')
        computer_score += 1
    elif human_choice == 'rock' and computer_choice == 'scissors':
        print('human wins')
        human_score += 1
    elif human_choice == 'paper' and computer_choice == 'rock':
        print('human wins')
        human_score += 1
    elif human_choice == 'paper' and computer_choice == 'scissors':
        print('computer wins')
        computer_score += 1
    elif human_choice == 'scissors' and computer_choice == 'rock':
        print('computer wins')
        computer_score += 1
    elif human_choice == 'scissors' and computer_choice == 'paper':
        print('human wins')
        human_score += 1
    print()