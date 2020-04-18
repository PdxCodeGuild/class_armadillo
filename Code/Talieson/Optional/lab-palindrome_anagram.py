# Lab: Palindrome and Anagram


# check_palindrome function takes a string input and returns if it is the
# same word backwards as it is forward.
def check_palindrome(word):
    backwards_word = word[::-1]
    if backwards_word == word:
        return True
    return False


# test = "racecar"
# print(check_palindrome(test))


# this function takes 2 words and checks if they contain the same set of
# letters. It returns True is so.
def anagram_checker(input, input2):
    # Here we convert to lower, get rid of spaces, and sort the lists.
    input = sorted(input.replace(" ", "").lower())
    input2 = sorted(input2.replace(" ", "").lower())
    print(input, input2)
    if input == input2:
        return True
    return False


word1 = "buTT"
word2 = "tu  bt"
print(anagram_checker(word1, word2))
