import requests
import string
import json
import time

print("Welcome Quote Finder\n")
# time.sleep(2)

user = input("Use a keyword to find a quote: ")

page = "https://favqs.com/api/quotes?page=1&filter={user}"

# Pulling from the api link.
authorization = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

response = requests.get(page, authorization["Authorization"])

print(response.text)
# Converting the .json into a readable Dict. form for python.
# info = json.loads(response.text)
# print(info)
