

# used Nicholas Kalinin's code as a reference
import requests

# text = open('http://www.gutenberg.org/cache/epub/61878/pg61878.txt')  # open the file
# contents = text.read()  # read the contents
# print(contents)


# try:
#     text = open('http://www.gutenberg.org/cache/epub/61878/pg61878.txt')
#     contents = text.read()
#     print(contents)
# except (IOError, OSError) as e:
#     print(e)
# finally:
#     text.close()

# 1) get the text from the file, via "with open..." or using requests

response = requests.get('http://www.gutenberg.org/cache/epub/61878/pg61878.txt')
text = response.text
# print(text) <--this prints out the WHOLE book

# 2) get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]

lines = text.split('\r')
print(lines[200:800])




# junk_start = text.find('***')
# print(junk_start)
# print(text[junk_start:junk_start+100])
# print(text[800:900])

# lines = text.split('\n')
# print(lines[103:110])




# 3) build up word_counts, a dictionary where the key is the word and the value is the count

word_counts = {
  'the': 10,
  'a': 1,
  'hello': 1,
  'that': 2
}
words = list(word_counts.items()) # .items() returns a list of tuples
print(words)
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
  print(words[i])