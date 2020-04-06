
def card_value(card):
    if card == 'A':
        return 1
    elif card == 'J' or card == 'Q' or card == 'K':
        return 10
    return int(card)


def main():
    card1 = input('what is your first card? ').upper()
    card2 = input('what is your second card? ').upper()
    card3 = input('what is your third card? ').upper()

    total = card_value(card1) + card_value(card2) + card_value(card3)

    if card1 == 'A' and total <= 11:
        total += 10
    if card2 == 'A' and total <= 11:
        total += 10
    if card3 == 'A' and total <= 11:
        total += 10

    if total < 17:
        print('hit!')
    elif total < 21:
        print('stay!')
    elif total == 21:
        print('blackjack!')
    else:
        print('busted!')

main()