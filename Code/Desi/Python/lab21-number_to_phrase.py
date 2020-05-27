import random


# references
# https://pypi.org/project/num2words/
# https://stackoverflow.com/questions/19504350/how-to-convert-numbers-to-words-in-python



# Handle numbers from 0-99.

# Lab 21: Number to Phrase


# ask for user input



nums_1to19 = [
         "zero",
         "one",
         "two",
         "three",
         "four",
         "five",
         "six",
         "seven",
         "eight",
         "nine",
         "ten",
         "eleven",
         "twelve",
         "thirteen",
         "fourteen",
         "fifteen",
         "sixteen",
         "seventeen",
         "eighteen",
         "nineteen",
]

n_20 = "twenty"
n_30 = "thirty"
n_40 = "forty"
n_50 = "fifty"
n_60 = "sixty"
n_70 = "seventy"
n_80 = "eighty"
n_90 = "ninety"

# ask for user input
x = int(input("Choose a number you want to translate into words: "))
# converting the list into a string
List_x = list(str(x))
# takes 'ones' place and turns it into an integer
ones = int(List_x[-1])
# changing from number form
of_ones = nums_1to19[ones]
# adding 'zero' so that it doesn't add additional zeros
if of_ones == "zero" and len(List_x) != 1:
        of_ones = ''
if x < 20:
        number = nums_1to19[x]
# scanning through every number the user provides
elif List_x[-2] == '2':
        number = '{} {}'.format(n_20, of_ones)
elif List_x[-2] == '3':
        number = '{} {}'.format(n_30, of_ones)
elif List_x[-2] == '4':
        number = '{} {}'.format(n_40, of_ones)
elif List_x[-2] == '5':
        number = '{} {}'.format(n_50, of_ones)
elif List_x[-2] == '6':
        number = '{} {}'.format(n_60, of_ones)
elif List_x[-2] == '7':
        number = '{} {}'.format(n_70, of_ones)
elif List_x[-2] == '8':
        number = '{} {}'.format(n_80, of_ones)
elif List_x[-2] == '9':
        number = '{} {}'.format(n_90, of_ones)
print('Translated, your output is :' , number)




# # rounds down to the nearest tens
# tens_digit = user_input//10
# # e.g. 100//10 = 10
# # print(tens_digit)
# # gives the remainer(ones place)
# ones_digit = user_input%10
# print(ones_digit)








# len(0,99)

# 79 --> seventy-nine 

# x = 79
# tens_digit = x//10, 70//10 = 7
# ones_digit = x%10, 9%10 = 






# Convert a given number into its English representation. For example:
#  67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.

# x = 67
# tens_digit = x//10
# ones_digit = x%10
# Hint 2: use the digit as an index for a list of strings.