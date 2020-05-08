
# import requests library to get http requests

import requests
#import regular expression library to use regex syntax
import re


# referred to:
# https://regex101.com/r/nRy8cd/1
# https://docs.python.org/3.6/howto/regex.html#regex-howto
# https://docs.python.org/3.6/library/re.html#re-syntax
# https://www.w3schools.com/python/ref_string_split.asp
# https://github.com/PdxCodeGuild/class_armadillo/blob/master/0%20General/05%20-%20Regular%20Expressions.md
# https://github.com/PdxCodeGuild/class_armadillo/blob/master/Code/Matthew/demos/demo_regex2.py
# https://github.com/PdxCodeGuild/class_armadillo/blob/master/Code/Talieson/Lab19-compute_ari.py
# watched youtube video to figure regex
# https://www.youtube.com/watch?v=UQQsYXa1EHs

def book():
response = requests.get("http://www.gutenberg.org/files/120/120-0.txt")
text = response.text
text = text.split('\n')
lines = text[100:130]
print(lines)

# replace all characters with an empty string
def replace_text(text):
    # searching for characters in text
    for character in text:
        # if character is --- below--- replace with ""
        if character in (";", ".", "!", "?", "!", ",",
                         ":", "'", "-", "â", "(", ")"):
            text = text.replace(character, "")
    return text

# list of words
def word_count(text):
  # cleanup text
  text = text_clean(text)
 # empty list
  word_list = []
  # make all the words in the list lowercase and remove spaces
  # The split() method splits a string into a list. You can
  #  specify the separator, default separator is any whitespace.
  words = text.lower().split()
  # for loop to add words to a list
  for word in words:
      word_list.append(word)
  return len(word_list)


# count the characters in the text
def wordz(text):
    # call our cleaning function
    text = text_clean(text)
    characters = 0
    # for loop to find wordz
    for character in text:
        # built-in method used for string handling. 
        # The isalpha() methods returns “True” if all 
        # characters in the string are alphabets, Otherwise, 
        # It returns “False”.
        if character.isalpha():
            # count up if the character has letters 
            characters += 1 #return the count
    return characters



# use regex to catch all instances of sentences and return
def sentences(text):
    # regular expression with raw string followed by capture group
    # represented by square brackets, ^ signifies beginning with a 
    # ., ?, ! - this is how we know it's a sentence
    characters = (r"([^\.\?\!]*)")

