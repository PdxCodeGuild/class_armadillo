# Lab 12 Peaks and Valleys
# Troy Fitzgerald

'''Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

Visualization of test data:

Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
POI							P			V					P			V			
Example I/O:

                                                      X                 X
                                                   X  X  X           X  X
                              X                 X  X  X  X  X     X  X  X
                           X  X  X           X  X  X  X  X  X  X  X  X  X
                        X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
>>> peaks(data)
[6, 14]
>>> valleys(data)
[9, 17]
>>> peaks_and_valleys(data)
[6, 9, 14, 17]'''

'''Version 1'''
# imports the module.
import random

# data in a list for determining peaks and valleys.
data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]

# defines the function. 
def find_peaks(data):
    # blank list.
    peak = []
    # for loop for going over the indices for peaks.
    for i in range(1, len(data)-1): 
        left_limit = data[i-1]
        middle_point = data[i]
        right_limit = data[i+1]
        if left_limit < middle_point and right_limit < middle_point:
            peak.append(i)
    return peak
print(find_peaks(data))


# defines the function.
def find_valleys(data):
    # blank list.
    valley = []
    # for loop for going over the indices for valleys.
    for i in range(1, len(data)-1):
        left_limit = data[i-1]
        middle_point = data[i]
        right_limit = data[i+1]
        if left_limit > middle_point and right_limit > middle_point:
            valley.append(i)
    return valley
print(find_valleys(data))

# defines function for combining the peaks and valleys indices.
def peaks_and_valleys(peaks, valleys):
    
    print(peaks + valleys)
# combines function results in a list.    
peaks_and_valleys(find_peaks(data), find_valleys(data))





    







