"""

Lab 12: Peaks and Valleys

Define the following functions:

1. peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

2. valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both 
the left and the right.

3. peaks_and_valleys - uses the above two functions to compile a single list of the peaks and 
valleys in order of appearance in the original data.

"""
#       0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# return indices of peaks (a peak has a lower number to its left and right)
def peaks(data):
    peak_indices = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak_indices.append(i)
    return peak_indices

#return indices of valleys (a valley has larger numbers to its left and right)
def valleys(data):
    valley_indices = []
    for i in range(1, len(data)-1): 
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left > middle and right > middle:
            valley_indices.append(i)
    return valley_indices

#use the peaks and valleys functions to compile a single list of peaks and valleys in order of appearance
def peaks_valleys(data):
    pnv_indices = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            pnv_indices.append(i)
        elif left > middle and right > middle:
            pnv_indices.append(i)
    return pnv_indices

print(peaks(data)) # [6, 14]
print(valleys(data)) # [9, 17]
print(peaks_valleys(data)) # [6, 9, 14, 17]