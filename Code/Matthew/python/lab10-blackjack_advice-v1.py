


def get_card(message):
  card = input(message)
  card = card.upper()
  if card in ['A', 'ACE']:
    return 'A'
  elif card in ['J', 'JACK']:
    return 'J'
  return card


def card_value(card):
  if card == 'A':
    return 1
  elif card in ['10', 'J', 'Q', 'K']:
    return 10
  return int(card)

print(card_value('J'))

card_values = {
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
  'J': 10,
  'Q': 10,
  'K': 10
}
print(card_values['J']) # 10


card1 = get_card('what is your first card? ')
card2 = get_card('what is your second card? ')
card3 = get_card('what is your third card? ')

total = card_values[card1] + card_values[card2] + card_values[card3]

if total < 17:
  print(total, 'hit')
elif total < 21:
  print(total, 'stay')
elif total == 21:
  print(total, 'blackjack')
else:
  print(total, 'bust')
