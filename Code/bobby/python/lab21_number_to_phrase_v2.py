import math

number = int(input("Enter number to print: "))

numph = ["zero","one","two","three","four","five","six","seven","eight","nine"]
numph_teen = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
numph_tens =["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
numph_hunds = ["hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]

if number <= 9:
    print(numph[number].capitalize())
elif number >= 10 and number <= 19:
    tens = number % 10
    print(numph_teen[tens].capitalize())
elif number >=100 and number <=999:
    hundreds = number %100
    print(numph_hunds[hundreds].capitalize())

elif number > 19 and number <= 999:
    ones = number // 10
    twos = ones - 2
    tens = number % 10
    threes = ones - 3
    hundreds = number //100

    if tens == 0:
        print(numph_tens[twos].capitalize())
    elif tens != 0:
        print(numph_tens[twos].capitalize() + " " + numph[tens])
    elif 