import random
import math

class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'

test = Node(1)
test2 = Node(3, id(test))

class Stack:
    def __init__(self):
        self.root = None
    def push(self, element): # insert an element at the start (new root)
        self.root = Node(element, self.root)
    def pop(self): # remove an element from the start (the root becomes the next node)
        number = self.root.element
        self.root = self.root.next
        return number
    def peek(self): # returns the element on the root node or None if there is no root
        return self.root.element if self.root != None else None
    def length(self): # return the number of elements
        current_node = self.root
        count = 0
        while current_node != None:
            count += 1
            current_node = current_node.next
        return count
    def __str__(self):
        return f"{self.root}"

s = Stack()
s.push(5)
s.push(6)
print(s.length()) # 2
print(s.pop()) # 6
print(s.pop()) # 5

def linear_search(list_of_numbers, target):
    for number in range(len(list_of_numbers)):
        if list_of_numbers[number] == target:
            return number
    return None

def binary_search(list_of_numbers, target):
    low_index = 0
    high_index = len(list_of_numbers) - 1
    
    while low_index <= high_index:
        
        mid_index = ((high_index + low_index) // 2)
        if list_of_numbers[mid_index] < target:
            low_index = mid_index
        elif list_of_numbers[mid_index] > target:
            high_index = mid_index
        else:
            return mid_index
    return None

def bubble_sort(list_of_numbers):
    sorted_list = False
    while not sorted_list:
        for i in range(len(list_of_numbers) - 1):
            # print(i)
            if i != len(list_of_numbers) - 1:
                if list_of_numbers[i] > list_of_numbers[i + 1]:
                    save = list_of_numbers[i + 1]
                    list_of_numbers[i+1] = list_of_numbers[i]
                    list_of_numbers[i] = save
        for i in range(len(list_of_numbers) - 1):
            # print(i)
            if i != len(list_of_numbers) - 1:
                print(list_of_numbers[i], list_of_numbers[i+1])
                if list_of_numbers[i] < list_of_numbers[i + 1] or list_of_numbers[i] == list_of_numbers[i + 1]:
                    sorted_list = True
                else:
                    sorted_list = False
                    break
    return list_of_numbers

def quick_sort(list_of_numbers):
    print(list_of_numbers)
    low = list()
    high = list()

    if len(list_of_numbers) == 0:
        return list_of_numbers

    pivot = list_of_numbers[0]
    list_of_numbers.remove(pivot)

    for i in range(len(list_of_numbers)):
        # print(i)
        if list_of_numbers[i] <= pivot:
            low.append(list_of_numbers[i])
        else:
            high.append(list_of_numbers[i])
    if len(low) == 1 and len(high) == 1:
        return [low[0], pivot, high[0]]
    elif len(low) == 1:
        return [low[0], pivot] + high
    elif len(high) == 1:
        return low + [pivot, high[0]]

    # print(low, pivot, high)
    low_half = quick_sort(low)
    # print(low_half)
    low_half.append(pivot)
    high_half = quick_sort(high)
    # print(high_half)

    return low_half + high_half

if if __name__ == "__main__":
    
    numbers = [1,2,3,4,5,6,7,8,9]
    numbers1 = [8,35,12,2,4,6,34,7,2,9]
    numbers2 = [8,35,12,2,4,6,34,7,2,9]

    print(linear_search(numbers, 9))
    print(binary_search(numbers, 1))
    print(bubble_sort(numbers1))
    print("-"*40)
    print(quick_sort(numbers2))