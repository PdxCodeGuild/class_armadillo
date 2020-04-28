#   Lab 18 Version 1
#   Kyle Harasimowicz


import string
not_a_letter = "`~-!@#$%^&*()_+=?:;,.\"”[]}{â€1234567890™"
dict_words = {}

# import the text to be evaluated
import requests
response  = requests.get('https://www.gutenberg.org/files/215/215-0.txt')
text = response.text
#text = paragraph

# Clean text to remove all admin information
text = text[text.find("Chapter I. Into the Primitive"):text.find("End of the Project Gutenberg EBook")]

# Clean text to remove UTC Codes, extranious punctuation.
text = text.replace('â€™', '\'').replace('\x80\x99', '\'').replace('\x80\x9d', '\'').replace('\x80\x9c', '\'')#.replace('-', ' ')
for letter in not_a_letter:
    text = text.replace(letter, '')
text = text.replace('  ', ' ').replace('   ', ' ')
text = text.lower().split()

# take text and return a list of all the words.
def list_of_words(text):
    word_list = []
    words = text
    for word in words:
        word_list.append(word)
    return word_list

words = list_of_words(text)
#print(words)

# list of the most commonly used articles, prepositions, 'being' verb conjugations, and conjuntions
common_words = ['the', 'and', 'be', 'of', 'was', 'to', 'a', 'his', 'in', 'it', 'the', 'and', 'of', 'he', 'was', 'to', 'a', 'his', 'in', 'it', 'that', 'with', 'him', 'they', 'had', 'as', 'for', 'on', 'were', 'at', 'but', 'not', "\x80\x99s", 'by', 'them', 'from', '\x80\x9d', 'out', 'into', 'this', 'an', 'their']

# generate a list of words and their frequency
for count in words:
    if count not in dict_words:
        dict_words[count] = 0
    # Set to 1: the common articles, prepositions, 'being' verbs, and conjuntions
    # attempting to get a better 'sense' of the unique words used in this book
    elif count in dict_words and count in common_words:
        dict_words[count] = 1
    else:
        dict_words[count] += 1

result = list(dict_words.items())
#print(result)

# sort the tuples into top 10
result.sort(key=lambda tup: tup[1], reverse=True) 
for i in range(min(30, len(result))):
    print(result[i])
