'''missing_char('kitten') → ['itten', 'ktten',
'kiten', 'kiten', 'kittn', 'kitte']'''

def missing_char(word):
    list1 = []
    # word = list(word)
    for i in range(len(word)):
        list1.append(list(word))
    
    increment = 0

    for word in list1:
        word = word.pop(increment)
        increment += 1

    for word in list1:
        print(''.join(word), end=' ')



missing_char('kitten') # ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

