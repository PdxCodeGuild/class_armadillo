# Problem 1

# Given a the two lists below, combine them into a dictionary.


def combine(list1, list2):
    new_dictionary = {}
    for index in range(len(list1)):
        new_key = list1[index]  # variable containing stringe value for new key
        new_value = list2[index]  # value to associate with key at same index
        new_dictionary[new_key] = new_value


fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
# combine(fruits, prices)  # {'apple':1.2, 'banana':3.3, 'pear':2.1}


# Problem 2

# Using the result from the previous problem, iterate through
# the dictionary and calculate the average price of an item.


def average_of_values(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
        average_value = round(total / len(dictionary.values()), 2)
    return average_value


combined = {'apple': 1.2, 'banana': 3.3, 'pear': 2.1}
print(average_of_values(combined))  # 2.2


# Problem 3

# Average numbers whose keys start with the same letter. Output a
# dictionary containing those letters as keys and the averages.


def unify(dictionary):

    unified_dictionary = {}

    for key in dictionary.keys():
        first_letter_of_key = key[0]

        if first_letter_of_key not in unified_dictionary.keys():
            unified_dictionary[first_letter_of_key] = dictionary[key]
        # if the key already exists in unified dictionary
        else:
            unified_dictionary[first_letter_of_key] += dictionary[key]

    for values in unified_dictionary.values():
        # we need to find an average


letter_number_pairs = {'a1': 5, 'a2': 2, 'a3': 3, 'b1': 10, 'b2': 1,
                       'b3': 1, 'c1': 4, 'c2': 5, 'c3': 6}
unify(letter_number_pairs)  # {'a': 3, 'b': 4, 'c': 5}
