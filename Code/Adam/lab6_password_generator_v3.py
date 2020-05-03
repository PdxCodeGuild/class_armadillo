"""
Lab 6: Password Generator =====================================================

Let's generate a password of length n using a while loop and random.choice, 
this will be a string of random characters, e.g. a62xB95. Hint: random.choice 
can be used to pick a character out of a string, as well as an element out of 
a list.

Version 3 (optional)
Ask the user for how many lowercase letters, uppercase letters, numbers, and 
special characters they'd like in their password. You do not want the pieces 
in order (e.g. 3 lowercase letters followed by 3 uppercase letters...). You 
can use list(password_string) or password_string.split('') to convert the 
string to a list, random.shuffle(password_list) to shuffle it, and then 
''.join(password_list) to turn it back into a string.

"""
import string
import random


# have the user specify the number of: lowercase letters, uppercase letters, numbers, and special characters 
# keeping the list seperate will make it easier to specify how many we want
lower_case = list(string.ascii_lowercase)
random.shuffle(lower_case) # shuffling the lists instead of choosing a random item from it later.
# print(lower_case)

upper_case = list(string.ascii_uppercase)
random.shuffle(upper_case)
# print(upper_case)

numbers = list(string.digits)
random.shuffle(numbers)
# print(numbers)


spec_chars = list(string.punctuation)
random.shuffle(spec_chars)
# print(spec_chars)



num_lower = input('How many lowercase letters would you like in your password? ') # user inputs an amount
num_lower = int(num_lower) # converts that amount to an int
random_lower =[]
i = 0 
for i in range(num_lower): # repeat the loop num_lower times
    random_lower.append(lower_case.pop(i)) # on each loop append rand_lower with a char from lower_case; remove it from lower_case with pop()
    i += 1 
print(random_lower) # testing


num_upper = input('How many uppercase letters would you like in your password? ')
num_upper = int(num_upper)
random_upper = []
i = 0 
for i in range(num_upper):
    random_upper.append(upper_case.pop(i))
    i += 1
print(random_upper) # testing


num_nums = input('How many numbers would you like in your password? ')
num_nums = int(num_nums)
random_nums = []
i = 0 
for i in range(num_nums):
    random_nums.append(numbers.pop(i))
    i += 1
print(random_nums) # testing


num_spec = input('How many special characters would you like in your password? ')
num_spec = int(num_spec)
random_spec = []
i = 0 
for i in range(num_spec):
    random_spec.append(spec_chars.pop(i))
    i += 1
print(random_spec) # testing


# combine our list of random letters
random_master = random_lower + random_upper + random_nums + random_spec
# print(random_master)
random.shuffle(random_master)
# print(random_master)
password = ''.join(random_master)
print(password)


# testing
# print(random_lower)
# print(random_upper)
# print(random_nums)
# print(random_spec)
# print(random_master)
# print(password)

