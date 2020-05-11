import re
from string import ascii_letters
from math import ceil

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

with open('metamorphosis.txt', 'r') as text_file:
    text = text_file.read()

# set the regex pattern for separating by sentence 
# and use re to split the text at that expression
sentence_regex = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
sentences = re.split(sentence_regex, text)

# since word length isn't an issue,
# we can split the text by spaces to get the words
words = text.replace('\n', ' ').split(' ')

# make a list of all characters
# that are letters.
all_chars = []
for char in text:
    if char in ascii_letters:
        all_chars.append(char)

# calculate counts
number_of_sentences = len(sentences)
number_of_words = len(words)
number_of_chars = len(all_chars)

# print(f'{number_of_sentences = }\n{number_of_words = }\n{number_of_chars = }')

# calculate automated readability index
ari = ceil(((4.71 * (number_of_chars / number_of_words)) + (.5 * (number_of_words / number_of_sentences))) - 21.43)

# pull the values out of the dictionary
ages = ari_scale[ari]['ages']
grade_level = ari_scale[ari]['grade_level']

# print results
print(f"The text in question is recommended for ages {ages} or for those with a {grade_level.lower()} reading level.")