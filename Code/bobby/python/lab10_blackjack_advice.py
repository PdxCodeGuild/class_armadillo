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


# Lab 10 Blackjack advice... game simulator

# The import time modual so that I can give user time to read 
# each message before the next one pops up so they don't have 
# to scroll up to read previous messages.
import time

# I am using a dictionary to store the card values for the 
# the program to pull from instead of hard programming each 
# card. The way I got around the issue of the Ace card having 
# dual value in the game (1 and 11) I assigned to diffrent 
# values depending on if the user entered a A or a.
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

# Welcome message.
print(" Welcome to the Blackjack Table")
time.sleep(2)
# showing the user the value of each card.
print(" a - 1,\n 2 - 2,\n 3 - 3,\n 4 - 4,\n 5 - 5,\n 6 - 6,\n 7 - 7,\n 8 - 8,\n 9 - 9,\n 10- 10,\n J - 10,\n Q - 10,\n K - 10,\n A - 11\n")
time.sleep(2)

# This is where the user inputs their first card dealt.
first_card = input("what is your first card? ")

# This is where the user inputs the second card they was dealt, 
# and also where the user can decide weither or not they want to 
# use their ace as a 1 or 11
second_card = input("what is your next card? ")

# This is where the program adds the first two cards.
hand_total = card_value[first_card] + card_value[second_card]

# This is the part of the program that advises the user on if t
# hey should hit or stay, or informs them if they went Bust 
# or made Blackjack (21). If the user stays, bust or gets a blackjack the program gives an exit message
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

    # This section is where the program gives the user the option to "Hit" or "Stay". 
    # If the user hits the program asked what is the next card then loops back to the top of the while loop
    user_answer = input("Would you like to Hit or Stay? ")
    if user_answer == 'Hit':
        next_card = input("What is your next card? ")
        hand_total += card_value[next_card]
    # If the user chooses to say the program runs the exit message. and ends
    elif user_answer == 'Stay':
        print("Thanks for Playing")
        break