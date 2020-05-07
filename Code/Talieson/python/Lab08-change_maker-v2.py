

# This lab takes a dollar value and returns the number of coins
# that make up that value, defaulting to the highest coin possible.
run = True

while run:
    # Take users input as a float.
    change_amount = float(input("Enter the dollar amount: $"))
    # Convert it to an amount in pennies.
    change_amount = (change_amount * 100)
    # Take the amount and divide by coin value, setting change_amount to
    # the new total, while defining the amount of that coin type.
    quarters = change_amount // 25
    change_amount -= quarters * 25
    dimes = change_amount // 10
    change_amount -= dimes * 10
    nickles = change_amount // 5
    change_amount -= nickles * 5
    pennies = change_amount

    # Return the amount of each coin type.
    print(f''' Your change is:
            {quarters} quarters,
            {dimes} dimes,
            {nickles} nickles,
            and {pennies} pennies.''')
