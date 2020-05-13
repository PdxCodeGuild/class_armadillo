# Lab 23 Computer Science - Data Structures & Algorithms Version 3: 


# Version 3 - Bubble Sort (optional)
# Bubble sort is one of the simplest and least efficient sorting algorithms. We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.

procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped = false
        for i := 1 to n - 1 inclusive do
            /* if this pair is out of order */
            if A[i - 1] > A[i] then
                /* swap them and remember something changed */
                swap(A[i - 1], A[i])
                swapped := true
            end if
        end for
    until not swapped
end procedure

def procedure bubbleSort(A : list of sortable items):


















#Old version of lab 23

# # Version 3 - Stack
# # Using the following Node class, let's implement some data structures.
# # https://www.geeksforgeeks.org/stack-in-python/

# class Node:
#     def __init__(self, element, next=None):
#         self.element = element
#         self.next = next

#     def __str__(self):
#         return f'({self.element}, {self.next is not None})'
# # A stack can be visualized like a stack of plates, and provides two main methods: push which adds 
# # an element to the top, and pop which removes an element from the top and returns it. 
# # A stack is a FILO "first-in-last-out" data structure.

# # Stub:

# class Stack:
#   def __init__(self):
#     self.root = None
#   def push(self, element): # insert an element at the start (new root)
#     ...
#     return
#   def pop(self): # remove an element from the start (the root becomes the next node)
#     ...
#   def peek(self): # returns the element on the root node or None if there is no root
#     ...
#   def length(self): # return the number of elements
    
#     ... # x = y.length

#   def __str__(self):
#     ...

# s = Stack() # s is the class
# s.push(5) # this mean go inside the stack and run the function called push number 5 is the value passing it 
# s.push(6)
# print(s.length()) # 2
# print(s.pop()) # 6
# print(s.pop()) # 5



