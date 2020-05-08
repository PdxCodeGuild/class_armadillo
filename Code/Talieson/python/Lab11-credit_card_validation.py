# Credit card validation iterates through a series of equations to ensure
# a credit card number is valid.


def validate_credit_card(card):
    # Convert the input string into a list of ints
    card = list(card)

    # Convert each string to an int.
    for i in range(len(card)):
        card[i] = int(card[i])

    # Slice off the last digit. That is the check digit.
    check_digit = card.pop(-1)

    # Reverse the digits.
    card.reverse()

    # Iterate over every other list element in the reversed list and double it.
    for i in range(0, len(card), 2):
        card[i] = card[i] * 2

    # Iterate over every number in the list and subtract nine from numbers > 9.
    for i in range(len(card)):
        if card[i] > 9:
            card[i] -= 9
    print(card)

    # Iterate over every number in the list and sum all values.
    card_sum = 0
    for i in range(len(card)):
        card_sum = card_sum + card[i]

    # Take the second digit of that sum.
    card_sum = card_sum % 10
    print(card_sum)
    # If that matches the check digit, the whole card number is valid.
    if card_sum == check_digit:
        return True
    else:
        return False


is_valid = validate_credit_card('4556737586899895')
print(is_valid)
