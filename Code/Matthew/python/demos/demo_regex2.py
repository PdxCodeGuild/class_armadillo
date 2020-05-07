
import re

# https://regex101.com/r/nRy8cd/1

# text containing phone numbers
text = '''
512-123-1617
(167) 151-1678
523   -   156 1567
My phone number is 555-124-1678
9285919698
55-555-5555
55
'''

# raw strings ignore escape sequences
# print('hello\tworld') # hello     world
# print(r'hello\tworld') # hello\tworld

# find all the matching phone numbers
pattern = r'\(?(\d{3})[) -]*(\d{3})[ -]?(\d{4})'
results = re.findall(pattern, text)
print(results)

# combine each tuple in the result into a string
results = [t[0] + t[1] + t[2] for t in results]
print(results)
