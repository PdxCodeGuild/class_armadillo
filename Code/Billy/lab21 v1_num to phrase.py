from colorama import Fore
import time

# welcome message
print('''\nWelcome to NUMBER TO PHRASE! 
(Enter 'quit' to exit...)''')

time.sleep(1)

# dictionary for unique integer keys, no math required
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

# dicitionary for tens digit and floor dividing input num
pattern_dict = {
    2 :'twenty',
    3 :'thirty',
    4 :'forty',
    5 :'fifty',
    6 :'sixty',
    7 :'seventy',
    8 :'eighty',
    9 :'ninety',   
}

while True: # loop for selecting unique num, math for pattern number, quit and input validation
    num = input('\nEnter your number (0-99): ').lower().strip() # user input number as string
    if num.isnumeric() == False and num == 'quit': # checks if 'quit' was entered, if so exits program
        time.sleep(0.5)
        print('\nGood bye!\n')
        exit()
    elif num.isnumeric() == False or int(num)<0 or int(num)>99: # if words other than 'quit' entered or number not 0-99
        print(Fore.RED + '\nINVALID ENTRY!\n' + Fore.RESET) # prints invalid message and returns to top of loop
        continue 
    else: # when valid string is entered (a number 0-99)
        num = int(num) # converts string to integer
        if num < 20: # if num < 20, prints output directly from unique dictionary, returns to top of loop
            print('Your number phrase is: ' + Fore.MAGENTA + f'{unique_dict[num]}' + Fore.RESET)
        elif num%10 != 0: # if num is not even tens (=>20), will allow + 'hyphen unique number), returns to top of loop
            print('Your number phrase is: ' + Fore.MAGENTA + f'{pattern_dict[num//10]}-{unique_dict[num%10]}' + Fore.RESET)
        else: # only num%10==0 should remain, even tens (=>20), will take direct from pattern dict, returns to top of loop 
            print('Your number phrase is: ' + Fore.MAGENTA + f'{pattern_dict[num//10]}' + Fore.RESET) 





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