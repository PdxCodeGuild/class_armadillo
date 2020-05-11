# Lab 21 Number to Phrase
# Troy Fitzgerald

'''Version 2
Handle numbers from 100-999.'''

# imports the module.
import math

# assigns numbers in a dictionary from 0-19.
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
    10: 'ten',
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
# assigns numbers in a dictionary from 20-90 by tens..
nums_2 = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
    0: ''
} 
# assigns numbers in a dictionary from 100-900 by hundreds.
nums_3 = {
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
    # if number less than 20.
    if nums < 20:
        return nums_1[nums]
    # if number less than 100.
    elif nums < 100:
        ones_digit = nums%10
        tens_digit = nums//10
        return nums_2[tens_digit] + '-' + nums_1[ones_digit]
    # if number less than 999.
    elif nums < 999:
        hundreds_digit = nums//100
        nums -= hundreds_digit *100
        tens_digit = nums//10
        ones_digit = nums%10
        #print(hundreds_digit)
        return nums_3[hundreds_digit]+ '-' +  nums_2[tens_digit] + '-' + nums_1[ones_digit] 



nums = user_question
phrase = (nums_to_phrase(nums))
print(f'Your number in English is {phrase}.')