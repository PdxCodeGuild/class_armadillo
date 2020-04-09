
# print(round(3.1415963, 2))

input_amount = input('What is the amount you\'d like to break into change? $')

amount = int(float(input_amount)*100)

# bool('True')
# int()
# float()
# str()
# list()
# tuple()
# dict()

coins = [
    ('quarters', 25),
    ('dimes', 10),
    ('nickels', 5),
    ('pennies', 1)
]
coin_counts = []
for coin in coins:
    coin_count = amount // coin[1]
    amount -= coin_count * coin[1]
    coin_counts.append(coin_count)

print('$' + input_amount + ' is ...')
for i in range(len(coin_counts)):
    print('\t' + coins[i][0] + ': ' + str(coin_counts[i]))
