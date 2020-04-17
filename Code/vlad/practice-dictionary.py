#Practice Problems: Dictionaries
"""
Practice Problems: Dictionaries https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/practice/practice04-dictionaries.md (edited) 
"""

# Dictionaries Practice
# April 15, 2020

# dictionaries are key:value pairs where the value
# is referenced by calling the key within the dictionary

# dictionary values can contain any datatype,
# including lists and other dictionaries

# fruit_prices = {
#     'apple': .35,
#     'blueberries': .99, 
#     'peaches': .5
# }

# print(fruit_prices['apple'])

# fruit_prices['apple'] = .75  # to replace the value at a specific key

# print(fruit_prices['apple'])

# ----------------------------------------------------------------- #

# Problem 1

def combine(list1, list2):
    '''
    Given a the two lists below, combine them into a dictionary.
    '''

    new_dictionary = {}       # method 1 to create blank dictionary
    # new_dictionary = dict() # method 2 for blank dictionary

    for index in range(len(list1)):
        # print(f"index = {index}")
        # print(f'{index = }')  # New syntax in Python 3.8 to print a variable with a label

        new_key = list1[index]   # variable contiaining string value for new key
        new_value = list2[index] # variable containing value to associate with new key

        # set the value at the new key in the dictionary to the new value
        new_dictionary[new_key] = new_value  

    return new_dictionary


# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]

# print(combine(fruits, prices))

# ----------------------------------------------------------------- #


# Problem 2

def average_of_values(dictionary):
    '''
    Iterate through a dictionary and calculate the average price of an item.
    '''

    total = 0  # current total value
    number_of_values = len(dictionary.values())  # number of values in dictionary

    # loop through each value in the dictionary

    # dictionary.values() and .keys() return iterable objects. Not lists.
    # They can be looped through, but not subscripted with [] and index values

    for value in dictionary.values():
        # add each consecutive value in the dictionary to the total
        total += value  

    # calculate the average value
    # round to avoid endless decimals
    average_value = round(total / number_of_values, 2) 

    return average_value 

combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}

# print(average_of_values(combined))

# ----------------------------------------------------------------- #


# Problem 3
  
def unify(dictionary):
    '''
    Average numbers whose keys start with the same letter. 
    Output a dictionary containing those letters as keys and the averages.
    '''
    # will hold the sum of the values for each letter key
    unified = {}

    # will hold the total of occurances of each letter key  
    key_counts = {}
    
    # loop through each item in the dictionary,
    # unpacking the (key,value) tuple for each item
    for key, value in dictionary.items():

        # if the first letter of each key is not in the unified dict
        if key[0] not in unified:
            
            # add the key to the unified dict and set its initial value
            # to the value to the current value of the original dict
            unified[key[0]] = value

            # do the same with the counts dict,
            # except the start value will be 1 because
            # this is the first occurance of that key
            key_counts[key[0]] = 1
        
        # if they current key is already in each dict
        else:
            # add the value to the value at the current key in the unified dict
            unified[key[0]] += value
            # increment the count for the current key
            key_counts[key[0]] += 1

    # print(f"{unified = }")
    # print(f"{key_counts = }")

    # loop through all the keys in the unified dict    
    for key in unified:

        # divide the total at each key by the number of occurances of that key
        # floor division gives an integer amount. Regular division gives floats
        unified[key] //= key_counts[key]  
        
    # return the newly unified dictionary
    return unified

my_dictionary = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

#  A different dictionary with more keys:
#  my_dictionary = {
#     'a1':5, 'a2':2, 'a3':3, 'a4': 55, 'a5':3, 
#     'b1':10, 'b2':1, 'b3':1, 'b4':45, 
#     'c1':4, 'c2':5, 'c3':6, 'c4':88
# }

print(unify(my_dictionary))

# ----------- #
# ----------- #
# uncommented version of the above solution:

# def unify(dictionary):
#     '''
#     Average numbers whose keys start with the same letter. 
#     Output a dictionary containing those letters as keys and the averages.
#     '''    
#     unified = {}
#     counts = {}  

#     for key, value in dictionary.items():

#         if key[0] not in unified:
#             unified[key[0]] = value
#             counts[key[0]] = 1   

#         else:
#             unified[key[0]] += value
#             counts[key[0]] += 1  

#     print(f"{unified = }")
#     print(f"{counts = }")

#     for key in unified:
#         unified[key] //= counts[key] 

#     return unified  

# ---------- #
# ---------- #
# Incomplete solution from live-coding in class:

# def unify(dictionary):

#     unified_dictionary = {}

#     # loop through each key in original dictionary
#     for key in dictionary.keys():
        
#         # grab the first letter of the current key
#         first_letter_of_key = key[0]

#         # if the first letter of the key is not already in the new dictionary, add it
#         if first_letter_of_key not in unified_dictionary.keys():

#             # create a new key that is the first letter of the original key
#             # and assign the original value to it.
#             unified_dictionary[first_letter_of_key] = dictionary[key]
        
#         # if the new key already exists in the new dictionary
#         else:

#             # add the value at the original key to the new dictionary at the new key
#             unified_dictionary[first_letter_of_key] += dictionary[key]

#     # for value in unified_dictionary.values():


# ---------- #
# ---------- #

# MISC

# employees = {
#     '001': {
#         'first_name': 'Keegan',
#         'last_name': 'Good',
#         'address': '123 Faux Ave'
#     },
#     '002': 'Jon',
#     '003': 'Matthew',
# }

# employee = employees['001']

# print(employees['001']['address'])