

#       0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


# iterating over the elements
# for element in data:
#   print(element)

# iterating over a range
# for i in range(10) # 0, 1, 2, ... 9
# for i in range(20) # 0, 1, 2, ... 19
# for i in range(0, 10) # 0, 1, 2, ... 9
# for llama in range(5, 10) # 5, 6, 7, 8, 9

# iterating over the indices
# for i in range(len(data)):
#   print(data[i])

# example - adding of numbers
def sum_pairs(nums):
  output = []
  # crashes because i+1 will be one past the end
  # for i in range(0, len(nums)):
  for i in range(0, len(nums)-1):
    print(i, nums[i])
    total = nums[i] + nums[i+1]
    output.append(total)
  return output

print(sum_pairs([1, 2, 3, 4])) # [3, 5, 7]
print(sum_pairs([6, 1, 4])) # [7, 5]