
def linear_search(nums, value):
    if value not in nums:
        return None 
    else:
        index = nums.index(value)
        return index

nums = [1, 2, 3, 4, 5 6, 7, 8]
index = linear_search(nums, 4)

print(index)


def binary_search(nums, value):
    low = nums[0]
    high = nums[-1]
    mid = int(len(nums) / 2)

nums = nums.sort()

print(nums)