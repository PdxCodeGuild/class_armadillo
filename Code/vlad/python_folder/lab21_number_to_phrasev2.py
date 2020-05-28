#Lab 21: Number to Phrase Version 2:

"""Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings.



Version 2
Handle numbers from 100-999."""

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


# def convert_num_to_word(digits):
#     hundreds_digit = digits//100 #findout how to get the numbers here so it produce a humdred digit
#     tens_digit  = (digits - hundreds_digit * 100)//10 # take away the hundreds digits and leave it with a single digit that represent hundreds
#     ones_digit  = digits%10
#     # print(single_digit)
#     print(hundreds_digit)
#     # print(two_digit[60],single_digit[7])
#     #print((three_digit[hundreds_digit]) + '-' + (two_digit[tens_digit]) + '-' + (single_digit[ones_digit]))
#     print(f"{three_digit[hundreds_digit]} {two_digit[tens_digit]} {single_digit[ones_digit]}")
#      

# single_digit = {
#     0: 'Zero',
#     1:'One', 
#     2:'Two', 
#     3:'Three', 
#     4:'Four', 
#     5:'Five', 
#     6:'Six',
#     7:'Seven',
#     8:'Eight',
#     9:'Nine'
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

# three_digit = {
#     1:'One Hundred', 
#     2:'Two Hundred', 
#     3:'Three Hundred', 
#     4:'Four Hundred', 
#     5:'Five Hundred', 
#     6:'Six Hundred',
#     7:'Seven Hundred',
#     8:'Eight Hundred',
#     9:'Nine Hundred'
# }


# digits = int(input('enter a number: ')) # user input
# convert_num_to_word(digits)








#Without a function: works the same as the program above
# single_digit = {  
#     1:'One', 
#     2:'Two', 
#     3:'Three', 
#     4:'Four', 
#     5:'Five', 
#     6:'Six',
#     7:'Seven',
#     8:'Eight',
#     9:'Nine'
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

# three_digit = {
#     1:'One Hundred', 
#     2:'Two Hundred', 
#     3:'Three Hundred', 
#     4:'Four Hundred', 
#     5:'Five Hundred', 
#     6:'Six Hundred',
#     7:'Seven Hundred',
#     8:'Eight Hundred',
#     9:'Nine Hundred'
# }


# digits = int(input('enter a number: ')) # user input
# hundreds_digit = digits//100 #findout how to get the numbers here so it produce a humdred digit
# tens_digit  = (digits - hundreds_digit * 100)//10 # take away the hundreds digits and leave it with a single digit that represent hundreds
# ones_digit  = digits%10
# # print(single_digit)
# print(hundreds_digit)
# # print(two_digit[60],single_digit[7])
# #print((three_digit[hundreds_digit]) + '-' + (two_digit[tens_digit]) + '-' + (single_digit[ones_digit]))
# print(f"{three_digit[hundreds_digit]} {two_digit[tens_digit]} {single_digit[ones_digit]}")