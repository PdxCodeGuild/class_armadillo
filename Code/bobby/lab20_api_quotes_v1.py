import requests
import string
import json


page = "https://favqs.com/api/qotd"
# Pulling from the api link.
response = requests.get(page)

# Converting the .json into a readable form for python.
info = json.loads(response.text)

# Printing the wanted info from the link.
print(info["quote"] ["body"]) # The random quote ie. "We find delight in the beauty and happiness of children that makes the heart too big for the body.""
print(info["quote"] ["author"]) # The Author of the random quote ie. Ralph Waldo Emerson

