# Lab 10: Blackjack Advice

# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

#     Less than 17, advise to "Hit"
#     Greater than or equal to 17, but less than 21, advise to "Stay"
#     Exactly 21, advise "Blackjack!"
#     Over 21, advise "Already Busted"

# Print out the current total point value and the advice.

# Define a dictionary of card names and their point values
card_values = {
    'A' :1,
    '2' :2,
    '3' :3,
    '4' :4,
    '5' :5,
    '6' :6,
    '7' :7,
    '8' :8,
    '9' :9,
    '10':10,
    'J' :10,
    'Q' :10,
    'K' :10,
}

#  ask the user for the first two card they were dealt
first_card  = input("What is your first card? ")
second_card = input("What is your second card? ")

# add those card values together by 
# using their names as keys in our dictionary
hand_total = card_values[first_card] + card_values[second_card]

# print(f"{hand_total = }")  # print variable with label in python 3.8

while True:
    if hand_total < 17:
        print(f"{hand_total} - Hit!")
    elif hand_total >= 17 and hand_total < 21:   # another way to write: 17 <= hand_total < 21 
        print(f"{hand_total} - Stay!")
    elif hand_total == 21:
        print(f"{hand_total} - Blackjack!")
        break
    else:
        print(f"{hand_total} - Busted!")
        break


    # ask the user how they would like to do.
    user_answer = input("Would you like to hit or stay? ")
    
    # if they hit, ask them for the value
    # of their next card, add it to the hand 
    # total and go to the top of the loop
    if user_answer == 'hit':
        next_card  = input("What is your next card? ")
        hand_total += card_values[next_card]

    # if they stay, break the loop
    elif user_answer == 'stay':
        print("thanks for playing")
        break