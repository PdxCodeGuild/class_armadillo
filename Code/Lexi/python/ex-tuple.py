import requests
import re

def get_random_books():
  response = requests.get('http://www.gutenberg.org/ebooks/search/?sort_order=random')
  # return URL
  text = response.text
  # looking for path
  links_pattern = r'\/ebooks\/(\d+)'
  # looking for class attribute
  titles_pattern = r'class="title">(.+)<\/span>'
  # yields all results with those two params
  links = re.findall(links_pattern, text)
  # titles are found
  titles = re.findall(titles_pattern, text)
  # print links
  print(links)
  print(titles)
# naming 'text' var

# will

books = get_random_books()
# response obj equals the value link
response = requests.get(books[book_index]['link'])
text = response.text
print(text)