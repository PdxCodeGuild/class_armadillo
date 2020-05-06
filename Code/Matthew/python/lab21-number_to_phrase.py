


import random

# 0-19 fixed - one word for the number
# 20-99 follow a pattern

def number_to_phrase(x):
    # ones = {
    #     0: 'zero',
    #     1: 'one',
    #     2: 'two',
    #     3: 'three',
    #     4: 'four',
    #     5: 'five',
    #     6: 'six',
    #     7: 'seven',
    #     8: 'eight',
    #     9: 'nine',
    #     10: 'ten'
    # }
    # tens = {
    #     2: 'twenty',
    #     3: 'thirty'
    # }
    ones = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]
    teens = [
        'ten',      # index 0
        'eleven',   # index 1
        'twelve',   # index 2
        'thirteen', # index 3
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen',
    ]
    tens = [
        'twenty', # index 0
        'thirty', # index 1
        'forty', # index 2
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety' # index 7
    ]
    if x < 10:
        return ones[x]
    elif x < 20:
        return teens[x-10]
    elif x < 100:
        # split the number into its tens and ones digit
        tens_digit = x//10
        ones_digit = x%10
        # we don't want eighty-zero
        if ones_digit == 0:
            return tens[tens_digit-2]
        # use the tens and ones digit to look up the corresponding strings
        # we subtract 2 from the tens digit because the tens list starts at 20
        return tens[tens_digit-2] + '-' + ones[ones_digit]
    elif x < 1000:
        hundreds_digit = x//100
        tens_digit = (x//10)%10
        ones_digit = x%10
        # print(hundreds_digit, tens_digit, ones_digit)
        if tens_digit == 0:
            if ones_digit == 0:
                # e.g. 100, 200
                return ones[hundreds_digit] + ' hundred'
            # e.g. 103, 104
            return ones[hundreds_digit] + ' hundred and ' + ones[ones_digit]
        if tens_digit == 1:
            # e.g. 112, 517
            return ones[hundreds_digit] + ' hundred and ' + teens[ones_digit]
        if ones_digit == 0:
            # e.g. 440, 620
            return ones[hundreds_digit] + ' hundred and ' + tens[tens_digit-2]
        # e.g. 545, 897
        return ones[hundreds_digit] + ' hundred and ' + tens[tens_digit-2] + '-' + ones[ones_digit]


# x = random.randint(100, 999)
# x = 517
# print(x, number_to_phrase(x))

for i in range(1000):
    # x = int(input('enter a number: '))
    print(i, number_to_phrase(i))

# works for x == 1
def roman_numeral(x):
    if x == 1:
        return 'I'
    return None

