# Version 4 is adding the functionality of choosing which currency to use

run = True
currency_check = True
symbol = ""

while run:
    while run and currency_check:
        # Take the type of currency from the user
        currency = input('''
Please select the currency you want to use
Available currencies: Dollars, Pesos, Euros, and Yen. ''')

        # decide which currency library we're using based on input
        if currency == "Dollars":
            currency_check = False
            symbol = "$"
            coins = [
                ("quarters", 25, 0),
                ("dimes", 10, 0),
                ("nickels", 5, 0),
                ("pennys", 1, 0)
            ]
        elif currency == "Pesos":
            currency_check = False
            symbol = "Mex$"
            coins = [
                ("10 peso coin", 1000, 0),
                ("5 peso coin", 500, 0),
                ("2 peso coin", 200, 0),
                ("1 peso coin", 100, 0),
                ("50 centavos coin", 50, 0),
                ("20 centavos coin", 20, 0),
                ("10 centavos coin", 10, 0)
            ]
        elif currency == "Euros":
            currency_check = False
            symbol = u"€"
            coins = [
                ("2 Euro coin", 200, 0),
                ("1 Euro coin", 100, 0),
                ("50 cent coin", 50, 0),
                ("20 cent coin", 20, 0),
                ("10 cent coin", 10, 0),
                ("5 cent coin", 5, 0),
                ("2 cent coin", 2, 0),
                ("1 cent coin", 1, 0)
            ]
        elif currency == "Yen":
            currency_check = False
            symbol = "¥"
            coins = [
                ("500 Yen coin", 50000, 0),
                ("100 Yen coin", 10000, 0),
                ("50 Yen coin", 5000, 0),
                ("10 Yen coin", 1000, 0),
                ("5 Yen coin", 500, 0),
                ("1 Yen coin", 100, 0)
            ]
        else:
            print("please enter a valid currency type. ")

    # Take the amount of the currency now that we know the type
    currency_amount = float(input(f"Enter the {currency} amount: {symbol}"))

    # store the input amount so we don't make changes for final output
    input_amount = currency_amount

    # Turn the amount into cents
    currency_amount = (currency_amount * 100)

    # Split the currency current list into indivdual ists by tuple place.
    coin_names = [coin[0] for coin in coins]
    coin_values = [coin[1] for coin in coins]
    coin_quantity = [coin[2] for coin in coins]

    # divide the change amount by each coin, and return the quanity as an int.
    for i in range(len(coins)):
        coin_quantity[i] = currency_amount // coin_values[i]
        currency_amount = currency_amount - coin_quantity[i] * coin_values[i]
        coin_quantity[i] = int(coin_quantity[i])

    # Then we'll finally print how many of each coin we've got.
    print(f'{symbol}{input_amount} is ...')
    for i in range(len(coins)):
        print('\t' + coin_names[i] + ': ' + str(coin_quantity[i]))

    run = False

    # Quick check to see if there is more conversion to be done.
    while not run:
        go_again = input("Do you have more conversion to do? (Y/N) ")
        if go_again == "Y":
            run = True
            currency_check = True
            break
        if go_again == "N":
            exit()
        else:
            print("That is not a valid response.")
