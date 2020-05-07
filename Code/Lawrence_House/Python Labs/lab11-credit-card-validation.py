# Convert the input string into a list of ints.

#Slice off the last digit. that is the check digit
cc_digits = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5] 
check_digit = cc_digits.pop(-1)


# Reverse the digits
cc_digits.reverse()

# Double every other element in the reversed list.

for i in range(0,len(cc_digits),2):
    cc_digits[i] *= 2

# Subtract nine from numbers over 9

for i in range(0,len(cc_digits),):
    if cc_digits[i] > 9:
        cc_digits[i] -= 9

  
# Sum all values

cc_digits = sum(cc_digits)

# Take the second digit of that sum.

last_check = cc_digits % 10

# if that matches the check digit, the whole card number is valid

if check_digit == last_check:
    print('valid')
else:
    print('invalid')