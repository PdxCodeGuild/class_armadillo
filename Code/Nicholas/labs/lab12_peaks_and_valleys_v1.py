#this lab defines 3 functions based on peaks, valleys, and peaks and valleys within a list of numbers

def peaks(data_set):  #defining peaks in function
    peaks_list = []  #creates empty list
    for i in range(1, len(data_set)-1):  #establishes which indexes we will run through 
        if data_set[i] > data_set[i-1] and data_set[i] > data_set[i+1]:  #get peak values' index with if statement
            peaks_list.append(i) #adds peak indexes to list
    return peaks_list          
  
def valleys(data_set):  #defining valleys in function
    valley_list = []  #creates empty list
    for i in range(1, len(data_set)-1):
        if data_set[i] < data_set[i-1] and data_set[i] < data_set[i+1]:
            valley_list.append(i)
    return valley_list 
    
def peaks_and_valleys(data_set):  #defining peaks and valleys in function
    peak_and_valley_list = []
    for i in range(1, len(data_set)-1):
        if data_set[i] > data_set[i-1] and data_set[i] > data_set[i+1] or data_set[i] < data_set[i-1] and data_set[i] < data_set[i+1]: #adds peaks and valleys together
            peak_and_valley_list.append(i)
    return peak_and_valley_list       

data_set = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]           
print(peaks(data_set))  # [6, 14]
print(valleys(data_set))  # [9, 17]
print(peaks_and_valleys(data_set))  # [6, 9 ,14, 17]

     