

import requests
import json

response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en')

quote = json.loads(response.text)
quote_text = quote['quoteText']
quote_author = quote['quoteAuthor']

print(f'{quote_text} - {quote_author}')

