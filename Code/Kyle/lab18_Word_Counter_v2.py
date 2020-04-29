# Lab 18 Word Counter Version 2
# Kyle Harasimowicz

import requests
import string
not_a_letter = "`~!@#$%^&*()_+=?:;,\"”[]}{â€1234567890\™"

# import the text to be evaluated

response  = requests.get('https://www.gutenberg.org/files/215/215-0.txt')
text = response.text
#text = paragraph

# Clean text to remove all admin information
text = text[text.find("Chapter I. Into the Primitive"):text.find("End of the Project Gutenberg EBook")]

# Clean text to remove UTC Codes, extranious punctuation.
text = text.replace('â€™', '\'').replace('â€', '\"')
for letter in not_a_letter:
    text = text.replace(letter, '')
text = text.replace('  ', ' ').replace('   ', ' ').replace('\\', '')
text = text.replace("x80x99", '\'').replace('x80x9d', '\'').replace('x80x9c', '\'')#.replace('-', ' ')
text = text.replace('\x80\x99', '\'').replace('\x80\x9d', '\'').replace('\x80\x9c', '\'')
text = text.lower().split()

# take text and return a list of all the words.
def list_of_words(text):
    word_list = []
    # removes all periods. Periods needed for future word pair function.
    text = text.replace('.', '')

    words = text
    for word in words:
        word_list.append(word)
    #print(word_list)
    return word_list

# Take text and return a list of word pairs
def list_of_word_pairs(text):
    #create list to store word pairs
    word_pair_list = []
    # assign the whole text to a new variable
    all_words = text
#   loop i  over range | text length | second to last word
    for word in range(len(all_words)-1):
#     loop text of first word + " " + text of first word + one after
        if all_words[word] + " " + all_words[word + 1] not in word_pair_list:
            word_pair_list.append(all_words[word] + " " + all_words[word + 1])
    return word_pair_list
    print(word_pair_list)


word_pairs = list_of_word_pairs(text)
# print(word_pairs)

dict_words = {}

# generate a list of words and their frequency
for count in word_pairs:
    if count not in dict_words:
        dict_words[count] = 0
    else:
        dict_words[count] += 1

result = list(dict_words.items())
print(result)

# sort the tuples into top 30
result.sort(key=lambda tup: tup[1], reverse=True) 
for i in range(min(30, len(result))):
    print(result[i])