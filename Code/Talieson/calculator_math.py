# This function adds two numbers
def addition(num1, num2):
    result = num1 + num2
    return result


# This function subtracts two numbers
def subtraction(num1, num2):
    result = num1 - num2
    return result


# This function multiplies two numbers
def multiplication(num1, num2):
    result = num1 * num2
    return result


# This function checks for division of 0 then divides two numbers
def division(num1, num2):
    if num1 == 0 or num2 == 0:
        print("You can't divide by 0!")
    else:
        result = num1 / num2
        return result


# This function finds the mean by taking the sum of a list of numbers
# and dividing by the amount of numbers in that list.
def mean(nums):
    return sum(nums) / len(nums)


# This function finds the median of a list of numbers
def median(nums):
    # here we define the amount of numbers in the list and sort ascending
    nums = sorted(nums)
    size = len(nums)
    # this defintes the middle index if the list is an odd number.
    # if it's not it takes the left of the middle two index.
    index = (size - 1) // 2
    # if the list is odd, just return the middle number
    if size % 2:
        return nums[index]
    # else, average the number at index, and the number to it's right
    else:
        return nums[index] + nums[index + 1] / 2


# This function finds the mode of a list of numbers
def mode(nums):
    # establish an empty library
    output = {}
    # iterate through the numbers.
    for num in nums:
        # if the number isn't in the library key, add it with value 1
        if num not in output:
            output[num] = 1
        # if the key is in the library, add 1 to it's value
        else:
            output[num] += 1
    # return the value of the key of output with the highest value
    return max(output, key=output.get)
