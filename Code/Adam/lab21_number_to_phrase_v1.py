"""
Lab 21: Number to Phrase ======================================================

Verion 1
Convert a given number into its English representation. For example: 67 becomes 
'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

#x = 67
tens_digit = x//10
ones_digit = x%10

Hint 2: use the digit as an index for a list of strings.

"""

"""input integer, output english representation"""


# for converting ones_digit to English representation
def int_to_string(ones_digit):
    output = ''
    if ones_digit == 9:
        output = 'Nine'
    elif ones_digit == 8:
        output = 'Eight'
    elif ones_digit == 7:
        output = 'Seven'
    elif ones_digit == 6:
        output = 'Six'
    elif ones_digit == 5:
        output = 'Five'
    elif ones_digit == 4:
        output = 'Four'
    elif ones_digit == 3:
        output = 'Three'
    elif ones_digit == 2:
        output = 'Two'
    elif ones_digit == 1:
        output = 'One'
    elif ones_digit == 0:
        output = ''
    return output


# for converting numbers between 10 and 19
def teen_to_string(ones_digit):
    output = ''
    if ones_digit == 9:
        output = 'Nineteen'
    elif ones_digit == 8:
        output = 'Eighteen'
    elif ones_digit == 7:
        output = 'Seventeen'
    elif ones_digit == 6:
        output = 'Sixteen'
    elif ones_digit == 5:
        output = 'Fifteen'
    elif ones_digit == 4:
        output = 'Fourteen'
    elif ones_digit == 3:
        output = 'Thirteen'
    elif ones_digit == 2:
        output = 'Twelve'
    elif ones_digit == 1:
        output = 'Eleven'
    elif ones_digit == 0:
        output = 'Ten'
    return output


num = 15
print(f'You input: {num}') 

tens_digit = num//10 # floor division 10 for tens_digit
ones_digit = num%10  # modulas 10 for ones_digit
# print(f'tens_digit: {tens_digit}') # for testing
# print(f'ones_digit: {ones_digit}')

# for converting tens_digit to english representation
if 9 <= tens_digit < 10:
    print(f'Ninety {int_to_string(ones_digit)}')
elif 8 <= tens_digit < 9:
    print(f'Eighty {int_to_string(ones_digit)}')
elif 7 <= tens_digit < 8:
    print(f'Seventy {int_to_string(ones_digit)}')
elif 6 <= tens_digit < 7:
    print(f'Sixty {int_to_string(ones_digit)}')
elif 5 <= tens_digit < 6:
    print(f'Fifity {int_to_string(ones_digit)}')
elif 4 <= tens_digit < 5:
    print(f'Forty {int_to_string(ones_digit)}')
elif 3 <= tens_digit < 4:
    print(f'Thirty {int_to_string(ones_digit)}')
elif 2 <= tens_digit < 3:
    print(f'Twenty {int_to_string(ones_digit)}')
elif 1 <= tens_digit < 2:
    print(teen_to_string(ones_digit))
elif tens_digit == 0:
    print(ones_digit)