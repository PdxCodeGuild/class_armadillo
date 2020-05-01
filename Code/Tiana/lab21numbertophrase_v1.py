#Lab 21: Number to Phrase Version 1

  
# Convert a given number into its English representation. 
# Cover cases 0-9 first, then 10-19, then 20-99

#Ask the user for a number
num = int(input("Enter a number to convert: "))


#use a if statement if num is in dictionary
#Use modulus to extract the ones and tens digit.  
tens_digit = num//10
ones_digit = num%10


#Number conversion dictionary
numbers = {
    0:'zero', 
    1:'one', 
    2:'two', 
    3:'three', 
    4:'four', 
    5:'five', 
    6:'six',
    7:'seven',
    8:'eight', 
    9:'nine',
    10:'ten',
    11: 'eleven', 
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

#Check if num is > or < 10 to determine wich value you need
if num < 10 and ones_digit in numbers:
    print(f"The word version is: {numbers[ones_digit]}")

if num > 10 and tens_digit in numbers:
    print(f"The word version is: {numbers[tens_digit]}")


