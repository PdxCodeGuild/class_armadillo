# Lab 21 takes an integer input of any number 1 - 999 and returns it's english
# translation.

# These dictionaries contain the values that form the output.
ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 0: ""}
tens = {1: {1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen",
            5: "fifteen", 6: "sixteen", 7: "seventeen", 8: "eighteen",
            9: "ninteen", 0: "ten"},
        2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninty", 0: ""}
hundreds = {1: "one hundred and", 2: "two hundred and", 3: "three hundred and",
            4: "four hundred and", 5: "five hundred and", 6: "six hundred and",
            7: "seven hundred and", 8: "eight hundred and",
            9: "nine hundred and", 0: ""}

# Main run loop
while True:
    # tested loop takes, and validates, input
    while True:
        number = (input('''
    Enter a number to get it's english translation.
    if finished, enter done.
        '''))
        if number.isdigit():
            number = int(number)
            break
        elif number in ['done', 'quit', 'exit']:
            print("Thanks for using numbers to english translation!\n")
            exit()
        else:
            print("please enter a valid number between 0 - 999.")

    # floor divide to get the front digit
    hund_dig = number // 100
    # floor divide minus the first digit * 100 to get the second digit
    ten_dig = (number - hund_dig*100) // 10
    # use modulus to get final digit
    one_dig = number % 10
    # check if we have a 1 in our second digit
    if ten_dig == 1:
        # access nested dictionary to get special names in "-teens"
        output = f"{hundreds[hund_dig]} {tens[ten_dig][one_dig]}"
    # test for edge case of a 0 being input
    elif hund_dig == 0 and ten_dig == 0 and one_dig == 0:
        output = "zero"
    # if we don't have outlier inputs, assemble output message
    else:
        output = f"{hundreds[hund_dig]} {tens[ten_dig]} {ones[one_dig]}"

    print(f"\n\t{number} in english is {output}!")
