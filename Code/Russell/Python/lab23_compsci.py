

def linear_search(nums, value):
    for num in range(len(nums)): # loop for the length of the list entered
        if nums[num] == value:   # check if each number is equal to the second argument
            return num           # return the index of the element if located
        
     
        else:
            return 'number not found'
        
        

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 34)
print(index) 


