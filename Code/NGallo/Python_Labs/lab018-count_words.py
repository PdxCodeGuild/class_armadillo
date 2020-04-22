import requests
import string 


def count_words():
  # recieves information from web address. 
  response_from_website = requests.get('http://www.gutenberg.org/cache/epub/32950/pg32950.txt')
  book = response_from_website.text.lower()
  list_of_strings = book.split()

  # remove punctuation from each word
  table = str.maketrans('', '', string.punctuation)
  stripped = [w.translate(table) for w in list_of_strings]
  stripped.sort() 
  sorted_stripped_book = stripped

  words_and_counts = {}

  for word in sorted_stripped_book:
    if word not in words_and_counts: 
      words_and_counts[word] = 1
    if word in words_and_counts:
      words_and_counts[word] += 1
  
  words = list(words_and_counts.items()) # .items() returns a list of tuples
  words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
  for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

  return words_and_counts

def ask_the_user(dictionary_of_words):
  user_word = input("enter the word you would like to find: ")

  if user_word in dictionary_of_words:
    times_occurred = dictionary_of_words[user_word]
    print(f"Your word {user_word} was in the book and occurred {times_occurred}")
  else:
    print("That word was not found in the dictionary")

# saving the function return to the global scope
dictionary = count_words()
ask_the_user(dictionary)


'''
Lab 18: Count Words
Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronyms, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

1.Open the file.
2 Make everything lowercase, strip punctuation, split into a list of words.
3 Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
4 Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
Version 2
9 Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

Version 3 (optional)
Let the user enter a word, then show the words which most frequently follow it.

'''