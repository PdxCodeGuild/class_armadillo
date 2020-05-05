# finding the index given the element

#  I
nums = [1, 2, 3, 4, 5, 6, 7, 8]
    # I
# [1, 2, 3, 4, 5, 6, 7, 8]
    #    I
# [1, 2, 3, 4, 5, 6, 7, 8]

def linear_search(nums, value):
    for num in nums:
        if num == value:
            return nums.index(value)


# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
print(linear_search(nums, 5)) # 4