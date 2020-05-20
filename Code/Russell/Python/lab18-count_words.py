
import requests

# get the text from the file, via using requests
# requests allow you to send http requests with python

book = requests.get('https://www.gutenberg.org/cache/epub/8492/pg8492.txt')

text = book.text

text = text.lower() # change the text to lowercase
book_list = text.split() # turns the text into a list of words


# iterate through each element in the book list; remove special characters and numbers
for i in range(len(book_list)):
    book_list[i] = book_list[i].strip('!@#$%^&*()_-;][]:}{\'\",./?;:\\|<>')
    book_list[i] = book_list[i].strip('1234567890')


#  build up word_counts, a dictionary where the key is the word and the value is the countword_dictionary = {}
word_dictionary = {}
for word in book_list:
    if word in word_dictionary:
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = 1

    

words = list(word_dictionary.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])