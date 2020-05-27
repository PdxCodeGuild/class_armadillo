
import string

# 1) get the text from the file, via "with open..." or using requests

filename = 'Code\Lawrence_House\metamorp.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# 2) get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]

words = text.split()

punc_table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(punc_table) for w in words]
words = [word.lower() for word in stripped]

# 3) build up word_counts, a dictionary where the key is the word and the value is the count

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

# 4) Print the most frequent top 10 out with their counts. You can do that with the code below.

words = list(word_counts.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
print("The Top 10 most common words are:\n")
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
  print(words[i][0], words[i][1])
