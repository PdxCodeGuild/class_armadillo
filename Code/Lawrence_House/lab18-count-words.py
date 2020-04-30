
import string

# remove = dict.fromkeys(map(ord, '\n ' +string.punctuation))

# 1) get the text from the file, via "with open..." or using requests

# response = requests.get('http://www.gutenberg.org/cache/epub/23540/pg23540.txt')
# text = response.text

# with open('metamorp.txt') as inputfile:
#   f = inputfile.read().translate(remove)

filename = 'Code\Lawrence_House\metamorp.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# 2) get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]

words = text.split()
# words = text.find('***')

punc_table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(punc_table) for w in words]
words = [word.lower() for word in stripped]

print(words)


# junk_start = text.find('***')
# print(junk_start)
# print(text[junk_start:junk_start+100])
# print(text[800:900])

# lines = text.split('\n')
# print(lines[103:110])


# 3) build up word_counts, a dictionary where the key is the word and the value is the count

# def char_count(word):
#   word_counts = {
      
#     }
#   for word in words:
#     word_counts['word': +1]
#     return word_counts

# print(char_count(words))


# words = list(word_counts.items())
# words.sort(key=lambda tup: tup[1], reverse=True)
# for i in range(min(10, len(words0))):
#   print(words[i])

# 4) Print the most frequent top 10 out with their counts. You can do that with the code below.

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
#   print(words[i][0], words[i][1])
