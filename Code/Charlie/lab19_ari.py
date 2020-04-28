
# Lab 19: Compute Automated Readability Index

# Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

# ARI Formula  4.71(characters/words)+.05(words/sentences)-21.43

# The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

# Scores correspond to the following ages and grad levels:

import requests
import re
import string
# book = '''MARLEY was dead: to begin with. There is no doubt
# whatever about that. The register of his burial was
# signed by the clergyman, the clerk, the undertaker,
#  and the chief mourner. Scrooge signed it: and
#  Scrooge's name was good upon 'Change, for anything he
#  chose to put his hand to. Old Marley was as dead as a
#  door-nail.

#  Mind! I don't mean to say that I know, of my
#  own knowledge, what there is particularly dead about
#  a door-nail. I might have been inclined, myself, to
#  regard a coffin-nail as the deadest piece of ironmongery
#  in the trade. But the wisdom of our ancestors
#  is in the simile; and my unhallowed hands
#  shall not disturb it, or the Country's done for. You
#  will therefore permit me to repeat, emphatically, that
#  Marley was as dead as a door-nail.

#  Scrooge knew he was dead? Of course he did.
#  How could it be otherwise? Scrooge and he were
#  partners for I don't know how many years. Scrooge
#  was his sole executor, his sole administrator, his sole
#  assign, his sole residuary legatee, his sole friend, and
#  sole mourner. And even Scrooge was not so dreadfully
#  cut up by the sad event, but that he was an excellent
#  man of business on the very day of the funeral,'''




book = "hello guys how are you"

book = book.lower()

list = book.split()

word_count = len(list)

num_letters_in_word = []
for i in range(len(card)):
         card[i] = int(card[i])

for i in range(word_count):
    list = num_letters_in_word.append(i)


# return word_count
print(num_letters_in_word)
print(word_count)






# Score  Ages     Grade Level
#     1       5-6    Kindergarten
#     2       6-7    First Grade
#     3       7-8    Second Grade
#     4       8-9    Third Grade
#     5      9-10    Fourth Grade
#     6     10-11    Fifth Grade
#     7     11-12    Sixth Grade
#     8     12-13    Seventh Grade
#     9     13-14    Eighth Grade
#     10     14-15    Ninth Grade
#     11     15-16    Tenth Grade
#     12     16-17    Eleventh grade
#     13     17-18    Twelfth grade
#     14     18-22    College





# ari_scale = {
#      1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
#      2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
#      3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
#      4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
#      5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
#      6: {'ages': '10-11', 'grade_level':    '5th Grade'},
#      7: {'ages': '11-12', 'grade_level':    '6th Grade'},
#      8: {'ages': '12-13', 'grade_level':    '7th Grade'},
#      9: {'ages': '13-14', 'grade_level':    '8th Grade'},
#     10: {'ages': '14-15', 'grade_level':    '9th Grade'},
#     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
#     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
#     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
#     14: {'ages': '18-22', 'grade_level':      'College'}
# }