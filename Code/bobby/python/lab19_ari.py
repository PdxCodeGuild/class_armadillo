
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


# This is the ARI (Dictionary) scale that the program pulls from later to make the calculation on what level an eBook is
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


    


# Requesting the URL
response = requests.get("http://www.gutenberg.org/cache/epub/5200/pg5200.txt")

# Define the text that you want, in this case it is Metamorphosis by Franz Kafka
text = response.text
# print(text)

#  defineing a clean list of words within the text
clean_list = text.split("r")
print(clean_list[26 : 2003])

for char in text:
    if char in "1234567890-=!@#$%^&*()_+,./\|":
        text = text.replace(char, " ")
text = text.lower()

# splits the lines of the text into a list
lines = text.split("\n")

# This replaces the the white white space in the text 
characters = text.replace(" ", "")
characters = len(characters)

# This splits the sentences into list
sentence = re.split(r"( ? <= [^ A - Z]), [.?!] + ( ? = [A - Z])", text)
sentence = len(sentence)


# This is where I am buliding and splitting the word list
word_list = text.split()
word_count = len(word_list)
# building a word count dict for the value of a word and count.
count = {}
for words in word_list:
    if word_count not in count:
        count[words] = 1   
    else:
        count[words] += 1
# .items() returns a list of tuples        
words = list(count.items())


# This is the math portiong of the program that calculates the eBook and sorts out what grade level and age catagory the publication is for
ari = math.ceil(((4.71 * ( characters / word_count)) + 0.5 * (word_count / sentence) - 21.43))
if ari > 14:
    ari = 14


# Printing the calculation and showing what which grade level and age cat the eBook is for.
print(f'''\nThe ARI for {response} is {ari}.
\nThis corresponds to \'{ari_scale[ari]['grade_level']}\' level of difficulty 
that is suitable for an average person {ari_scale[ari]['ages']} years old.\n''') # The ARI for <Rsponse [200]> is 14. 
# This corresponds to 'Collage' level of difficulty 
# that is sutable for an average person 18 - 22 yeara old.
