#Lab 12: Peaks and Valleys Version 1

# Define the following functions:

# peaks - Returns the indices of peaks. A peak has a lower number on both 
# the left and the right.

# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both
#  the left and the right.

# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and 
# valleys in order of appearance in the original data.


# >>> peaks(data)
# [6, 14]
# >>> valleys(data)
# [9, 17]
# >>> peaks_and_valleys(data)
# [6, 9, 14, 17]


#data from instructions
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#functions to return data
def peaks(data):
    peak_nums = []
    for i in range(1, len(data)-1):
       if data[i] > data[i-1] and data[i] > data[i+1]:
            peak_nums.append(i)
    return peak_nums

def valleys(data):
    valley_nums = []
    for i in range(1, len(data)-1):
        if data[i] < data[i+1] and data[i] < data[i-1]:
            valley_nums.append(i)
    return valley_nums

def peaks_and_valleys(data):
    return sorted(peaks(data) + valleys(data))  #will combine both funtions and return the value

#will print[6,14]
print(peaks(data))

#will print[9,17]
print(valleys(data))

#will print[6,9,14,17]
print(peaks_and_valleys(data))