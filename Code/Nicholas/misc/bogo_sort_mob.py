import random

def random_list(n): # generates and returns a list of length n, with random values between 0 and 100
    nums = []
    for i in range(n):                   # create empty list       
        num = random.randint(0, 100)     # loop n times
        nums.append(num)                 #generate a random number
        
    return nums                          #return nums list   

def shuffle(nums): 
    for index in range(len(nums)-1):                 # for each index in the list
        rand_index = random.randint(0, len(nums)-1)  # generate random index within the list
        
        temp = nums[index]                            # set aside original value at index 
        nums[index] = nums[rand_index]                 # assign value rand_index to current index
        
        nums[rand_index] = temp                      # pull down original value and set it to the rand_index   
    
    return nums

def is_sorted(nums): 
    for i in range(len(nums) - 1): # for each index in the list (number items in list -1)
        if nums[i] > nums[i+1]:    # if value at i is greater than the value at the net index
            return False 
    
    return True    


def bogosort(nums):
  while not is_sorted(nums):  # while list is not sort
    nums = shuffle(nums) # bogosort
    print(nums)
  return nums    



nums = random_list(5)
print(nums)
sorted_nums = bogosort(nums)
print(sorted_nums)

