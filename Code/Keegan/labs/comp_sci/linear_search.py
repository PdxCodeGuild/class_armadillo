from random import randint

def linear_search(nums, query):
    for num in nums:
        if num == query:
            return nums.index(num)
    
    return 'nope'

MAX_NUMS = 20
HIGH = 20

nums = sorted([randint(1,HIGH) for i in range(0, MAX_NUMS)])

print(f"I've generated a list of {MAX_NUMS} random numbers 1-{HIGH}.")
query = input(f'Enter a number 1-{HIGH} to search the list: ')
while not query.isdigit():
    print(f'Please enter a whole number 1-{HIGH}: ')

query = int(query)

index = linear_search(nums, query)

print('\n' + ', '.join([str(n) for n in nums]))

if index == 'nope':
    print(f'{query} was not found.')
else:
    print(f'{query} is located at index: {index}')
