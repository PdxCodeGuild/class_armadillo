import requests # request package

# 1.)Requesting the URL
response = requests.get("http://www.gutenberg.org/cache/epub/5200/pg5200.txt")

# Define the text that you want, in this case it is Metamorphosis by Franz Kafka
text = response.text
# print(text)

# 2.) To define a clean list of words within the text
clean_list = text.split("r")
print(clean_list[200:800])

# junk_start = text.find("***")
# print(junk_start)
# print(text[junk_start:junk_start+100])
# print(text[800:900])
# clean_list2 = text.split("\n")

#3.) To build a word count dict for the value of a word and count.
count = {}
for word in response:
    if word not in count:
        count[word] = 1   
    else:
        count[word] += 1
words = list(count.items())# .items() returns a list of tuples
print(words)

words.sort(key=lambda tup: tup[1], reverse = True)# Sorts largest to smallest, based on count. 
for i in range(min(10, len(words))):# print the top 10 words, or all of them, whichever is smaller
    print(words[i])