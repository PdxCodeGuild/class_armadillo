import requests
import string
import json
import time

print("Welcome Quote Finder\n")
# time.sleep(2)

user = input("Use a keyword to find a quote: ")


# Pulling from the api link.
authorization = {'Authorization': 'Token token="95251f84fa0c7fc3e4d869ef7ebad17e"'}
page = "https://favqs.com/api/quotes?page=1&filter={user}"
response = requests.get(page, authorization)

print(response.text)
# Converting the .json into a readable Dict. form for python.
# info = json.loads(response.text)
# print(info)
