#lab11-credit_card_validation sample by the instructor: 

def validate_credit_card(card):
    # Convert the input string into a list of ints

    # Slice off the last digit. That is the check digit.

    # Reverse the digits.

    # Double every other element in the reversed list.

    # Subtract nine from numbers over nine.

    # Sum all values.

    # Take the second digit of that sum.
    
    # If that matches the check digit, the whole card number is valid.
    ...


is_valid = validate_credit_card('4556737586899855')
print(is_valid) # True