# Version 2     Have the user enter a dollar amount (1.36), convert this to the total in pennies.

# User enters a dollar amount

amount = float(input("Enter a dollar amount: "))

# Multiplies amount by 100

i_amount = int(float(amount)*100)

# Conversion to individual coins

q_amount = i_amount//25
i_amount -= q_amount*25

d_amount = i_amount//10
i_amount -= d_amount*10

n_amount = i_amount//5
i_amount -= n_amount*5

p_amount = i_amount//1   

# Total amount in different coins

print(q_amount, 'quarters')
print(d_amount, 'dimes')
print(n_amount, 'nickels')
print(p_amount, 'pennies')
