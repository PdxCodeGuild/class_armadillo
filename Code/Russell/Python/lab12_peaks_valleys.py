# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

# valleys - Returns the indices of 'valleys'. 
# A valley is a number with a higher number on both the left and the right.

# peaks_and_valleys - uses the above two functions to compile a single 
# list of the peaks and valleys in order of appearance in the original data.


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks_index = [] 
    for i in range(len(data)): 
        if i != 0 and i != len(data) -1: # excludes the indexes at the beginning and end of the data
            # if the data at an index is greater than the previous index
            # and greater than the following index, append the index number to the list
            if data[i] > data[i-1] and data[i] > data[i+1]: 
                peaks_index.append(i)                       
    return peaks_index

  


def valleys(data):
    valleys_index = [] 
    for i in range(len(data)): 
        if i != 0 and i != len(data) -1:
            if data[i] < data[i-1] and data[i] < data[i+1]: 
                valleys_index.append(i)                       
    return valleys_index

def peaks_and_valleys(data):
    peaks_combined = peaks(data)
    valleys_combined = valleys(data)
    peaks_combined.extend(valleys_combined) #adds valley data to the peaks data to make one list
    peaks_combined.sort() #sorts the combined list of idexes in ascending order
    return peaks_combined


  
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))

