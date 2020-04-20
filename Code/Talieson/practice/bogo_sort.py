
import random


# generates and returns a list of length n, with random values between 0 & 100
def random_list(num):
    num_list = []
    for num in range(num):
        num_list.append(random.randint(0, 100))
    return num_list


def shuffle(nums):
    for i in range(len(nums)-1):
        # random_num1 = random.randint(0,len(nums)-1)
        # random_num2 = random.randint(0,len(nums)-1)
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
        else:
            continue
        print(f'{nums}')

    return nums


def is_sorted(nums):

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
