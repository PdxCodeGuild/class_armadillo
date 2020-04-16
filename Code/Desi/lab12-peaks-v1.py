# did you say 'i will be the llama? '
#worked with Lexi and Jon

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6]
def peaks(data):
    # show us the highest points in the data (surrounded by lower points)
    # range(start,stop,step)
    output = []
    for i in range(1, len(data)-1): #end of the data)
        print(data[i-1])
        print(data[i])
        print(data[i+1])
        print(f'Index is {i} AND Data is {data[i]}')
        if data[i] > data[i-1] and data[i] > data[i+1]:
            output.append(i)
    return output    #functions should always return - or else it's not a function

print(peaks(data))


# Index is 1 AND Data is 2
# Index is 2 AND Data is 3
# Index is 3 AND Data is 4
# Index is 4 AND Data is 5
# Index is 5 AND Data is 6
# Index is 6 AND Data is 7
# Index is 7 AND Data is 6
# Index is 8 AND Data is 5
# Index is 9 AND Data is 4
# Index is 10 AND Data is 5
# Index is 11 AND Data is 6
# Index is 12 AND Data is 7
# Index is 13 AND Data is 8
# Index is 14 AND Data is 9
# Index is 15 AND Data is 8
# Index is 16 AND Data is 7
# Index is 17 AND Data is 6
# Index is 18 AND Data is 7
# Index is 19 AND Data is 8
# Index is 20 AND Data is 9
# Index is 21 AND Data is 8
# Index is 22 AND Data is 7

def valleys(data):
    output = []
    for i in range(1, len(data)-1): #end of the data)
        if data[i] < data[i-1] and data[i] < data[i+1]:
            output.append(i)
    return output    #functions should always return - or else it's not a function

print(valleys(data))
#     # show us the lowest points in the data

# def peaks_and_valleys


# #make rows and columns
# # how do we get rows?

# # how do we get columns

# #how to print 
# hello_world = f'hello world'
# print(hello_world)