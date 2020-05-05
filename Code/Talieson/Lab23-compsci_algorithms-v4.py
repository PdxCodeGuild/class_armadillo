# Lab 23 involves a variety of algorithms.
# insertion_sort function satisfies requirements for version 4.

import random


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
            i += 1
        break
    return(items)


items = [random.randint(1, 10) for i in range(random.randint(5, 50))]
print(insertion_sort(items))
