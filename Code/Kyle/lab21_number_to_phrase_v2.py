# Lab 21 Number to Phrase Version 2
# Kyle Harasimowicz
# Where we're going, we don't need MODULOUS


print("Welcome to Lab 21: Number to Phrase. Give me any number between 0 and 999, and I'll tell you the English representation.")
kill_commands = ["quit", "q", "exit", "stop", "esc", "escape"] 
ones_digit = ""
tens_digit = ""
hundreds_digit = ""
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
dict_hundreds = {
    1 : 'One-Hundred',
    2: 'Two-Hundred',
    3: 'Three-Hundred',
    4: 'Four-Hundred',
    5: 'Five-Hundred',
    6: 'Six-Hundred',
    7: 'Seven-Hundred',
    8: 'Eight-Hundred',
    9: 'Nine-Hundred'
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
    while not number.isnumeric or not int(number) <= 999:
        print("That is not a number between 0 and 999. Please try again. \n")
        break

    x = str(number)

    default_list = [0, 0, 0]
    string_list = []
    for digit in x:
        string_list.append(digit)


    if len(string_list) == 1:   # if the number is onely a ones digit
        default_list[2] = int(string_list[0])   # ones digit replaces third digit in default list
        if default_list == [0, 0, 0]:
            print(f"\n{number} is: Zero. ")
        else:
            ones_digit = dict_ones[default_list[2]]     # Pulls the one's digit from the one's dict.
            result = ones_digit                     # new variable for clarity
            result = result.strip()
            print(f"\n{number} is: {result}. ")

    elif len(string_list) == 2:     # if the number is a tens and ones digit
        default_list[1] = int(string_list[0])   # tens digit replaces second digit in default list
        default_list[2] = int(string_list[1])   # ones digit replaces third digit in default list
        
        # the variables below are requred
        # dictionary index int cannot be a literal index of list
        # such as 'default_list[1]'
        teens = default_list[1]
        ones = default_list[2]

        # For numbers 10-19
        if default_list[1] == 1:
            tens_digit = dict_tens[teens][ones]
            result = tens_digit
            print(f"\n{number} is: {result}. ")
        
        # All other 10s digits
        else:
            tens_digit = dict_tens[default_list[1]]     # Pulls the ten's digit from the ten's dict.
            ones_digit = dict_ones[default_list[2]]

            if ones_digit == "":
                result = tens_digit
            else:
                result = tens_digit + "-" + ones_digit
                result = result.strip()

            print(f"\n{number} is: {result}. ")

    elif len(string_list) == 3:     # if the number is a hundreds, tens, and ones digit
        default_list[0] = int(string_list[0])   # hundreds digit replaces first digit
        default_list[1] = int(string_list[1])   # tens digit replaces second digit in default list
        default_list[2] = int(string_list[2])   # ones digit replaces third digit in default list

        hundreds_digit = dict_hundreds[default_list[0]]     # Pulls the hundred's digit from the hundred's dict.
        tens_digit = dict_tens[default_list[1]]     
        ones_digit = dict_ones[default_list[2]]
        result = tens_digit + "-" + ones_digit
        result = result.strip()                     #clean white-space at this point, need the space between 100s and 10s
        result = hundreds_digit + " " + result      # concatenate result
        print(f"\n{number} is: {result}. ")

