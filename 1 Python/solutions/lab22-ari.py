

import math
import re
import string


def count_characters(text):
    count = 0
    for char in text:
        if char.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
            count += 1
    return count

    # return len(re.findall('\w', text))


def count_words(text):
    # text = text.replace('—', ' ')
    # text = text.replace('-', ' ')
    # print(text.split())
    # return len(text.split())

    return len(re.findall('[\w’]+', text))

def count_sentences(text):
    count = 0
    for char in text:
        if char in '.!?':
            count += 1
    return count

    #return len(re.findall('[\.?!]+', text))



file_name = 'white_horse.txt'

with open('white_horse.txt', 'r', encoding='utf-8') as f:
    text = f.read()


n_characters = count_characters(text)
n_words = count_words(text)
n_sentences = count_sentences(text)

print(n_characters)
print(n_words)
print(n_sentences)

# regex
# 368059
# 87671
# 6146

# non-regex
# 367991
# 87653
# 6146


ari = 4.71*(n_characters/n_words) + 0.5*(n_words/n_sentences)-21.43
ari = int(ari + 0.5)
if ari > 14:
    ari = 14

ari_scale = {
    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages': '6-7', 'grade_level': '1st Grade'},
    3: {'ages': '7-8', 'grade_level': '2nd Grade'},
    4: {'ages': '8-9', 'grade_level': '3rd Grade'},
    5: {'ages': '9-10', 'grade_level': '4th Grade'},
    6: {'ages': '10-11', 'grade_level': '5th Grade'},
    7: {'ages': '11-12', 'grade_level': '6th Grade'},
    8: {'ages': '12-13', 'grade_level': '7th Grade'},
    9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}

grade_level = ari_scale[ari]

output = '-'*80 + '\n'
output += 'The ARI for ' + file_name + ' is ' + str(ari) + '\n'
output += 'This corresponds to a ' + grade_level['grade_level'] + ' level of difficulty\n'
output += 'that is suitable for an average person ' + grade_level['ages'] + ' years old\n'
output += '-'*80
print(output)



