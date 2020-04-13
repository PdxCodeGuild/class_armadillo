
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!

def validate_credit_card(card):
# convert the input string into a list of ints.
    card = list(card)
# convert each string to an int.
    for i in range(len(card)):
        card[i] = int(card[i])
# Slice off the last digit. That is the check digit.
    check_digit = card.pop(-1)
# Reverse the digits.
    card.reverse()
# Double every other element in the reversed list.
    for i in range(0, len(card), 2):
        card[i] = card[i] * 2   
# Subtract nine from numbers over nine.
    for i in range(len(card)):
        if card[i] > 9:
            card[i] -= 9
    print(card)        
# Sum all values.
    value_sum = 0 
    for i in range(len(card)):
        value_sum = value_sum + card[i]
# Take the second digit of that sum.
    value_sum = value_sum % 10
    print(value_sum)
# If that matches the check digit, the whole card number is valid.
    if value_sum == check_digit:
        return True
    else:
        return False    


is_valid = validate_credit_card('4556737586899855')
print(is_valid)
