# def missing_char(word):
#   starter = input('What\'s the word? : ')
#   output = ""
#   for i in range(0,len(starter)):
#     output = i + i
#   return word
# print (missing_char(starter))

# above is concept error

def double_letters(word):
  output word = ""
  for char in word:
    #print(char + char = word)
    # output_word = output_word + char + char

    output_word += char + char
  return output_word
print(double_letters('hello'))