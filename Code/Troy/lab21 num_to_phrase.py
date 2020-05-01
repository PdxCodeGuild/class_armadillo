# Lab 21 Number to Phrase
# Troy Fitzgerald

'''
Convert a given number into its English representation. For 
example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

Hint 2: use the digit as an index for a list of strings.'''

# import the module.
import math

# assigns numbers in dictionary for 1-10.
nums_1 = {
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
    10: 'ten'
}
# assigns numbers in dictionary 11-19.
nums_2 = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}
# assigns numbers in dictionary for higher for numbers by 10.
nums_3 = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
} 

# asks the user for a number.
user_question = int(input('What is your number? '))

# defines the function for the user input.
def nums_to_phrase(nums):
    # if number less than 10.
    if nums < 10:
        return nums_1[nums]
    # if number less than 20
    elif nums < 20:
        return nums_2[nums]
    # if number greater than 20 but less than 100.
    elif nums < 100:
        tens_digit = nums//10
        ones_digit = nums%10
        return nums_3[tens_digit] + '-' + nums_1[ones_digit]
        print(tens_digit)       
        print(ones_digit)

    
nums = user_question
phrase = (nums_to_phrase(nums))
print(f'Your number in English is {phrase}.')

