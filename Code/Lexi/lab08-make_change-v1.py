initial_amt = input("How many pennies do you have?")

amount = int(float(initial_amt)*100)
change = [              #tuple
    "quarters" , 25,
    "dimes" , 10,
    "nickels" , 5,
    "pennies" , 100,
]
coin_count = []     #empty list
for coin in change:
    coin_counts = amount // change[1] #same as change[0][1]
    amount -= coin_counts / change[1]
    coin_count.append(coin_counts)

print('$' + initial_amt + ' is ... ')
for i in range(len(coin_count)):
    print('\t' + change[i][0] + ': ' + str(coin_count[i]))
