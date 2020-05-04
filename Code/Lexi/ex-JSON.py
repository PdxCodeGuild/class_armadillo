# based off of Lab 20 - quotes
# if-else for matching quotes
# practice using API key
# going through page results to yield
page =1
while True:
  keyword = input("Enter a term to search for quotes: ")
  if keyword == '':
    break
  while True:
    print(f'Page {page} for search term {keyword}') # our url
    url = ''
    headers = {'Authorization' : 'Token token ='}
    response = requests.get(url, headers) # send request to the API
    data = json.loads(response.text) # turn JSON string into a python dict
    print(data)

    #check if we got any results
    if data['quotes'][0]['body'] == 'No quotes found':
      print('no quotes found')
    print(data['quotes']['body'] + '" - ' + quote['author'])

    for quote in data['quotes']:
      print('"' + quote['body'] + '" - ' + quote['author'])

      print()

    # check if we are at the last page
    if data['last_page']:
      break

    # ask user if they want the next page
    next_page = input('Would you like to see the next page? (y/n): ')

def get_quotes(keyword,page=1):
  url = f'https:'
  headers = {'Authorization' : 'Token token ='}
  response = requests.get(url, headers) # send request to the API
  data = json.loads(response.text) # turn JSON string into a python dict
  output = []
  for quote in data['quotes']:
    output.append({
      'body': quote['body'],
      'author': quote['author'],
    })
    return output

# we are getting the JSON file then cleaning it up
data = get_quotes('nature')
print(data)
# we want to keep formatting it so it's easy to read
data = get_quotes('whale')
print(data)

exit()

