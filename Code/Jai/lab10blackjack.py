card_values = {'A':1, 
    '2':2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

first_card  = input("What is your first card? ")
second_card = input("What is your second card? ")
hand_total = card_values[first_card] + card_values[second_card]


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


user_answer = input("Would you like to hit or stay? ")

if user_answer == 'hit':
        next_card  = input("What is your next card? ")
        hand_total += card_values[next_card] 

elif user_answer == 'stay':
    print('thanks for playing')