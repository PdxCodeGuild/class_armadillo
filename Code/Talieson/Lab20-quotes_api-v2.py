import requests
import json
from secrets import qotd_head


def get_quote():
    # Request JSON info from the quote API, store in response.
    response = requests.get("https://favqs.com/api/qotd")
    # Parse the data into a dictionary.
    data = json.loads(response.text)
    # Print a string containing the quote and author of the quote.
    return(f'''  \"{data['quote']['body']}\"
        - {data['quote']['author']}''')


# our function to return a single quoute from a search of categories.
def get_quotes_by_category(category, num, page):
    url = f"https://favqs.com/api/quotes?page={page}&filter={category}"
    response = requests.get(url, headers=qotd_head)
    data = json.loads(response.text)

    # If we don't get a quote back, return False.
    if data['quotes'][0]['body'] == 'No quotes found':
        print("ERROR: there are no quotes in that category.")
        return False
    # Otherwise, return our quote.
    else:
        return(f'''  \"{data['quotes'][num]['body']}\"
        - {data['quotes'][num]['author']}''')


# main run loop.
while True:
    # this determines the index of the category list that will be returned.
    quote_number = 0
    page = 1
    valid_choice = False
    # Main user input
    category = input('''
Enter quote category or random to generate a quote.
If you're finished, enter exit.
    ''').lower().strip()
    print()
    if category == "exit":
        exit()
    # if user need a random quote, call our first function.
    elif category == "random":
        print(get_quote())
    # if user wants a category, call our 2nd function that searches
    else:
        # make sure it's a valid search, and flip our valid_choice
        if get_quotes_by_category(category, quote_number, page):
            print(get_quotes_by_category(category, quote_number, page))
            valid_choice = True
        # Enter a second loop that allows for more quotes from that category
        while valid_choice:
            another = input("Another quote from this category? (Y/N) ").upper()
            # if the quote is on the first page, call our function.
            if another == "Y" and quote_number < 24:
                # access the next index of the list of quotes
                quote_number += 1
                print(get_quotes_by_category(category, quote_number, page))
            # if we've reached the end of the page, go to the next, reset index
            elif another == "Y" and quote_number >= 24:
                page += 1
                quote_number = 0
                get_quotes_by_category(category, quote_number, page)
            elif another == "N":
                break
            else:
                print("Please enter a valid response.")
