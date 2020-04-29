# PDX Code Guild Fullstack Course
# Lab 20 Quote API
# Samuel Purdy
# 4/29/2020

import requests
import json
from secrets import authorization

# Gets the data from favQs website using an API. It will return 
# all the data from a specific webpage if the tag exists. If the 
# webpage does not exist, it will return false.
# tag = the catagory of quotes the user wishes to see.
# page = the page number the user wishes to see. The default is 1 
# because thats where we want to start when looking at the quotes.
def get_data(tag, page = 1):
    address = f"https://favqs.com/api/quotes?page={page}&filter={tag}"
    response = requests.get(address, headers = authorization).text
    data = json.loads(response)
    # Checks to make sure that there is a quote for the catagory 
    # from the data given. If there is a quote, it will return 
    # the data.
    if data['quotes'][0]['id'] != 0:
        return data
    # If there were no quotes, it will print the appropriate message, 
    # then return false.
    print("That was not a valid catagory, please try another.")
    return False

# Prints the options available to the user.
# number = page number.
def print_options(number):
    print(f"                            page - {number}")
    print("\"<\" - last page   \"done\" - exit   \">\" - next page")

# Prints the quotes from the page. It also returns the current 
# page number as well.
# data = data from the webpage to load.
def print_page(data):
    for i in range(len(data['quotes'])):
        print(data['quotes'][i]['body'] + "\n")
        print(data['quotes'][i]['author'] + "\n\n")
    return data['page']

# Initializing empty variables
user_input = str()
data = None
current_page = int()
current_catagory = str()

# Loops through the entire program
while True:
    # If this is the first time running through the program, it 
    # will ask for the catagory first so it has something to print. 
    # Otherwise it will continue running as if it already has a 
    # valid catagory.
    if data == None:
        while True:
            user_input = input("Enter in a catagory you wish to view: ")
            current_catagory = user_input
            data = get_data(user_input)
            if data:
                break
    # Does whatever operation based on what option was chosen.
    # Breaks the loop and exits the program.
    if user_input == "done":
        break
    # Goes to the previous page by sending the current catagory 
    # and a new current page.
    elif user_input == "<":
        current_page -= 1
        data = get_data(current_catagory, current_page)
    # Goes to the next page by sending the current catagory and 
    # a new current page.
    elif user_input == ">":
        current_page += 1
        data = get_data(current_catagory, current_page)
    
    # Displays all quotes from the page and prints the options 
    # for the user.
    current_page = print_page(data)
    print_options(current_page)

    # This loop handles the user input from every time after the first.
    while True:
        user_input = input("Enter in an option or a catagory: ")
        # Checks to see what input the user used.
        if user_input == "done" or user_input == "<" or user_input == ">":
            # Makes sure the user didn't try to go back a page when 
            # there was no page to go back to.
            if current_page == 1 and user_input == "<":
                print("You're already at the first page!")
            # Makes sure the user didn't try to go forward a page 
            # when there was no page to go to.
            elif data['last_page'] and user_input == ">":
                print("You're already on the last page!")
            # Breaks the loop with an option instead of a catagory.
            else:
                break
        # sets the current catagory and gets the data for the user to display. 
        # If the data is valid, it will break the loop.
        else:
            current_catagory = user_input
            data = get_data(user_input)
            if data:
                break
    