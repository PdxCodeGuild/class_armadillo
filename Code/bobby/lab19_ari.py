
import requests
import re
import math




    # Score  Ages     Grade Level
    #  1       5-6    Kindergarten
    #  2       6-7    First Grade
    #  3       7-8    Second Grade
    #  4       8-9    Third Grade
    #  5      9-10    Fourth Grade
    #  6     10-11    Fifth Grade
    #  7     11-12    Sixth Grade
    #  8     12-13    Seventh Grade
    #  9     13-14    Eighth Grade
    # 10     14-15    Ninth Grade
    # 11     15-16    Tenth Grade
    # 12     16-17    Eleventh grade
    # 13     17-18    Twelfth grade
    # 14     18-22    College


# 1.)Requesting the URL
response = requests.get("http://www.gutenberg.org/cache/epub/5200/pg5200.txt")

# Define the text that you want, in this case it is Metamorphosis by Franz Kafka
text = response.text
# print(text)

# 2.) To define a clean list of words within the text
clean_list = text.split("r")
print(clean_list[26 : 2003])

for char in text:
    if char in "1234567890-=!@#$%^&*()_+,./\|":
        text = text.replace(char, " ")
text = text.lower()

lines = text.split("\n")

characters = text.replace(" ", "")
characters = len(characters)



sentence = re.split(r"? <= [^ A - Z], [.?!]) + (? =[A - Z]", text)
sentence = len(sentence)

word_list = text.split()
words = len(words)
#3.) To build a word count dict for the value of a word and count.
count = {}
for word in word_list:
    if word not in count:
        count[word] = 1   
    else:
        count[word] += 1
words = list(count.items())# .items() returns a list of tuples
print(words)



words.sort(key=lambda tup: tup[1], reverse = True)# Sorts largest to smallest, based on count. 
for i in range(min(10, len(words))):# print the top 10 words, or all of them, whichever is smaller
    print(words[i])


ari = math.celi(4,71* ( characters / words) + 0.5* (words / sentence) - 21.43)
if ari > 14:
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

print(f'''\nThe ARI for {response} is {ari}.
\nThis corresponds to \'{ari_scale[ari]['grade_level']}\' level of difficulty 
that is suitable for an average person {ari_scale[ari]['ages']} years old.\n''')