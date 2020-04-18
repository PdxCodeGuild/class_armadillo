

import os
import re


def toc(main_path, relative_path='', depth=0):
  
  full_path = os.path.join(main_path, relative_path)
  if os.path.isfile(full_path) and full_path.endswith('.md'):
    with open(full_path, 'r', encoding='utf-8') as markdown_file:
      text = markdown_file.read()
    pattern = r'^#+[\w ]+$'
    headings = re.findall(pattern, text, re.MULTILINE)
    output = []
    for heading in headings:
      heading = heading[heading.find('# ')+2:]
      sub_link = relative_path + '#' + heading.lower().replace(' ', '-')
      sub_link = sub_link.replace('\\', '/')
      output.append({
        'name': heading,
        'link': sub_link,
        'depth': depth
      })
    return output
  elif os.path.isdir(full_path):
    contents = os.listdir(full_path)
    output = []
    for name in contents:
      sub_path = os.path.join(relative_path, name)
      sub_link = sub_path.replace('\\', '/')
      sub_output = toc(main_path, sub_path, depth+1)
      if len(sub_output) > 0:
        output.append({
          'name': name,
          'link': sub_link,
          'depth': depth
        })
        output.extend(sub_output)
    return output
  return []


  # full_path = os.path.join(main_path, os.path.sep.join(relative_path))
  # contents = os.listdir(full_path)
  # output = []
  # for name in contents:
  #   path = os.path.join(full_path, name)
  #   if os.path.isdir(path):
  #     sub_relative_path = relative_path.copy()
  #     sub_relative_path.append(name)
  #     sub_output = toc(main_path, )
  # print(contents)


main_path = r'C:\Users\flux\programs\class_armadillo'
table = toc(main_path)
for row in table:
  print('  '*row['depth'] + '- [' + row['name'] + '](' + row['link'].replace(' ', '%20') + ')')
# print(table)














