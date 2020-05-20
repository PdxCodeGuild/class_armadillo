# Let's write a python program to give basic blackjack playing advice 
# during a game by asking the player for cards. 
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. 
# Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. 
# Use the following rules to determine the advice:


deck = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'K': 10,
    'Q': 10,
    'J': 10,
}



hand = []

for i in range(3):
    user_input = input('What is your card?')
    hand.append(deck[user_input])


hand_total = sum(hand)

if hand_total < 11:
    deck['A'] = 11
if hand_total < 17:
    print('Hit')
elif hand_total <= 20:
    print('Stay')
elif hand_total == 21:
    print('Blackjack!')
else:
    print('Bust')
