# # finding the index given the element

# #  I
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
#     # I
# # [1, 2, 3, 4, 5, 6, 7, 8]
#     #    I
# # [1, 2, 3, 4, 5, 6, 7, 8]

# def linear_search(nums, value):
#     for num in nums:
#         if num == value:
#             return nums.index(value)


# # nums = [1, 2, 3, 4, 5, 6, 7, 8]
# # index = linear_search(nums, 3)
# print(linear_search(nums, 5)) # 4

# L        M           H
[1, 2, 3, 4, 5, 6, 7, 8]
# L  M     H
[1, 2, 3, 4, 5, 6, 7, 8]
#    L  M  H
[1, 2, 3, 4, 5, 6, 7, 8]

// A - the list
// n - the length of the list
// T - the value we're searching for
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful

def binary_search(nums, value):
  ...
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2