# V2 of lab 21 converts a user provided integer (100-999) to its English number phrase.
hundreds = { 1 : 'one hundred',  # hundreds place dict
             2 : 'two hundred',
             3 : 'three hundred',
             4 : 'four hundred',
             5 : 'five hundred',
             6 : 'six hundred',
             7 : 'seven hundred',
             8 : 'eight hundred',
             9 : 'nine hundred',
             }

tens = {0 : '',  # tens place dict
        1 : {0 : ' ten',  #teens dict nested within tens place dict
             1 : ' eleven',
             2 : ' twelve',
             3 : ' thirteen',
             4 : ' fourteen',
             5 : ' fifteen',
             6 : ' sixteen',
             7 : ' seventeen',
             8 : ' eighteen',
             9 : 'nineteen',   
            },
        2 : ' twenty',
        3 : ' thirty',
        4 : ' forty',
        5 : ' fifty',
        6 : ' sixty',
        7 : ' seventy',
        8 : ' eighty',
        9 : ' ninety',
        }   

ones = {0 : '',  # ones place dict
        1 : '-one',
        2 : '-two',
        3 : '-three',
        4 : '-four',
        5 : '-five',
        6 : '-six',
        7 : '-seven',
        8 : '-eight',
        9 : '-nine',
        }                  
# user inputs digit num here:
user_num = int(input('Enter a number (100-999) to convert to its English phrase equivalent: ' ))

hundreds_digit = user_num//100  # floor divides 100's place to match with dict
tens_digit = (user_num - hundreds_digit*100)//10  # multiplies 100's place digit times 100.  Then subs user num by product. Floor divides difference by 10.
ones_digit = user_num%10 #user nums modulus 10
if tens_digit == 1:  # if 10's digit is one, pulls from teens list nest in tens dict
    num_phrase = hundreds[hundreds_digit] + tens[tens_digit][ones_digit]  #adds those dicts together
    print(num_phrase)
else: 
    num_phrase = hundreds[hundreds_digit] + tens[tens_digit] + ones[ones_digit]  # otherwise, concatenates different dicts for number phrase
    print(num_phrase)




