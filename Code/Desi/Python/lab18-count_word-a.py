import requests
import string



def count_words():
    # 1) get the text from the file, via "with open..." or using requests
    little_women = requests.get('http://www.gutenberg.org/cache/epub/514/pg514.txt')
    # convert book to lowercase text and splits string
    book = little_women.text.lower().split()
    # strip book of punctuation
    punct = '*,.;!&%$?"()[]0123456789#/'
    # loops over length of book and strips punctuation
    for i in range(len(book)):
        book[i] = book[i].strip(punct)
    # creates dictionary
    common_words = {}
    # loops over text finding words and adding them to dictionary
    for word in book:
        if word not in common_words:
            common_words[word] = 1
        else:
            common_words[word] += 1
    # returns list of tuples
    words = list(common_words.items())
    # sorts largest to smalles based on count
    words.sort(key=lambda tup: tup[1], reverse=True)
    # prints words
    for i in range(min(10, len(words))):
        print(words[i])
    return common_words
# calls function.
count_words()





    
    
    
    
    
    # # returns a list of strings after breaking the given string by the specified separator.
    # lines =  text.split('\r')
    # # limit text file to lines 200 - 800
    # paragraph = lines[200:800]
    # # print text selection
    # print(paragraph)

    # # ===============================================================================


    # # Make everything lowercase,  strip punctuation, split into a 
    # # list of words
    # # AttributeError: 'list' object has no attribute 'lower'
    # string2 = paragraph.lower(str(paragraph))
    # print(string2)
    # x = string2.replace("o", "")
    # print(x)
    # # ==========================================================

    # # strip punctuation
    # for character in book:
    #     if character in (";", ":", ",", "!", "?", "'"):
    #     text = text.replace(character, "")

    # print(text)

    # # ==========================================================


    # # Split into a list of words

    # x = txt.split()
    # print(x)
    # txt = ""
    # x = txt.split()
    # print(x)


    # #=================================================================================

    # # 3A. Your dictionary will have words as `keys` and counts as `values`.

    # #iterate each word in list of words
    # word_counts = {}
    # for keys in x:
    #     if keys not in word_counts:
    #         word_counts[keys] = 1
