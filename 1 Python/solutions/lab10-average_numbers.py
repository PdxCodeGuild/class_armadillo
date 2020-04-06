"""
Lab 10: calculate the average of a list of numbers
"""
import random

# nums = [5, 0, 8, 3, 4, 1, 6]

nums = [1, 1, 2, 2, 2, 3]

# nums = []
# for i in range(20):
#     nums.append(random.randint(1,10))



# nums = []
# while True:
#     num_str = input('enter a number (or \'done\' if done): ')
#     if num_str == 'done':
#         break
#     else:
#         nums.append(float(num_str))


def mean(nums):
    # total = 0
    # for num in nums:
    #     total += num
    # average = total/len(nums)
    average = sum(nums)/len(nums)
    return average


def median(nums):
    nums = nums.copy()
    nums.sort()
    if len(nums)%2 == 0:
        # 0 1 2 3, 4//2 2
        a = nums[len(nums)//2-1]
        b = nums[len(nums)//2]
        return [a, b]
    else:
        # 0 1 2, 3//2=1
        return [nums[len(nums)//2]]


# r = median([1,2,3])
# if type(r) is float:
#
# r = median([1,2,3])
# if len(r) == 1:





def mode_al(num_list):
    for i in num_list:
        try:
            exec(f"n{i}_counter += 1")
        except NameError:
            exec(f"n{i}_counter = 1")
    largest_count = 0
    for i in num_list:
        if eval(f"n{i}_counter > largest_count"):
            exec(f"largest_count = n{i}_counter")
    mode_list = []
    for i in num_list:
        if eval(f"n{i}_counter == largest_count and i not in mode_list"):
            exec(f"mode_list.append(i)")
    return mode_list

# counts = {}
# nums = [1, 1, 2, 2, 2, 3]
# loop
# counts = {1: 1}
# counts = {1: 2}
# counts = {1: 2, 2:1}
# counts = {1: 2, 2:2}
# counts = {1: 2, 2:3}
# counts = {1: 2, 2:3, 3:1}


# counts = {1: 2, 2: 3, 3: 1}

def mode(nums):
    counts = {}
    for num in nums:
        # counts[num] = counts.get(num, 0) + 1
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        # print(f'{num} {counts}')
    print(counts)
    counts = list(counts.items())  # .items() returns a list of tuples
    print(counts)
    counts.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    print(counts)
    return counts[0][0]



nums.sort()
print(f'mean: {mean(nums)}')
print(f'median: {median(nums)}')
print(f'mode: {mode(nums)}')

