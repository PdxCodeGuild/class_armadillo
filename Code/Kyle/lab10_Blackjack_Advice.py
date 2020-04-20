
import random
card1 = ""
card2 = ""
card3 = ""
card4 = ""
first_hand = ""
second_hand = ""
third_hand = ""
blackjack_dict = {}
card_deck = ""


# blackjack_dict = { 
#   "A" : 11,
#   "2" : 2,
#   "3" : 3,
#   "4" : 4,
#   "5" : 5,
#   "6" : 6,
#   "7" : 7,
#   "8" : 8,
#   "9" : 9,
#   "10" : 10,
#   "J" : 10,
#   "Q" : 10,
#   "K" : 10
# }

# def another_card():
#     return random.choice(card_deck)

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
  'K': 10
}

def another_card():
    return random.choice(card_deck)

card_deck = list(blackjack_dict.keys())
card1 = random.choice(card_deck)
card2 = random.choice(card_deck)

print(f'Your first card is: {card1}.')
print(f'Your second card is: {card2}.')

first_hand = blackjack_dict[card1] + blackjack_dict[card2]

if first_hand == 21:
    print(f"{first_hand}! Blackjack! You won. ")
elif first_hand < 17:
    print(f"{first_hand}. I suggest you Hit. ")
elif first_hand >= 17 and first_hand < 21:
    print(f"{first_hand}. I suggest you Stay. ")

second_round = input("Do you 'hit' or 'stay?' ").lower().split()
# while not second_round.isalpha():
#     print("I don't understand that answer. Please enter only 'Hit' or 'Stay' ")
#     second_round = input("Do you 'hit' or 'stay?' ").lower().split()

if second_round == "hit" or second_round == "h":
    card3 = another_card()
    #card3 = random.choice(card_deck)
    print(f'Your third card is: {card3}')
elif second_round == "stay" or second_round == "s":
    card3 = 0

## getting a keyerror of: '' when this line is run, but unsure of why.
# entering 'hit' or 'stay', and the input line is coded with .split() 
# to remove any spaces.
second_hand = first_hand + blackjack_dict[card3]

if second_hand == 21:
    print(f"{second_hand}! Blackjack! You won. ")
elif second_hand < 17:
    print(f"{second_hand}. I suggest you Hit. ")
elif second_hand >= 17 and second_hand < 21:
    print(f"{second_hand}. I *strongly* suggest you Stay. ")
elif second_hand > 21:
    print(f"{second_hand}...You should have stayed. Bust, you lose. ")