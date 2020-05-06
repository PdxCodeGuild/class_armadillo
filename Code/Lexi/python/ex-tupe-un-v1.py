#python code on tuples

def result(x,y):
    return x * y

#function with normal vars
print(result(10, 100))

#a tuple is created
z = (10,100)

# tuple is passed
#function unpacked them

print(result(*z))

#https://stackoverflow.com/questions/1455602/printing-tuple-with-string-formatting-in-python
#Note that the % syntax is obsolete. Use str.format, which is simpler and more readable: