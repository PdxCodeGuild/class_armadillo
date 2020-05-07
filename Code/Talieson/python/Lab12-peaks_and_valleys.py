
# Peaks & valleys takes a list of integers & returns indexes of numbers
# that are higher then the value before & after (peaks) & indexes of numbers
# where they are lower then the value of the index before & after (valleys)

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

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

print(data)
print(peaks)
print(valleys)
print(peaks_and_valleys)