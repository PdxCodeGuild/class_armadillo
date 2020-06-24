import requests
import string


def count_words():
    url = 'http://www.gutenberg.org/cache/epub/16643/pg16643.txt'
    book = requests.get(url)
    book = response.text.lower().split
    punctuation = '*,.;!&%$?"()[]0123456789#/'
    for i in range(len(book)):
        book[i] = book[i].strip(punct)
        txt =  {}

        for word in book:
            if word not in txt:
                txt[word]= 1
            else:
                text[word] += 1
            words = list(txt.items())

            words.sort(key=lambda tup:tup[1], reverse= True)

            for i in range(min(10, len(words))):
                print(words[1])
                return txt
count_words()






