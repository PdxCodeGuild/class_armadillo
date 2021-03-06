#Lab 11: Credit Card Validation!

def validate_credit_card(card):
    #'4556737586899855'
    # Convert the input string into a list of ints YAY
    card = list(card)
    card_ints = []
    for char in card:
        card_ints.append(int(char))
    card = card_ints
    # Slice off the last digit. That is the check digit. YAY
    check_digit = card.pop(-1)
    # Reverse the digits. YAY
    card.reverse()  # .reverse() list method reverses list in place
    # Double every other element in the reversed list.  YAYAYA
    # card[index1:how_many:step] <= I like this but could be hard to iterate over every other item
    #  gives the index of each item, not the item at each index
    # for item in card:
    #     print(f"{item = } index: {card.index(item)}")  
    # print(f"{len(card) = }") => 15 
    new_list = []
    i = 0
    while i < len(card):
        # print(f"{i % 2 = }") => 0, 1, 0, 1, 0, 1, ...
        # do something when i % 2 = 1 multiply i by 2
        if i % 2 == 0:
            new_list.append(card[i] * 2)
        else:
            new_list.append(card[i])
        i += 1
    card = new_list
    # Subtract nine from numbers over nine.
    i = 0
    while i < len(card):
        num = card[i]
        if num > 9:
            num = num - 9
            card[i] = num
        i += 1
    # Sum all values.
    card = sum(card)
    # Take the second digit of that sum.
    card = str(card)
    match = int(card[1])
    print(f"{match = }")
    # If that matches the check digit, the whole card number is valid.
    print(f"{check_digit = }\n")
    if match == check_digit:
        return True
    # return match == check_digit ... the return statement can be written this way
is_valid = validate_credit_card('4556737586899855')
print(f"{is_valid = }") # True




# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!