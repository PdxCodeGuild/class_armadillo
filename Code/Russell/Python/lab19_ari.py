import requests
import re
import math
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


book = requests.get('https://www.gutenberg.org/cache/epub/375/pg375.txt')

text = book.text

index_stars = text.find('***') 
index_stars = text.find('\n', index_stars) 
text = text[index_stars:]

index_stars = text.rfind('*** END') 
text = text[:index_stars]



text_list = text.split()  
for i in range(len(text_list)):
    text_list[i] = text_list[i].strip('1234567890@#$%^&*()_-;][]:}{\'\",/;:\\|<>')

word_length = []
for element in text_list: # iterates through the list of words and appends the length of each word to a new list 
    word_length.append(len(element))

word_length_average = 4.71 * (sum(word_length) / len(text_list)) 

                     
sentences = re.split('\?|\.|\!', text) # regular expression splits the text into a list of sentences using multiple delimiters.
words = []
for sentence in sentences: # iterates through the list of sentences, splits sentences into words and appends words to a list
    words.append(sentence.split(' '))
    if len(sentence) <= 1:
        sentences.remove(sentence)

word_count = []
for word in words: # iterates through the words list and appends the length of each word to a new list
    word_count.append(len(word))
words_per_sentence = .5 * ((sum(word_count)) / len(sentences))



ari_score = round((words_per_sentence + word_length_average) - 21.43)

print(f"The book is for ages {ari_scale[ari_score]['ages']} or {ari_scale[ari_score]['grade_level']}")





