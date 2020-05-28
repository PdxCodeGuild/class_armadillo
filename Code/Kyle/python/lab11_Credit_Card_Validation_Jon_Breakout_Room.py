# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
cc_digits = [5,6,1,0,5,9,1,0,8,1,0,1,8,2,5,0] # 16 Credit card digits.
check_digit = cc_digits.pop(-1) # Popping off last digit, and saving it to a variable.
print(f'Check digit is: {check_digit}')
# Reverse the digits.
cc_digits.reverse() # .reverse() is a list method, that reverse every element in the list
# Double every other element in the reversed list.
#  5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
#  10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
for i in range(0,len(cc_digits),2): # range(start,stop,step)
    # looping with range to get the index number, then passing the index number to the list, to get specific element in list.
    cc_digits[i] *= 2 # getting element from list with index(i), and multiplying by 2
# Subtract nine from numbers over nine.
for i in range(0,len(cc_digits),): # range(start,stop,step)
    if cc_digits[i] > 9: # checking if element is greater than 9
        cc_digits[i] -= 9 
# Sum all values.
cc_digits = sum(cc_digits) # adding elements in the list together with sum() method
# Take the second digit of that sum.
last_check = cc_digits % 10 # using modulas to find the second digit (85)
# If that matches the check digit, the whole card number is valid.
if check_digit == last_check: # boolean check (true or false)
    print('Valid')
else:
    print('Invalid')
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!