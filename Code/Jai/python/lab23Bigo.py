#v1 linear_search
def linear_search(nums, value):
    if value not in nums:
        return None
    else: 
        index = nums.index(value)
        return index




nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index)



#v2 binary search

#low_index

def binary_search(nums, value):
    nums.sort()
    low = nums[0]
    high = nums[-1]    
    mid = int(len(nums) / 2)
    while low <= high:
        if nums 

nums = [7, 6, 4, 2, 1, 5, 3, 8,]
index = binary_search(nums, 3)
#print(index)


