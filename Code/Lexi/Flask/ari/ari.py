

import re
import string
import requests
import math


def count_sentences(text):
    text = text.lower()


    abbreviations = ['st.', 'mr.', 'ms.', 'mrs.', 'rev.', 'dr.', 'a.d.', 'b.c.', 'jr.', 'sr.', 'b.c.e.', 'c.e.', 'phd.']
    for abbreviation in abbreviations:
        text = text.replace(abbreviation, abbreviation.replace('.', ''))

    return text.count('.') + text.count('?') + text.count('!')




def count_words(text):
    results = re.findall(r"[\w']+", text)
    return len(results)


def count_characters(text):
    counter = 0
    for char in text:
        if char in string.ascii_letters:
            counter += 1
    return counter




response = requests.get('http://www.gutenberg.org/cache/epub/61995/pg61995.txt')
text = response.text

sentences = count_sentences(text)
words = count_words(text)
characters = count_characters(text)

print(f'{sentences=}')
print(f'{words=}')
print(f'{characters=}')

ari = 4.71*(characters/words) + 0.5*(words/sentences) - 21.43
print(ari)
ari = round(ari) # round to the nearest whole 
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

print(f'The ARI for the given text is {ari}, which corresponds to ages {ari_scale[ari]["ages"]} which is {ari_scale[ari]["grade_level"]}')
