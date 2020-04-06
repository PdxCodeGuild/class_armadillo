
# Lab: Average Numbers

We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember `len` will give you the length of a list.

The code below hows how to loop through an array, and prints the elements one at a time.
```python
nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])

```

## Version 2

Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

```python
nums = []
nums.append(5)
print(nums)
```

Below is an example input/output:


```
> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4
```

## Version 3

Calculate the median. The median is the number in the middle when the list is sorted. If there's an even number of numbers, the median is a list of the two numbers in the middle. Remember the `sort` method on lists.

## Version 4 (optional)

The mode is the number that occurs the most. There may be multiple modes. Hint: use a dictionary to count the occurances of each number, the key can be the number, the value can be the number of occurances. If it's not in the dictionary, add it and set it's value to one. If it's already in the dictionary, increment that value.

```python
counts = list(word_dict.items()) # .items() returns a list of tuples
counts.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
print(counts)
```
