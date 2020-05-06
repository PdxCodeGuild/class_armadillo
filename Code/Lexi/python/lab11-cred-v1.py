# Lab 11: Credit Card Validation
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

#disclaimer: USED TALIESON'S CODE AS REF
def validate_cc(card):
    #card = long(input("Please input a credit card number"))
    # card = long(input("Please input a credit card number"))
    #NameError: name 'long' is not defined
    #check_digit = card.pop(len(card)


# Convert the input string into a list of ints
    card = list(card)
    for i in range (len(card)):
        card[i] = int(card[i])

# Slice off the last digit. That is the check digit.

    check_digit = card.pop(-1)

# Reverse the digits.
    card.reverse() # reverse() list method reverses list in place
    
    print(f"Before reverse: {card} = ")


# Double every other element in the reversed list.
    for i in range(0, len(card), 2):
        card[i] *= 2


# Subtract nine from numbers over nine.
    for i in range(len(card)):
        if card[i] > 9:
            card[i] -= 9
        print(card) 

# Sum all values.

    card_sum =0
    for i in range(len(card)):
        card_sum += card[i]

# Take the second digit of that sum.

    card_sum %= 10
    print(card_sum)

# If that matches the check digit, the whole card number is valid.
    if card_sum == check_digit:
        return True
    else:
        return False

is_valid = validate_cc('5371016189687383')
print(validate_cc)

'''   RESULTAT:
Before reverse: card = [8, 3, 7, 8, 6, 9, 8, 1, 6, 1, 0, 1, 7, 3, 5]
[7, 3, 14, 8, 12, 9, 16, 1, 12, 1, 0, 1, 14, 3, 10]
[7, 3, 14, 8, 12, 9, 16, 1, 12, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 12, 9, 16, 1, 12, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 12, 9, 16, 1, 12, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 3, 9, 16, 1, 12, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 3, 9, 16, 1, 12, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 3, 9, 7, 1, 12, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 3, 9, 7, 1, 12, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 3, 9, 7, 1, 3, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 3, 9, 7, 1, 3, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 3, 9, 7, 1, 3, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 3, 9, 7, 1, 3, 1, 0, 1, 14, 3, 10]
[7, 3, 5, 8, 3, 9, 7, 1, 3, 1, 0, 1, 5, 3, 10]
[7, 3, 5, 8, 3, 9, 7, 1, 3, 1, 0, 1, 5, 3, 10]
[7, 3, 5, 8, 3, 9, 7, 1, 3, 1, 0, 1, 5, 3, 1]
7'''