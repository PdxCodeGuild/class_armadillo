# Lab 11: Credit Card Validation
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

def validate_cc(card):
    card = int(input("Please input a credit card number"))
    check_digit = card.pop(len(card))


# Convert the input string into a list of ints


# Slice off the last digit. That is the check digit.

check_digit[stringlength::-1]

# Reverse the digits.


# Double every other element in the reversed list.


# Subtract nine from numbers over nine.


# Sum all values.


# Take the second digit of that sum.


# If that matches the check digit, the whole card number is valid.


# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!