# Lab 21 Number to Phrase
# Kyle Harasimowicz

# Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.

# x = 67
# tens_digit = x//10
# ones_digit = x%10


print("Welcome to Lab 21: Number to Phrase. Give me any number between 0 and 000, and I'll tell you the English representation.")
ones_digit = ""
tens_digit = ""
hundreds_digit = ""


# Ask user for number
number = input("\nNumber: ")

# Validate numeric input
while not number.isnumeric or not int(number) <= 999:
    print("That is not a number between 0 and 999. Please try again. \n")

x = str(number)

old_list = [0, 0, 0]
new_list = []


while True:
    if len(x) == 1:
        old_list[2] = x
        break
    elif len(x) == 2:
        old_list[1] = x[0]
        old_list[2] = x[1]
        break
    elif len(x) == 3:    
        old_list = []
        for digit in x:
            old_list.append(digit)
        break
 

print(old_list)

dict_ones = {
    0 : "",
    1: "one",
    2 : "two",
    3 : "three",
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

dict_teens = {
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen'
}

dict_tens = {
    1 : dict_teens,
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

if old_list[0] == 0 and old_list[1] == 1:
    english_number = dict_tens[1][old_list[2]]
    print(english_number)


# def get_ones():

# if x == 1:
#     ones_digit = "One. "
# elif x == 2:
#     ones_digit = "Two. "
# elif x == 3:
#     ones_digit = "Three. "
# elif x == 4:
#     ones_digit = "Four. "
# elif x == 5:
#     ones_digit = "Five. "
# elif x == 6:
#     ones_digit = "Six. "
# elif x == 7:
#     ones_digit = "Seven. "
# elif x == 8:
#     ones_digit = "Eight. "
# elif x == 9:
#     ones_digit = "Nine. "



# if len(new_list) == 1:
#     route = single_digit
    
# elif len(new_list) == 2:
#     if new_list[0] == 1:
#         route = double_digit_teens
#     else:
#         route = double_digit
# elif len(new_list) == 3:
#     route = triple_digit
# else:
#     print("N/a")




# # if x == 0:
# #     ones_digit - "Zero. "

# elif x == 10:
#     tens_digit = "Ten. "


# english_number = hundreds_digit + tens_digit + ones_digit

# english_number = english_number.strip().split()
# english_number = ''.joint(.english_number)
# english_number = int(english_number)

