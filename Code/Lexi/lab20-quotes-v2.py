import requests
import json

# Prompt the user for a keyword, list 

keyword = input("Enter a keyword to search for quotes : ")
# make formatted string to use line 6 for quote category
url = f'https://favqs.com/api/quotes?page=1&filter={keyword}'

# must comment out two lines below in order to make it work,
# WHY? b/c access token is needed
# response = requests.get(url)
# print(response.text)

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)
print(response.text)
# the quotes you get in response, and 
# print(keyword)
# # prompt the user to either show the 
# if-else
# # next page or enter a new keyword. 
# # You can use string concatenation to build the URL.
# what?
