

import re
import string
import random




with open('white_horse.txt', 'r') as file:
    contents = file.read()


# fruits = ['apples', 'bananas']
# fruits.append('pear')
# print(fruits)

contents = contents.replace('â€™', '\'')
contents = contents.replace('â€”', ', ')
contents = contents.lower()

sentences = re.split('[\\.!?]', contents)


sentences = [sentence.replace('\n', ' ') for sentence in sentences]

pairs = []
for sentence in sentences:
    words = sentence.split()
    words = [word.strip(string.punctuation + string.whitespace) for word in words]
    sentence_pairs = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    pairs.extend(sentence_pairs)



word_dict = {}
for pair in pairs:

    # list = word_dict.get(pair[0], [])
    # list.append(pair[1])
    # word_dict[pair[0]] = list

    if pair[0] in word_dict:
        word_dict[pair[0]].append(pair[1])  # add the second word to the list
    else:
        word_dict[pair[0]] = [pair[1]]  # add a list with a single element


word = random.choice(list(word_dict.keys()))
n_words = 200
output = ''
for i in range(n_words):
    output += word + ' '
    word = random.choice(word_dict[word])

print(output)

