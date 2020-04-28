import requests
import time
from colorama import Fore

welcome_msg = '\nWelcome to LITERARY WORD ACCOUNTANT!' 
i = 0
while i < len(welcome_msg): # prints welcome message one letter at a time in green color
    print(Fore.GREEN + welcome_msg[i], end='', flush=True)
    time.sleep(0.05)
    i += 1

# dictionary for book library
books = {
    1: '''"The History of Don Quixote, Vol. I" by Miguel de Cervantes''',
    2: '''"The History of Don Quixote, Vol. II" by Miguel de Cervantes''',
    3: '''"The Count of Monte Cristo" by Alexandre Dumas''',
}

time.sleep(0.5)

print(Fore.RESET + f'\n\nAVAILABLE BOOKS:\n1. {books[1]}\n2. {books[2]}\n3. {books[3]}')

time.sleep(1)

print('\n\nAVAILABLE FUNCTIONS:\nA. Words\nB. Word Pairs\n')

time.sleep(1)

# allows the user to select from a catalog of books
def book_selection(book_number): # URL of plain text UTF-8 version of book in Project Gutenberg (www.gutenberg.org) 
    book_list = {
        1: 'https://www.gutenberg.org/files/5921/5921-0.txt',
        2: 'https://www.gutenberg.org/files/5946/5946-0.txt',
        3: 'https://www.gutenberg.org/files/1184/1184-0.txt', 
    }
    return book_list[book_number] # returns the book variable for entry of URL into book_text() function below

# book = 'http://www.gutenberg.org/cache/epub/5903/pg5903.txt' # example book selection for test purposes



# 1. Get the text from the file, via "with open..." or using requests

def book_text(book):
    response = requests.get(book) # makes request to a web page using the book's URL in book variable 
    return response.text # returns the text variable (content of the response, in unicode)



# 2. Get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]

def clean_words(text):
    # junk removal from text file, so that non-literary material (top/bottom text) is not included in word count
    text = text[text.find('***') + 3:] # slices text up to first '***' in the text, then adds 3 indices to include those '***' in the slice (top junk)
    text = text[text.find('***') + 3:] # slices the few words that are before the second '***' in text, adds the 3 indices for second '***' (top junk)
    text = text[:text.find('***')] # slices everything after the third '***', which is bottom junk
    
    # tests for junk removal and word cleanse      
    # print(text[:200]) # sample of top text
    # print(text[200:]) # sample of bottom text

    # punctuation and number removal
    for char in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~': # iterates through each character in punct variable above to remove punctuation
        text = text.replace(char, "") # when character in punct variable is in text, it replaces it with ""(removal)
    for char in '0123456789': # removes numbers
        text = text.replace(char, "")  
    return text.lower().split() # changes all char to lower case, splits words into list by delimiter: white space (default)



def pair_noshift(clean_text): # pairing of words begins with first word of text
    paired_text_noshift = [' '.join(clean_text[i:i + 2]) for i in range(0, len(clean_text), 2)]
    if len(paired_text_noshift) % 2 == 1: # determines if book has odd number of words (last word in text would not have a pair)
        del paired_text_noshift[-1] # deletes the last word in text if text has odd number of words
    return paired_text_noshift


def pair_shift(clean_text): # pairing of words begins with second word of text
    paired_text_shift =  [' '.join(clean_text[i:i + 2]) for i in range(1, len(clean_text), 2)] # adjusted range ignores first word of text
    if len(paired_text_shift) % 2 == 1: # determines if book has odd number of words (last word in text would not have a pair)
        del paired_text_shift[-1] # deletes the last word in text if text has odd number of words
    return paired_text_shift    
    

# 3. Build up word_counts (a dictionary where the key is the word and the value is the count)

def make_dictionary(clean_text): # makes dictionary of single word counts
    word_counts = {} # dictionary for capturing entries generated below
    for word in clean_text: # iterates each of the words in cleaned text
        if word in word_counts: # if word is already in dictionary, it increments count
            word_counts[word] += 1
        else: # if word is not in dictionary yet, it adds it with count of 1
            word_counts[word] = 1  
    return word_counts # returns dictionary with clean words and their counts

