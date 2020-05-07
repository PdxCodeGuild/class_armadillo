from colorama import Fore

def binary_search(nums, value): # function to search for a particular value in list and return index value
    low = 0 # sets lower bound for search range
    up = len(nums)-1 # sets lower bound for search range, actual index number is one less than list length
    nums.sort() # sorts input list into ascending order
    while low <= up: # ensures a searchable range
        mid = (low + up) // 2 # calculates mid using index numbers
        if nums[mid] < value: # if value at the mid index position is less than target value
            low = mid + 1 # lower bound is moved up to just ahead of mid, returns to top of loop to recalulare mid
        elif nums[mid] > value: # if value at the mid index position is more than target value
            up = mid - 1 # upper bound is moved just behind the mid, returns to top of loop to recalulare mid
        else:
            return mid # gets here if nums[mid] equals target, will return that index position (mid), program is complete
    return -1000 # returns value (arbitrary) if input number is not in list...results in None, program is complete      


nums = [1, 2, 3, 4, 5, 6, 7, 8] # input list
value = int(input('\nPlease enter the number for which you\'d like to search: ')) # turns input number to int, no input validation  
index = binary_search(nums, value) # calls function to look for input value in the list
if index != -1000: # print statement if value found
    print(f''''{value}' was found at index {index}.''')
else: # print statement in red if value not found
    print(Fore.RED + f'''Sorry! '{value}' is not there.\n''' + Fore.RESET)  



'''
# Lab 23 - Computer Science - Algorithms


[Big-O Notation](https://en.wikipedia.org/wiki/Big_O_notation) is a measure of the complexity
 of an algorithm, specifically how many steps an algorithm takes depending on the size of the input. 
 For example, performing a linear search on a list of `n` elements takes, on average, `n/2` steps, 
 so we say a linear search is `O(n)`. We throw away multiplicative and additive factors to characterize 
 algorithms independently of the hardware it's running on. 
 [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

## Version 1 - Linear Search

Implement linear search, which simply loops through the given list and check if each element is equal to 
the value we're searching for. If it is, return the index at which it was found, otherwise, return a value 
indicating that it was not found.

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

Implement [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm), 
which requires that a list is sorted. Begin by defining two indices: `low` and `high`. 
Initialize `low` as the lowest index in the list and `high` as the highest. 
Loop while `low` is less then `high`. For each iteration, calculate a third index `mid` 
which is in the middle between `low` and `high`. If the element at `mid` is the one you're 
searching for, return it, otherwise check is the target value is less than or greater than 
the one at `mid`. If it's less, make `high` equal to `mid` and loop. If it's greater, make 
`low` equal to `mid` and loop. If the loop terminates without returning, return a value 
indicating that it was not found.

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
'''