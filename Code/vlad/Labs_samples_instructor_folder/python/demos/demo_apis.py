


import requests
import json

# from secrets import chuck_norris_api_key
# print(chuck_norris_api_key)
# exit()

# get a random quote
# response = requests.get('https://api.chucknorris.io/jokes/random') # send request to chuck norris api
# data = json.loads(response.text) # turn the json into a python dictionary
# print(data['value'])


# people_json = '{"people":[{"name":"Joe","age":123},{"name":"Jane","age":456}]}'
# # print(people[45:49]) # using string operations is not the way to go
# people_data = json.loads(people_json) # turn a json string into a python dictionary
# print(people_data['people'][0]['name']) # Joe
# people_data['people'][0]['age'] += 1 # e.g. update a value
# people_json = json.dumps(people_data) # turn a python dictionary into a json string
# print(people_json)



def get_categories():
  response = requests.get('https://api.chucknorris.io/jokes/categories')
  return json.loads(response.text)
# print(get_categories()) # ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', ...]

# def get_fact():
#   response = requests.get('https://api.chucknorris.io/jokes/random') # send request to chuck norris api
#   data = json.loads(response.text) # turn the json into a python dictionary
#   return data['value']
# print(get_fact()) # <some terrible chuck norris fact>


# def get_fact_for_category(category):
#   url = f'https://api.chucknorris.io/jokes/random?category={category}'
#   response = requests.get(url)
#   data = json.loads(response.text)
#   return data['value']
# print(get_fact_for_category('science')) # <some terrible chuck norris fact>


# a more flexible/extensible function
def get_fact(category=None):
  # if not category:
  # if category == None:
  if category is None:
    response = requests.get('https://api.chucknorris.io/jokes/random')
  else:
    url = f'https://api.chucknorris.io/jokes/random?category={category}'
    response = requests.get(url)
  data = json.loads(response.text) # turn the json into a python dictionary
  return data['value']
# print(get_fact()) # get a random fact
# print(get_fact('science')) # get a science fact







categories = get_categories() # categories is a list of strings
# print(categories)

while True:
  # prompt the user to choose a category
  print('Which category of Chuck Norris facts would you like?')
  print('Leave blank to get a random quote, or \'done\' to quit')
  # print('\n\t'.join([f'{i} {categories[i]}' for i in range(len(categories))]))
  for i in range(len(categories)):
    print(f'  {i} {categories[i]}')
  
  user_input = input('> ')
  if user_input == 'done':
    break
  elif user_input == '':
    fact = get_fact()
    print(fact)
  else:
    category_index = int(user_input)
    selected_category = categories[category_index] # get the selected category
    # print(selected_category)
    fact = get_fact(selected_category)
    print(fact)
  



