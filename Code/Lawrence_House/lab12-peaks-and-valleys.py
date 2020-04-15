#   Version 1

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    output_peaks = []
    for i in range(1, len(data)-1):
       if data[i] > data[i-1] and data[i] > data[i+1]:
            output_peaks.append(i)
    return output_peaks

def valleys(data):
    output_valleys = []
    for i in range(1, len(data)-1):
        if data[i] < data[i+1] and data[i] < data[i-1]:
            output_valleys.append(i)
    return output_valleys

def peaks_and_valleys(data):
    return sorted(peaks(data) + valleys(data))

print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
