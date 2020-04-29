

import requests

# 1) get the text from the file, via "with open..." or using requests

response = requests.get('https://www.gutenberg.org/files/50828/50828-0.txt')
text = response.text
# print(text) <--this prints out the WHOLE book

# 2) remove spaces btw words and only select 600 lines

text = text.split()
lines = text[200:800]
print(lines)

# Your dictionary will have words as keys and counts
#  as values. If a word isn't in your dictionary yet, 
# add it with a count of 1. If it is, increment its count.

# new_dict = {}
# words = list(new_dict.items()) # .items() returns keys and values


# find and replace odd characters with blank string
def text_clean(text):
    for character in text:
        if character in (";", ".", "!", "?", "!", ",",
                         ":", "'", "-", "â", "(", ")"):
            text = text.replace(character, "")
    return text

#take our text in and return a list of word
def word_count(text):
  # we need to call clean text function
  text = text_clean(text)
  # create an empty list
  word_list = []
  # lowercase and take out white space
  words = text.lower().split()
  # iterate over words, add to list
  for word in words: 
    word_list.append(word)
  return len(word_list)


# count characters
def character_count(text):
  #call 1st function
  text = text_clean(text)
  # empty purse
  characters = 0
  # make a for loop per word
  # isalpha() does not take any parameters
# 1.True- If all characters in the string are alphabet.
# 2.False- If the string contains 1 or more non-alphabets.
  for character in text:
    if character.isalpha():
      # increment up one
      characters += 1
      # return needed in for loop
  return (characters)

# Use regex to identify sentences
def sentences(text):
  sentence_syntax = (r'('