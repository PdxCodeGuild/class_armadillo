








# a and b are called parameters
# def add(a, b):
#     return a + b
# print(add(5, 2))
# print(add(8, 1))

# fruits = ['apples', 'bananas', 'pears']
# fruits = fruits.append('cherries')
# print(fruits)



# values = [False, 0, 0.0, '', [], {}, True, 1, 5.6, 'hello']
# for value in values:
#     if value:
#         print(f'{value} is truthy')
#     else:
#         print(f'{value} is falsy')


# # bad
# num = input('enter a number')
# if num:
#     num = int(num)
# else:
#     print('don\'t enter a blank string')

# # good
# if num != '':
#     num = int(num)
# else:
#     print('don\'t enter a blank string')

# # good
# is_raining = False
# if is_raining:

# problem 1

def is_even(llama):
    return llama%2 == 0
    # if llama%2 == 0:
    #     return True
    # return False

# print(is_even(5)) # False
# print(is_even(6)) # True


# problem 2

def opposite(a, b):
    # return (a > 0 and b < 0) or (a < 0 and b > 0)
    return a*b < 0
# print(opposite(10, -1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False


# '_'.join(['a', 'b', 'c']) # a_b_c



# Problem 3

# iterables: string, list, range, reversed(), tuple, set, dictionary
# print(list(reversed([1, 2, 3])))
# print(sorted([3, 1, 2]))
# print(list(range(1, 10)))


def near_100(num):
    return num >= 90 and num <= 110

    # less good version
    # if num in range(90, 111):
    #     return True
    # else:
    #     return False
# print(near_100(89)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True


def maximum_of_three(a, b, c):

    # nums = [a, b, c]
    # nums.sort()
    # return nums[-1]

    # nums = sorted([a, b, c])
    # return nums[-1]

    # return max(a, b c)
    
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# print(maximum_of_three(5,6,6)) # 6
# print(maximum_of_three(5,6,2)) # 6
# print(maximum_of_three(-4,3,10)) # 10
# print(maximum_of_three(20,3,10)) # 20



def print_powers_2():
  #for x in range(0, 21):
  #  print(2 ** x)
  i = 0
  while i < 21:
    print(2 ** i)
    i += 1


# print_powers_2() # 1, 2, 4, 8, 16, 32, ...




def double_letters(word):
    new_list = []
    for char in word:
        doubled = char*2
        print(doubled)
        new_list.append(doubled)
    # return list(word*2)
    print(new_list)
    return ''.join(new_list)
# print(double_letters('hello')) # hheelllloo
# print(double_letters('llama'))


def multiply_letters(word, repeat=2):
    new_list = []
    for char in word:
        doubled = char*repeat
        new_list.append(doubled)
    return ''.join(new_list)
# print(multiply_letters('hello')) # hheelllloo
# print(multiply_letters('llama', repeat=4))


# def print(value, end='\n'):
#     ...
# print('hello', end='')


def double_letters_keegan(word, repeat=2):
    return ''.join([char*repeat for char in word])
# print(double_letters_keegan('llama', repeat=45))




def latest_letter(word):
    # new_list = []
    # for char in word:
    #     new_list.append(char)

    # print(word)
    new_list = list(word)
    # print(new_list)
    new_list.sort()
    # print(new_list)
    return new_list[-1]

    # return sorted(word)[-1]

    # running_latest_letter = 'a'
    # for char in word:
    #     if ord(char) > ord(running_latest_letter):
    #         running_latest_letter = char
    # return running_latest_letter


# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v
# print(latest_letter('antidisestablishmentarianism')) # t



# index = 'hello world world world'.find('world')
# print(index)
# index = 'hello world world world'.find('world', index+1)
# print(index)
# index = 'hello world world world'.find('world', 13)
# print(index)
# index = 'hello world world world'.find('world', 19)
# print(index)






def count_hi(text):
  # return text.count('hi')
#   for char in text:
#     print(char)
#   for i in range(len(text)-1):
#     print(text[i], text[i+1])

print(count_hi('hihi')) # 2
# print(count_hi('hihellohi')) # 2
# print(count_hi('abc123hi456')) # 1







def count_letter(letter, word):
    letter_count = 0
    # new_list = list(word)
    # new_list.sort()
    for char in word:
        # print(f'comparing {char} and {letter}')
        if char == letter:
            # print('\t incrementing letter count')
            letter_count += 1
        # print(char)
    return letter_count
# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2


