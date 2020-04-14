import random

high = int(input("How high should we go? "))
low = int(input("How low should we go? "))
length = int(input("How far should our mountain stretch? "))

data = []
for i in range (length):
    data.append(random.randint(low, high))

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