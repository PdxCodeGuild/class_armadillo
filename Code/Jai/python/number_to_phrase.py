
#ignore these modules idk what does what yet 
import math 
import string 
import numbers


#first thing i know is that i want the user to give me a number
user_num = int(input("give me a number to convert: "))
print(f"you want to convert the number {user_num}")

#next thing is the code that he gave us to get the tens and ones 
tens_digit = int(user_num)//10
ones_digit = int(user_num)%10
print(tens_digit)
print(ones_digit)

#after that i have to get those two numbers in a list..that was what i was asking how to do..
user_num = list(str(user_num))
print(user_num)


ones_digit = user_num[]
print(ones_digit)

#so now this is the dictionary for all of the phrases that we gonna covert. (i tried to make it accurate but im not sure if i had to be precise as to say 20: twenty so play around with that)

#this is the tens dictionary
tens_digit_dic = {{1: 'one', 
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
11: 'eleven', 
12: 'twelve',
13: 'thir',
14: 'four',
15: 'fif',
16: 'sixty',
17: 'seventy',
18: 'eighty',
19: 'nine',
20: 'twenty',
30: 'thirty',
40: 'forty',
50: 'fifty',
60: 'sixty',
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

a = user_num
if user_num == tens_digit():
    print(ten_digit[a])