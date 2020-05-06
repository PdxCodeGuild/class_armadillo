# Returns the average number of the list.
def mean(list1):
    avg_number = 0
    # loops through the list to grab all the values at each index.
    for i in list1:
        avg_number += i
    # Returns the total sum of all the values divided by the 
    # length of the list to give the average.
    return avg_number / len(list1)

# Returns the middle value in the list. 
def median(list1):
    return list1[len(list1)//2]

# Returns the mode of the list.
def mode(list1):
    number_of_occurances = dict()
    # Loops through the list to check if the number in the
    # list has occured already.
    for i in list1:
        # If the number has occured in the dictionary, it
        # will add another value at the key of the occurance
        # to record how many times it has been spotted in
        # the list.
        if number_of_occurances.get(i, False):
            number_of_occurances[i] += 1
        # If the number has not occured in the dictionary,
        # it will create another key with the default value of
        # 1 set to it as it was the first time it was recorded
        # in the list.
        else:
            number_of_occurances.setdefault(i, 1)
    # Current highest is just the first value of the list. This
    # is used to check since we can't assign a value that was
    # not in the list.
    current_highest = list1[0]
    # Loops through the loop to record the current key with the
    # highest number of occurances.
    for occurance in number_of_occurances:
        if number_of_occurances[occurance] > number_of_occurances[current_highest]:
            current_highest = occurance
    # Returns the current highest value in the dictionary.
    return current_highest

def get_number_list():
    list_of_numbers = list()
    user_input = str()
    # Loops until the user is done recording inputs for their 
    # list.
    while user_input != "done":
        user_input = input("Enter a number or \"done\" ")
        if user_input.isnumeric():
            list_of_numbers.append(int(user_input))
    # Sorts the list so we can get the median later.
    list_of_numbers.sort()
    # Returns a sorted list of numbers.
    return list_of_numbers

# Gets the number list from the user.
list_to_test = get_number_list()
# Performs operations on the list and prints them to the user.
print(f"The list of numbers: {list_to_test}")
print(f"The mean of the list: {mean(list_to_test)}")
print(f"The median of the list: {median(list_to_test)}")
print(f"The mode of the list: {mode(list_to_test)}")