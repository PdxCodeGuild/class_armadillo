import math
import string 
 


 #dictionaries of ones teens and tens digits
ones = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',}

teens = {11: 'eleven',  12: 'twelve', 13: 'thirteen',14: 'fourteen', 15: 'fifteen',
16: 'sixteen',17:'seventeen', 18:'eighteen', 19:'nineteen'}

tens = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

#recieve user input
num = int(input("enter a number to convert: "))

#function to convert numbers to phrase
def num_phrase(nums): 
    if num < 10: #if the input is less than 10 then it will return the value of ones
        return ones[nums]
    elif num <20: #if th input is les than 20 than it will return the value of teens
        return teens[nums]
    elif num < 100: #if the iput is less than 100 then it will do this math
        ones_digit = nums%10 
        tens_digit = nums//10
        return tens[tens_digit] + '-' + ones[ones_digit]

nums = num
phrase = (num_phrase(nums))
print(f'your number is: {phrase}')
     
    






