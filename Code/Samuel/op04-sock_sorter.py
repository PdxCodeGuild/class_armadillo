# PDX Code Guild Fullstack Course
# Optional Lab 4 Tree
# Samuel Purdy
# 4/23/2020

import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']

# Generates a random assortment of colored socks and returns it.
def generate_socks():
    socks = list()
    for i in range(100):
        socks.append((random.choice(sock_types), random.choice(sock_colors)))
    return socks

# Counts the number of socks and returns a dictionary containing 
# the number of socks for each type.
# socks = list of socks to count.
def count_socks(socks):
    sorted_socks = dict()
    # Loops through the list of socks
    for i in range(len(socks)):
        # If the socks have already been added to the dictionary, 
        # incriment their value.
        # If they are not, the will create a new entry in the dictionary 
        # and set the default value to one.
        if sorted_socks.get(socks[i][0] + " " + socks[i][1], False):
            sorted_socks[socks[i][0] + " " + socks[i][1]] += 1
        else:
            sorted_socks.setdefault(socks[i][0] + " " + socks[i][1], 1)
    # Returns the sorted numbers of socks
    return sorted_socks

# Counts the pairs of socks and returns it.
# socks_numbers = a sorted dictionary of socks
def count_pairs(socks_numbers):
    sock_pairs_and_spares = dict()
    # For every sock, it will record the number of pairs and spares, 
    # and save them to a new entry in the dictionary.
    for sock in socks_numbers:
        number_of_pairs = socks_numbers[sock] // 2
        number_of_spares = socks_numbers[sock] % 2
        sock_pairs_and_spares.setdefault(sock, (number_of_pairs, number_of_spares))
    # Returns a dictionary containing pairs and spares of sock types.
    return sock_pairs_and_spares

# Prints the socks and if they have any spare socks.
# socks_numbers_pairs is a dictionary containing the number of pairs 
# and spares of each sock type.
def print_socks(socks_numbers_pairs):
    # Loops through the dictionary of socks and prints how many pairs 
    # there are and if there are any spare socks of that type.
    for sock in socks_numbers_pairs:
        print("There are " + str(socks_numbers_pairs[sock][0]) + f" pairs of {sock} socks", end="")
        if socks_numbers_pairs[sock][1] > 0:
            print(" with 1 extra", end= "")
        print(".")

# Makes a list of socks.
socks = generate_socks()
# Counts the socks and makes a dictionary.
counted_socks = count_socks(socks)
# Counts the pairs and spares.
counted_socks = count_pairs(counted_socks)
# Prints the counted socks.
print_socks(counted_socks)