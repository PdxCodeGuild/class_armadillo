#dictionary for numbers 0-19
number_to_phrase = { 0 : 'zero', #key is number, value is english number
                     1 : 'one', 
                     2 : 'two',
                     3 : 'three', 
                     4 : 'four', 
                     5 : 'five',
                     6 : 'six',
                     7 : 'seven',
                     8 : 'eight',
                     9 : 'nine',
                     10: 'ten',
                     11: 'eleven',
                     12: 'twelve',
                     13: 'thirteen',
                     14: 'fourteen',
                     15: 'fifteen',
                     16: 'sixteen',
                     17: 'seventeen',
                     18: 'eighteen',
                     19: 'nineteen',
                    }
#this condition pulls from dictionary for number under 19.
user_num = 0
if user_num <=19:
    user_num = int(input('Enter a number to convert it into its English representation: ')) #takes number as integer
    if user_num in number_to_phrase: #if input in dictionary, print phrase
        print(number_to_phrase[user_num])
    else:  #if number greater than or equal to 20, then this condition:
        tens_digit = user_num//10 #floor divide input by 10 for 10's place
        ones_digit = user_num%10 #modulus input by 10 for 1's place
        
        if tens_digit == 2:  #if the 10's place is certain number, prints out english number
            a = ("twenty")
        elif tens_digit == 3:
            a = ("thirty")
        elif tens_digit == 4:
            a = ("fourty")
        elif tens_digit == 5:
            a = ("fifty")
        elif tens_digit == 6:
            a = ("sixty")
        elif tens_digit == 7:
            a = ("seventy")
        elif tens_digit == 8:
            a = ("eighty")
        elif tens_digit == 9:
            a = ("ninety")     

        if ones_digit == 0:  # if one's place is zero, then prints nothing
            b = ("")    
        elif ones_digit == 1:  #if one's place is these numbers, prints hyphen and number
            b = ("-one")
        elif ones_digit == 2:
            b = ("-two")
        elif ones_digit == 3:
            b = ("-three")
        elif ones_digit == 4:
            b = ("-four")
        elif ones_digit == 5:
            b = ("-five")
        elif ones_digit == 6:
            b = ("-six")
        elif ones_digit == 7:
            b = ("-seven")
        elif ones_digit == 8:
            b = ("-eight")
        elif ones_digit == 9:
            b = ("-nine")

        print(a + b)  # prints 10's and 1's places concatenated.


