# Version 1: Get a Random Quote
# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.
import requests
import json

url = ('https://favqs.com/api/qotd')
data = requests.get(url)
text = json.loads(data.text)


subj = text['quote']['tags'][0]
quote = text['quote']['body']
auth = text['quote']['author']
print(f' \n QUOTE OF THE DAY IS ABOUT: \'{subj}\' - stating \"{quote}\" by the author, {auth}')

# {
#   "qotd_date": "2020-05-27T00:00:00.000+00:00",
#   "quote": {
#     "id": 45785,
#     "dialogue": false,
#     "private": false,
#     "tags": [
#       "peace"
#     ],
#     "url": "https://favqs.com/quotes/buddha/45785-those-who-are-",
#     "favorites_count": 0,
#     "upvotes_count": 1,
#     "downvotes_count": 0,
#     "author": "Buddha",
#     "author_permalink": "buddha",
#     "body": "Those who are free of resentful thoughts surely find peace."
#   }
# }
