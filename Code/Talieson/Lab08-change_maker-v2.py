run = True

while run:
    change_amount = float(input("Enter the dollar amount: $"))
    change_amount = (change_amount * 100)
    print(change_amount)

    quarters = change_amount // 10
    change_amount -= quarters * 25
    dimes = change_amount // 10
    change_amount -= dimes * 10
    nickles = change_amount // 5
    change_amount -= nickles * 5
    pennies = change_amount

    print(f''' Your change is:
            {quarters} quarters,
            {dimes} dimes,
            {nickles} nickles,
            and {pennies} pennies.''')

    run = False
