


coins = {
    'quarter': .25,
    'dime': .10,
    'nickel': .05,
    'penny': .01,
}

num = input("Enter dollar amount to convert: ")
while not num.isdigit():
    num = input("You must enter a dollar amount!: ")
else:
    num = int(num)

list = list(coins.keys())

c_unit = input(f"Enter the unit to convert from {list}: ")

num = num // coins[c_unit]



print(num)

