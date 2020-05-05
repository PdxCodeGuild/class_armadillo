# Lab 21 Number to Phrase
# Troy Fitzgerald

'''Version 2
Handle numbers from 100-999.'''

# imports the module.
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

nums_4 = {
    1: 'one-hundred',
    2: 'two-hundred',
    3: 'three-hundred',
    4: 'four-hundred',
    5: 'five-hundred',
    6: 'six-hundred',
    7: 'seven-hundred',
    8: 'eight-hundred',
    9: 'nine-hundred'
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
        ones_digit = nums%10
        tens_digit = nums//10
        return nums_3[tens_digit] + '-' + nums_1[ones_digit]
        print(tens_digit)       
        print(ones_digit)

    elif nums < 999:
        hundreds_digit = nums//100
        nums -= hundreds_digit *100
        tens_digit = nums//10
        ones_digit = nums%10
        if tens_digit == 1:
            tens = nums_2[10 + ones_digit]
            ones = ''
            tens_and_ones = tens   
        elif tens_digit <= 9:
            tens = nums_3[tens_digit]
            ones = nums_1[ones_digit]
            tens_and_ones = tens + '-' + ones
            return nums_4[hundreds_digit] + '-' + tens_and_ones
    
nums = user_question
phrase = (nums_to_phrase(nums))
print(f'Your number in English is {phrase}.')

