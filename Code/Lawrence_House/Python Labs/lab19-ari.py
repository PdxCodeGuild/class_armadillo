import string
import re
import math


filename = 'Code\Lawrence_House\metamorp.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# 

regex = r'([A-Z][^\.!?]*[\.!?])'
sentence_list = re.findall(regex, text)
sentences = len(sentence_list)

words = text.split()

punc_table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(punc_table) for w in words]
words = [word.lower() for word in stripped]

def char_count(word):
    number_of_chars = 0
    for word in words:
        for char in word:
            number_of_chars += 1
    return number_of_chars

characters = char_count(words)

words = len(words)




# def letter_count
# if char in ascii.lower 

# print(word_count(100))

# characters = ()

ari = 4.71*(characters/words) + 0.5*(words/sentences) - 21.43
ari = round(ari)
print(ari)


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



print(f"The ARI for the given text is {ari}, which corresponds to ages {ari_scale[ari]['ages']} which is {ari_scale[ari]['grade_level']}")