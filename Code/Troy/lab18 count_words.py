'''Let's write a python module to analyze a given text file containing a book 
for its vocabulary frequency and display the most frequent words to the user in 
the terminal. Remember there isn't any "perfect" way to identify a word in 
english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

Open the file.

Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in
your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the 
code below.


# word_dict is a dictionary where the key is the word and the value is the count'''

# imports the module.
import requests
import string

# defines the function.
def count_words():
    # requests the book from the URL.
    badger_book = requests.get('http://www.gutenberg.org/cache/epub/36830/pg36830.txt')
    # converts the book to text, lower case, and splits the strings.
    book = badger_book.text.lower().split()
    # strips the book of punctuation.
    punctuation = '*,.;!&%$?"()[]0123456789#/'
    for i in range(len(book)):
        book[i] = book[i].strip(punctuation)
    # creates the dictionary.
    frequent_words = {}
    # loops over the text finding the words and increases them by increments of 1, adding them to the dictionary.
    for word in book:
        if word not in frequent_words:
            frequent_words[word] = 1
        else:
            frequent_words[word] += 1
    # returns a list of tuples.
    words = list(frequent_words.items()) 
    # sorts largest to smallest, based on count.    
    words.sort(key=lambda tup: tup[1], reverse=True)  
    # prints the top 10 words, or all of them, whichever is smaller.
    for i in range(min(10, len(words))): 
        print(words[i])
    return frequent_words
# calls the function.
count_words()


    