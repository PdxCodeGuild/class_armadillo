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