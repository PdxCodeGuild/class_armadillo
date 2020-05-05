

# Computer Science - Algorithms

[Big-O Notation](https://en.wikipedia.org/wiki/Big_O_notation) is a measure of the complexity of an algorithm, specifically how many steps an algorithm takes depending on the size of the input. For example, performing a linear search on a list of `n` elements takes, on average, `n/2` steps, so we say a linear search is `O(n)`. We throw away multiplicative and additive factors to characterize algorithms independently of the hardware it's running on. [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)


## Version 1 - Linear Search

Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.

Example run:
```
 I
[1, 2, 3, 4, 5, 6, 7, 8]
    I
[1, 2, 3, 4, 5, 6, 7, 8]
       I
[1, 2, 3, 4, 5, 6, 7, 8]
```

Stub:
```python
def linear_search(nums, value):
  ...
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
```

## Version 2 - Binary Search

Implement [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm), which requires that a list is sorted. Begin by defining two indices: `low` and `high`. Initialize `low` as the lowest index in the list and `high` as the highest. Loop while `low` is less then `high`. For each iteration, calculate a third index `mid` which is in the middle between `low` and `high`. If the element at `mid` is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at `mid`. If it's less, make `high` equal to `mid` and loop. If it's greater, make `low` equal to `mid` and loop. If the loop terminates without returning, return a value indicating that it was not found.

Example run:
```
 L        M           H
[1, 2, 3, 4, 5, 6, 7, 8]
 L  M     H
[1, 2, 3, 4, 5, 6, 7, 8]
    L  M  H
[1, 2, 3, 4, 5, 6, 7, 8]
```

Psuedocode:
```
// A - the list
// n - the length of the list
// T - the value we're searching for
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful
```

Stub:
```python
def binary_search(nums, value):
  ...
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
```


## Version 3 - Stack

Using the following Node class, let's implement some data structures.

```python
class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'
```

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

## Version 4 - Linked List (optional)

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
