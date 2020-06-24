import requests



response = requests.get('http://www.gutenberg.org/cache/epub/4715/pg4715.txt')

text = response.text.lower()
stars = text.find('***')
stars = text.find('\n', stars)
text = text[stars:]

stars = text.rfind('*** END')
text = text[:stars]
text = text.replace(',', '-')

for punctuation in ',.':
    text = text.replace(punctuation, '-')

words = text.split()
print(len(words))

def letters(word):
    for char in word:
        if char not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True
    
def not_letter(word):
    for char in word:
        if char not in 'abcdefghijklmnopqrstuvwxyz':
            return True
    return False

counter = {
    'the': 20,
    'a': 20,
    'i': 20,
    'don\'t': 15,
}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

words = list(counter.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
 
    print(words[i][0], words[i][1])







