#Lab 18: Count Words V2!:
#Version 2
# Count how often each unique pair of words is used, 
# then print the top 10 most common pairs with their counts.

# Installed the following on the terminal: pip3 install requests 
# pip3 only need to be installed once

import requests
import string


# 1) get the text from the file, via "with open..." or using requests

response = requests.get('http://www.gutenberg.org/cache/epub/28437/pg28437.txt')

text = response.text

#text = text[100:len(text)-100]
# print(text)
# for word in text:
#     print(word)
# 2) get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]

text = text.lower()
#system = text.replace(',:,;""''/?}{]}[*%$#@!><_-+=`~.', '')
#system1 = system.strip('\n')
# system1 = system.replace(".", " ")
# print(system)

# translate chars 
str1 = " .,:?;123456789()[]#\@<>$%^&*+-=!/\"'"
str2 = "                                    "
#''/?}{]}[*%$#@!><_-+=`~.',''"'\n\r\'
# print(len(str1))
# print(len(str2))
# replace with 
#maketrans(str1, str2)

table = text.maketrans(str1, str2)
translated = text.translate(table)
# print(translated)

#Returns a translation table to be used in translations
#translate()	#Returns a translated string
# make a string into a list: 

#string.split("delimiter")
def convert(string):
    # list1 = list(string.split(" "))
    list1 = string.split()
    return list1
# str1 = text
#print(convert(translated))

list_of_words = convert(translated)

# junk_start = text.find('***')
# print(junk_start)
# print(text[junk_start:junk_start+100])
# print(text[800:900])

# lines = text.split('\n')
# print(lines[103:110])
# print (text.strip( '*' ))

# 3) build up word_counts, a dictionary where the key is the word and the value is the count

# word_counts = {
#   'the': 10,
#   'a':  4 
#   'hello': 1,
#   'that': 2
# }
# å

# initialize empty dictionary
#new_dict = dict () 
# new_dict = dict()
new_dict = {}

# loop over convert(translated) checking each word convert(translated)

# nested if statements within the forloop that checks whether that word is already in the dictioanry
# If it is, add value += 1
# if the word is not in the dictionary, add word as key, set value to `1`
#tuple unpacking = for i, word in enumerate(list_of_words):

#Version 2
# Count how often each unique pair of words is used, 
# then print the top 10 most common pairs with their counts.

for i, word in enumerate(list_of_words): 
        #print(i,word)
        if i >= len(list_of_words)-1:
            break
            
        next_word = list_of_words[i+1]
        word_plus_one = f'{word} {next_word}' # we are turning it into a string
        # Check if the word is already in dictionary 
        if word_plus_one in new_dict: 
            # Increment count of word by 1 if the word is already in the dictionary
            new_dict[word_plus_one] = new_dict[word_plus_one] + 1
        else: 
            # Add the word_plus_one to dictionary with count 1 if the word_plus_one is not in the dictionary
            new_dict[word_plus_one] = 1
# print(list_of_words[4467])
# print(new_dict) 
#Print the contents of dictionary 
# for key in list(new_dict.keys()): 
#    print(key, ":", new_dict[key]) 

# word_dict is a dictionary where the key is the word and the value is the count
words = list(new_dict.items()) # .items() returns a list of tuples
#print(words)
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

# >>> list = ['a','b','c']
# >>> list
# ['a', 'b', 'c']
# >>> for i, letter in enumerate(list):
# ...     print(i,letter)
# ... 
# 0 a
# 1 b
# 2 c

# list = ['a','b','c']
# list()
# ['a', 'b', 'c']
# for i, letter in enumerate(list):
#     print(i,letter)
