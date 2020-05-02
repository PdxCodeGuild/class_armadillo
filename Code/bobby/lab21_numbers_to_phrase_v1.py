import math

number = int(input("Enter number to print: "))

numph = ["zero","one","two","three","four","five","six","seven","eight","nine"]
numph_teen = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
numph_tens =["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


if number <= 9:
    print(numph[number].capitalize())
elif number >= 10 and number <= 19:
    tens = number % 10
    print(numph_teen[tens].capitalize())
elif number > 19 and number <= 99:
    ones = number // 10
    twos = ones - 2
    tens = number % 10
    if tens == 0:
        print(numph_tens[twos].capitalize())
    elif tens != 0:
        print(numph_tens[twos].capitalize() + " " + numph[tens])