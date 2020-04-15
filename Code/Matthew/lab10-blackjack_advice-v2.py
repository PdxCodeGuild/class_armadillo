
import random


card_values = {
  'a': 1,
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


card_names = list(card_values.keys())
card1 = random.choice(card_names)
card2 = random.choice(card_names)

print(f'Your first card is {card1} with value {card_values[card1]}')
print(f'Your second card is {card2} with value {card_values[card2]}')

total = card_values[card1] + card_values[card2]
if total < 17:
  print(total, 'hit')
  card3 = random.choice(card_names)
  print(f'Your third card is {card3} with value {card_values[card3]}')
  total = card_values[card1] + card_values[card2] + card_values[card3]
  print(total)
elif total < 21:
  print(total, 'stay')
elif total == 21:
  print(total, 'blackjack')










