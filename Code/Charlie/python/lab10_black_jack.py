


print('---------------------')
print('Welcome to BlackJack')
print('---------------------')



cards = {
    'A': [1, 11],
    '2': [2, 2],
    '3': [3, 3],
    '4': [4, 4],
    '5': [5, 5],
    '6': [6, 6],
    '7': [7, 7],
    '8': [8, 8],
    '9': [9, 9],
    '10': [10, 10],
    'J': [10, 10],
    'Q': [10, 10],
    'K': [10, 10]
    }

# key is 'A' valuve is [whatever is in here ]

card_1 = input('Whats your first card? ')

card_2 = input('Whats your second card? ')

card_3 = input('Whats your third card? ')


sum_1 = (cards[card_1][0] + cards[card_2][0] + cards[card_3][0])

sum_2 = (cards[card_1][1] + cards[card_2][1] + cards[card_3][1])

if sum_1 < 17:
    print(f'{sum_1} Hit ')
elif sum_1 >= 17 and sum_1 < 21:
    print(f'{sum_1} Stay ')
elif sum_1 == 21:
    print(f'{sum_1} BLACKJACK ')
else:
    print(f'{sum_1} YOU BUSTED ')

if sum_2 < 17:
    print(f'{sum_2} Hit ')
elif sum_2 >= 17 and sum_2 < 21:
    print(f'{sum_2} Stay ')
elif sum_2 == 21:
    print(f'{sum_2} BLACKJACK ')
else:
    print(f'{sum_2} YOU BUSTED ')
