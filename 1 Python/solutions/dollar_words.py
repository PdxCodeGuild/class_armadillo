import string



# if we give each letter a value (a=1, b=2, ..., z=26)
# the letters of which words sum to 100?
# e.g. hospital
words_path = r'C:\Users\flux\programs\class_iguana\1 Python\data\english.txt'
output_path = r'C:\Users\flux\programs\class_iguana\1 Python\data\output.txt'

with open(words_path) as file:
    words = file.read().split('\n')
    words = [word for word in words if len(word) > 5]
    words = [word.lower() for word in words]


    # words2 = []
    # for word in words:
    #     word = word.lower()
    #     if len(word) > 5:
    #         words2.append(word)
    # words = words2






# words = [(word, sum([string.ascii_lowercase.index(char)+1 for char in word if char in string.ascii_lowercase])) for word in words]
#
# words.sort(key=lambda x: x[1], reverse=True)
#
# with open(output_path, 'w') as output_file:
#     output_file.write('\n'.join([f'{x[0]} {x[1]}' for x in words if x[1] > 0]))




# def add(a, b):
#     return a + b
# add = lambda a, b: a + b



word_counts = []
for word in words:

    # value_count = sum([string.ascii_lowercase.index(char)+1 for char in word if char in string.ascii_lowercase])

    value_count = 0
    for char in word:
        if char in string.ascii_lowercase:
            value_count += string.ascii_lowercase.index(char) + 1
    density = value_count/len(word)
    word_counts.append({'word': word, 'count': value_count, 'density': density})


word_counts.sort(key=lambda x: x['density'], reverse=True)
# print('\n'.join([x['word'] + ' ' + str(x['density']) for x in word_counts[:100]]))

for word_count in word_counts[:100]:
    print(word_count['word'] + ' ' + str(word_count['density']))


