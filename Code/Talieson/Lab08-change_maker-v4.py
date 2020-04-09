# Version 4 is adding the functionality of choosing which currency to use

run = True
currency_check = True

while run:
    while run and currency_check:
        # Take the amount from the user
        currency = input('''Available currency types are: Dollars, Pesos, Euros
                            Please select the currency you want to use. ''')
        if currency == "Dollars":
            currency_check = False
            coins = [
                ("quarters", 25, 0),
                ("dimes", 10, 0),
                ("nickels", 5, 0),
                ("pennys", 1, 0)
            ]

        elif currency == "Pesos":
            currency_check = False
            coins = [
                ("", 1000, 0),
                ("", 500, 0),
                ("", 200, 0),
                ("", 100, 0),
                ("", 50, 0),
                ("", 20, 0),
                ("", 10, 0)
            ]

        elif currency == "Euros":
            currency_check = False
            coins = [
                ("", 200, 0),
                ("", 100, 0),
                ("", 50, 0),
                ("", 20, 0),
                ("", 10, 0),
                ("", 5, 0),
                ("", 2, 0),
                ("", 1, 0)
            ]
        else:
            print("please enter a valid currency type. ")

    currency_amount = float(input(f"Enter the {currency} amount: $"))
    # Turn the amount into cents
    currency_amount = (currency_amount * 100)

    # Split the currency current list into indivdual ists by tuple place.
    coin_names = [coin[0] for coin in coins]
    coin_values = [coin[1] for coin in coins]
    coin_quantity = [coin[2] for coin in coins]

    # divide the change amount by each coin, and return the quanity as an int.
    coin_quantity[0] = currency_amount // coin_values[0]
    currency_amount = currency_amount - coin_quantity[0] * coin_values[0]
    coin_quantity[0] = int(coin_quantity[0])
    coin_quantity[1] = currency_amount // coin_values[1]
    currency_amount = currency_amount - coin_quantity[1] * coin_values[1]
    coin_quantity[1] = int(coin_quantity[1])
    coin_quantity[2] = currency_amount // coin_values[2]
    currency_amount = currency_amount - coin_quantity[2] * coin_values[2]
    coin_quantity[2] = int(coin_quantity[2])
    coin_quantity[3] = currency_amount
    coin_quantity[3] = int(coin_quantity[3])

    # Then we'll finally print how many of each coin we've got.
    print(f''' Your change is:
            {coin_quantity[0]} {coin_names[0]},
            {coin_quantity[1]} {coin_names[1]},
            {coin_quantity[2]} {coin_names[2]},
            and {coin_quantity[3]} {coin_names[3]}.''')

    run = False

    # Quick check to see if there is more conversion to be done.
    while not run:
        go_again = input("Do you have more conversion to do? (Y/N) ")
        if go_again == "Y":
            run = True
            break
        if go_again == "N":
            exit()
        else:
            print("That is not a valid response.")
