
#ignore these modules idk what does what yet 
import math 
import string 
import numbers
import decimal

#first thing i know is that i want the user to give me a number
user_num = input("give me a number to convert: ")
print(f"you want to convert the number {num}")

#next thing is the code that he gave us to get the tens and ones 
tens_digit = int(user_num)//10
ones_digit = int(user_num)%10
print(tens_digit)
print(ones_digit)

#after that i have to get those two numbers in a list..that was what i was asking how to do..
user_num = list(user_num)
print(user_num)

#so now this is the dictionary for all of the phrases that we gonna covert. (i tried to make it accurate but im not sure if i had to be precise as to say 20: twenty so play around with that)

#this is the tens dictionary
tens_digit_dic = { 1: 'eleven', 
2: 'twelve',
3: 'thir',
4: 'four',
5: 'fif',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'nine',
10: 'twenty',
11: 'thirty',
12: 'forty',
13: 'fifty',
14: 'sixty',
70: 'seventy',
80: 'eighty',
90: 'ninety',
}

#this is the ones dictionary
ones_digit = {1: 'one', 
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
}
#now we have to figure out what kind of loop or statement to use to convert it..

for num in user_num():
    if 