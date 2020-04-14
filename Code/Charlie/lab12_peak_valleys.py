
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
 

def peaks(data):
    output = []
    for i in range(1, len(data))-1:

        if data[1] > data[i-1] and data [i] > data[i+1]:
            output.append(i)
    return output



def valleys(data):
    output = []
    for i in range(1, len(data))-1:

        if data[1] < data[i-1] and data [i] < data[i+1]:
            output.append(i)
    return output

def peaks_and_valleys(data):
    output_peaks_valleys = []
    for i in range(1, len(data)-1):
        if data[i-1]<data[i]>data[i+1] or data[i-1]>data[i]<data[i+1]:
            output_peaks_valleys.append(i)
    return output_peaks_valleys


data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))



for value in data:
    print('x'*value)

for i in range(len(data)):
    for j in range(data[i]):
        print('x', end='')
    print()


