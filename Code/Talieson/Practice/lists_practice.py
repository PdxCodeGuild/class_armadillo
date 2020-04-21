# List Practice
# Problem 1
# Get a string from the user, print out another string, doubling ever letter


def double_letters(word):
    for i in word:
        print(i*2, end="")
    return ""


# print(double_letters("hello"))

# Problem 2
# Write a function that atakes a string, and returns a list of strings,
# each missing a different character.


def missing_char(word):
    # create an empty list to hold word copies
    word_list = []

    # loop through each letter in the word
    for index in range(1, len(word) + 1):
        # create a copy of the word minus that letter

        # slice the word into two parts
        left_part = word[0:index - 1]
        right_part = word[index:len(word)]

        # combine the two parts
        new_word = left_part + right_part

        # add each word to the list
        word_list.append(new_word)
    return word_list


word = "kitten"
print(missing_char(word))


# print(missing_char('kitten'))
# Problem 5
# write a function that returns the reverse of a list.


def reverse(nums):
    nums.reverse()
    return nums


# print(reverse[1,2,3])


# Problem 6
# Write a function to move all the elements of a list with value less than 10
# to a new list and return it.


def extract_less_than_ten(nums):
    new_list = []
    for num in nums:
        if num < 10:
            new_list.append(num)
    return new_list

# print(extract_less_than_ten([2, 8, 12, 18]))


# Problem 7
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    new_list = []
    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2:
                new_list.append(num1)
    return new_list

# print(common_elements([1, 2, 3], [2, 3, 4]))

# Problem 8
# Write a function to combine two lists of equal
# length into one, alternating elements.


def combine(letters, numbers):
    new_list = []
    i = 0
    while i <= len(letters)-1:
        new_list.append(letters[i])
        new_list.append(numbers[i])
        i += 1
    return new_list


# print(combine(['a', 'b', 'c'], [1, 2, 3]))  # ['a', 1, 'b', 2, 'c', 3]

# Problem 9
# Given a list of numbers, and a target number, find a pair of numbers
# from the list that sum to a target number. Optional: return a list of
# all pairs of numbers that sum to a target value.


def find_pair(nums, target):
    new_list = []
    for num in nums:
        for num2 in nums:
            if num + num2 == target:
                new_list.append(num)
    return new_list

# print(find_pair([5, 6, 2, 3, 4], 7)) # [5, 2]

# Problem 10

# Write a function that merges two lists into a single list, where each
# element of the output list is a list containing two elements, one
# from each of the input lists.


def merge(nums1, nums2):
    new_list = []
    for index in range(0, len(nums1), 1):  # 0, 1, 2
        new_list.append([nums1[index], nums2[index]])
    return new_list


# print(merge([5, 2, 1], [6, 8, 2]))  # [[5,6],[2,8],[1,2]]

# Problem 11

# Write a function `combine_all` that takes a list of lists,
# and returns a list containing each element from each of the lists.


def combine_all(nums):
    new_list = []
    for num1 in nums:
        for num2 in num1:
            new_list.append(num2)
    return new_list

# print(combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]))  # [5,2,3,4,5,1,7,6,3]

# Problem 12

# Write a function that takes `n` as a parameter, and returns a list
# containing the first `n` [Fibonacci Numbers]
# (https://en.wikipedia.org/wiki/Fibonacci_number).


def fibonacci(n):
    fibonacci_list = [1, 1]
    for i in range(2, n):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    return fibonacci_list


# print(fibonacci(8))  # [1, 1, 2, 3, 5, 8, 13, 21]


# Problem 13

# Write functions to find the minimum, maximum, mean, and
# (optionally) mode of a list of numbers.


def minimum(nums):
    nums.sort()
    return nums[0]


def maxmimum(nums):
    nums.sort()
    return nums[-1]


def mean(nums):
    return sum(nums) / len(nums)


def mode(nums):
    output = {}
    for num in nums:
        if num not in output:
            output[num] = 1
        else:
            output[num] += 1
    print(output)
    return max(output, key=output.get)


# numbers = [2, 3, 6, 6, 3, 3]
# print(mode(numbers))
