
def card_value(card):
    if card == 'A':
        return [1, 11]
    elif card == 'J' or card == 'Q' or card == 'K':
        return [10]
    return [int(card)]

# card_values = {'A': 1, '2': 2}

def add_card_values(card1, card2):
    output = []
    for value1 in card1:
        for value2 in card2:
            output.append(value1 + value2)
    return output

def main():
    card1 = input('what is your first card? ')
    card2 = input('what is your second card? ')
    card3 = input('what is your third card? ')

    total = add_card_values(card_value(card1), card_value(card2))
    total = add_card_values(total, card_value(card3))

    total.sort(reverse=True)
    # total.reverse()
    total = [value for value in total if value <= 21]

    total = total[0]
    print(total, end=' ')
    if total < 17:
        print('hit!')
    elif total < 21:
        print('stay!')
    elif total == 21:
        print('blackjack!')
    else:
        print('busted!')

main()