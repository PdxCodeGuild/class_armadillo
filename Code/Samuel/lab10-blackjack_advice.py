# PDX Code Guild Fullstack Course
# Lab 10 Blackjack Advice
# Samuel Purdy
# 4/13/2020

import string

# Counts the number of aces in a hand
number_of_aces = -1

# Ace possibilties. Doesn't count double 11s because those go over immediatly
aces_possible = {
    0: [1,11],
    1: [2,12],
    2: [3,13]
}

# Returns a list containing the score number and the number of aces used based on the card given.
# Returns 10 for Jacks, Queens, and Kings, but 0 for the number of aces.
# Returns 0 for Aces, but 1 for the number of aces.
# Returns the integer value of the card, but 0 for the number of aces.
def set_number_score(card):
    aces = 0
    if card.upper() == "J" or card.upper() == "Q" or card.upper() == "K":
        return [10, aces]
    elif card.upper() == "A":
        aces += 1
        return [0, aces]
    else:
        return [int(card), aces]

# Prints the advice based on the score given.
def get_advice(score):
    if score < 17:
        return "Hit"
    elif score >= 17 and score < 21:
        return "Stay"
    elif score == 21:
        return "Blackjack!"
    else:
        return "Busted :C"

# Gets the inputs from the user.
card1 = input("What is your first card? ")
card2 = input("What is your second card? ")
card3 = input("What is your third card? ")

# Adds the score together based on the the first index of the list returned
score = set_number_score(card1)[0] + set_number_score(card2)[0] + set_number_score(card3)[0]

# Sets the number of aces based on the second index of the list returned
number_of_aces += set_number_score(card1)[1] + set_number_score(card2)[1] + set_number_score(card3)[1]

# Gives advice if there are no aces in the hand
if number_of_aces == -1:
    
    print(f"{score} {get_advice(score)}")
elif number_of_aces > -1:
    print(f"{(score + aces_possible[number_of_aces][0])} {get_advice(score + aces_possible[number_of_aces][0])}")
    print(f"You also have another option since you have {number_of_aces + 1} number of aces in your hand")
    print(f"{(score + aces_possible[number_of_aces][1])} {get_advice(score + aces_possible[number_of_aces][1])}")
