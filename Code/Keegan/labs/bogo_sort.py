# Desi, Kyle, Nicholas, Vlad, Troy, Keegan

import random

def random_list(n):
    '''
    Generates and returns a list of length n, with random values between 0 and 100
    '''

    nums = []                            # create empty list
    for i in range(n):                   # loop n times
        num = random.randint(0, 100)     # generate a random number
        nums.append(num)                 # add the random number to our list
    
    return nums                          # after the loop is done, return the list


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
def shuffle(nums): 
    '''
    randomly re-arranges a list by
    iterating through the indices of the list.
    for each index, generate a random index (random.randint)
    swap the elements at the two indices
    ''' 

    for index in range(len(nums) - 1):                     # for each index in the list
        rand_index = random.randint(0, len(nums) - 1)  # generate a random index within the list
        
        temp = nums[index]                          # set aside the original value at index
        nums[index] = nums[rand_index]             # asign value rand_index to the current index
        
        nums[rand_index] = temp                    # pull down our original value and set it to the rand_index
    
    return nums


def is_sorted(nums): 
    '''
    checks if a list is sorted

    iterate through the indices of the list
    if the element at the current index is greater than the element at the next index, 
    the list isn't sorted, and you can return False

    if you get through the entire list and each element is less than or equal to the next element, 
    the list is sorted, and you can return True
    '''

    for i in range(len(nums) - 1):   # for each index in the list (number of items in list minus 1)
        if nums[i] > nums[i + 1]:    # if the value at i is greater than the value at the next index
            return False             # return false
    
    return True  # if we make it all the way through the loop, return True

def bogosort(nums):
    while not is_sorted(nums):
        nums = shuffle(nums)
        print(nums)
    return nums


# step 1
# nums = random_list(100)
# print(nums)

# step 2
# nums = random_list(10)
# nums = [i for i in range(10)]
# print(nums)
# shuffled = shuffle(nums)
# print(shuffled)

# step 3
# nums = [1, 2, 3, 4]
# print(is_sorted(nums)) # true
# nums = [1, 2, 4, 3]
# print(is_sorted(nums)) # false

# finale
nums = random_list(9)
print(nums)
sorted_nums = bogosort(nums)
print(sorted_nums)
