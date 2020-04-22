

import requests
import string
not_letter = ',.?!@:;'

# 2) get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]
def list_of_words(text):
    words = []
    for text in not_letter:
        text = text.replace(not_letter, ' ')
    print(text)
    
    for char in text:
        words.append(char)
    return words
    

# for i in range(len(word)):
#     words[i] = words[i].strip(',.?!@:;')
   

# junk_start = text.find('***')
# print(junk_start)
# print(text[junk_start:junk_start+100])

# print(lines[103:110])

# 3) build up word_counts, a dictionary where the key is the word and the value is the count

# word_counts = {
#     'the': 20,
#     'a': 20,
#     'i': 20,
#     'don\'t': 15,
# }

# words = list(word_counts.items())

response = requests.get('http://www.gutenberg.org/files/46/46-0.txt')
print("downloaded book")
text = response.text.lower().split()
words = list_of_words(text)
# words = words.strip(',.?!@:;')
print(words[100:200])
# print(words)

# words.sort(key=lambda tup: tup[1], reverse=True)

# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])