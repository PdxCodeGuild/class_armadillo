from colorama import Fore
import time

# welcome message prints on two lines
print('''\nWelcome to NUMBER TO PHRASE! 
(Enter 'quit' to exit...)''')

time.sleep(1)

# dictionary for unique integer keys, no patterns
unique_dict = {
    0 :'zero',
    1 :'one',
    2 :'two',
    3 :'three',
    4 :'four',
    5 :'five',
    6 :'six',
    7 :'seven',
    8 :'eight',
    9 :'nine',
    10 :'ten',
    11 :'eleven',
    12 :'twelve',
    13 :'thirteen',
    14 :'fourteen',
    15 :'fifteen',
    16 :'sixteen',
    17 :'seventeen',
    18 :'eighteen',
    19 :'nineteen',
}

# dicitionary for tens digit place...except 10-19 
tens_pattern_dict = {
    2 :'twenty',
    3 :'thirty',
    4 :'forty',
    5 :'fifty',
    6 :'sixty',
    7 :'seventy',
    8 :'eighty',
    9 :'ninety',   
}

# dicitionary for hundreds place
hundr_pattern_dict = {
    1 :"one hundred",
    2 :'two hundred',
    3 :'three hundred',
    4 :'four hundred',
    5 :'five hundred',
    6 :'six hundred',
    7 :'seven hundred',
    8 :'eight hundred',
    9 :'nine hundred',   
}

while True: # loop for selecting unique num, math for pattern number, quit and input validation
    hundreds = '' # keeps track of the dictionary key for each digit group as loop iterates over input number
    tens = ''
    ones = ''
    num = input('\nEnter your number (0-999): ').lower().strip() # user input number as string
    if num.isnumeric() == False and num == 'quit': # checks if 'quit' was entered, if so exits program
        time.sleep(0.5)
        print('\nGood bye!\n')
        exit()
    elif num.isnumeric() == False or int(num)<0 or int(num)>999: # if words other than 'quit' entered or number not 0-999
        print(Fore.RED + '\nINVALID ENTRY!\n' + Fore.RESET) # prints invalid message and returns to top of loop
        continue 
    else: # when valid string is entered (a number 0-999)
        nums = [int(x) for x in str(num)] # converts input string to list of numbers for iteration below
        num = int(num) # converts input to integer for greater than, less than comparisons
        if num < 20: # if num < 20, prints output directly from unique dictionary, returns to top of loop
            print('Your number phrase is: ' + Fore.MAGENTA + f'{unique_dict[num]}' + Fore.RESET)
        elif 20 <= num < 100: # 20-99...two index positions in list of input numbers
            for i in range(len(nums)-1): #iterates over input string that was converted to list
                tens = nums[0] # first digit of 2 digit number is always in tens place, set the first digit as tens key
                if nums[1] != 0: # if second digit is not a zero 
                    ones = nums[1] # set the second digit as ones key (unique_dict)
            if nums[1] != 0: # print output for 21-29, 31-39, 41-49, etc
                print('Your number phrase is: ' + Fore.MAGENTA + f'{tens_pattern_dict[tens]}-{unique_dict[ones]}' + Fore.RESET)        
            else: # separate print statment for 20, 30, 4, etc...since no hyphen
                print('Your number phrase is: ' + Fore.MAGENTA + f'{tens_pattern_dict[tens]}' + Fore.RESET)
        elif num >= 100: # 100-999...three index positions in list of input numbers
            for i in range(len(nums)-1): # iterates over list of input numbers 
                hundreds = nums[0] # 1xx-9xx...sets digit in that spot as hundreds key
                if nums[1] == 1: # x10-x19...checks for teens due to being in unique dict for print without hyphen 
                    ones = nums[2] + 10 # math to set ones digit since must key unique dict but digits are in two different indices
                elif nums[1] != 0 and nums[2] == 0: # x20, x30, x40 ...checks for whole tens
                    tens = nums[1]  # set digit in that spot as tens key       
                elif nums[1] == 0 and nums[2] != 0: # x01-x09...checks for single ones digits, no hyphen
                    ones = nums[2] # sets that digit as ones key (unique_dict) if ones key not already set above 
                else: # 121-129, 131-139, etc....accounts for last remaining numbers and tens and ones keys appropriately
                    tens = nums[1]
                    ones = nums[2]
            if nums[1] == 0 and nums[2] == 0: # 100, 200, 300, etc...print outputs...no 
                print('Your number phrase is: ' + Fore.MAGENTA + f'{hundr_pattern_dict[hundreds]}' + Fore.RESET)
            elif nums[1]== 0  or nums[1] == 1: # 101-119...print outputs
                print('Your number phrase is: ' + Fore.MAGENTA + f'{hundr_pattern_dict[hundreds]} {unique_dict[ones]}' + Fore.RESET)
            elif nums[1] != 1 and nums[2] == 0: # 120, 130, 140, etc...print outputs
                print('Your number phrase is: ' + Fore.MAGENTA + f'{hundr_pattern_dict[hundreds]} {unique_dict[ones]}' + Fore.RESET)
            else: # 121-129, 131-139, etc....print outputs...with hyphens
                print('Your number phrase is: ' + Fore.MAGENTA + f'{hundr_pattern_dict[hundreds]} {tens_pattern_dict[tens]}-{unique_dict[ones]}' + Fore.RESET)




'''
# Lab 21: Number to Phrase
Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

```python
x = 67
tens_digit = x//10
ones_digit = x%10
```
Hint 2: use the digit as an index for a list of strings.

## Version 2

Handle numbers from 100-999.

## Version 3 (optional)

Convert a number to roman numerals.

## Version 4 (optional)

Convert a time given in hours and minutes to a phrase.
'''