# rain data lab 22

# maybe we want to use regex and list of dicts as a tuple

# from module import a class
from datetime import datetime

# date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# date = datetime.strptime('03/25/2016', '')

date = datetime.strptime(date_str, '%d-%b-%Y')
print(date)

# access the properties of that obj
# print(date.year)
# print(data.month)
# print(date.day)
# print(date)

date_tuple = (date.year, date.month, date.day)
print(date_tuple)

#turn the datetime object back into a string
print(data.strftime('%d-%b-%Y'))

exit()

text = '''
'''

# see line 16 of matt's rain files

# it's a list comprehension

