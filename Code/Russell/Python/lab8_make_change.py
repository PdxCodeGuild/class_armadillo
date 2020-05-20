amount = input("Enter dollar amount to convert to change.")
amount = int(float(amount)*100)

quarters = amount // 25
amount -= quarters * 25

dimes = amount // 10
amount -= dimes * 10

nickels = amount // 5
amount -= nickels * 5

pennies = amount // 1
amount -= pennies * 1

print(f'Quarters: {quarters}')
print(f'Dimes: {dimes}')
print(f'Nickels: {nickels}')
print(f'Pennies: {pennies}')

