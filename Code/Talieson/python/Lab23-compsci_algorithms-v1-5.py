# Lab 23 involves a variety of algorithms.
# Lab 23 v1 is satisfied by the linear search function
# Lab 23 v2 is satisfied by binary_search function
# Lab 23 v3 is satisfied by the bubble sort function
# Lab 23 v4 is satisfied by the insertion_sort function
# Lab 23 v5 uses the remaining functions
# linear and binary search work best with a non random list.
# inspired by Big-O Notation https://en.wikipedia.org/wiki/Big_O_notation
import random


def linear_search(items, value):
    for i in range(len(items)):
        if items[i] == value:
            return i


# https://en.wikipedia.org/wiki/Binary_search_algorithm
def binary_search(items, target_num):
    cur_num = 0
    len_nums = len(items)
    range_nums = len_nums - 1
    # go through the whole list
    while cur_num <= range_nums:
        # find the mid point between current spot and the end
        mid_num = ((cur_num + range_nums) / 2)
        # check if the mid is less then destination num
        if items[mid_num] < target_num:
            cur_num = mid_num + 1
        elif items[mid_num] > target_num:
            range_nums = mid_num - 1
        else:
            return mid_num
    return False


# https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(items):
    while True:
        # boolean variable checked below
        swapped = False
        # check each index
        for i in range(len(items)-1):
            # if it's bigger then the thing to it's left, swap them
            if items[i + 1] > items[i]:
                items[i], items[i + 1] = items[i + 1], items[i]
                # flip our swapped switch
                swapped = True
            # we made a swap, so leave our loop
            if swapped:
                break
        # we made it all the way through without swapping, break out
        if not swapped:
            break
    # give our sorted list back
    return items


# https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(items):
    while True:
        # This will be an iterating variable to identify what to compare
        i = 1
        # When it reaches the end of the list, we're done.
        while i < len(items):
            index = i
            # compare indexes to the one on the left, then shift if lower
            while index > 0 and items[index-1] > items[index]:
                items[index], items[index - 1] = items[index - 1], items[index]
                index -= 1
            # these are sorted, move to next iteration of comparison
            i += 1
        break
    return(items)


# https://en.wikipedia.org/wiki/Quicksort
# Main function, begins recursive function call
def quick_sort(items):
    # establish low and high variables
    quicksort_recursive(items, 0, len(items) - 1)


def quicksort_recursive(items, low, high):
    if low < high:
        list_partition = partition(items, low, high)
        quicksort_recursive(items, low, list_partition)
        quicksort_recursive(items, list_partition + 1, high)


def partition(items, low, high):
    # establishes mid number to pivot on
    pivot = items[low + (high - low) / 2]
    # iterate out from that point to get the numbers on either side
    i = low - 1
    j = high + 1
    while True:
        i += 1
        # if left item lower move it left
        while items[i] < pivot:
            j = j - 1
        while items[j] > pivot:
            if i >= j:
                # we've got our partion
                return j
        # make the swap
        items[i], items[j] = items[j], items[i]


items = [random.randint(1, 10) for i in range(random.randint(5, 50))]
# print(linear_search(items, 3))
# print(binary_search(items, 4))
# print(bubble_sort(items))
# print(insertion_sort(items))
# print(quick_sort(items))
