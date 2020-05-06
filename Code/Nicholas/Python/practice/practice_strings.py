
# Practice: Strings



# ```python
# def add(a, b):
#     return a + b
# #print(add(5, 2))
# #print(add(8, 1))
# ```


## Problem 1

# Get a string from the user, print out another string, doubling every letter.

# def double_letters(word):
#     doubled_word = ''  # create empty string for new doubled word
#     for letter in word:  #iterate over letters in the word
#         letter *= 2  #multiply each letter by 2
#         doubled_word += letter  #add each doubled letter to new word
#     return doubled_word  #return new doubled word    
      
     
# print(double_letters('hello')) # hheelllloo


## Problem 2

# Write a function that takes a string, and returns a list of strings, each missing a different character.


# def missing_char(word):
#     word_list = []  #create empty list for new strings
#     for index in range(1, len(word)+1):  #loop through each letter in word
#         left_part = word[0:index - 1]  #split word into two separate parts
#         right_part = word[index:len(word)]  

#         new_word = left_part+right_part  #add two parts together
#         word_list.append(new_word)  #add new word to list

#     return word_list    

# print(missing_char('kitten')) # ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']


## Problem 3
# Return the letter that appears the latest in the english alphabet.

# def latest_letter(word):
#     return sorted(word)[-1]
    
# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v


# ## Problem 4

# Write a function that returns the number of occurances of 'hi' in a given string.


def count_hi(text):
  word = 'hi'
  for word in text:
      word.count(hi)
print(count_hi('hihi')) # 2


# ## Problem 5

# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

# ```python
# def cat_dog(text):
#   ...
# print(cat_dog('catdog')) # True
# print(cat_dog('catcat')) # False
# print(cat_dog('catdogcatdog')) # True
# ```

# ## Problem 6

# Return the number of letter occurances in a string.
# ```python
# def count_letter(letter, word):
#     ...
# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2
# ```

# ## Problem 7

# Convert input strings to lowercase without any surrounding whitespace.

# ```python
# def lower_case(text):
#   ...
# print(lower_case("SUPER!")) # 'super!'
# print(lower_case("        NANNANANANA BATMAN        ")) # 'nannananana batman'