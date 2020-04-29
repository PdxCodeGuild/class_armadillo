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

#converting JSON into a dictionary
dictionary = json.loads(response.text)
print(dictionary)

#RESULT
# Enter a keyword to search for quotes : {"page":1,"last_page":false,"quotes":[{"id":0,"favorites_count":0,"favorite":false,"dialogue":false,"body":"No quotes found","tags":[]}]}
# {'page': 1, 'last_page': False, 'quotes': [{'id': 0, 'favorites_count': 0, 'favorite': False, 'dialogue': False, 'body': 'No quotes found', 'tags': []}]}

# print(contacts['contacts'][0]['name']) # Joe
# print(json.loads(contacts, indent=4, sort_keys=True))


# the quotes you get in response, and 
# print(keyword)
# # prompt the user to either show the 
# if-else
# # next page or enter a new keyword. 
# # You can use string concatenation to build the URL.
# what?
