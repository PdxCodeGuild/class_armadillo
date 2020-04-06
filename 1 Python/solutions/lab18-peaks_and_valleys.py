"""
Lab 18: Peaks and Valleys
find 'peaks' and 'valleys' in a list of ints
a 'peak' is a number which is greater than the number on the left and right
a 'valley' is a number which is less that the number on the left and right

                                                      X                 X
                                                   X  X  X           X  X
                              X                 X  X  X  X  X     X  X  X
                           X  X  X           X  X  X  X  X  X  X  X  X  X
                        X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# >>data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# >>> peaks(data)
# [6, 14]
# >>> valleys(data)
# [9, 17]
"""


import random

# find the indices of the peaks
def peaks(data):
    peak_indices = []
    for i in range(1, len(data)-1): #loop through the list, avoiding the end-points
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak_indices.append(i)
    return peak_indices


# def peaks2(data):
#     r = []
#     for i in range(len(data)):
#         if i == 0 or i == len(data)-1:
#             continue
        



# find the indices of the valleys
def valleys(data):
    valley_indices = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left > middle and right > middle:
            valley_indices.append(i)
    return valley_indices



'''
Here's an alternative version, using a regular for-loop with continue to over the first and last values.

def peaks(data):
    peak_indices = []
    for i in range(len(data)): #loop through the list, avoiding the end-points
        if i == 0 or i == len(data)-1:
            continue
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak_indices.append(i)
    return peak_indices
'''


def draw(data):
    largest = max(data)
    for i in range(largest, 0, -1):
        row = ''
        for j in range(len(data)):
            if i <= data[j]:
                row += 'X'
            else:
                row += ' '
        print(row)


def let_it_rain(x):
    r = 0
    for j in range(max(x)):
        i = 0
        while i < len(x) and x[i] < j:  # skip over openings on the left
            i += 1
        while i < len(x):
            if x[i] < j:  # trace out a valley
                i0 = i
                while i < len(x) and x[i] < j:  # find the other side of the valley
                    i += 1
                if i == len(x):  # we went off the right side
                    break
                else:  # we reached the other end of a valley
                    r += i - i0 + 1
            i += 1

    return r



def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    
    draw(data)
    
    data = []
    for i in range(20):
        data.append(random.randint(1,10))
        
    draw(data)
    
    print()
    print()
    
    
    data = []
    current_value = 5
    direction = random.choice([-1, 1])
    for i in range(20):
        data.append(current_value)
        current_value += direction
        if current_value < 1:
            current_value = 1
            direction = 1
        else:
            if random.random() < 0.2:
                direction = random.choice([-1, 1])
    draw(data)
    
    # for datum in data:
        # print('x'*datum)
        # for i in range(datum):
        #     print('x', end='')
        # print()
    
    #print(peaks(data))
    #print(valleys(data))
    # draw(data)
    # print()
    # print()
    # print()
    # print(let_it_rain(data))

main()



















