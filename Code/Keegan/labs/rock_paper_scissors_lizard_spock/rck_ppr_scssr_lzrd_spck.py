#RPS
import random

# scissors cut paper covers rock crushes lizard
# poisons spock smashes scissors decapitates lizard
# eats paper disproves spock vaporizes rock crushes scissors

def get_outcome_message(computer_choice, user_choice):
    '''
    Returns a short message describing the outcome of the game.
    '''

    messages = {
        'rockpaper'     : 'Paper covers Rock!',
        'rockscissors'  : 'Rock smashes Scissors!',
        'rocklizard'    : 'Rock smashes Lizard!',
        'rockspock'     : 'Spock vaporizes Rock!',
        'paperscissors' : 'Scissors cut Paper!',
        'paperlizard'   : 'Lizard eats Paper!',
        'paperspock'    : 'Paper disproves Spock!',
        'scissorslizard': 'Scissors decapitate Lizard!',
        'scissorsspock' : 'Spock smashes Scissors!',
        'lizardspock'   : 'Lizard poisons Spock!',

    }
    
    # check each key in messages dict
    # if the key contains the comp and user choices,
    # return the message at that key.
    for key in messages:
        if computer_choice in key and user_choice in key:
            message = messages[key]
    
    return message

choices = {
    'rock': { 
        'paper':0,
        'scissors':1,
        'lizard': 1,
        'spock': 0,
    },
    'paper': {
        'rock':1,
        'scissors':0,
        'lizard': 0,
        'spock': 1,
    },
    'scissors': {
        'rock':0,
        'paper':1,
        'lizard': 1,
        'spock': 0,
    },
    'lizard': {
        'rock': 0,
        'paper': 1,
        'scissors': 0,
        'spock': 1,
    },
    'spock': {
        'rock': 1,
        'paper': 0,
        'scissors': 1,
        'lizard': 0
    },
}


print("\n" + "-"*63)
print("Hello, Hooman! Let's play Rock, Paper, Scissors, Lizard, Spock!")
print("-"*63)

game_on = True
while game_on:

    user_choice = input("\nPlease choose 'Rock', 'Paper', 'Scissors', 'Lizard', or 'Spock: ")
    while user_choice not in choices.keys():
        print("That's not a valid choice.")
        user_choice = input("Please choose 'Rock', 'Paper', 'Scissors', 'Lizard', or 'Spock: ")

    computer_choice = random.choice(list(choices.keys()))

    print(f"\nThe computer picked {computer_choice.title()} and you picked {user_choice.title()}")
    if user_choice == computer_choice:
        print(f"You tied!")
    else:
        print(get_outcome_message(computer_choice, user_choice))
        
        if choices[user_choice][computer_choice] == 1:
            print("You won!")
        else:
            print("You lost!")
    

    while True:
        play_again = input("\nWould you like to play again?\nEnter 'y' for yes and 'n' for no: ").strip().lower()
        if play_again == 'y':
            break
        elif play_again == 'n':
            print("\nThanks for playing! Goodbye")
            game_on = False
            break
        else:
            print(f"\n\"{play_again}\" is not a valid choice.")
            continue