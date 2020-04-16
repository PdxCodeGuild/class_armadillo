



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]




data_index = len(data)

print(f'data_index')

def peaks(data):
    output = []
    for i in range (len(data)):
       continue 
        if data[i] > data[i - 1]  and data[i] > data [i +1]:
            output.append(i)
            return output

   peak_num = int(6, 14)
   return(peak_num)
  
​
def valleys(data):
  ​valley_num = int(9, 17)
  return(valley_num) 

def peaks_and_valleys(data):
   valley_peaks = valleys + peaks
   return(valleys + peaks)
​
'''​data_index = len(data) # turning data into a index
for i in range(0,data_index,): # looping over the range of data_index
    print(f'Index: {i}', f'Value: {data[i]}') # checking the index against data




data = data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(data)) # [6, 14]
print(valleys(data)) # [9, 17]
print(peaks_and_valleys(data)) # [6, 9, 14, 17]
Collapse
