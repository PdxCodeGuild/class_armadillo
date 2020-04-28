#Lab 19: Compute Automated Readability Index:

"""
Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

ARI Formula

The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:

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
Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

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
The output should look something like the following:
--------------------------------------------------------
The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.
"""

import requests
import re

# response = requests.get('http://www.gutenberg.org/cache/epub/28437/pg28437.txt')

# text = response.text

def char_word_sentence():
    response = requests.get('http://www.gutenberg.org/cache/epub/28437/pg28437.txt')
    text = response.text
    text = text.lower()
    split_words = ("([\w][\w']*\w)")
    # split_characters = 0
    # split_sentences = 0 
    words = re.findall(split_words, text)
    # chars = re.findall(split_characters, text)
    # sentences = re.findall(split_sentences, text)

    print(words)
    # print(chars)
    # print(sentences)


#return a list of dictionaries
 
    for i in range(len(words)):
        text1 = []
        text1.append({
        'words': words[i]
        #   'chars': chars[i],
        #    'sentences': sentences[i]
        })
    return text1

char_word_sentence()

# # get random books from project gutenberg
# def get_random_books():
#   response = requests.get('https://www.gutenberg.org/ebooks/search/?sort_order=random')
#   text = response.text
#   links_pattern = r'\/ebooks\/(\d+)'
#   titles_pattern = r'class="title">(.+)<\/span>'
#   links = re.findall(links_pattern, text)
#   titles = re.findall(titles_pattern, text)
#   print(links)
#   # print(titles)

#   # ['/ebooks/3256', '/ebooks/58647'...] -> ['gutenberg.org/ebooks/3256/', ..]
#   # links = ['https://www.gutenberg.org/' + link for link in links]

#   # will not work for book urls like http://www.gutenberg.org/cache/epub/21301/pg21301.txt
#   links = [f'https://www.gutenberg.org/files/{code}/{code}-0.txt' for code in links]
#   titles = titles[3:] # remove the first 3 results
  
#   # zip turns two lists into a list of tuples
#   # the first element of each tuple is from the first list
#   # the second element of each tuple is from the second list
#   # return list(zip(titles, links))

#   # return a list of dictionaries
#   books = []
#   for i in range(len(titles)):
#     books.append({
#       'title': titles[i],
#       'link': links[i]
#     })
#   return books

# regex split into sentences:


# text = """\
# Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.
# """
# sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

# for stuff in sentences:
#         print(stuff) 

#regex split into words:  https://www.geeksforgeeks.org/python-extract-words-from-given-string/

"""
Instead of regex, you can use string-functions:

to_be_removed = ".,:!" # all characters to be removed
s = "John's mom went there, but he wasn't there. So she said: 'Where are you!!'"

for c in to_be_removed:
    s = s.replace(c, '')
s.split()

"""
#regex split into characters:

"""
st="Ladegårdsvej 8B7100 Vejle"
reg=r'([0-9]{4})'
rep=re.split(reg,st)
print rep
"""
#==========================

# initializing string   
text_string = """
Know him?

!@#$%^^&&*&*()_+? Well you might say I practically grew up with him. He was my hero in
those days. I thought few wiser or greater men ever lived. In my eyes he
was greater than Babe Ruth, Lindy, or the President.!!! 

Of course, time, and my growing up caused me to bring him into a
perspective that I felt to be more consonant with his true position in
his field of endeavor. When he died his friends mourned for fond
remembrance of things past, but privately many of them felt that he had
outlived his best days. Now with this glorious vindication, I wonder how
many of them are still alive to feel the twinge of conscience....

Oh, we're delighted of course, but it seems incredible even today to us
elated oldsters. Although we were always his staunchest admirers, in
retrospect we can see now that no one believed more than we that he did
it strictly for the dollar. It is likely there was always a small corps
of starry-eyed adolescents who found the whole improbable saga entirely
believable, or at least half believed it might be partly true. The
attitude of the rest of us ranged from a patronizing disparagement that
we thought was expected of us, through grudging admiration, to
out-and-out enthusiasm.

Certainly if anybody had taken the trouble to consider it--and why
should they have?--the landing of the first manned ship on our satellite
seemed to render him as obsolete as a horde of other lesser and even
greater lights. At any rate, it was inevitable that the conquest of the
moon would be merely a stepping-stone to more distant points.

"""

# to print list of words: 
# # printing original string 
# print ("The original string is : " +  text_string) 
  
# # using regex( findall() ) 
# # to extract words from string 
# extract_word = re.findall(r'\w+', text_string) 
  
# # printing result 
# print ("The list of words is : " +  str(extract_word)) 