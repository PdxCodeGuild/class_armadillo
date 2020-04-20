

import os
import re
import pyperclip


def toc(main_path, relative_path='', depth=0):
  full_path = os.path.join(main_path, relative_path) # get the full path
  if os.path.isfile(full_path) and full_path.endswith('.md'): # if it's a file with the extension .md
    with open(full_path, 'r', encoding='utf-8') as markdown_file: # open it
      text = markdown_file.read() # read the contents
    pattern = r'^#+.+$' # a pattern for fulling out headings
    headings = re.findall(pattern, text, re.MULTILINE) # get all the headings from the file
    output = [] # our output list of dicts
    for heading in headings: # loop over the headings
      sub_depth = heading.count('#')
      heading = heading[heading.find('# ')+2:] # get the text of the heading
      sub_link = relative_path + '#' + heading.lower().replace(' ', '-') # generate the link to the path
      sub_link = sub_link.replace('\\', '/') # fix \ to /
      sub_link = sub_link.replace('`', '')
      output.append({ # add the link to the list
        'name': heading,
        'link': sub_link,
        'depth': depth + sub_depth - 2
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
        if not sub_path.endswith('.md'):
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
# print(table)
# for row in table[:200]:
#   print('  '*row['depth'] + '- [' + row['name'] + '](' + row['link'].replace(' ', '%20') + ')')




table = ['  '*row['depth'] + '- [' + row['name'] + '](' + row['link'].replace(' ', '%20') + ')' for row in table]
table = table[:400]
table = '\n'.join(table)
print(table)
pyperclip.copy(table)
