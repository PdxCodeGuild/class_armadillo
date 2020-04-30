# Lab 20 Quote API Version 1
# Kyle Harasimowicz

import string
import random
import requests
import json
import re
bad_char = string.punctuation + string.digits
print(bad_char)

# permutations of yes and no answers
affirmatives = ['yes', 'y', 'yeah', 'yea', 'yas', 'ya', 'yah', 'yessir', 'sure', 'okay', 'fine', 'whynot', "definitely", "absolutely", "ofcourse"]
negatives = ['no', 'n', 'naw', 'nah', 'nope', 'negative', 'neg', 'definitelynot', 'noway', "absolutelynot", "ofcoursenot", "idontthinkso"]

# pulls a random quote from the 'favqs.com' website.
def generate_quote():
    response = requests.get("https://favqs.com/api/qotd")
    quote_dict = json.loads(response.text)  

    print(f"\"{quote_dict['quote']['body']}\"" )
    print(f" - {quote_dict ['quote']['author']}\n")

# Asks the user if they'd like to play again
# increased functionality uses regex to pull yes or no out of answers
def another_quote():
    while True:
        again = input("Would you like see another quote? ").lower()
        question = again
        question = question.split()
        question = ''.join(question)
        for letter in bad_char:
            question = question.replace(letter, "")
        if question in affirmatives:
            print("")
            generate_quote()
        elif question in negatives:
            question = question.title()
            print(f"{question}? Alright then - Goodbye!")
            quit()
        elif question == "maybe" or question == "perhaps":
            question = question.title()
            print(f"{question}? How about this one: ")
            print("\"The risk of a wrong decision is preferable to the terror of indecision.\"")
            print(" - Maimonides\n")
            continue
        elif question not in affirmatives and question not in negatives:
            # add a space to each side of the string, required for testing clean yes/no below
            add_spaces = len(again) + 1
            again_2 = again.rjust(add_spaces).ljust(add_spaces)
            # new variable names for clarity and to keep original question variable 
            test_for_no = again_2
            test_for_yes = again_2
            test_maybe = again_2
            # Replace all the punctuation with a space to clean text
            for letter in bad_char:
                test_for_no = test_for_no.replace(letter, ' ')
                test_for_yes = test_for_yes.replace(letter, ' ')
                test_maybe = test_maybe.replace(letter, ' ')
            
            # creat variable to test input string against several permutations of yes/no 
            # to pull a possible answer
            maybe_no = re.compile(' no | naw | nah | naw | nope | negative ')
            maybe_yes = re.compile(' yes | yea | yeah | yah | yah | affirmative ')
            maybe = re.compile(' maybe | perhaps ')
            # test no's variable against the input question, and generate response
            if maybe_no.search(test_for_no) and not maybe_yes.search(test_for_yes):
                print(f"'{again}'? I think I found a 'no' in there, somewhere. Goodbye!")
                quit()

            # test yes's variable against the input question, and generate response
            elif maybe_yes.search(test_for_yes) and not maybe_no.search(test_for_no):
                print(f"'{again}'? I think I found a 'yes' in there, somewhere. Good enough for me.\n")
                generate_quote()

            # can't get the last option below to work, testing when both [yes] and [no] appear.

            #elif maybe_yes.search(test_for_yes):
            #     if maybe_no.search(test_for_no):
            #         print(f"'{again}'...? I'm pulling a 'yes' and 'no' out of that.")
            #         print("Let's try that question again.\n")
            #         break
            
            elif maybe.search(test_maybe):
                maybe_no = maybe_no.title()
                print(f"{maybe_no}? How about this one: ")
                print("\"The risk of a wrong decision is preferable to the terror of indecision.\"")
                print(" - Maimonides\n")
                continue

            else:
                print("I'm sorry, I don't understand your response. Please answer affirmatively or negatively.")
                continue
        
        # else:
        #     print("Else option.")
        #     continue



print("Welcome to Lab 20, version 1: Quote API")
print("Here's a random quote from the website, 'FaveQs.com:'\n ")
generate_quote()
another_quote()
