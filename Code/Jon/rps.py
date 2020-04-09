import random

winning = [
    ['rock', 'scissors'],
    ['scissors', 'paper'],
    ['paper', 'rock'],
]

while True:
    user_input = input('\nPlease enter (rock, paper, scissors): ')
    computer_move = random.choice(['rock', 'scissors', 'paper'])

    for i in winning:
        if user_input == i[0] and computer_move == i[1]:
            print(f'You won! User chose {user_input} and computer chose {computer_move}.')
            break
        if computer_move == i[0] and user_input == i[1]:
            print(f'You Lost! User chose {user_input} and computer chose {computer_move}.')
            break
        if user_input == computer_move:
            print(f'Tie! User chose {user_input} and computer chose {computer_move}.')
            break

    play_again = input('\nDo you want to play again? (y or n): ')
    if play_again != 'y':
        print('Goodbye!')
        break
    else:
        continue