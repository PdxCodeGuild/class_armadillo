import re
# match only checks for a match at the beginning of a string.
# re.match("c", "abcdef")    # no match
# alpha = re.match("c", "abcdef")
# print(alpha)


re.search("c", "abcdef")   # match
bravo = re.search("c", "abcdef")   # match
print(bravo)