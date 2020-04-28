


# Computer Science - Data Structures

Using the following Node class, let's implement some data structures.

```python
class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'
```

## Version 1 - Stack

A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) can be visualized like a stack of plates, and provides two main methods: `push` which adds an element to the top, and `pop` which removes an element from the top and returns it. A stack is a `FILO` "first-in-last-out" data structure.


Stub:
```python
class Stack:
  def __init__(self):
    self.root = None
  def push(self, element): # insert an element at the start (new root)
    ...
  def pop(self): # remove an element from the start (the root becomes the next node)
    ...
  def peek(self): # returns the element on the root node or None if there is no root
    ...
  def length(self): # return the number of elements
    ...
  def __str__(self):
    ...

s = Stack()
s.push(5)
s.push(6)
print(s.length()) # 2
print(s.pop()) # 6
print(s.pop()) # 5
```



## Version 2 - Linked List

A [linked list](https://en.wikipedia.org/wiki/Linked_list) is like a regular list in Python, and provides methods for adding and removing elements. You may also like to follow [this tutorial](https://stackabuse.com/python-linked-lists/).

Stub:
```python
class LinkedList:
  def __init__(self):
    self.root = None
  def append(element): # add the element to the end
    ...
  def insert(element, index): # insert the element at the given index
    ...
  def remove(element): # remove the first occurrence of the element
    ...
  def find(element): # find the first occurrence of the element and return it
    ...
  def length(self): # return the length of the list
    ...

nums = LinkedList()
nums.append(5)
nums.append(6)
nums.insert(7, 0)
print(nums) # [7, 5, 6]
print(nums.find(5)) # 1
nums.remove(5)
print(nums) # [7, 6]
print(nums.length()) # 2
```



## Version 3 (optional) - Doubly Linked List

In a [doubly-linked list](https://en.wikipedia.org/wiki/Doubly_linked_list) each node maintains a reference to both the next and previous node. Implement a class `DoubleyLinkedList` with the same methods as `LinkedList` but with each node having a reference to both the `previous` and `next` nodes.






