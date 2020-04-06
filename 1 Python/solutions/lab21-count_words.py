import re
import operator
word_count = {}
pair_count = {}
# Opens and copies the text of a book's .txt file
with open('MobyDick.txt', 'r') as f:
    # Reads the file and converts it to lowercase
    input_file = f.read().lower()

# Strips punctuation and stores words in list
word_list = re.compile('\w+').findall(input_file)
# Loop through word list and counts words
for word in word_list:
    # If the word is not in the word dictionary add it
    if word not in word_count:
        word_count[word] = 1
    # If its in the word dictionary incriment the count
    else:
        word_count[word] += 1
# Loop through word list and counts pairs
for j in range(len(word_list) - 1):
    pair = str(word_list[j] + ' ' + word_list[j+1])
    # If the pair is not in the word dictionary add it
    if pair not in pair_count:
        pair_count[pair] = 1
    # If its in the pair dictionary incriment the count
    else:
        pair_count[pair] += 1
#Puts the single words in desending order based on which word appears the most
sorted_words = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
print('The top 10 most used single words are:')
for a in range(10):
    print(sorted_words[a])
#Puts the word pairs in desending order based on which word appears the most
sorted_pairs = sorted(pair_count.items(), key=operator.itemgetter(1), reverse=True)
print('The top 10 most used pair of words are:')
for b in range(10):
    print(sorted_pairs[b])