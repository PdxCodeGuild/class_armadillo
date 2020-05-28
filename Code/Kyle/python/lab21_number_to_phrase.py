# Lab 21 Number to Phrase Version 1
# Kyle Harasimowicz
# Where we're going, we don't need MODULOUS


print("Welcome to Lab 21: Number to Phrase. Give me any number between 0 and 99, and I'll tell you the English representation.")
kill_commands = ["quit", "q", "exit", "stop", "esc", "escape"] 
ones_digit = ""
tens_digit = ""
result = ""

dict_ones = {
    0 : "",
    1: "One",
    2 : "Two",
    3 : "Three",
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
}

dict_teens = {
    0: 'Ten',
    1: 'Eleven',
    2: 'Twelve',
    3: 'Thirteen',
    4: 'Fourteen',
    5: 'Fifteen',
    6: 'Sixteen',
    7: 'Seventeen',
    8: 'Eighteen',
    9: 'Nineteen'
}

dict_tens = {
    1 : dict_teens,
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety'
}


game = True
while game:

    # Ask user for number
    number = input("\nNumber: ").strip() 

    # quit option
    if number in kill_commands:
        print("\nThanks for playing.\nGoodbye! \n ")
        quit()
        

    # Validate numeric input
    while not number.isnumeric or not int(number) <= 99:
        print(f"\n{number} is not a number between 0 and 99. Please try again. \n")
        break

    x = str(number)

    default_list = [0, 0]
    string_list = []
    for digit in x:
        string_list.append(digit)


    if len(string_list) == 1:   # if the number is onely a ones digit
        default_list[1] = int(string_list[0])   # ones digit replaces second digit in default list
        if default_list == [0, 0]:
            print(f"\n{number} is: Zero. ")
        else:
            ones_digit = dict_ones[default_list[1]]     # Pulls the one's digit from the one's dict.
            result = ones_digit                     # new variable for clarity
            result = result.strip()
            print(f"\n{number} is: {result}. ")

    elif len(string_list) == 2:     # if the number is a tens and ones digit
        default_list[0] = int(string_list[0])   # tens digit replaces first digit in default list
        default_list[1] = int(string_list[1])   # ones digit replaces second digit in default list
        
        # the variables below are requred
        # dictionary index int of int cannot be a literal index of list
        # such as 'default_list[1]'
        teens = default_list[0]
        ones = default_list[1]

        # For numbers 10-19
        if default_list[0] == 1:
            tens_digit = dict_tens[teens][ones]
            result = tens_digit
            print(f"\n{number} is: {result}. ")
        
        # All other 10s digits
        else:
            tens_digit = dict_tens[default_list[0]]     # Pulls the ten's digit from the ten's dict.
            ones_digit = dict_ones[default_list[1]]

            if ones_digit == "":
                result = tens_digit
            else:
                result = tens_digit + "-" + ones_digit
                result = result.strip()

            print(f"\n{number} is: {result}. ")



