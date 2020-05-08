#RPS
import random

choices = {
    'rock': {
        'paper':0,
        'scissors':1
    },
    'paper': {
        'scissors':0,
        'rock':1
    },
    'scissors': {
        'rock':0,
        'paper':1
    }
}

game_on = True
while game_on:
    print("\n" + "-"*50)
    print("Hello, Hooman! Let's play rock, paper, scissors!")
    print("-"*50)

    user_choice = input("\nPlease choose 'rock', 'paper', or 'scissors': ")
    while user_choice not in choices.keys():
        print("That's not a valid choice.")
        user_choice = input("Please choose 'rock', 'paper', or 'scissors': ")

    computer_choice = random.choice(list(choices.keys()))

    print(f"\nThe computer picked {computer_choice} and you picked {user_choice}")
    if user_choice == computer_choice:
        print(f"You tied!")
    else:
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