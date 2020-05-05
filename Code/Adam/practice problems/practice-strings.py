"""---------------------------------Practice Strings---------------------------------"""

# # Problem 1
# # Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    return ''.join([i*2 for i in word])
    
# print(double_letters('bubbles'))

# #Problem 5 (not from strings)

def reverse(nums):
    nums.reverse()
    return nums

mylist = [1, 2, 3] 
# print(reverse(mylist))

# # Problem 2
# # Write a function that takes a string, and returns a list of strings, each missing a 
# # different character.

# def missing_char(word): # need to break up the string and populate the list
    strings_list = [] # heres the list
    for char in word: # need a loop that sends each letter at the position of i to stringslist
        strings_list.append(char)
        print(char)
    print(strings_list)
    return word


