#Lab 21: Number to Phrase Version 1:

"""Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. 

Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings.


Version 2
Handle numbers from 100-999."""

# Convert a given number into its English representation

"""  Handle numbers from 0-99. break it donw in smaller pieces below """
# Handle numbers from 0-9
# Handle numbers from 10-19
# Handle numbers from 20-29
# Handle numbers from 30-39
# Handle numbers from 40-49
# Handle numbers from 50-59
# Handle numbers from 60-69
# Handle numbers from 70-79
# Handle numbers from 80-89
# Handle numbers from 90-99
import math
import string

# x = 67
# tens_digit = x//10 # to get the
# ones_digit = x%10
# Hint 2: use the digit as an index for a list of strings.
#Convert a given number into its English

#def convert_num_to_word():

# use if statements to check if number are in the 11

# to count for numbers zero to 10
digit_one = { 
    0: "Zero", 
    1:'One', 
    2:'Two', 
    3:'Three', 
    4:'Four', 
    5:'Five', 
    6:'Six',
    7:'Seven',
    8:'Eight',
    9:'Nine',
    10:'Ten'
}

# to count for the numbers in teen 
digit_two = {
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

# count for numbers ten digits 
digit_three = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
} 


user_input = int(input('enter a number to convert to words please: '))

def numbers_phrase(nums):
    
    if nums < 10:
        return digit_one[nums]

    elif nums < 20:
        return digit_two[nums]
    
    elif nums < 100:
        tens_digit = nums//10
        ones_digit = nums%10
    # if nums < 0:
        # return digit_one[nums]
        # return digit_three[tens_digit]
        return digit_three[tens_digit] + '-' + digit_one[ones_digit]
        # enter a number to convert to words please: 50
        # your number to phase is: fifty-Zero  Learn how to remove the zero here

    
nums = user_input
phrase = (numbers_phrase(nums))
print(f'your number to phase is: {phrase}')


# def number(Number):
    # if 0 <= Number <= 19:
    #     return num2words1[Number]
    # elif 20 <= Number <= 99:
    #     tens, remainder = divmod(Number, 10)
    #     return num2words2[tens - 2] + '-' + num2words1[remainder] if remainder else num2words2[tens - 2]
    # else:
    #     print('Number out of implemented range of numbers.')


# single_digit = { 
#     0: "zero", 
#     1:'One', 
#     2:'Two', 
#     3:'Three', 
#     4:'Four', 
#     5:'Five', 
#     6:'Six',
#     7:'Seven',
#     8:'Eight',
#     9:'Nine',
#     10:'Ten'
# }

# two_digit = {
#     1:'Ten', 
#     2:'Twenty', 
#     3:'Thirty', 
#     4:'Forty', 
#     5:'Fifty', 
#     6:'Sixty',
#     7:'Seventy',
#     8:'Eighty',
#     9:'Ninety'
# }

# user_input = int(input('enter a number: '))
# x = user_input
# ones_digit  = x%10
# # print(single_digit)
# tens_digit  = x//10
# # print(tens_digit)
# # print(two_digit[60],single_digit[7])
# print((two_digit[tens_digit]) + '-' + (single_digit[ones_digit]))

    # num = input('Which ')
    # if num == '0': 
    #     print("Zero ", end = " ") 
    # elif num == '1': 
    #         print("One ", end = " ")
    # elif num == '2': 
    #         print("Two ", end = " ")
    # elif num == '3': 
    #         print("Three ", end = " ")
    # elif num == '4': 
    #         print("Four ", end = " ")
    # elif num == '5': 
    #         print("Five ", end = " ")
    # elif num == '6': 
    #         print("Six ", end = " ")
    # elif num == '7': 
    #         print("Seven ", end = " ")
    # elif num == '8': 
    #         print("Eight ", end = " ")
    # elif num == '9': 
    #         print("Nine ", end = " ")     

    # def number(Number):
    # if 0 <= Number <= 19:
    #     return num2words1[Number]
    # elif 20 <= Number <= 99:
    #     tens, remainder = divmod(Number, 10)
    #     return num2words2[tens - 2] + '-' + num2words1[remainder] if remainder else num2words2[tens - 2]
    # else:
    #     print('Number out of implemented range of numbers.')