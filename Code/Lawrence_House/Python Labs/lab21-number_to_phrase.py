# Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Get Seed number input from user

x = int(input('Enter a Number from 0-999: '))

# Determine number at each place

# x = 67
hundreds_digit = x//100
tens_digit = x//10
ones_digit = x%10

# print(tens_digit)
# print(ones_digit)

# print(seed_number)

# Dictionaries containing English phrase

ones = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

tens = {
    0: '',
    1:  {
        0: 'ten',
        1: 'eleven',
        2: 'twelve',
        3: 'thirteen',
        4: 'fourteen',
        5: 'fifteen',
        6: 'sixteen',
        7: 'seventeen',
        8: 'eighteen',
        9: 'nineteen',
        },
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

hundreds = {
    1: 'one hundred',
    2: 'two hundred',
    3: 'three hundred',
    4: 'four hundred',
    5: 'five hundred',
    6: 'six hundred',
    7: 'seven hundred',
    8: 'eight hundred',
    9: 'nine hundred',
}

# Function for number conversion

def english(seed_number):
    if x < 10:
        return ones[x]
    elif x >= 10 and x < 20:
        return tens[1][ones_digit]
    elif x >= 20 and x < 100:
        return tens[tens_digit]+'-'+ones[ones_digit]

print(english(x))