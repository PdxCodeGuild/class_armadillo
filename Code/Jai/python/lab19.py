import string
import requests
import re
import math


response = requests.get('http://www.gutenberg.org/cache/epub/28437/pg28437.txt')
txt = response.text


def word(text):
    
    txt = text.lower()
    split_words = ("([\w][\w']*\w)")
    words = re.findall(split_words, text)
  
    num_of_words = len(words)
    return num_of_words



num_of_words = word(txt)




def characters(chars):
    return len([char for char in chars if char in string.ascii_letters])  

num_of_chars = characters(txt)




def sentences(text):
    sentence_count = 0

    for character in txt:
       
        if character == '.' or character == '!' or character == '?':
            sentence_count += 1
           
    return sentence_count

num_of_sentences = sentences(txt)


ari = 4.71*(num_of_chars/num_of_words)+0.5*(num_of_words/num_of_sentences)-21.43

ari = math.ceil(ari)


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

print(f'''The ARI for gettysburg-address.txt is {ari} 
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty 
that is suitable for an average person {ari_scale[ari]['ages']} years old.''')