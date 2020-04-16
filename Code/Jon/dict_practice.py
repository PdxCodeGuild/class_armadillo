# Practice 4: Dictionaries
# For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

# Problem 1
# Given a the two lists below, combine them into a dictionary.
def combine(fruits, prices):
    fruit_prices = {}
    for i in range(len(fruits)):
        # fruit_prices[fruits[i]] = prices[i] 
        # OR
        fruit_prices.setdefault(fruits[i], prices[i])
        # OR
    # fruit_prices = dict(zip(fruits, prices))
    return fruit_prices

fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
print(combine(fruits, prices)) # {'apple':1.2, 'banana':3.3, 'pear':2.1}

# Problem 2
# Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.
def average(combined):
    sum1 = 0
    for fruit in combined:
        sum1 += combined[fruit]
        
    return sum1 / len(combined)

# combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
# print(average(combined)) #-> 2.2

# Problem 3
# # Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.
def unify(dict1):
    a1 = 0
    b2 = 0
    c3 = 0
    
    for i in dict1:
        if i.startswith('a'):
            a1 += dict1[i]
        if i.startswith('b'):
            b2 += dict1[i]
        if i.startswith('c'):
            c3 += dict1[i]

    a1 /= 3
    b2 /= 3
    c3 /= 3

    new_dict = {}
    # for i in dict1:
    #     new_dict.setdefault(i, dict1[i])
    new_dict.setdefault('a', int(a1))
    new_dict.setdefault('b', int(b2))
    new_dict.setdefault('c', int(c3))
    # -> {'a':3, 'b':4, 'c':5}
    return new_dict

dict1 = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
print(unify(dict1)) # -> {'a':3, 'b':4, 'c':5}


