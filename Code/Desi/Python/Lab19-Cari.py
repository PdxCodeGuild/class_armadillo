import re
import math
import requests  

def ari():

    book = requests.get('http://www.gutenberg.org/cache/epub/23540/pg23540.txt')

    text = book.text
    character = chars(text)
    words = word(text)
    sentences = sentence(text)
    

    ari = 4.71 * (character/words) + 0.5 * (words/sentences) -21.43
    rounded = math.ceil(ari)

    # ari = math.ceil(4.71 * (chars/words) + 0.5 * (words/sentences) -21.43)
            

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


    print (f"The ARI score is {rounded}\n which correlates to the {ari_scale[rounded]['grade_level']} level\nwhich is appropriate for ages {ari_scale[rounded]['ages']}.")


def chars(text):
    character = 0
    for chars in text:
        if chars.isalpha():
            character +=1
    
    return character



punctuation = r',@#$%^&&**():;'

def word(text):
    counting = text.lower().split()
    for i in range(len(counting)):
        counting[i] = counting[i].strip(punctuation)
    some = len(counting)
    
    return some

def sentence(text):
    count_sentence = 0
    for char in text:
        if char in [',', '!', '?']:
            count_sentence += 1
    
    return count_sentence

ari()