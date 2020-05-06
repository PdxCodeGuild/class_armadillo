
#Problem 1 Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    output_word = ""
    for char in word:
        # print(char+char = word)
        # output_word = output_word + char + char

        output_word += char + char

    return output_word

# print(double_letters('hello')) # hheelllloo


# Problem 6
# Return the number of letter occurances in a string.

def count_letter(letter, word):
    # output_word = ""
    # for char in word:
    #     if char == letter:
    #         output_word += letter
    # return len(output_word)
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
        print(char, letter, counter)
    return counter

# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2

# Problem 7
# Convert input strings to lowercase without any surrounding whitespace.

def lower_case(text):
    text = text.lower()
    text = text.strip()
    # for i in range()
    return text

print(lower_case("SUPER!")) # 'super!'
print(lower_case("        NANNANANANA BATMAN        ")) # 'nannananana batman'