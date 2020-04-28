# demo_regex #3 April 28 2020:

import requests
import re

# get random books from project gutenberg
def get_random_books():
  response = requests.get('https://www.gutenberg.org/ebooks/search/?sort_order=random')
  text = response.text
  links_pattern = r'\/ebooks\/(\d+)'
  titles_pattern = r'class="title">(.+)<\/span>'
  links = re.findall(links_pattern, text)
  titles = re.findall(titles_pattern, text)
  print(links)
  # print(titles)

  # ['/ebooks/3256', '/ebooks/58647'...] -> ['gutenberg.org/ebooks/3256/', ..]
  # links = ['https://www.gutenberg.org/' + link for link in links]

  # will not work for book urls like http://www.gutenberg.org/cache/epub/21301/pg21301.txt
  links = [f'https://www.gutenberg.org/files/{code}/{code}-0.txt' for code in links]
  titles = titles[3:] # remove the first 3 results
  
  # zip turns two lists into a list of tuples
  # the first element of each tuple is from the first list
  # the second element of each tuple is from the second list
  # return list(zip(titles, links))

  # return a list of dictionaries
  books = []
  for i in range(len(titles)):
    books.append({
      'title': titles[i],
      'link': links[i]
    })
  return books








books = get_random_books()
for i in range(len(books)):
  print(i, books[i]['title'])
book_index = int(input('Which book would you like to see? '))
response = requests.get(books[book_index]['link'])
text = response.text
print(text)
