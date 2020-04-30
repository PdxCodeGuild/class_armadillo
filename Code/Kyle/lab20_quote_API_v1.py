# Lab 20 Quote API Version 1
# Kyle Harasimowicz

import string
import random
import requests
import json
import re
punctuation = string.punctuation
print(punctuation)

affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'whynot', "definitely", "absolutely", "ofcourse"]
negatives = ['no', 'n', 'nope', 'negative', 'definitelynot', 'noway', "absolutelynot", "ofcoursenot", "idontthinkso"]

def generate_quote():
    response = requests.get("https://favqs.com/api/qotd")
    quote_dict = json.loads(response.text)  

    print(f"\"{quote_dict['quote']['body']}\"" )
    print(f" - {quote_dict ['quote']['author']}\n")


def another_quote():
    while True:
        again = input("Would you like see another quote? ").lower()
        question = again
        question = question.replace(punctuation, ' ')
        question = question.split()
        question = ''.join(question)
        if question in affirmatives:
            print("")
            generate_quote()
        elif question in negatives:
            question = question.title()
            print(f"{question}? Alight then - Goodbye!")
            quit()
        elif question not in affirmatives and question not in negatives:
            again = again.replace(punctuation, " ")
            maybe_no = re.compile(' no ')
            if maybe_no.search(again):
                print(f"'{again}'? My best guess is that's probably a negative. Goodbye!")
                quit()
            else:
                print("I'm sorry, I don't understand your response. Please answer affirmatively or negatively.")
                
        else:
            print("I'm sorry, I don't understand your response. Please answer affirmatively or negatively.")


# def maybe_a_no():
#     test = input("Question:").lower()
#     maybe_no = re.compile('no ')
#     if maybe_no.search(test):
#         print("User answer is probably a negative")
#     else:
#         print("I don't understand your answer")


print("Welcome to Lab 20, version 1: Quote API")
print("Here's a random quote from the website, 'FaveQs.com:'\n ")
#generate_quote()
another_quote()
#maybe_a_no()