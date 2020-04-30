# PDX Code Guild Fullstack Course
# Lab 21 Number to Phrase
# Samuel Purdy
# 4/30/2020

import string

# Predefined variables
first_place = ["Zero", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine"]
teens = [" Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
second_place = [" Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
others = [" Hundred", " Thousand", " Million", " Billion", " Trillion", " Quadrillion"]

# Returns a list of numbers based on the string that is sent.
# number = a number that is of type string.
def make_list_of_numbers(number):
    number_list = list()

    # Loops through the entire string until the string length is 0, 
    # then it breaks. While its looping, the string is broken up 
    # into sections of 3 characters and added to the list.
    while True:
        # If the length of the string is still greater than 3,
        # it will keep cutting it down until the string is empty.
        if len(number) > 3:
            number_list.append(number[:3])
            number = number[3:]
        # If the length is not greater than 3 it will just add the 
        # last of the number to the end of the list then break.
        else:
            number_list.append(number)
            break
    return number_list

# Gets the whole number from the user and returns a reversed number.
def get_whole_number():
    user_input = " "
    # So long as the number is not whole, it will keep asking the 
    # user for a valid input.
    while not user_input.isnumeric():
        user_input = input("Please enter in a whole number: ")
        
        # Just makes sure that the user doesn't enter in a number 
        # leading with 0 if it is not 0.
        if user_input[0] == "0" and len(user_input) > 1:
            print("Please don't enter in a number leading with 0")
            user_input = " "

    # user_input[::-1] means that it is returning a string that's 
    # being iterated from the back as opposed to the front. This 
    # makes running through the reverse string easier since we 
    # don't know how many numbers follow the first few. It also 
    # makes it more modular, for instance, if we wanted more 
    # 'illion' strings, we could just add them to the list.
    return user_input[::-1]

# Returns a full phrased number based on what is sent.
# hundred = a string with at most 3 characters in it, representing 
# a number in reverse.
def send_word(hundred):

    # Initializing Variables
    tens_place = str()
    hundreds_place = str()

    # If the length of the number is just 1 character, it will
    # return whatever the real number at the beginning is.
    if len(hundred) == 1:
        return first_place[int(hundred[0])]
    
    # Checks to see if the second character is in the teens, 
    # adding the appropriate string the the word.
    if (int(hundred[1])*10) // 10 == 1:
        tens_place = second_place[int(hundred[0])-1]

    # Checks which tens place the second character is in. If 
    # the first place has no number, it will simply add no number.  
    if hundred[1] == "0":
        if hundred[0] != "0":
            tens_place = first_place[int(hundred[0])]
    # If there is no remainder of the ones and the tens place 
    # together, it adds just the tens place.
    elif ((int(hundred[1])*10) + int(hundred[0])) % 10 == 0:
        tens_place = second_place[int(hundred[1])-1]
    # Checks to see if the number is in the teens, and sets the 
    # tens place to the number based on that place.
    elif hundred[1] == "1" and hundred[0] != "0":
        tens_place = teens[int(hundred[0])-1]
    # Otherwise, it just adds them both together.
    else:
        tens_place = second_place[int(hundred[1])-1] + first_place[int(hundred[0])]
    
    # If there are just two characters, it will return the 
    # tens and ones place.
    if len(hundred) == 2:
        return tens_place
    
    # Adds whatever phrased number is at the end of the string
    # plus 'hundred' to complete the phrase
    hundreds_place = first_place[int(hundred[2])] + others[0]
    return hundreds_place + tens_place

# Returns a phrase based on a list of stringed reversed numbers 
# that are sent.
# number = list of string reversed numbers.
def make_word(number):
    made_word = str()
    # Loops through the list and adds phrases together
    for i in range(len(number)):
        if i != 0:
            made_word = others[i] + made_word
        if len(number) == 1:
            return send_word(number[0])
        # Adds whatever 'other' part to the beginning of the 
        # string to return
        made_word = send_word(number[i]) + made_word

    return made_word

print(make_word(make_list_of_numbers(get_whole_number())))

