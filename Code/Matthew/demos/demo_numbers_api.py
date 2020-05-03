

import requests
import json

# testing
# url = 'http://numbersapi.com/42?json'
# response = requests.get(url)
# print(response)
# print(f'status code {response.status_code}')
# print(f'encoding {response.encoding}')
# print(f'headers {response.headers}')

# turn the json string in the response into a python dictionary
# data = json.loads(response.text)
# data = response.json()
# print(data['text'])

while True:
  type = input('What type of fact would you like to see? (math, trivia, date) ')
  if type in ['math', 'trivia', 'date']:
    if type == 'math':
      number = input('what is the number or \'random\'? ')
      url = f'http://numbersapi.com/{number}/math?json'
    elif type == 'trivia':
      number = input('what is the number or \'random\'? ')
      url = f'http://numbersapi.com/{number}?json'
    elif type == 'date':
      month_day = input('what is the month/day? ')
      url = f'http://numbersapi.com/{month_day}?json'
    response = requests.get(url)
    if response.text == '':
      print('error getting fact')
    else:
      data = response.json()
      print(data['text'])
  elif type in ['done', 'exit', 'quit']:
    break
  else:
    print('type not recognized')

