# Mob Lab with Keegan

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

    new_list = []
    i = 0
    while i < len(card):
    
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