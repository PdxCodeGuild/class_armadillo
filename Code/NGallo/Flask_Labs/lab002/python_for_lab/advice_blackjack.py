deck = {
        # key: value
        'ace':1,
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
        'A': 11,
    }
def blackjack(card1,card2,card3):
    # Building deck using STRINGS as keys, so we can us user_input as the key to access the card values. deck[user_input]
    
    hand = [card1, card2, card3] # Initializing empty deck to list from website

    hand_total = 0
    for card in hand: # looping the contents of the hand variable
        hand_total += deck[card]

    print(hand_total)
        if 1 in hand and sum(hand) < 11: # checking if there is an Ace in the hand, AND THEN checking if the sum is greater than 11, IF SO execute code below
            hand.append(10) # adding 10 value to hand if code above is True. Adding 10 makes the Ace 11
    hand_total = sum(hand) # Getting the total of the hand to do comparisons below.
    # I think this is straight foward here.
    #HIT
    if hand_total < 17: 
        return(f'HIT! {hand}')
    #STAY
    elif hand_total <= 20:
        return(f'STAY! {hand}')
    #BLACKJACK
    elif hand_total == 21:
        return('BLACKJACK!')
    #BUST
    else:
        return(f'BUST! {hand}')