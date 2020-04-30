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
and grade level as scores of 14.'''

# imports module.
import requests
import re
import random
import math


# defines the function.
def compute_ari():

    '''body of text loaded in from a file'''
    # assigns the variable to the object to get the book from the URL.
    find_a_book = requests.get('http://www.gutenberg.org/cache/epub/36830/pg36830.txt')
    # assigns the variables for the below functions.
    text = find_a_book.text
    letters = char_count(text)
    word_1 = word_count(text)
    sentences_1 = sentence_count(text)
    # ARI Formula in 'f' string format.
    ari = f'4.71 * ({letters}/{word_1}) + 0.5 * ({word_1}/{sentences_1}) -21.43'
    # ARI Formula rounding the results up. 
    ari = math.ceil(4.71 * (letters/word_1) + 0.5 * (word_1/sentences_1) -21.43)
    print(ari)
    
    # defines the ARI scale in a dictionary.
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
    # prints the ARI score and pertinent information from the ari_scale dictionary.
    print (f"The ARI score is {ari}\nwhich correlates to the {ari_scale[ari]['grade_level']} level\nwhich is appropriate for ages {ari_scale[ari]['ages']}.")


# defines the function for counting the sentences.
def sentence_count(text):
    num_of_sentences = 0
    for char in text:
        if char in ['.', '!', '?']:
            num_of_sentences += 1
    return num_of_sentences
      

# defines punctuation.
punctuation = r',@#$%^&*():;'

# defines the function to count the words.
def word_count(text):
    words = text.lower().split()
    for i in range(len(words)):
        words[i] = words[i].strip(punctuation)
    num_of_words = len(words)
    return num_of_words

# defines the functions to count the characters.
def char_count(text):
    num_of_chars = 0
    for char in text:
        if char.isalpha():
            num_of_chars += 1 
    return num_of_chars

# calls the function.
compute_ari()
