from random import randint

def binary_search(nums, query):
    left = 0               # left index
    right = len(nums) - 1  # right index

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < query:
            left = mid + 1

        elif nums[mid] > query:
            right = mid - 1 

        else:
            return mid
    
    return 'nope'

MAX_NUMS = 20
HIGH = 20

nums = sorted([randint(1,HIGH) for i in range(0, MAX_NUMS)])

print(f"I've generated a list of {MAX_NUMS} random numbers 1-{HIGH}.")
query = input(f'Enter a number 1-{HIGH} to search the list: ')
while not query.isdigit():
    print(f'Please enter a whole number 1-{HIGH}: ')

query = int(query)

index = binary_search(nums, query)

print('\n' + ', '.join([str(n) for n in nums]))

if index == 'nope':
    print(f'{query} was not found.')
else:
    print(f'{query} is located at index: {index}')
