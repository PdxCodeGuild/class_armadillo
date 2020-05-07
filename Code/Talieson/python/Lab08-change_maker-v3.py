# Version 3 of change_maker adds the currency to a list of tuples
# this version is built to allow for future expansion to addition currency

run = True

while run:
    # Take the amount from the user
    change_amount = float(input("Enter the dollar amount:  $"))
    # Turn the amount into cents
    change_amount = (change_amount * 100)

    # Establish coin name, value, and current quantity.
    coins = [
                ("quarters", 25, 0),
                ("dimes", 10, 0),
                ("nickels", 5, 0),
                ("pennys", 1, 0)
            ]

    # Split the currency current list into indivdual ists by tuple place.
    coin_names = [coin[0] for coin in coins]
    coin_values = [coin[1] for coin in coins]
    coin_quantity = [coin[2] for coin in coins]

    # divide the change amount by each coin, and return the quanity as an int.
    coin_quantity[0] = change_amount // coin_values[0]
    change_amount = change_amount - coin_quantity[0] * coin_values[0]
    coin_quantity[0] = int(coin_quantity[0])
    coin_quantity[1] = change_amount // coin_values[1]
    change_amount = change_amount - coin_quantity[1] * coin_values[1]
    coin_quantity[1] = int(coin_quantity[1])
    coin_quantity[2] = change_amount // coin_values[2]
    change_amount = change_amount - coin_quantity[2] * coin_values[2]
    coin_quantity[2] = int(coin_quantity[2])
    coin_quantity[3] = change_amount
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
