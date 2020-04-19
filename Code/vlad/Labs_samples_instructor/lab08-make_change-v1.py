#lab08-make_change-v1 sample by instructor: 

input_amount = input('What is the amount you\'d like to break into change? $')

# amount = float(input_amount)
# quarters = amount // .25
# amount -= quarters * .25
# print(quarters)

amount = int(float(input_amount)*100)

quarters = amount // 25
amount -= quarters * 25
dimes = amount // 10
amount -= dimes * 10
nickles = amount // 5
amount -= nickles * 5
pennies = amount

print(f'${input_amount} is {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies')