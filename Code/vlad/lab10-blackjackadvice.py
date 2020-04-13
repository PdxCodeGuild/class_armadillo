#Lab 10: Blackjack Advice


# Building deck using STRINGS as keys, so we can us user_input as the key to access the card values. deck[user_input]
deck = {
    # key: value
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
    'Q': 10,
    'K': 10,
}
hand = [] # Initializing empty deck to add to
for i in range(3): # making a for loop to just loop the content within by setting the range to 3
    user_input = input('What card do you want?: ') # Asking the user for a card and looping
    hand.append(deck[user_input]) # getting the card value, then appending that card to the empty list
for card in hand: # looping the contents of the hand variable
    if 1 in hand and sum(hand) < 11: # checking if there is an Ace in the hand, AND THEN checking if the sum is greater than 11, IF SO execute code below
        hand.append(10) # adding 10 value to hand if code above is True. Adding 10 makes the Ace 11
hand_total = sum(hand) # Getting the total of the hand to do comparisons below.
# I think this is straight foward here.
#HIT
if hand_total < 17: 
    print(f'HIT! {hand}')
#STAY
elif hand_total <= 20:
    print(f'STAY! {hand}')
#BLACKJACK
elif hand_total == 21:
    print('BLACKJACK!')
#BUST
else:
    print(f'BUST! {hand}')



