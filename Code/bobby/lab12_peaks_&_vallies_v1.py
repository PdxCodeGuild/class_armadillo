# Data given from the Lab 12 discripton
ata = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def high_points(data):
    high_points_index = []
    for i in range(len(data)):

        # Over looks the first and last index of the data list, when the data
        #  is > the index before it and > than the next index.
        if i != 0 and i != len(data) -1: 
            if data[i] > data[i - 1] and data[i] > data[i + 1]:
                high_points_index.append(i)
    return high_points_index



def low_points(data):
    low_points_index = []
    for i in range(len(data)):

        # Also over looks the first and last index of the data list, when the data
        #  is < the index before and the > then the next index.
        if i != 0 and i != len(data) -1:
            if data[i] < data[i - 1] and data[i] < data[i + 1]:
                low_points_index.append(i)
    return low_points_index


def high_and_low_points(data):
    # Combines the high_points data.
    highs_combined = high_points(data)

     # Combines the low_points data
    lows_combined = low_points(data) 

    # Combines both the the high_points and low_points data to form a new list of both
    highs_combined.extend(lows_combined)

    # This sorts the new list in ascention for lowest to highest
    highs_combined.sort()
    return highs_combined


print(high_points(data)) # [6, 14]
print(low_points(data)) # [9, 17]
print(high_and_low_points(data)) # [6, 9, 14, 17]