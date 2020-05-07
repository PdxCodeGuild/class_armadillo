import requests
import json
import time


print("Welcome Quote Finder\n")
time.sleep(2)

user = input("Use a keyword to find a quote: ")

page = f"https://favqs.com/api/quotes?page=1&filter={user}"
authorization= {'Authorization': 'Token token="95251f84fa0c7fc3e4d869ef7ebad17e"'}
response = requests.get(page, headers=authorization)
info_dic = json.loads(response.text)
info_dic1 = info_dic["quotes"]
print(info_dic1[0]["body"])
print(info_dic1[0]["author"])

