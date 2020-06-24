


# split turns a string into a list of strings
# if given no parameters it splits on whitespace
fruits = 'apples bananas \n\tpears'
print(fruits.split()) # ['apples', 'bananas', 'pears']

# if given a delimiter it will split on that
fruits = 'apples_bananas_pears'
print(fruits.split('_')) # ['apples', 'bananas', 'pears']

# replace will replace all occurances of a string
mystring = '>  hello there!  <'
print(mystring.replace(' ', '')) # >hellothere!<

# strip removes characters from the beginning and end of a string
# if given no parameter it strips on whitespace
# notice the space between 'hello' and 'there' remains
mystring = '  \t\n hello there!  \t'
print(mystring.strip()) # hello there!

# strip can also be given a string of characters to remove
punctuation = '~!@#$%^&()_'
mystring2 = '$hello! there!!'
print(mystring2.strip(punctuation)) # hello! there

