
def peaks(data):
[6, 14] [6, 5, 7] [6,11,9]

def valleys(data):
[9, 17] [5, 8, 4][ 9, 14, 6]

def peaks and valleys(data):
[6, 9, 14, 17]

data = [1, 2, 3, 4, 5, 6, 7, 8, ]
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))

data = 1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9

data_index = len(data)

for i in range (0, data_index,):
    print(f"Index: {i}")










Lab 12: Peaks and Valleys
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both 
the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and 
valleys in order of appearance in the original data.

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