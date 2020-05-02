import datetime
from re import findall
from math import ceil

# define the path and open text file
text_path = "D:\Learn Coding\Videos\class_armadillo\Code\Desi\rain_data_example_code.txt"
with open(text_path, "r") as file:
    text = file.read()

date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016