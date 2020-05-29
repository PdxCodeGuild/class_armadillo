"""

Lab 18: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

1. Open the file.
2. Make everything lowercase, strip punctuation, split into a list of words.
3. Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
4. Print the most frequent top 10 out with their counts. You can do that with the code below.

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

"""
from collections import Counter
import string
import requests

# def ten_most_frequent_words(dictionay): # build a function for finding 10 most frequent qords

# url = 'https://www.gutenberg.org/files/215/215-0.txt' # Call of the wild from Project Gutenberg

# 1) Open the file.
# starter code
response = requests.get('https://www.gutenberg.org/files/215/215-0.txt')
text = response.text


# 2. Make everything lowercase, strip punctuation, split into a list of words.
text = text.lower()
# text = text.split(' ')
# print(text)

text = text.replace('â\x80\x99', '\'')
text = text.replace('â\x80\x94', ' ')
text = text.replace('â\x80\x9d', '')
text = text.replace('â\x80\x9c', '')
text = text.replace('å\x93', 'e')
text = text.replace('\'s', '')
# text = text.replace('')

# starter code
ebook_start = text.find('***')
ebook_end = text.find(
    'end of the project gutenberg ebook of the call of the wild, by jack london')
# print(ebook_start)
# print(ebook_end)
text = text[ebook_start:ebook_end]


for char in ['!', '"', '#', '$', '%', '-', '&', "'", '.', '(', ')', '+', ',', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']:
    # print(char)
    text = text.replace(char, ' ')
text = text.split()
# print(text)

words_in_book = {}

# iterate over text.
for word in text:
    if word in words_in_book:  # if the word is already a keyword in the dictionary...
        words_in_book[word] += 1  # add 1 to its value
    # if the word is not in the dictionary..
    elif word not in words_in_book.keys():
        words_in_book[word] = 0  # add the word with a value of 0
        words_in_book[word] += 1  # add 1 to its value


words = list(words_in_book.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

# # alternative using counter
# # print(words_in_book)
# count = Counter(words_in_book)
# ten_most_common = count.most_common(10)  # returns top 10 values


# # Print the most frequent top 10 out with their counts. 
# print(f'The ten most common words are: {ten_most_common}')
