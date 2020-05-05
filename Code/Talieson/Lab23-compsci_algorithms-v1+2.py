# Lab 23 involves a variety of algorithms.
# Lab 23 v1 is satisfied by the linear search function
# Lab 23 v2 is satisfied by binary_search function

# import random
# import matplotlib.pyplot as plt


def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i


def binary_search(nums, target_num):
    cur_num = 0
    len_nums = len(nums)
    range_nums = len_nums - 1
    # go through the whole list
    while cur_num <= range_nums:
        # find the mid point between current spot and the end
        mid_num = ((cur_num + range_nums) / 2)
        # check if the mid is less then destination num
        if nums[mid_num] < target_num:
            cur_num = mid_num + 1
        elif nums[mid_num] > target_num:
            range_nums = mid_num - 1
        else:
            return mid_num
    return False


nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index)  # 2
