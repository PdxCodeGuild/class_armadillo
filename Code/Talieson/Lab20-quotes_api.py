import requests
import json

# Request JSON info from the quote API, store in response.
response = requests.get('https://favqs.com/api/qotd')
# Parse the data into a dictionary.
data = json.loads(response.text)
# Print a string containing the quote and author of the quote.
print(f" \"{data['quote']['body']}\"\n  - {data['quote']['author']}")
