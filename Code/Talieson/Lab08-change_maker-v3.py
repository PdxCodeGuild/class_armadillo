run = True

while run:
    change_amount = float(input("Enter the dollar amount ($__.__?) "))
    change_amount = (change_amount * 100)

    coins = [
                ("quarters", 25, 0),
                ("dimes", 10, 0),
                ("nickels", 5, 0),
                ("pennys", 1, 0)
            ]

    coin_names = [coin[0] for coin in coins]
    print(coin_names)

    coin_values = [coin[1] for coin in coins]
    print(coin_values)

    coin_quantity = [coin[2] for coin in coins]
    print(coin_quantity)

    coin_quantity[0] = change_amount // coin_values[0]
    change_amount = change_amount - coin_quantity[0] * coin_values[0]
    coin_quantity[1] = change_amount // coin_values[1]
    change_amount = change_amount - coin_quantity[1] * coin_values[1]
    coin_quantity[2] = change_amount // coin_values[2]
    change_amount = change_amount - coin_quantity[2] * coin_values[2]
    coin_quantity[3] = change_amount

    print(f''' Your change is:
            {coin_quantity[0]} {coin_names[0]},
            {coin_quantity[1]} {coin_names[1]},
            {coin_quantity[2]} {coin_names[2]},
            and {coin_quantity[3]} {coin_names[3]}.''')

    run = False
