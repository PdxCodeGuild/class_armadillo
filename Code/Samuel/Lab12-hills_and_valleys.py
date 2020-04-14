# PDX Code Guild Fullstack Course
# Lab 12 Peaks and Valleys
# Samuel Purdy
# 4/13/2020

from colorama import Fore

# Sets of tests.
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
test = [1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1]
land_test = dict()


# Returns a list containing the indexes of the peaks in the list given.
def peaks(data_input):
    list_of_peaks = []
    # For each value in data_input, loop
    for i in range(1, len(data_input)-1):
        # If the value at data_input[i] is greater than the values at
        # data_input[i+1] and data_input[i-1], append list_of_valleys
        # with the current index.
        if data_input[i] > data_input[i+1] and data_input[i] > data_input[i-1]:
            list_of_peaks.append(i)
    return list_of_peaks


# Returns a list containing the indexes of the valleys in the list given.
def valleys(data_input):
    list_of_valleys = []
    # For each value in data_input, loop
    for i in range(1, len(data_input)-1):
        # If the value at data_input[i] is lesser than the values at
        # data_input[i+1] and data_input[i-1], append list_of_valleys
        # with the current index.
        if data_input[i] < data_input[i+1] and data_input[i] < data_input[i-1]:
            list_of_valleys.append(i)
    return list_of_valleys


# Returns a list containing the sorted indexes of the valleys and peaks in the
# list given.
def peaks_and_valleys(data_input):
    return sorted(peaks(data_input) + valleys(data_input))


# Gets the locations of the lakes, returning a list of tuples.
def get_tuple_lakes(data_input):
    # Predefined variables
    list_of_tuples = []
    current_peak = -1
    height = -1
    # For each index in data_input, loop
    for i in range(len(data_input)):
        # If the index is not the beginning or end of the list, continue.
        if i != 0 and i != len(data_input):
            # If the value at data_input[i] is equal to the current height,
            # continue.
            if data_input[i] == height:
                # Append list_of_tuples with current_peak, i, and the height.
                list_of_tuples.append((current_peak, i, height))
                # Resets the variables
                current_peak = -1
                height = -1
            # If the current height is height is lower than the last value in
            # data_input, return list_of_tuples.
            # This is done if the last few values in data_input aren't high
            # enough to meet the current height as to not have floating lakes.
            elif data_input[i] < height and i == len(data_input)-1:
                return list_of_tuples
            # Checks for the first peak it can detect and records the
            # information.
            elif data_input[i] > data_input[i+1] and data_input[i] > data_input[i-1]:
                current_peak = i
                height = data_input[i]
    return list_of_tuples


# Returns a dictionary with lakes filled based on the dictionary given, and
# the tuples that are given to indicate lakes.
# tuples = (lower_index_peak, high_index_peak, height_of_peaks).
def fill_lakes(tuples, land):
    # For each tuple in list tuples, loop.
    for i in range(len(tuples)):
        # For each value between lower_index_peak, and high_index_peak, loop.
        for x in range(tuples[i][0], tuples[i][1]):
            # For each value between 0 and the height, loop.
            for y in range(tuples[i][2]):
                # If the current value at the given index is not occupied by
                # land ("X"), replace it with water ("0").
                if land[x][y] != "X":
                    land[x][y] = "0"
    return land


# Prints the land using a dictionary of land, and a list of numbers.
def print_land(land_input, data_input):
    x = 0
    y = max(data_input)-1
    # While y is greater than -1, loop
    while y > -1:
        # While x is less than the number of values in data_input, loop.
        while x < len(data_input):
            # If the value at the given indexs is X, change the color of the
            # foreground to Green.
            if land_input[x][y] == "X":
                print(Fore.GREEN, end="")
            # If the value at the given indexs is 0, change the color of the
            # foreground to Blue.
            elif land_input[x][y] == "0":
                print(Fore.BLUE, end="")
            # If the index is not at the end of data_input, end with " "
            # instead of "\n".
            if x != len(data_input)-1:
                print(land_input[x][y], end=" ")
            # Else, print as normal
            else:
                print(land_input[x][y])
            x += 1
        x = 0
        y -= 1
    # Resets the color input
    print(Fore.RESET, end="")
    # Prints a line at the bottom of the land based on the length of
    # data_input.
    print("* "*len(data_input))


# Makes a land dictionary based on the input list given.
def make_dict(list_input):
    return_dict = dict()
    # For each value in list list_input, loop.
    for x in range(len(list_input)):
        # Add a new list to dictionary return_dict with key x
        return_dict.setdefault(x, [])
        i = 0
        # While i < 10, loop
        while i < max(list_input):
            # If i is less than the value of list_input[x], append the list at
            # return_dict[x]with "X", otherwise, append with " ".
            if i < list_input[x]:
                return_dict[x].append("X")
            else:
                return_dict[x].append(" ")
            i += 1
    return return_dict


# Sets land_test to the dictionary that make_dict(data) returns
land_test = make_dict(data)

# Prints the land
print_land(land_test, data)

# Prints the peaks, valleys, and lakes.
print(f"Peaks: {peaks(data)}")
print(f"Valleys: {valleys(data)}")
print(f"Peaks and Valleys: {peaks_and_valleys(data)}")
print(f"Current Lakes: {get_tuple_lakes(data)}")

# Printes the lakes in the dictionary land_test.
print_land(fill_lakes(get_tuple_lakes(data), land_test), data)

# Prints the lake locations of test.
print(get_tuple_lakes(test))

# Makes a new dictionary and prints the lakes based on the tuples
# given from test.
print_land(fill_lakes(get_tuple_lakes(test), make_dict(test)), test)
