from colorama import Fore

def linear_search(nums, value): # function to search for a particular value in list and return index value
    for i in range(len(nums)): # iterates through input list
        if nums[i] == value: # if the value of an index position equals input value
            return i # returns that index and function breaks
    return -1000 # if nothing found returns this value 

nums = [1, 2, 3, 4, 5, 6, 7, 8] # input list 
value = int(input('\nPlease enter the number for which you\'d like to search: ')) # turns input number to int, no input validation  
index = linear_search(nums, value) # calls function to look for '3' in the list
if index != -1000: # print statement if value found
    print(f''''{value}' was found at index {index}.\n''')
else: # print statement in red if value not found
    print(Fore.RED + f'''Sorry! '{value}' is not there.\n''' + Fore.RESET)    



'''
# Lab 23 Computer Science - Data Structures & Algorithms

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
'''