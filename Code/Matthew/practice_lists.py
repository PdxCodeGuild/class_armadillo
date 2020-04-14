
import random



# print(random.choice(['apples', 'bananas', 'pears'])) # apples, bananas, or pears

# print(random.randint(5, 10)) # 5, 6, 7, 8, 9, 10
# for i in range(5, 10) # 5, 6, 7, 8, 9




def random_element(mylist):
  return mylist[random.randint(0, len(mylist)-1)]

# for i in range(100):
#   print(random_element(['apples', 'bananas', 'pears'])) # 'apples', 'bananas' or 'pears'


# fruits = ['apples', 'bananas', 'pears']
# fruits.append('cherries')




def get_numbers():
  numbers = []

  # myinput = input("Enter a number (or 'done'): ")
  # while myinput != 'done':
  #   numbers.append(int(myinput))
  #   myinput = input("Enter a number (or 'done'): ")
  
  while True:
    myinput = input("Enter a number or 'done': ")
    if myinput == 'done':
      break
    numbers.append(int(myinput))

  return numbers


# print(get_numbers())
# example run -----------------
# Enter a number (or 'done'): 5
# Enter a number (or 'done'): 34
# Enter a number (or 'done'): 515
# Enter a number (or 'done'): done
# [5, 34, 515]


def is_even(number):
  return number % 2 == 0

def eveneven(numbers):
  count = 0
  for number in numbers:
    if is_even(number):
      count += 1
  return is_even(count)

# print(eveneven([1, 2, 3, 4, 5, 6, 7, 8])) # True
# print(eveneven([5, 6, 2])) # True
# print(eveneven([5, 5, 2])) # False
# print(eveneven([5, 5, 2, 4, 8, 1, 3])) # False




def find_pair(nums, target):
  # for num1 in nums:
  #   for num2 in nums:
  #     print(f'{num1}+{num2}', end=' ')
  #   print()
  for num1 in nums:
    for num2 in nums:
      if num1 + num2 == target:
        return [num1, num2]
  return None

# print(find_pair([5, 6, 2, 3], 7)) # [5, 2]
# print(find_pair([5, 6, 2, 3], 99)) # None

def common_elements(nums1, nums2):
  output = []
  for num1 in nums1:
    for num2 in nums2:
      if num1 == num2:
        output.append(num1)
  return output
# print(common_elements([1, 2, 3], [2, 3, 4])) # [2, 3]
# print(common_elements([1, 2, 3, 4], [2, 3, 4, 5])) # [2, 3]

test_nums1 = []
for i in range(random.randint(10, 20)):
  test_nums1.append(random.randint(0, 20))
test_nums2 = []
for i in range(random.randint(10, 20)):
  test_nums2.append(random.randint(0, 20))


print(test_nums1)
print(test_nums2)
print()

test_nums1 = list(set(test_nums1))
test_nums2 = list(set(test_nums2))
print(test_nums1)
print(test_nums2)
print()

print(common_elements(test_nums1, test_nums2))


