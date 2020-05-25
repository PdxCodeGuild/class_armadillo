# lab 19

# mistakes - made wrong import
# couldn't open correct, corresponding text file

from re import findall
from math import ceil

# 1) get the text from the file, via "with open..." or using requests

text_path = ('/Users/alex/Desktop/class_armadillo/Code/Lexi/python/canoe.txt')
with open(text_path, 'r') as file:
  text = file.read()

# find and replace odd characters with blank string
def text_clean(text):
    for character in text:
        if character in (";", ".", "!", "?", "!", ",",
                         ":", "'", "-", "â", "(", ")"):
            text = text.replace(character, "")
    return text
print(text)

#FIND OUT HOW MANY WORDS THERE ARE
def word_count(text):
  text = text_clean(text)
  word_list = []
  words = text.lower().split()
  for word in words: 
    word_list.append(word)
  return len(word_list)
print(f'~~this is how many words there are: {word_count(text)}')


# FIND OUT HOW MANY CHARACTERS THERE ARE
def character_count(text):
  text = text_clean(text)
  characters = 0
  for character in text:
    if character.isalpha():
      characters += 1
  return (characters)
print(f' ++ this is how many characters there are: {character_count(text)}')

# Use regex to findall sentences
def sentences(text):
  sentence_syntax = r'([/./!/?]*)'
  sentences = len(findall(sentence_syntax, text))
  return sentences

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

first_step = word_count(text)
second_step = character_count(text)
third_step = sentences(text)

# FORMULA

ari_calc = ceil( (  (second_step / first_step) * 4.71) +
                ((first_step / second_step) * 0.5) - 21.43)

print (f'''

--------------------------------------------------------
The ARI for canoe.txt is {ari_calc}
This corresponds to a(n) {ari_scale[ari_calc]['grade_level']} of difficulty
that is suitable for an average person {ari_scale[ari_calc]['ages']} years old.
--------------------------------------------------------
''')