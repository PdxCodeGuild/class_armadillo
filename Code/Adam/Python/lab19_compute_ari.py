"""
# Lab 19: Compute Automated Readability Index

Compute the ARI for a given body of text loaded in from a file. The automated 
readability index (ARI) is a formula for computing the U.S. grade level for a 
given block of text. The general formula to compute the ARI is as follows:

4.71(characters/words) + 0.5 (words/sentences) -21.43

If the result is a decimal, always round up. Scores greater than 14 should be
presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:

```
    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College
```

Once you’ve computed the ARI score, you can use the dictionary ari_scale to 
look up the age range and grade level.


The output should look something like the following:
```
--------------------------------------------------------
The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.
--------------------------------------------------------
```

"""


import requests
import string
import math


def count_chars(text):
    counter =0
    # iterate over the text
    for char in text:
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # increment a counter if char is in letters
        if char in letters:
            counter += 1
    return counter


# remove punctuation and split text to a list
def count_words(text):
    # delare a dictionary containing a translation table that maps each 
    # character in the intabstring into the character at the same position 
    # in the outtab string. Then this table is passed to the translate() function.
    translator = str.maketrans('', '', string.punctuation) 
    no_punc_text = text.translate(translator) 
    word_list = no_punc_text.lower().split()
    return len(word_list) # return the length of the list


# remove periods from abbreviations so that the remaining periods mark the end of a sentence
def count_sentences(text):
    # make text lower case so abbreviations appear as they do in abbreviations list
    text = text.lower() 
    abbreviation = ['dr.', 'phd.', 'mrs.', 'ms.', 'mr.', 'b.c.', 'b.c.e.', 'a.d.', 'jr.', 'sr.', 'rev.', 'st.']
    for abbrev in abbreviation:
        # Replace the periods in abbreviations with empty string 
        # and the abbrevations with the modified abbreviations
        text = text.replace(abbrev, abbrev.replace('.', ''))
        text = text.replace('?', '.')
        text = text.replace('!', '.')
    return text.count('.')


# load ebook from project gutenberg
response = requests.get('https://www.gutenberg.org/files/215/215-0.txt')
# declare variable and assign it a string contain the loaded book
text = response.text


ebook_start = text.find('***')
# print(ebook_start)
ebook_end = text.rfind('***')
# print(ebook_end)
# slice out non book text
text = text[ebook_start:ebook_end]
# print(text)

# replace errors in text with correct char
text = text.replace('â\x80\x99', '\'')
text = text.replace('â\x80\x94', ' ')
text = text.replace('â\x80\x9d', '')
text = text.replace('â\x80\x9c', '')
text = text.replace('å\x93', 'e')
text = text.replace('\'s', '')

# delcare variables to compute the ARI
chars = count_chars(text)
words = count_words(text)
sentences = count_sentences(text)
# print(chars)
# print(words)
# print(sentences)


# compute the ARI
ari = 4.71*(chars/words) + 0.5*(words/sentences) - 21.43
# round the ARI to 2 decimal points
ari = round(ari, 2)

# if the ARI is lower thank 1 its kindergarden
# if ARI is higher than 14 its college
if ari < 1:
    ari = 1
elif ari > 14:
    ari = 14


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


# use ari to select the correspong dictionary and the value of grade level
# inert them into an f string
print('---------------------------------------------------------')
print(f'The ARI for this book is {ari}.')
print(f'This corresponds to a {ari_scale[ari]["grade_level"]} level of difficulty')
print(f'that is suitable for an average person {ari_scale[ari]["ages"]} years old.')
print('---------------------------------------------------------')