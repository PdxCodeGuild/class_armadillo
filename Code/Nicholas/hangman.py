
def load_words(path):
    with open('contacts.json', 'r') as file:
        text = file.read()
        for words in text:
            