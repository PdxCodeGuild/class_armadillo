# Lab 19 Compute ARI
# Troy Fitzgerald

'''Compute the ARI for a given body of text loaded in from a 
file. The automated readability index (ARI) is a formula for 
computing the U.S. grade level for a given block of text. The 
general formula to compute the ARI is as follows:
ARI Formula
The score is computed by multiplying the number of characters 
divided by the number of words by 4.71, adding the number of 
words divided by the number of sentences multiplied by 0.5, and 
subtracting 21.43. If the result is a decimal, always round up. 
Scores greater than 14 should be presented as having the same age 
and grade level as scores of 14.
Scores correspond to the following ages and grade levels:
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
Once you’ve computed the ARI score, you can use the following 
dictionary to look up the age range and grade level.
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
    }'''

import requests
import re

def compute_ari():

    '''body of text loaded in from a file'''

    find_a_book = requests.get('http://www.gutenberg.org/cache/epub/36830/pg36830.txt')

    words = find_a_book.text.lower().split()

    punctuation = r',@#$%^&*():;'

    for i in range(len(words)):
        words[i] = words[i].strip(punctuation)
    return words

#'''ARI Formula'''
# ari = 4.71 * (characters/words) + 0.5 * (words/sentence) -21.43

def word_count(words):
    num_of_words = 0
    for word in words:
        num_of_words += 1 
    return num_of_words
print(word_count(compute_ari()))


def char_count(eaches):
    num_of_chars = 0
    for word in eaches:
        for char in word:
            num_of_chars += 1 
    return num_of_chars
print(char_count(compute_ari()))




def sentence_count(lines):
    lines = 0
    for line in lines:
        

      return len(sentences)


compute_ari()