
import random


def peaks(data):
  output = []
  for i in range(1, len(data)-1):
    if data[i] > data[i-1] and data[i] > data[i+1]:
          
      output.append(i)

  # for i in range(len(data)):
    # if i == 0 or i == len(data)-1:
    #   continue
    # if data[i] > data[i-1] and data[i] > data[i+1]:
    #   output.append(i)

    # if i != 0 and i != len(data)-1:
    #   if data[i] > data[i-1] and data[i] > data[i+1]:
    #     output.append(i)

    # if i != 0 and i != len(data)-1 and data[i] > data[i-1] and data[i] > data[i+1]:
    #   output.append(i)
  return output


def valleys(data):
  output = []
  for i in range(1, len(data)-1):
    if data[i] < data[i-1] and data[i] < data[i+1]:
      output.append(i)
  return output

def peaks_and_valleys(data):
  p = peaks(data)
  v = valleys(data)
  p.extend(v)
  p.sort()
  return p

  # output = []
  # for i in range(1, len(data)-1):
  #   if (data[i] > data[i-1] and data[i] > data[i+1]) or (data[i] < data[i-1] and data[i] < data[i+1]):
  #     output.append(i)
  # return output



# data = []
# for i in range(20):
#   data.append(random.randint(1, 9))
# print(data)

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(data)) # [6, 14]
print(valleys(data)) # [9, 17]
print(peaks_and_valleys(data)) # [6, 9, 14, 17]


# printing vertically - v1
# for value in data:
#   print('x'*value)

# printing vertically - v2
# for i in range(len(data)):
#   for j in range(data[i]):
#     print('x', end='')
#   print()

# printing horizontally
for i in range(max(data), 0, -1): # down the rows
  for j in range(len(data)): # across the columns
    if i <= data[j]: # if the current row index is less than the value at that column
      print('X', end='')
    else:
      print(' ', end='')
  print()

pks = peaks(data)
vys = valleys(data)

for i in range(len(data)):
  if i in pks:
    print('P', end='')
  elif i in vys:
    print('V', end='')
  else:
    print(' ', end='')
print()
