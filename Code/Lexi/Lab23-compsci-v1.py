#v1 LINEAR SEARCH

def linear_search(nums, value):
  # if statement to check if it's in there
  # wouldn't work if else was first
  if value not in nums:
    return None
  else:
    index = nums.index(value)
    return index

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(f'\n{index} is the index of the value you chose\n')

# print(numx[3])
# print(nums.index(3))

# v2 BINARY SEARCH
def binary_search(nums, value):
  nums.sort()
  low = nums[0]
  high = nums[-1]
  mid = int(len(nums) / 2)
  print(mid)

nums = [7, 6, 4, 2, 1, 5, 3, 8]
index = binary_search(nums, 3)



