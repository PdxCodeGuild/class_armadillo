import re
# match only checks for a match at the beginning of a string.
# re.match("c", "abcdef")    # no match
# alpha = re.match("c", "abcdef")
# print(alpha)


re.search("c", "abcdef")   # match
bravo = re.search("c", "abcdef")   # match
print(bravo)

# ^ is a carat that signifies the beginning of a sentence.
# $ signifes the end of a sentence.

# . ^ $ * + ? { } [ ] \ | ( )

# ? Causes the resulting RE to match 0 or 1 repetitions of 
#      the preceding RE. ab? will match either ‘a’ or ‘ab’.

# [] ---> Used to indicate a set of characters in a set.

# * Causes the resulting RE to match 0 or more repetitions
#    of the preceding RE, as many repetitions as are possible.   
#    ab* will match ‘a’, ‘ab’, or ‘a’ followed by any 
#    number of ‘b’s.


