
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks = []
valleys = []
peaks_and_valleys = []

for i in range (1, len(data)-1):
    if data[i] > data[i-1] and data[i] > data[i+1]:
        peaks.append(i)
    if data[i] < data[i-1] and data[i] < data[i+1]:
        valleys.append(i)

peaks_and_valleys = peaks + valleys

for i in range (max(data), min(data), -1):

    for j in range(len(data)):
        if data[j] >= i:
            print("X", end = " ")
        else:
            print(" ", end = " ")
    print()
print(data)
print(peaks)
print(valleys)
# row number greater then the value at index