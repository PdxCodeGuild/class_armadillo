import requests
import re
import math

book = 'https://www.gutenberg.org/files/140/140-0.txt' # book selection

# get the text from the file, via "with open..." or using requests
response = requests.get(book) # makes request to a web page using the book's URL in book variable 
text = response.text # returns the text variable (content of the response, in unicode)

# junk removal from text file, so that non-literary material (top/bottom text) is not included in ARI calculation
text = text[text.find('***') + 3:] # slices text up to first '***' in the text, then adds 3 indices to include those '***' in the slice (top junk)
text = text[text.find('***') + 3:] # slices the few words that are before the second '***' in text, adds the 3 indices for second '***' (top junk)
text = text[:text.find('***')] # slices everything after the third '***', which is bottom junk
    
# punctuation removal (except ' ? . ( ) , ! " : ; ) 
for char in '#$%&*+-/<=>@[\\]^_`{|}~': # iterates through each punct character to remove that punctuation from text
    text = text.replace(char, "") # when a character in punct variable is in text, it replaces it with ""(removal)

characters = len(text.replace(' ', '')) # replaces spaces in text string with '' to create long string of only characters and counts characters

words = len(text.split()) # splits text string into list of words by white space delimiter (default) and counts words

sentences = len(re.split(r'(?<=[^A-Z].[.?!]) +(?=[A-Z])', text)) # regex (regular expression) to break text string into list of sentences and counts sentences

ari = math.ceil(4.71*(characters/words) + 0.5*(words/sentences) - 21.43) # rounds up ARI to integer
if ari > 14: # makes ARI max of 14
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

print(f'''\nThe ARI for {book} is {ari}.
\nThis corresponds to \'{ari_scale[ari]['grade_level']}\' level of difficulty 
that is suitable for an average person {ari_scale[ari]['ages']} years old.\n''')




'''
Lab 19: Compute Automated Readability Index (4/28/20) 11.25.38, 11.27.19

Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

![ARI Formula](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/878d1640d23781351133cad73bdf27bdf8bfe2fd)

The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. **If the result is a decimal, always round up.** Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:

```
    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College
```

Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

```python
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
```

The output should look something like the following:
```
--------------------------------------------------------
The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.
--------------------------------------------------------
```
'''