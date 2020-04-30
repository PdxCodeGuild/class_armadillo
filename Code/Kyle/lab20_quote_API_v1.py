# Lab 20 Quote API Version 1
# Kyle Harasimowicz

import string
import random
import requests
import json

affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way']

def generate_quote():
    response = requests.get("https://favqs.com/api/qotd")
    quote_dict = json.loads(response.text)  

    print(f"\"{quote_dict['quote']['body']}\"" )
    print(f" - {quote_dict ['quote']['author']}\n")


def another_quote():
    while True:
        question = input("Would you like see another quote? ")
        if question in affirmatives:
            print("")
            generate_quote()
        elif question in negatives:
            question = question.title()
            print(f"{question}? Alight then - Goodbye!")
            quit()
        else:
            print("I'm sorry, I don't understand your response. Please answer affirmatively or negatively.")


print("Welcome to Lab 20, version 1: Quote API")
print("Here's a random quote from the wesbite, 'FaveQs.com:'\n ")
generate_quote()
another_quote()