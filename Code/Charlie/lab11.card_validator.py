


def validate_credit_card(card):
     # convert the input string into a list of ints.
     card = list(card)
     # convert each string to an int.
     for i in range(len(card)):
         card[i] = int(card[i])
     # slices off the last digit.
     check_digit = card.pop(-1)
     # reverses the digits.
     card.reverse()
     # iterates over every otherlist  element in the reversed list and doubles it.
     for i in range(0, len(card), 2):
         card [i] = card[i] * 2
     # iterates over every number in the list and subtracts nine from numbers > 9.
     for i in range(len(card)):
         if card[i] > 9:
            card[i] -= 9
     print(card)
     # iterates over very number in the list and sum all values.
     card_sum = 0
     for i in range(len(card)):
         card_sum = card_sum + card[i]

     # takes the second digit of that sum.
     card_sum = card_sum % 10
     print(card_sum)
     # if that matches the check digit, the whole card number is valid.
     if card_sum == check_digit:
         return True
     else:
         return False


is_valid = validate_credit_card('4556737586899855')
print(is_valid)