def make_pair_dictionary(paired_text_noshift, paired_text_shift): # combines 2 sets of word pair counts into single dictionary
    word_counts = {} # dictionary for capturing entries generated below
    for pair in paired_text_noshift: # iterates each of the word pairs in the list
        if pair in word_counts: # if pair is already in dictionary, it increments count
            word_counts[pair] += 1
        else: # if pair is not in dictionary yet, it adds it with count of 1
            word_counts[pair] = 1  
    for pair in paired_text_shift: # iterates each of the word pairs in the list
        if pair in word_counts: # if pair is already in dictionary, it increments count
            word_counts[pair] += 1      
        else: # if pair is not in dictionary yet, it adds it with count of 1
            word_counts[pair] = 1  
    return word_counts

# print(word_counts) # test purposes        


# 4. print the most frequent top 10 out with their counts 

def top_words(word_counts):
    top_list = [] # list for capturing the tuples that are generated below
    words = list(word_counts.items()) # .items() turns the dictionary into a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sorts the tuples from largest to smallest, based on count
    for i in range(min(length, len(words))):  # prints the top occurring (# selected by user) words, or all of them, whichever is smaller
        top_list.append(words[i]) # sends the tuples to the top_list, as the for loop iterates
    return top_list # returns completed top_list hen loop is done, contains top occurring sorted tuples
    
    # print(top_list) # test purposes


# desired print format for output
def print_list(top_list):
    print(f'\nThe top {length} counts in {books[book_number]} are:')
    i = 0 # provides counter variable for producing printed number bullets for output
    for word in top_list: # used to print top_list vertically
        print(str(i+1) + '.', word) # str enables concatenation of integer + string
        i += 1 # increments counter 
    print('\n') # for appearance, skips a line before terminal command prompt that appears when programs end
     

# merges above functions
def word_accountant_word(): 
    book = book_selection(book_number)
    text = book_text(book)
    clean_text = clean_words(text)
    word_counts = make_dictionary(clean_text)
    top_list = top_words(word_counts)
    print_list(top_list)


def word_accountant_pairs(): 
    book = book_selection(book_number)
    text = book_text(book)
    clean_text = clean_words(text)
    paired_text_noshift = pair_noshift(clean_text)
    paired_text_shift = pair_shift(clean_text)
    word_counts = make_pair_dictionary(paired_text_noshift, paired_text_shift)
    top_list = top_words(word_counts)
    print_list(top_list)


# main program that includes input validation and selects the proper functions as determined by user input
while True:
    book_number = input('Please enter your book selection (1, 2, or 3): ') # input into book_selection() function to select dictionary entry    
    if book_number not in '1, 2, 3': # input validation using string
        print(Fore.RED + 'Invalid entry!' + Fore.RESET) # print in red color
    else: 
        book_number = int(book_number) # converts string to integer since book_list library keys are integers
        break    
while True:        
    function = input('Please enter the count function (A or B): ').lower() # will accept lower case entry    
    if function != 'a' and function != 'b': # input validation
        print(Fore.RED + 'Invalid entry!' + Fore.RESET)
    else: 
        break
while True:    
    length = input('How many of the top spots would you like to include on your list? ') # input into top_words() function to allow user to select number of words on top words list (top_list)
    if length.isnumeric() == False: # input validation, checking if string is numeric
        print(Fore.RED + 'Invalid entry!' + Fore.RESET)
    else:
        length = int(length) # converts to integer here since isnumeric() uses strings
        break
if function == 'a': # picks the proper count function based on user input
    word_accountant_word() # version 1
if function == 'b':
    word_accountant_pairs() # version 2



'''
# Lab 18: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on [Project Gutenberg](http://www.gutenberg.org).
Download it as a UTF-8 text file.

1. Open the file.
2. Make everything lowercase,  strip punctuation, split into a list of words.
3. Your dictionary will have words as `keys` and counts as `values`. If a word isn't in your dictionary yet, 
add it with a count of 1. If it is, increment its count.
4. Print the most frequent top 10 out with their counts. You can do that with the code below.

```(from python)
# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
```

Version 2 (optional)

Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

Version 3 (optional)

Let the user enter a word, then show the words which most frequently follow it.
'''