

import requests



response = requests.get('http://www.gutenberg.org/files/46/46-0.txt')
text = response.text.lower()
index_stars = text.find('***')
index_stars = text.find('\n', index_stars)
text = text[index_stars:]

index_stars = text.rfind('*** END')
text = text[:index_stars]
text = text.replace(',', '-')

for punctuation in ',.':
    text = text.replace(punctuation, '-')

words = text.split()
print(len(words))

# 2) get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]
def is_letters(word):
    for char in word:
        if char not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True
    
def no_letter(word):
    for char in word:
        if char not in 'abcdefghijklmnopqrstuvwxyz':
            return True
    return False
# for i in range(len(word)):
#     words[i] = words[i].strip(',.?!@:;')
# word_counts = {}
word_counts = {
    'the': 20,
    'a': 20,
    'i': 20,
    'don\'t': 15,
}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
# print(word_counts)








# for word in words:
#     if has is_letter(word):
#         print(word, end=' ')



# junk_start = text.find('***')
# print(junk_start)
# print(text[junk_start:junk_start+100])
# print(lines[103:110])

# 3) build up word_counts, a dictionary where the key is the word and the value is the count


words = list(word_counts.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    # print the top 10 words, or all of them, whichever is smaller
    print(words[i][0], words[i][1])








# for not_letter in text:
#         text = text.replace('not_letter', ' ')
#         print(text)
#         # print('hi')