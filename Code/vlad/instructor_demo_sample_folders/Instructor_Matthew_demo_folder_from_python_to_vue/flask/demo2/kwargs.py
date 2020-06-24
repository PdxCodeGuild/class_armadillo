



def add(a, b):
    return a + b

# print(add(5, 2)) # 7
# print(add(a=6, b=3)) # 9






def render_template(template_name, **kwargs):
    print(template_name)
    print(kwargs)

name = 'joe'
render_template('index.html', a=1, b=2, c=3, d=add(3, 1), name=name, animal='llama')

# example NOT using **kwargs
# def render_template(template_name, kwargs):
#     print(template_name)
#     print(kwargs)
# render_template('index.html', {'a':1, 'b': 2})




# *args - take any number of arguments

# print uses *args
# print('hello', 'world', 5, 2, 3, 1)


# *args - arguments get put into a list
def calculate_total(*nums):
    print(nums)
    total = 0
    for num in nums:
        total += num
    return total

print(calculate_total(1, 2, 3))


# equivalent example NOT using *args
def calculate_total(nums):
    print(nums)
    total = 0
    for num in nums:
        total += num
    return total
print(calculate_total([1, 2, 3]))
