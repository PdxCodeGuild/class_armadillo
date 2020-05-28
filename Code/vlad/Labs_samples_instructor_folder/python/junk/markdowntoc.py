


import os
import re

main_path = r'C:\Users\flux\programs\class_armadillo'
table = []

for root, dirs, files in os.walk(main_path, topdown=False):
  for file_name in files:
    if file_name.endswith('.md'):
      file_path = os.path.join(root, file_name)
      with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
      pattern = r'^#+[\w ]+$'
      headings = re.findall(pattern, text, re.MULTILINE)
      relative_path = os.path.relpath(file_path, main_path)
      depth = 1
      while relative_path.find('\\') != -1:
        relative_path = relative_path.replace('\\', '\n' + '  '*depth, 1)
        depth += 1
      depth -= 1
      # print(relative_path)
      
      headings = ['  '*depth + heading.replace('# ', '  - ').replace('#', '  ') for heading in headings]
      # print('\n'.join(headings))



      table.extend(relative_path.split('\n'))
      table.extend(headings)


      # depth = relative_path.count('\\') + 
      
    
print('\n'.join(table))
