import string
import requests
import math

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
response = requests.get('http://www.gutenberg.org/cache/epub/28437/pg28437.txt')
text = response.text
text = text.lower()
text_strings = text.split()
#print(text_strings)
#print(text)

#clean_text = text.split(punctuation)
#print(clean_text)
def word_count():
    punctuation = '0123456789.,;!&%$?"()[]#*\/'
    for i in range (len(text_strings)):
        text_strings[i] = text_strings[i].strip(punctuation)
        words_num = len(text_strings)
        return words_num

def num_of_sentences():
    sentence_list = text.split('.')
    num_of_sentences = len(sentence_list)
    return num_of_sentences

def char_count():
    string_list = ''.join([str(i) for i in text_strings ])
    char_num = len(string_list)
    return char_num


    
  
  

words = word_count()
characters = char_count()
sentences = num_of_sentences()
score = 4.71*(characters/words) + 0.5*(words/sentences) - 21.43
print(score)
score = math.ceil(score) 
if score < 1:
    score = 1
elif score > 14:
    score = 14



print(f'The Ari for the gettysburg adress is {score}')
print(f'this corresponds to ages {ari_scale[score]["ages"]}')
print(f'this corresponds to {ari_scale[score]["grade_level"]} level')
