print("--- Guess a Number ---")

def guess_a_number():

    word_dictionary = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 1000:"thousand"}

    user_number_input = input("enter a number to convert to words: ")

    # print(f"user_number_input: {user_number_input}")

    if user_number_input is True:
        print("enter a number!")
    else: 
        pass

    user_int = int(user_number_input)

# math
    user_int_mod_one = user_int %10
    print(f"mod one: {user_int_mod_one}")

    tens_digit = user_int - user_int_mod_one
    print(f"tens digit: {tens_digit}")

    hundredth_digit = user_int % 100
    print(f"hundredth digit: {hundredth_digit}")

    user_int_mod_hundredth = (user_int %100) // 10 * 10
    print(f"mod hundredth: {user_int_mod_hundredth}")

    remainder = (user_int - hundredth_digit) // 100
    print(f"remainder: {remainder}")
# if statements 
    if user_int <= 19:
        print(word_dictionary[user_int])
    elif user_int <= 99:
        print(f"you entered {word_dictionary[tens_digit]} {word_dictionary[user_int_mod_one]}")
    elif user_int >= 100:
        print(f"you entered {word_dictionary[remainder]} hundred {word_dictionary[user_int_mod_hundredth]} {word_dictionary[user_int_mod_one]}")
    else:
        pass
    # return number_to_phrase

guess_a_number = guess_a_number()

# print(guess_a_number)


'''
Lab 21: Number to Phrase
Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings.

Version 2
Handle numbers from 100-999.

Version 3 (optional)
Convert a number to roman numerals.

Version 4 (optional)
Convert a time given in hours and minutes to a phrase.

'''