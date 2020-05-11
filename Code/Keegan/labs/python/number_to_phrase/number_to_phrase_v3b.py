def get_user_number():
    '''Small REPL that asks the user for a number and 
    ensures the number is an integer between 1 and 999'''
    
    while True:
        try:
            number = input("\nPlease enter a whole number 1-999 to convert to a phrase: ")
            int(number)

        except ValueError :
            print("Error. You must enter a number.")
            continue
        
        return int(number)


def get_digit(number, digit):
    '''
    return the specified digit of a number
    get_digit(999, 100) => 900, 
    get_digit(999, 10) => 90 
    get_digit(1456, 1) => 6
    '''
    if digit == 1:
        return number % 10

    return number // digit

def to_roman_numeral(number):
    '''Convert a number 1-1000 into its roman numeral form'''

    # if number == 0:
    #     return numeral
    numerals = {
        1000 : 'M',
        500  : 'D',
        100  : 'C',
        50   : 'L',
        10   : 'X',
        5    : 'V',
        1    : 'I',
    }

    special_numerals = {
        4   : 'IV',
        9   : 'IX',
        40  : 'XL',
        90  : 'XC',
        400 : 'CD',
        900 : 'CM'  
    }
    numeral_keys = list(numerals.keys())
    numeral = ''
    
    if number in numerals: 
        numeral += numerals[number]
        return numeral
    elif number in special_numerals:
        numeral += special_numerals[number]
        return numeral

    # keys: 1000, 500, 100, 50, 10, 5, 1
    for key in numeral_keys:

        quotient = number // key
    
        n = quotient * key

        numeral += numerals[key] * quotient


        number -= n
    # print(f'{key = }, {quotient = }, {n =}, {numeral = }')

    return numeral

def split_number(number):
    # break number into its digits. 9999 => 9000, 900, 90, 9, 1234 => 1000, 200, 30, 4, 1222333 => 1222000, 300, 30, 3
    thousands = get_digit(number, 1000) * 1000
    hundreds = get_digit(number - thousands, 100) * 100
    tens = get_digit(number - thousands - hundreds, 10) * 10
    ones = get_digit(number, 1)
    

    #                                                                            __
    # reduce thousands digit if needed and generate                __            __ ___
    # appropriate lists of lines representing x1000 reduction      IV == 4000,   IV CXV  == 4,125,000 
    split_thousands = []
    line_layers = 0 
    while thousands >= 1000:

        thousands //= 1000
        line_layers += 1

        split_thousands.append(thousands % 1000)  # Split thousands into groups of 3 digits: 111222333000 => [111,222,333]
    
    split_num = split_thousands[::-1] + [hundreds, tens, ones]
    return split_num



def build_numeral(number):
    '''
        Returns a roman numeral representation of a given number, including the numeral itself 
        and superscript lines representing numbers are x1000
    '''
    lines_on_top = []   # superscript lines signifying the numeral is x1000
    numeral = []        # numeral combo

    
    split_num = split_number(number)
    
    for num in split_num:
        numeral.append(to_roman_numeral(num))

    return numeral

def main():
    '''
    Main operation function
    '''
    
    number = get_user_number()

    result = build_numeral(number)
    print(result)


    
main()