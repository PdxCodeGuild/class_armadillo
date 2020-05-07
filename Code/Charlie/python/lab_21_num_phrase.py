
def get_number():
    number = input("Enter a number to translate to english: ")
    if number.isdigit():
        number = int(number)
    elif number in ['done', 'quit', 'exit']:
        print("Goodbye!")
        exit()
    else:
        print("invalid response please enter number")

    # this is the dict that conatins the singile digit numbers
    one_number = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: ""}

    # this is the dic that contains the douible   
    two_numbers = {1: {1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen",
    5: "fifteen", 6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "ninteen", 0: "ten"},
    2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty",
    7: "seventy", 8: "eighty", 9: "ninty", 0: ""}

    three_numbers = {1: "one hundred and", 2: "two hundred and", 3: "three hundred and", 4: "four hundred and", 5: "five hundred and", 6: "six hundred and", 7: "seven hundred and", 8: "eight hundred and", 9: "nine hundred and",  0:  ""}

    # divide to get the first number
    three_digits = number // 100
    # divide minus the first number * 100 to get the second number
    two_digits = (number - three_digits*100) // 10
    # use modulus to get last number
    one_digit = number % 10
    # check if 1 in our second number
    if two_digits == 1:
        #dictionary to get special name in teen
        output = f"{three_numbers[three_digits]} {two_numbers[two_digits][one_digit]}"
    # test for a 0 being input
    elif three_digits == 0 and two_digits == 0 and one_digit == 0:
        output = "zero"
    
    else:
        output = f"{three_numbers[three_digits]} {two_numbers[two_digits]} {one_number[one_digit]}"
        print(f"{number} in english is{output}!")


    
                
get_number()




