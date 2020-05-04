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
    response = requests.get(url, headers)
    data = json.loads(response.text)
    if data['quotes'][0]['body'] == 'No quotes found':
      print('no quotes found')
    print(data['quotes']['body'] + '" - ' + quote['author'])

    for quote in data['quotes']:
      print('"' + quote['body'] + '" - ' + quote['author'])

      print()
    if data['last_page']:
      break
    next_page = input('Would you like to see the next page? (y/n): ')
