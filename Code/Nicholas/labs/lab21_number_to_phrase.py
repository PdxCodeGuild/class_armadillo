number_to_phrase = { 0 : 'zero', 
                     1 : 'one', 
                    '2' : 'two',
                    '3' : 'three', 
                    '4' : 'four', 
                    '5' : 'five',
                    '6' : 'six',
                    '7' : 'seven',
                    '8' : 'eight',
                    '9' : 'nine',
                    '10': 'ten',
                    '11': 'eleven',
                    '12': 'twelve',
                    '13': 'thirteen',
                    '14': 'fourteen',
                    '15': 'fifteen',
                    '16': 'sixteen',
                    '17': 'seventeen',
                    '18': 'eighteen',
                    '19': 'nineteen',
                    }
user_num = 0
if user_num <=19:
    user_num = int(input('Enter a number to convert it into its English representation: '))
    if user_num in number_to_phrase:
        print(number_to_phrase[user_num])
    else:




        # user_num = int(input('Enter a number to convert it into its English representation: '))

        tens_digit = user_num//10
        ones_digit = user_num%10
        
        if tens_digit == 2:
            a = ("twenty-")
        elif tens_digit == 3:
            a = ("thirty-")
        elif tens_digit == 4:
            a = ("fourty-")
        elif tens_digit == 5:
            a = ("fifty-")
        elif tens_digit == 6:
            a = ("sixty-")
        elif tens_digit == 7:
            a = ("seventy-")
        elif tens_digit == 8:
            a = ("eighty-")
        elif tens_digit == 9:
            a = ("ninety-")     

        if ones_digit == 1:
            b = ("one")
        elif ones_digit == 2:
            b = ("two")
        elif ones_digit == 3:
            b = ("three")
        elif ones_digit == 4:
            b = ("four")
        elif ones_digit == 5:
            b = ("five")
        elif ones_digit == 6:
            b = ("six")
        elif ones_digit == 7:
            b = ("seven")
        elif ones_digit == 8:
            b = ("eight")
        elif ones_digit == 9:
            b = ("nine")

        print(a + b)


