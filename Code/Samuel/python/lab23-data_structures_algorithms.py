# PDX Code Guild Fullstack Course
# Lab 23 Rain Data
# Samuel Purdy
# 5/5/2020

import random
import math

# Node Class
class Node:

    # Initializes the object
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    # Returns the elements in the object
    def __str__(self):
        return f'({self.element}, {self.next is not None})'

# Stack Class
class Stack:

    # Initializes the object
    def __init__(self):
        self.root = None
    
    # Sets the new root to a node with element given, and sets 
    # the next variable to what the current root address is.
    # element = is the new item thats being pushed at the top 
    # of the stack.
    def push(self, element):
        self.root = Node(element, self.root)

    # Saves the current element to a variable, then sets the 
    # current root to the Node(next) root and returns the 
    # saved variable.
    def pop(self):
        number = self.root.element
        self.root = self.root.next
        return number

    # Returns the element if there is a Node, None if there 
    # is not.
    def peek(self):
        return self.root.element if self.root != None else None
    
    # Returns a number of roots that contain nodes by looping 
    # through each Node(next)
    def length(self):
        current_node = self.root
        count = 0
        # Counts each non-none Node in the stack
        while current_node != None:
            count += 1
            current_node = current_node.next
        return count

    # Used to print the root.
    def __str__(self):
        return f"{self.root}"

# Returns the index of the target in a given list of integers. 
# If the number is not there, it will return none. It's slow 
# because it goes through each index one at a time with no 
# basis of searching or sorting. This is best utilized in a 
# unsorted list.
# list_of_numbers = a list of numbers to search through.
# target = the target we are searching for.
def linear_search(list_of_numbers, target):
    for number in range(len(list_of_numbers)):
        if list_of_numbers[number] == target:
            return number
    return None

# Returns the index of the target in a given list of integers. 
# If the number is not there, it will return none. This 
# searching algorithm is fast and only works with a sorted list. 
# If a list is not sorted, it will take about as long as the 
# linear search.
# list_of_numbers = a list of numbers to search through.
# target = the target we are searching for.
def binary_search(list_of_numbers, target):
    
    #Records a low and high index to search through.
    low_index = 0
    high_index = len(list_of_numbers) - 1
    
    # Loops until all indexs have been checked.
    while low_index <= high_index:
        
        # Sets the mid index to the middle of both the high and 
        # low index.
        mid_index = ((high_index + low_index) // 2)

        # If the target is greater than the mid, the low_index 
        # will be set to the mid index
        if list_of_numbers[mid_index] < target:
            low_index = mid_index
        # If the target is lower than the mid, the high_index 
        # will be set to the mid index
        elif list_of_numbers[mid_index] > target:
            high_index = mid_index
        # This assumes that the value at mid_index is the 
        # target and returns the index.
        else:
            return mid_index
    return None

# Returns a sorted list by moving two items at a time.
# list_of_numbers = A list of numbers to sort.
def bubble_sort(list_of_numbers):
    sorted_list = False

    # Keeps looping while the list is not sorted.
    while not sorted_list:
        for i in range(len(list_of_numbers) - 1):

            # If the current index is not the end of 
            # the list it will swap the two variables 
            # if the current indexed variable is 
            # greater than the next.
            if i != len(list_of_numbers) - 1:
                if list_of_numbers[i] > list_of_numbers[i + 1]:
                    save = list_of_numbers[i + 1]
                    list_of_numbers[i+1] = list_of_numbers[i]
                    list_of_numbers[i] = save

        # Loops through the list to see if all the numbers 
        # are sorted by seeing if the current indexed 
        # number is lesser than the next indexed number.
        for i in range(len(list_of_numbers) - 1):
            if i != len(list_of_numbers) - 1:
                if list_of_numbers[i] < list_of_numbers[i + 1] or list_of_numbers[i] == list_of_numbers[i + 1]:
                    sorted_list = True
                else:
                    sorted_list = False
                    break

    return list_of_numbers

# Sorts the list by using a divide and conquer algorithm 
# as well as recursion.
# list_of_numbers = A list of numbers to sort.
def quick_sort(list_of_numbers):
    low = list()
    high = list()

    # If there are no elements in the list, it will just 
    # return the list.
    if len(list_of_numbers) == 0:
        return list_of_numbers

    # Sets the pivot to the first variable of the list, 
    # then removes it from the list.
    pivot = list_of_numbers[0]
    list_of_numbers.remove(pivot)

    # Sorts the list of numbers into two seperate lists 
    # with the pivot as the delimiter, checking whether 
    # or not the current indexed element is lesser than 
    # or equal to, or greater than the pivot.
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] <= pivot:
            low.append(list_of_numbers[i])
        else:
            high.append(list_of_numbers[i])

    # Returns if one or both lists have just one variable in them.
    if len(low) == 1 and len(high) == 1:
        return [low[0], pivot, high[0]]
    elif len(low) == 1:
        return [low[0], pivot] + high
    elif len(high) == 1:
        return low + [pivot, high[0]]

    # Quicksorts the lower half and the higher half if there are 
    # more elements. This is where the recursion takes place if the 
    # list of numbers is extremely long.
    low_half = quick_sort(low)

    # Appends the pivot so it is saved in the end.
    low_half.append(pivot)
    high_half = quick_sort(high)

    # Returns a fully completed list.
    return low_half + high_half

# Tests
if __name__ == "__main__":
    
    numbers = [1,2,3,4,5,6,7,8,9]
    numbers1 = [8,35,12,2,4,6,34,7,2,9]
    numbers2 = [8,35,12,2,4,6,34,7,2,9]

    print(linear_search(numbers, 9))
    print(binary_search(numbers, 1))
    print(bubble_sort(numbers1))
    print("-"*40)
    print(quick_sort(numbers2))

    s = Stack()
    s.push(5)
    s.push(6)
    print(s.length()) # 2
    print(s.pop()) # 6
    print(s.pop()) # 5