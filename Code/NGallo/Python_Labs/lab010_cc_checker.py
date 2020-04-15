# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
cc_digits = [5,6,1,0,5,9,1,0,8,1,0,1,8,2,5,0]
check_digit = cc_digits.pop(-1)
print(f'Check digit is: {check_digit}')
# Reverse the digits.
cc_digits.reverse()
# Double every other element in the reversed list.
#  5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
#  10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
for i in range(0,len(cc_digits),2):
    cc_digits[i] *= 2
# Subtract nine from numbers over nine.
for i in range(0,len(cc_digits),):
    if cc_digits[i] > 9:
        cc_digits[i] -= 9
# Sum all values.
cc_digits = sum(cc_digits)
# Take the second digit of that sum.
last_check = cc_digits % 10
# If that matches the check digit, the whole card number is valid.
if check_digit == last_check:
    print('Valid')
else:
    print('Invalid')