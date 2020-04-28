# fibonacci Keegan explaining: 

def count_10(x):
    print(x)
    if x == 10:
        return x
    return count_10(x + 1)
# count_10(1)
def fibonacci(n, fib=[]):
    # if we've generated our target number of numbers, exit function
    if len(fib) == n:
        return fib
    # first two digits in fibonacci sequence are 1
    if len(fib) < 2:
        fib.append(1)
    # all other numbers in the sequence are the sum of the previous two
    else:
        # last element
        current = fib[len(fib) - 1]
        # second to last element
        prev = fib[len(fib) - 2]
        # add new element which is the sum of the previous two
        fib.append(current + prev)
    # call the function again within itself
    # and pass it the current fib list
    return fibonacci(n, fib)
print(fibonacci(8))