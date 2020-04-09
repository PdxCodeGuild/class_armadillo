import random

winning = [
    ('rock', 'scissors'),
    ('scissors', 'paper'),
    ('paper', 'rock'),
]

while True:
    user_input = input('\nPlease enter (rock, paper, scissors): ')
    computer_move = random.choice(['rock', 'scissors','paper'])

    win_message = f'You won! User chose {user_input} and computer chose {computer_move}.'
    lose_message = f'You Lost! User chose {user_input} and computer chose {computer_move}.'

    for i in winning:
        if user_input == i[0] and computer_move == i[1]:
            print(win_message)
            break
        if computer_move == i[0] and user_input == i[1]:
            print(lose_message)
            break

    play_again = input('\nDo you want to play again? (y or n): ')
    if play_again != 'y':
        break
    else: 
        continue