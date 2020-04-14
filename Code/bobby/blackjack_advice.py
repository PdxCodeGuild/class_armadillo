# Lab 10: Blackjack Advice
# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!

# Version 2 (optional)
# Aces can be worth 11 if they won't put the total point value of 
# both cards over 21. Remember that you can have multiple aces in
#  a hand. Try generating a list of all possible hand values by
#  doubling the number of values in the output whenever you 
# encounter an ace. For one half, add 1, for the other, add 11.
#  This ensures if you have multiple aces that you account for 
# the full range of possible values.



card_value = {
    "a" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10": 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 11
    }


first_card = input("what is your first card? ")
second_card = input("what is your next card? ")

hand_total = card_value[first_card] + card_value[second_card]

# hand_total = first_card + second_card

print(f"{hand_total = }")
while True:
    if hand_total < 17:
        print(f"{hand_total} - Hit me!")
    elif hand_total >= 17 and hand_total <= 21:
        print(f"{hand_total} - (Stay")
    elif hand_total == 21:
        print(f"{hand_total} - Blackjack")
       
    else:
        print(f"{hand_total} - Bust")

    user_answer = input("Would you like to hit or stay? ")
    if user_answer == 'hit':
        next_card = input("What is your next card? ")
        hand_total += card_value[next_card]

    elif user_answer == 'stay':
        print("Thanks for Playing")
        break