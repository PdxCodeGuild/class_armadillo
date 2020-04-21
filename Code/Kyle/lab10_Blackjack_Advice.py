
import random
card1 = ""
card2 = ""
card3 = ""
card4 = ""
card4 = ""
user_hand = ""
computer_hand = ""
blackjack_dict = {}
card_deck = ""

# Dictionary of blackjack keys/values. 
# Only set to one Ace value at this time.
blackjack_dict = {
  'A': 11,
  '2': 2,
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

# function to allow the user to play against a computer
def computer_game():
    computer_hand = ""
    card_deck = list(blackjack_dict.keys())
    ccard1 = random.choice(card_deck)
    ccard2 = random.choice(card_deck)
    computer_hand = blackjack_dict[ccard1] + blackjack_dict[ccard2]
    if computer_hand == 21:
        #computer_hand = 21
        print(f"The Computer's hand is : {computer_hand}.")
        return computer_hand  
    elif computer_hand < 17:
        ccard3 = random.choice(card_deck)
        computer_hand = computer_hand + blackjack_dict[ccard3]
        if computer_hand < 17:
            ccard4 = random.choice(card_deck)
            computer_hand = computer_hand + blackjack_dict[ccard4]
            print(f"The Computer's hand is : {computer_hand}.")
            return computer_hand
        else:
            print(f"The Computer's hand is : {computer_hand}.")
            return computer_hand
    elif computer_hand >= 17 and computer_hand < 21:
        print(f"The Computer's hand is : {computer_hand}.")
        return computer_hand

#function to generate another random card. 
def another_card():
    return random.choice(card_deck)

# def play_blackjack():    
while True:
    card_deck = list(blackjack_dict.keys())
    card1 = random.choice(card_deck)
    card2 = random.choice(card_deck)

    print(f'Your first card is: {card1}.')
    print(f'Your second card is: {card2}.')

    # user's first hand created by adding the key values of card 1 and card 2
    user_hand = blackjack_dict[card1] + blackjack_dict[card2]

    if user_hand == 21:
        print(f"{user_hand}! Blackjack! You won. ")
        break
    elif user_hand < 17:
        print(f"{user_hand}. I suggest you Hit. ")
    elif user_hand >= 17 and user_hand < 21:
        print(f"{user_hand}. I suggest you Stay. ")

    # Validate the options of hit or stay
    second_round = input("Do you 'hit' or 'stay?' ").lower()
    while not second_round.isalpha():
        print("I don't understand that answer. Please enter only 'Hit' or 'Stay' ")
        second_round = input("Do you 'hit' or 'stay?' ").lower()

    # given user input, a 3rd card is generated (or set to a 0 value)
    if second_round == "hit" or second_round == "h":
        card3 = another_card()
        print(f'Your third card is: {card3}')
    elif second_round == "stay" or second_round == "s":
        break

    #add the 3rd card to your first hand
    user_hand = user_hand + blackjack_dict[card3] 

    # evaluates user's hand value to determine advice given
    if user_hand == 21:
        print(f"{user_hand}! Blackjack! You won. ")
        break
    elif user_hand < 17:
        print(f"{user_hand}. I suggest you Hit. ")
    elif user_hand >= 17 and user_hand < 21:
        print(f"{user_hand}. I *strongly* suggest you Stay. ")
    elif user_hand > 21:
        print(f"{user_hand}...You should have stayed. Bust, you lose. ")
        break


    third_round = input("Do you 'hit' or do you 'stay?' ").lower()

    # Validate the options of hit or stay
    while not third_round.isalpha():
        print("I don't understand that answer. Please enter only 'Hit' or 'Stay' ")
        third_round = input("Do you 'hit' or 'stay?' ").lower()

    # given user input, a 4th card is generated (or set to a 0 value)
    if third_round == "hit" or third_round == "h":
        card4 = another_card()
        print(f'Your third card is: {card4}')
    elif third_round == "stay" or third_round == "s":
        break

    # add the 4th card to your second hand
    user_hand = user_hand + blackjack_dict[card4]

    # evaluates user's hand value to determine advice given
    if user_hand == 21:
        print(f"{user_hand}! Blackjack! You won. ")
        break
    elif user_hand < 17:
        print(f"{user_hand}. I suggest you Hit. ")
    elif user_hand >= 17 and user_hand < 21:
        print(f"{user_hand}. It is highly improbable that you will not bust if you request another card. Please, Stay. ")
    elif user_hand > 21:
        print(f"{user_hand}...I tried you warn you, but you pressed your luck too far. Bust, you lose. ")
        break


    fourth_round = input("Do you 'hit' or do you 'stay?' ").lower()

    # Validate the options of hit or stay
    while not fourth_round.isalpha():
        print("I don't understand that answer. Please enter only 'Hit' or 'Stay' ")
        fourth_round = input("Do you 'hit' or 'stay?' ").lower()

    # given user input, a 5th card is generated (or set to a 0 value)
    if fourth_round == "hit" or fourth_round == "h":
        card5 = another_card()
        print(f'Your third card is: {card5}')
    elif fourth_round == "stay" or fourth_round == "s":
        break

    # add the 5th card to your second hand
    user_hand = user_hand + blackjack_dict[card5]

    # evaluates user's hand value to determine advice given
    if user_hand == 21:
        print(f"{user_hand}! Blackjack! You won. ")
    elif user_hand < 17:
        print(f"{user_hand}. I suggest you Hit. ")
    elif user_hand >= 15 and user_hand < 21:
        print(f"{user_hand}. It is highly improbable that you will not bust if you request another card. Please, Stay. ")
    elif user_hand > 21:
        print(f"{user_hand}...I tried you warn you, but you pressed your luck too far. Bust, you lose. ")
#break

computer_game()
print(f"You're holding {user_hand}. Your machine adversary has {computer_hand}.")