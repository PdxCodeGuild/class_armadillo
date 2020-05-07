# PDX Code Guild Fullstack Course
# Lab 11 Credit Card Validation
# Samuel Purdy
# 4/23/2020

def is_valid(number):
    # Changes the string into a list.
    credit_card = list(number)
    # Loops through the list to change all numbers into a integer.
    for i in range(len(credit_card)):
        credit_card[i] = int(credit_card[i])
    # Records the last digit of the list and pops it.
    check_digit = credit_card[-1]
    credit_card.pop(-1)
    # Reverses the list.
    credit_card.reverse()
    # Multiplies every other digit in the list by 2.
    for i in range(0, len(credit_card), 2):
        credit_card[i] *= 2
    # If the number is greater than 9, it will subtract 9 from that number.
    for i in range(len(credit_card)):
        if credit_card[i] > 9:
            credit_card[i] -= 9
    sum_of_digits = 0
    # Gets the sum of all the credit card numbers.
    for i in range(len(credit_card)):
        sum_of_digits += credit_card[i]
    # If the remainder of the sum divided by 10 is equal to the recorded digit, 
    # the credit card number is valid and the function will return true. If not, 
    # it will return False.
    if sum_of_digits % 10 == check_digit:
        return True
    return False

print(is_valid("4556737586899855"))