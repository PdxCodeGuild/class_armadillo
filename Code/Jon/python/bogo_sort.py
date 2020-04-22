import random

def random_list(n): # generates and returns a list of length n, with random values between 0 and 100
    num_list = []
    for i in range(n):
        num_list.append(random.randint(0,100))
    return num_list

def shuffle(nums): # randomly re-arranges a list
  # iterate through the indices of the list
  # for each index, generate a random index (random.randint)
  # swap the elements at the two indices
  #
  # example
  # indices    0  1  2  3  4
  # elements   5, 7, 4, 2, 8
  # iter 1     i        j
  # elements   2, 7, 4, 5, 8
  # iter 2     j  i     
  # elements   7, 2, 4, 5, 8
  # iter 3           i     j
  # elements   7, 2, 8, 5, 4

    # random.shuffle(nums)

    for i in range(len(nums)-1):
        # random_num1 = random.randint(0,len(nums)-1)
        # random_num2 = random.randint(0,len(nums)-1)
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
        else:
            continue  
        print(f'{nums}')
        
    return nums

def is_sorted(nums): # checks if a list is sorted
  # iterate through the indices of the list
  # if the element at the current index is greater than the element at the next index, the list isn't sorted, and you can return False
  # if you get through the entire list and each element is less than or equal to the next element, the list is sorted, and you can return True
  #
  # e.g. 1,2,4,3
    if nums == sorted(nums):
        return True
    else:
        return False

def bogosort(nums):
    tries = 0
    while not is_sorted(nums):
        shuffle(nums)
        tries += 1
    return f'SORTED {nums} in {tries} tries.'

print(bogosort(random_list(7)))


# step 1
# nums = random_list(100)
# print(nums)

# step 2
# nums = random_list(100)
# print(nums)
# shuffle(nums)
# print(nums)

# step 3
# nums = [1, 2, 3, 4]
# print(is_sorted(nums)) # true
# nums = [1, 2, 4, 3]
# print(is_sorted(nums)) # false

# finale
# nums = random_list(100)
# print(nums)
# bogosort(nums)
# print(nums)