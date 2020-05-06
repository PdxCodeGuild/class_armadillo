import random
import math


def linear_search(num_list, value):

    for number in range(len(num_list)):
        if num_list[number] == value:
            return number
    else:
        print('no value found')
        
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
index = num_list.index(2)
print(index)


    


def binary_search(num_list, value):
    low_number = num_list[0]
    high_number = num_list[-1]
    while low_number <= high_number:
        middle_number = ((low_number + high_number) / 2)
        
        if num_list[middle_number] < value:
            low_number = middle_number + 1
            return middle_number
        elif num_list[middle_number] > value:
            high_number = middle_number - 1
            return middle_number
        
        else:
            return middle_number


num_list = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(num_list, 8)
print(index)
