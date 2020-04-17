
# Peaks & valleys takes a list of integers & returns indexes of numbers
# that are higher then the value before & after (peaks) & indexes of numbers
# where they are lower then the value of the index before & after (valleys)
# version 2 adds a visualization of the data.
# Version 3 allows user to input parameters for a random dataset


import random

# Take in parameters of how our mountian should look.
high = int(input("How high should we go? "))
low = int(input("How low should we go? "))
length = int(input("How far should our mountain stretch? "))

# create a random mountain range using the above parameters.
data = []
for i in range(length):
    data.append(random.randint(low, high))

# starting empty lists
peaks = []
valleys = []
peaks_and_valleys = []

# This iterates through the dataset and identifies peaks and valleys.
for i in range(1, len(data)-1):
    if data[i] > data[i-1] and data[i] > data[i+1]:
        peaks.append(i)
    if data[i] < data[i-1] and data[i] < data[i+1]:
        valleys.append(i)

peaks_and_valleys = peaks + valleys

# here we make a visual representation of the dataset with X's and print.
for i in range(max(data), min(data), -1):

    for j in range(len(data)):
        if data[j] >= i:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()

print(data)
print(peaks)
print(valleys)
# row number greater then the value at index
