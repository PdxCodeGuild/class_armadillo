data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak = []
valley = []
highs_and_lows = []
new_highs_and_lows = []
first_point = ""
third_point = ""
second_point = ""

# runs through the set of data, checking to see where the apex is
# compares each point to the point before and after to determine 'peak'
def peak_finder(data):
    peak = []
    for i in range(1, len(data)-1): 
        first_point = data[i-1]
        second_point = data[i]
        third_point = data[i+1]
        if first_point < second_point and third_point < second_point:
            peak.append(i)
    return peak


# runs through the set of data, checking to see where the 'bottom' is
# compares each point to the point before and after to determine 'valley'
def valley_finder(data):
    valley = []
    for i in range(1, len(data)-1):
        first_point = data[i-1]
        second_point = data[i]
        third_point = data[i+1]
        if first_point > second_point and second_point < third_point:
            valley.append(i)
    return valley


# runs through the set of data, checking to see where the apex and bottom are
# compares each point to the point before and after to determine 'peak'
# if the point, isn't a 'peak,' check to determine if it's a 'valley'
# if either, appends to the list 'highs_and_lows' 
def peaks_and_valleys(data):
    highs_and_lows = []
    for i in range(1, len(data)-1):
        first_point = data[i-1]
        second_point = data[i]
        third_point = data[i+1]
        if first_point < second_point and third_point < second_point:
            highs_and_lows.append(i)
        elif first_point > second_point and second_point < third_point:
            highs_and_lows.append(i)
    return highs_and_lows

# function takes the first two peaks and valleys functions,
# concatenates them into a new list,
# and then sorts that list to produce peaks and valleys, in order
def peaks_and_valleys_sorted(data):
    new_highs_and_lows = []
    new_highs_and_lows = peak_finder(data) + valley_finder(data)
    new_highs_and_lows = sorted(new_highs_and_lows)
    #print(new_highs_and_lows)
    return new_highs_and_lows


print("Welcome to Lab 12: Peaks and Valleys!")
print("We have a list of data:")
print(data)
print(f"The peaks in the list 'data' are at indexes: {peak_finder(data)}")
print(f"The valleys in the list 'data' are at indexes: {valley_finder(data)}")
print(f"The indexes of the peaks and valleys, in order, are: {peaks_and_valleys(data)}")
print("You could also combine your two peaks and valleys lists, ")
print("by declaring a new list (new_highs_and_lows), and concatenating your first two lists")
print(f"and then use the 'sorted()' function to get a NEW list of peaks and valleys: {peaks_and_valleys_sorted(data)}")
print(f"SEE? {peaks_and_valleys(data)} = {peaks_and_valleys_sorted(data)}. ")


