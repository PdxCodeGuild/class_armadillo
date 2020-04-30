import requests
import json
from colorama import Fore
import time

print('\nWelcome to QUOTE SEARCH BY KEYWORD!')

time.sleep(1) # time delay

key = input('\nPlease enter a keyword to search for quotes: ').lower().strip() # user input for keyword
pg = 1 # sets initial page number

while True:
  url = f'https://favqs.com/api/quotes/?filter={key}&page={str(pg)}' # url to API with inputs for keyword and string page number
  headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} # site requires API key to access list of quotes
  response = requests.get(url, headers=headers) # sends request to favqs.com website API for JSON
  quote_dict = json.loads(response.text) # creates dictionary from JSON
  if quote_dict['quotes'][0]['body'] == 'No quotes found': # checks that key to see if any quotes were found
    print(Fore.YELLOW + '''\nSorry. No quotes found.\n''' + Fore.RESET) # will print if no quotes found
    key = input(Fore.YELLOW + '\nPlease enter a keyword to search for quotes: ' + Fore.RESET).lower().strip() # asks for new input key
    continue # returns to top of program to reenter key
  else: # when quotes were found and exist in dictionary
    print(Fore.YELLOW + f'''\n{len(quote_dict['quotes'])} quotes associated with {key} - page {pg}:\n''' + Fore.RESET) # 25 quotes associated with (keywoard) - page 1:
    for quotes in quote_dict['quotes']: # iterates through each of the group of 25 'quotes' sub-dictionary entries
      print(f'''\n"{quotes['body']}"\n\t--{quotes['author']}\n''') # prints the 'body' and 'author' key values from each 'quotes' dictionary in quote_dict

  while True:
    choice = input(Fore.YELLOW + '''\nEnter 'next page', 'new' or 'exit': ''' + Fore.RESET).lower().strip() # user input for how to proceed after quotes printed
    if choice == 'next page' and quote_dict['last_page'] == False: # if not the last page, will proceed to next page
      pg += 1 # changes pg input in url above to next page
      break # breaks and returns to top of program to query next page
    elif choice == 'next page' and quote_dict['last_page'] == True: # if last page will automatically return to page 1
      time.sleep(1) # time delay before print
      print(Fore.YELLOW + '''\nThat was the last page...returning to page 1. ''' + Fore.RESET)
      pg = 1 # queries for page 1 with same keyword
      time.sleep(2)
      break # breaks and returns to top of program for query
    elif choice == 'new': # wil query for new keyword and resets page number
      key = input(Fore.YELLOW + '\nPlease enter a keyword to search for quotes: ' + Fore.RESET).lower().strip()
      pg = 1
      break 
    elif choice == 'exit': # will quit program when 'exit' is entered by user
      time.sleep(0.5)
      print(Fore.YELLOW + '\nGood bye!\n' + Fore.RESET) # good bye message
      exit()
    else: # input validation, returns to top of this loop after time delay to ask for input again.
      print(Fore.RED + '\nINVALID ENTRY!\n' + Fore.RESET) 
      time.sleep(0.5)






'''
Lab 20 Quote API (4/29/20)

For this lab we'll be using the [Favqs Quotes API](https://favqs.com/api) to first get a random quote, and then allow the user to find quotes by keyword. To accomplish this we'll be using the `requests` and `json` libraries. The example below uses a Chuck Norris joke API.

```python
import requests
import json

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url) # send the request to the api
print(response.text) # look at the raw json
data = json.loads(response.text) # turn the json into a python dictionary
print(data['value']) # get a part of the response data out of the dictionary
```


Version 1: Get a Random Quote

The URL to get a random quote is [https://favqs.com/api/qotd](https://favqs.com/api/qotd), 
send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.



Version 2: List Quotes by Keyword

The Favqs Quote API also supports getting a list of quotes associated with a given 
keyword `https://favqs.com/api/quotes?page=<page>&filter=<keyword>`. 
Prompt the user for a keyword, list the quotes you get in response, and prompt 
the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL.

```
> enter a keyword to search for quotes: nature
25 quotes associated with nature - page 1
<list of quotes>
> enter 'next page' or 'done': next page
25 quotes associated with nature - page 2
<list of quotes>
> enter 'next page' or 'done': done
> enter a keyword to search for quotes:
```

This API endpoint requires an API key be included in a request header. 
You can find documentation of specifying request headers [here](https://requests.readthedocs.io/en/master/user/quickstart/#custom-headers) 
and documentation on authorization with the Favqs API [here](https://favqs.com/api/) under "Authorization".

```python
url = 'https://favqs.com/api/quotes?page=1&filter=nature'
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)
```


Other Quote APIs

- [Programming Quotes](https://programming-quotes-api.herokuapp.com/)
- [Quotes Garden](https://pprathameshmore.github.io/QuoteGarden/)
  - get random quote `https://quote-garden.herokuapp.com/quotes/random`
  - get quotes by keyword `https://quote-garden.herokuapp.com/quotes/search/<keyword/
  '''