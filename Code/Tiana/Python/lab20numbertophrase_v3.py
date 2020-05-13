#Lab 20 Number to Phrase Version 3
#4/30/2020

#Convert a number to roman numerals.

#Ask the user for a number
num = int(input("Enter a number to convert: "))


#use a if statement if num is in dictionary
#Use modulus to extract the ones and tens digit.
tens_digit = num//10
ones_digit = num%10


#Roman numeral conversion dictionary
numbers = {
    0:'', 
    1:'I', 
    2:'II', 
    3:'III', 
    4:'IV', 
    5:'V', 
    6:'VI',
    7:'VII',
    8:'VIII', 
    9:'IX',
    10:'X',
    11: 'XI', 
    12: 'XII',
    13: 'XIII',
    14: 'XIV',
    15: 'XV',
    16: 'XVI',
    17: 'XVII',
    18: 'XVIII',
    19: 'XIX',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM'
}

#Check if num is > or < 10 to determine wich value you need
if num < 10 and ones_digit in numbers:
    print(f"The roman numeral is: {numbers[ones_digit]}")

if num > 9 and tens_digit in numbers:
    print(f"The roman numeral is: {numbers[tens_digit]}")

