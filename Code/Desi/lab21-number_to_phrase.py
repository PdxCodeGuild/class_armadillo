import random


# Handle numbers from 0-99.

# Lab 21: Number to Phrase


# ask for user input
question = int(input("Choose a number from 0-9: "))


ones = {
        0 : "zero",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine"
}

tens = {
        0 : "ten",
        1 : "eleven",
        2 : "twelve",
        3 : "thirteen",
        4 : "fourteen",
        5 : "fifteen",
        6 : "sixteen",
        7 : "seventeen",
        8 : "eighteen",
        9 : "nineteen"
} 

small_num = (ones, tens[question])
print(small_num)

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