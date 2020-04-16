#this lab defines 3 functions based on peaks, valleys, and peaks and valleys within a list of numbers

def peaks(data):  #defining peaks in function
    peaks_list = []  #creates empty list
    for i in range(1, len(data)-1):  #establishes which indexes we will run through 
        if data[i] > data[i-1] and data[i] > data[i+1]:  #get peak values' index with if statement
            peaks_list.append(i) #adds peak indexes to list
    return peaks_list          
  
def valleys(data):  #defining valleys in function
    valley_list = []  #creates empty list
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valley_list.append(i)
    return valley_list 
    ...
def peaks_and_valleys(data):  #defining peaks and valleys in function
    peak_and_valley_list = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1] or data[i] < data[i-1] and data[i] < data[i+1]: #adds peaks and valleys together
            peak_and_valley_list.append(i)
    return peak_and_valley_list       

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]           
print(peaks(data))  # [6, 14]
print(valleys(data))  # [9, 17]
print(peaks_and_valleys(data))  # [6, 9 ,14, 17]

for i in range(max(data), 0, -1):  #this creates peaks and valleys diagram with X's
    for x in range(len(data)):
        if i <= data[x]:
            print('X', end='')
        else:
            print(' ', end='')    
    print()        