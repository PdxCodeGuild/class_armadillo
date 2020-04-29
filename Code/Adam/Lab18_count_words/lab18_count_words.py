"""

Lab 18: Count Words =====================================================================

Let's write a python module to analyze a given text file containing a book for its 
vocabulary frequency and display the most frequent words to the user in the terminal. 
Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, 
contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

"""


import requests

# return True if the word only contains letters, otherwise return False
def is_all_letters(word):
    for char in word:
        if char not in 'abcdefghijklmnopqrstuvwxyz':
            return False
        return True


def has_nonletter(word):
    for char in word:
        if char not in 'abcdefghijklmnopqrstuvwxyz':
            return True
    return False


"""
1. Get the text from the file, via "with open..." or using requests
"""

url = 'https://www.gutenberg.org/files/56345/56345-0.txt'
response = requests.get(url)
text = response.text
# remove junk from the start of the text
index_stars = text.find('***') # find the line that starts with "*** START OF...""
index_stars = text.find('\n', index_stars) # find the end of that line
text = text[index_stars:] # remove everthing before that index


index_stars = text.rfind('*** END') # find the last occurance
text = text[:index_stars] # remove everything after that index
# print(text[index_stars:-100:index_stars+100])

"""
2.  Make everything lowercase, strip punctuation, split into a list of words.
"""

# a dictionary to store words as keys and their counts as the values.
word_counts = {}

text = text.lower() # make all of the text lowercase

text = text.replace('â\x80\x9c', '') # 'â\x80\x9c' found attached to words
text = text.replace('â\x80\x94', ' ') # found between two words
text = text.replace('â\x80\x9d', '') # found by itself and attached to words
text = text.replace('â\x80\x99', '\'') # found in place of '
text = text.replace('--', ' ')
text = text.replace(',', '')
text = text.replace('\'s', '')

# we don't care about adding extra spaces 
# split without parameters will split on combined whitespace

for punctuation in '.!?*,()[]"â©_ã±:;$-':
    text = text.replace(punctuation, ' ')
    
words = text.split()
# print(len(words))


for word in words:
    if not is_all_letters(word):
        print(word, end = ' ')


for word in words:
    # if not is_all_letters(word):
    if has_nonletter(word):
        print(word, end='  ')

"""
 3.  Your dictionary will have words as keys and counts as values. If a word isn't in your 
     dictionary yet, add it with a count of 1. If it is, increment its count.
"""

for word in words[300:6300]:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# print(word_counts)

sorted_words = list(word_counts.keys())
sorted_words.sort()
print('\n'.join(sorted_words))


"""
  4.  Print the most frequent top 10 out with their counts. You can do that with the code below.
"""

words = list(word_counts.items()) # .items() returns a list of tuples
words.sort(key = lambda tup: tup[1], reverse = True) # sort largest to smallest, based on count
for i in range(min(10, len(words))): # print the top 10 words, or all of them, whichever is smaller
    print(words[i][0], words[i][1])

    