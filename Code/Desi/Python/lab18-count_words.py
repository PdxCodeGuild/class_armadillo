import requests


# 1) get the text from the file, via "with open..." or using requests

response = requests.get('http://www.gutenberg.org/cache/epub/23540/pg23540.txt')
text = response.text
# print(text)

# lines =  text.split('\r')
# paragraph = lines[200:800]
# print(paragraph)

# ===============================================================================

# 2. Make everything lowercase.
# Python3 program to show the 
# working of lower() function 
# string1 = ("It was not so with thoughtful Milly she snuggled down on the piazza beside Julia, and looked on quietly")
# lower() function to convert  
#  string to lower_case 
# print("Original String")
# print(string1)
# print("\nConverted String:") 
# print(string1.lower()) 

#  =============================================================================================================================
# 3. strip punctuation
# string2 = ('It was not so with thoughtful Milly she snuggled down on the piazza beside Julia, and looked on quietly')
  
# # strip punctuation
# string2 = string2.lower()
# x = string2.replace("o", "")
# print(x)
 

# ==========================================================

# 4. split into a list of words




# #Strip punctuation
# txt = "It was not so with thoughtful Milly she snuggled down on the piazza beside Julia, and looked on quietly"
# x = txt.split()
# print(x)
# txt = ""
# x = txt.split()
# print(x)


#=================================================================================

# 3A. Your dictionary will have words as `keys` and counts as `values`.


# book_text = ("Hurrah!" said the leader again, Major Patten, swinging his tall fur
# cap, which was the pride of the whole company; "hurrah for the boy that
# risked his life to save a drowning baby!")


# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() 


# book_text = {






# }

 




# # i = 0

# # while(i < len(string)): 
# #     if(string[i] >= 'a' and string[i] <= 'z'):
# #         string1 = string1 + chr((ord(string[i]) - 32))
# #     else:
# #         string1 = string1 + string[i]
# #     i = i + 1
 
# # print("\nOriginal String in Lowercase  =  ", string)




# 2) get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]

# Original String in Lowercase  =   PRUDY KEEPING HOUSE.
# [('the', 10), ('a', 1), ('hello', 1), ('that', 2)]
# ('the', 10)
# ('that', 2)
# ('a', 1)
# ('hello', 1)



# junk_start = text.find('***')
# print(junk_start)

# junk_start = text.find('***')
# print(junk_start)
# lines = text.split('\r')
# print(lines[200:800])

# 508
# [('the', 10), ('a', 1), ('hello', 1), ('that', 2)]
# ('the', 10)
# ('that', 2)
# ('a', 1)
# ('hello', 1)

# print(text[junk_start:junk_start+100])
# print(text[800:900])

# lines = text.split('\n')
# print(lines[103:110])




#3) build up word_counts, a dictionary where the key is the word and the value is the count

word_counts = {
  'the': 10,
  'a': 1,
  'hello': 1,
  'that': 2
}



words = list(word_counts.items()) # .items() returns a list of tuples
print(words)
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
  print(words[i])