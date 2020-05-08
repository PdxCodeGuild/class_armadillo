    # num_places = [
    #     'quadrillion',
    #     'trillion',
    #     'billion',
    #     'million',
    #     'thousand'
    # ]
def get_user_number():
    '''Small REPL that asks the user for a number and 
    ensures the number is an integer between 1 and 999'''
    
    while True:
        try:
            number = input("\nPlease enter a whole number 1-999 to convert to a phrase: ")
            int(number)
            if not 0 < int(number) < 1000:
                raise ValueError

        except ValueError :
            print("Error. You must enter a number 1-999.")
            continue
        
        return int(number)

def number_to_phrase(split_num):
    '''Builds a phrase out of the number split into places,
    returns the complete phrase'''

    num_names = {
        0: {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'
        },
        1: {
            1: 'eleven',
            2: 'twelve',
            3: 'thirteen',
            4: 'fourteen', 
            5: 'fifteen', 
            6: 'sixteen',
            7: 'seventeen',
            8: 'eighteen',
            9: 'nineteen'
        },
        2: 'twenty',
        3: 'thirty',
        4: 'fourty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }

    # unpack each digit of split_num
    hundreds, tens, ones = split_num

    phrase = ''

    if hundreds > 0:
        phrase += num_names[0][hundreds] + ' hundred '

    if tens < 2:
        phrase += num_names[tens][ones]
    
    elif tens > 1:
        phrase += num_names[tens]
        if ones > 0:
            phrase += '-' + num_names[0][ones]
        
    return phrase

def get_hundreds(number):
    '''return the hundreds digit of a number'''
    return number // 100

def get_tens(number):
    '''return the tens digit of a number'''
    return number // 10

def get_ones(number):
    '''return the ones digit of a number'''
    return number % 10

def split_num(number):
    '''splits a number into hundreds, tens and ones digits.
       returns digits as a list'''
    hundreds = get_hundreds(number)
    tens = get_tens(number - (hundreds * 100))
    ones = get_ones(number - (tens * 10))

    return [hundreds, tens, ones]

def main():
    '''
    Main operation function
    '''
    number = get_user_number()
    num_digits = split_num(number)

    print(number_to_phrase(num_digits))


main()
