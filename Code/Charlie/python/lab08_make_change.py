
# Lab 8: Make Change



num = float(input("Enter dollar amount to convert: "))


 

coins = {
    'quarter': .25,
    'dime': .10,
    'nickel': .05,
    'penny': .01,
}

list = list(coins.keys())


c_unit = input(f"Enter the unit to convert from {list}: ")

num = num // coins[c_unit]



print(num)

