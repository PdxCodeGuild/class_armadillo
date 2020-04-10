dollar_amount = input('Enter a dollar amount to convert into coin denominations: $ ')#get in put from user
amount = int(float(dollar_amount)*100)

quarters = amount // 25  #floor divides into quarters first then proceeds through rest of coins
amount -= quarters*25  #subtracts the amount of quarters from total amount
print('quarters: ' + str(quarters)) #prints string quarters: and amount

dimes = amount // 10
amount -= dimes*10
print('dimes: ' + str(dimes))

nickels = amount // 5
amount -= nickels*5
print('nickels: ' + str(nickels))

pennies = amount // 1
amount -= pennies*1
print('pennies: ' + str(pennies))