# Lab 23 involves a variety of algorithms.
# Lab 23 v3 is satisfied by the bubble sort function

import random


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


items = [random.randint(1, 10) for i in range(random.randint(5, 50))]
print(bubble_sort(items))
