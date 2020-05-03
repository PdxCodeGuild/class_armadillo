# data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]

def peaks(data): # function to determine peaks
    output_peaks = [] # empty list for storing results as for loop interates
    for i in range(1, len(data)-1): # iterates second index to next to last index
            if data[i-1]<data[i]>data[i+1]: # determines if values on both sides are lower
                output_peaks.append(i) # if so, appends list with that index value
    return output_peaks 
    

def valleys(data): # same as def peaks(), except determines vallet if value higher on both sides
    output_valleys = []
    for i in range(1, len(data)-1):
        if data[i-1]>data[i]<data[i+1]:
            output_valleys.append(i)
    return output_valleys

def peaks_and_valleys(data): # combines above functions into one
    output_peaks_valleys = []
    for i in range(1, len(data)-1):
        if data[i-1]<data[i]>data[i+1] or data[i-1]>data[i]<data[i+1]:
            output_peaks_valleys.append(i)
    return output_peaks_valleys


data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9] # input data
print(peaks(data)) # calls each function with above data
print(valleys(data))
print(peaks_and_valleys(data))



'''
Lab 12: Peaks and Valleys
Define the following functions:

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
[6, 9, 14, 17]

Version 2 (optional)
Using the data list above, draw the image of X's above.

Version 3 (optional)
Make a function that takes in the dataset and a list of peaks, and returns a list of tuples representing lakes. Each tuple should have a starting x coordinate, an ending x coordinate, and a height. The height is relative to the base of the graph.

Version 4 (optional)
Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected.

                                                  X  O  O  O  O  O  X
                                               X  X  X  O  O  O  X  X
                          X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
                       X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
'''