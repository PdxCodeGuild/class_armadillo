import re



text_to_search ='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

351-55-4321
123.555.1234

Mr. Schafer
Mr Smith
Mrs.Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it an end'

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = pattern.finditer(text_to_search)

with open('data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)


# print(text_to_search[142:153])

# pattern = re.compile(r'\.') # searches for literal periods
