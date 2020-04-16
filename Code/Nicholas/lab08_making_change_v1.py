#this lab breaks down an amt of pennies into various coin denominations,
#it will count through the large denomination of coins before cycling to the next denomination

dollar_amount = int(input("Enter an amount of pennies to convert into coin denominations: "))
#will only accept penny quantity as int, not float
quarters = dollar_amount // 25  #floor divide amount
dollar_amount -= quarters*25  #subtracts amount from total
print('quarters: ' + str(quarters))  #prints numbers of coins

dimes = dollar_amount // 10
dollar_amount -= dimes*10
print('dimes: ' + str(quarters))

nickels = dollar_amount // 5
dollar_amount -= nickels*5
print('nickels: ' + str(nickels))

pennies = dollar_amount // 1
dollar_amount -= pennies*1
print('pennies: ' + str(pennies))
