
#ignore these modules idk what does what yet 
import math 
import string 
import numbers


ones = {
         0: 'zero',
         1: 'one',
         2: 'two',
         3: 'three',
         4: 'four',
         5: 'five',
         6: 'six',
         7: 'seven',
         8: 'eight',
         9: 'nine',
         10: 'ten'
     }
tens = {
         2: 'twenty',
         3: 'thirty',
         4: 'forty',
         5: 'fify',
         6: 'sixty',
         7: 'seventy',
         8: 'eighty',
         9: 'ninety'

     }



user_num = int(input("give me a number to convert: "))
print(f"you want to convert the number {user_num}")


tens_digit = int(user_num)//10
ones_digit = int(user_num)%10
print(tens_digit)
print(ones_digit)


user_num = list(str(user_num))
print(user_num)


ones_digit = user_num
print(ones_digit)

print((tens[tens_digit]) + '-' + (ones[ones_digit]))
