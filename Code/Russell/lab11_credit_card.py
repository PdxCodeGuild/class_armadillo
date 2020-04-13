# convert credit card number into a list of individual strings with .split()
card_number = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'.split()
# convert the list of strings into a list of integers
card_number = [int(i) for i in card_number]
# .pop() removes the last digit. Save the last digit to a variable.
check_digit = card_number.pop()
card_number.reverse() # .reverse() reverses the order of the list.

# in a range the length of the card number in steps of two: multiply that number by two
for num in range(0,len(card_number),2):
    card_number[num] *= 2 
# for each item in card_number, if the number is greater than 9, subtract 9
for num in range(0,len(card_number)):
    if card_number[num] > 9:
        card_number[num] -= 9

card_number = sum(card_number) # add all the digits together
last_digit = card_number % 10 # modulus 10 finds the second digit 

if last_digit == check_digit:
    print('Valid')
else:
    print('Not valid')