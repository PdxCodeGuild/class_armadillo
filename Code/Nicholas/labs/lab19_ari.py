import requests

response = requests.get('https://www.gutenberg.org/files/25344/25344-0.txt')

text = response.text
       
lines = text.split('\n')
text = lines[244:8722]
#sentence count
period_count = response.text.count('.')  
question_count = response.text.count('?')
exclamation_count = response.text.count('!')
print(period_count)
print(question_count)
print(exclamation_count)

sentence_count = int(period_count + question_count + exclamation_count)
print(sentence_count)


       


for char in text:  
    if char in '[]()@$%*-.?!,\'/:1234567890': #if nums and special characters within text:
        text=text.replace(char,' ')  #replace with blank space

#word count
words = len(response.text.split())
print(words)

# characters count
response.text.strip()
chars = 1
for i in range(len(text)):
    chars += chars
print(chars)



ARI = 4.71 * (chars/words) + 0.5 * (chars/sentence_count) - 21.43

print(ARI) #OverflowError: int too large to convert to float