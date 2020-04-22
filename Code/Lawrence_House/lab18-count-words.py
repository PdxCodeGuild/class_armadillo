
import string
import requests

remove_punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# 1) get the text from the file, via "with open..." or using requests

response = requests.get('http://www.gutenberg.org/cache/epub/5200/pg5200.txt')
text = response.text

# for word in text
    

# 2) get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]


print(word_list(text))

# junk_start = text.find('***')
# print(junk_start)
# print(text[junk_start:junk_start+100])
# print(text[800:900])

# lines = text.split('\n')
# print(lines[103:110])


# 3) build up word_counts, a dictionary where the key is the word and the value is the count

# word_counts = {
#   'the': 10,
#   'a': 1,
#   'hello': 1,
#   'that': 2
# }
# words = list(word_counts.items()) # .items() returns a list of tuples
# print(words)
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#   print(words[i])