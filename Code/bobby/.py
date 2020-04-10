def validate_credit_card(card):
    '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
    # Convert the input string into a list of ints
    card = list(card)
    
    card_ints = []
    
    for char in card:
        card_ints.append(int(char))

    card = card_ints
    
    # Slice off the last digit. That is the check digit.
   
    check_digit = card.pop(-1)

    # Reverse the digits.
    
    card.reverse()  
    
    # Double every other element in the reversed list.
    
    new_list = []
    i = 0
    while i < len(card):
        if i % 2 == 0:
            new_list.append(card[i] * 2)
        else:
            new_list.append(card[i])
        i += 1

    card = new_list
        #print(f"After reverse: {card = }\n")
    # Subtract nine from numbers over nine.
    i = 0 
    while i < len(card):
        num = card[i]
        if num > 9 :
            num = num - 9
            card[i] = num
        i += 1    
        
    # Sum all values.
    card = sum(card)
    # Take the second digit of that sum.
    card = str(card)
    card[1]
    print(f"{match[1] = }")
    # If that matches the check digit, the whole card number is valid.
    
    
    print(f"{check_digit = }\n")
    if match == check_digit:
        return True