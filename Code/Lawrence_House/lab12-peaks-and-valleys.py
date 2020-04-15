data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    output = []
    for i in range(1, len(data)-1):
       if data[i] > data[i-1] and data[i] > data[i+1]:
            output.append(i)
    return output

def valleys(data):
    output = []
    for i in range(1, len(data)-1):
        if data[i]

#def peaks_and_valleys(data):
#    p = peaks(data)
#    v = valleys(data)

#p.extend(v)
#p.sort(p)



#
#data_index = len(data)
#
#print(data_index)


#for i in range(0,data_index,):
#    print(f'Index: {data_index}', f'Value: {data[i]}')

#print(peaks(data)) # [6, 14]
#
#print(valleys(data)) # [9, 17]
#
#print(peaks_and_valleys(data)) # [6, 9, 14, 17]