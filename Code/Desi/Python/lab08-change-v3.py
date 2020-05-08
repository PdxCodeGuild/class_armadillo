# Lab 08


# input will be the total amount
change = input("What is the amount you want in change? : ")
amount = int(float(change)*100)

# Always break the total into the highest coin value first, resulting in the fewest amount of coins
coins = [("quarters", 25),  
        ("dimes", 10),      
        ("nickels", 5),      
        ("pennies", 1),      
]

# output will be the number of quarters, dimes, nickles, and pennies
coin_counts = [] # 4, 0 , 1, 0

for coin in coins:
    coin_count = amount // coin[1] #flight deck
    amount = amount - ( coin_count * coin[1] )
    #amount -= coin_count * coin[0]
    coin_counts.append(coin_count)

print('This is what you got (below) ')
for c in range(len(coin_counts)): 
    # coins from dictionary and first element in coins plus quarters (0), put it back into a string.
    print( coins[c][0] + ': ' + str(coin_counts[c]))

# 
#

