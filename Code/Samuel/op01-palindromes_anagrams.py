# PDX Code Guild Fullstack Course
# Optional Lab 1 Palindromes and Anagrams
# Samuel Purdy
# 4/17/2020

import string

# Returns true if both strings given that are turned into sorted lists are equal, false if not.
def is_anagram(str1, str2):
    if sorted(list(str1)) == sorted(list(str2)):
        return True
    return False

# Returns true if the reverse of the string given is equal to the string given, false if not.
def is_palindrome(str1):
    # Reverses the given string and saves it to a test variable.
    test_against = "".join(list(reversed(str1)))
    print(str1)
    print(test_against)
    if test_against == str1:
        return True
    return False

test1 = input("Please enter in a string that you want to test: ")

# Prints a success if the given string is a palindrome, if not, it will print a failure.
if is_palindrome(test1):
    print(f"{test1} is a palindrome!")
else:
    print(f"{test1} is not a palindrome!")

test2 = input(f"Please enter in another string to test against {test1} for an anagram: ")

# Prints a success if the given strings are anagrams, if not, it will print a failure.
if is_anagram(test1, test2):
    print(f"{test1} and {test2} are anagrams!!")
else:
    print(f"{test1} and {test2} are not anagrams!!")