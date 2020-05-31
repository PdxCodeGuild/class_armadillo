import requests 
import re
import string

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

book = requests.get('http://www.gutenberg.org/files/46/46-0.txt')
book = book.text.lower()
string_list = book.split()

def word_count():    
    punctuation = '0123456789.,;!&%$?"()[]#*/'
    for i in range(len(string_list)):
       string_list[i] = string_list[i].strip(punctuation)
    number_of_words = len(string_list)
    return number_of_words

def sentences_count():
    list_of_sentences = book.split('.')
    number_of_sentences = len(list_of_sentences)
    return number_of_sentences

def letter_count():
    list_string = ''.join([str(item) for item in string_list ])
    number_of_letters = len(list_string)
    return number_of_letters

def find_score(number_of_chars, number_of_sentence, number_of_words):
    score = round((number_of_letters / number_of_words) * 4.71 + (number_of_words / number_of_sentences) *.5 - 21.41)
    return score

number_of_words = word_count()
number_of_letters = letter_count()
number_of_sentences = sentences_count()
score = find_score(number_of_letters, number_of_sentences, number_of_words)

print(f"The ARI for the book A Christmas Carol, by Charles Dickensis is {score}.\nThis corresponds to a {ari_scale[score]['grade_level']} level of difficulty or is suitable for the average person {ari_scale[score]['ages']} years old.")

