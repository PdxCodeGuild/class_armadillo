# Version 2     Have the user enter a dollar amount (1.36), convert this to the total in pennies.

# User enters a dollar amount

i_amount = float(input("Enter a dollar amount: "))

# Multiplies amount by 100

amount = int(float(i_amount)*100)

# Gives total in pennies

print(amount,'pennies in total')