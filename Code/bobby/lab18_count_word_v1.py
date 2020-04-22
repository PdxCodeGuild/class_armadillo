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
count = {
    "the": 10,
    "a": 1,
    "hello": 1,
    "that": 2

}
# .items() returns a list of tuples
words = list(count.items())
print(words)

# Sorts largest to smallest, based on count. 
words.sort(key=lambda tup: tup[1], reverse = True)

# print the top 10 words, or all of them, whichever is smaller
for i in range(min(10, len(words))):
    print(words[i])