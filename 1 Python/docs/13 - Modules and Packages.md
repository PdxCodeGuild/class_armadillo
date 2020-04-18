
# Modules and Packages


## Modules

A module is one of the major organizational structures of a Python program. It allows you to encapsulate a collection of variables, function, and classes together to be re-used by other code. A module is defined by a file with the extension `py`.


#### module_example1.py

```python
x = 10
def add(a, b):
    return a + b
```

#### module_example2.py

```python
import module_example1
print(module_example1.x) # 10
print(module_example1.add(5, 2)) # 7
```


### Importing

Writing the whole file name every time you'd like to use a function from it can be tedious though, so we can use `from` to make our lives easier.

#### functions.py
```python
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y
```

#### test.py
```python
from functions import add, subtract

print(add(5,4))
print(subtract(5,4))

>>> 9
>>> 1
```

We can use the `as` keyword to shorten it even further:

#### test.py
```python
from functions import add as a, subtract as s

print(a(5,4))
print(s(5,4))

>>> 9
>>> 1
```

Other imports:
```python
import x
from x import * #Imports everything from file
x = __import__('X')
```

### \_\_name__

When a module is run directly or imported, a variable `__name__` is passed into it. If the module is run directly, `__name__` wil lbe `'__main__'`, otherwise it will be the module name itself. This allows you to execute code only when a module is run directly, and not when it's imported into another file.


#### module_example1.py

```python
x = 10

def add(a, b):
    return a + b

if __name__ == '__main__':
    # if this module is run directly, this code will execute
    # if the module is imported into another, it won't run
    x = add(5, 2)
    print(f'5 + 2 = {x}')
```

#### module_example2.py

```python
import module_example1
print(module_example1.x) # 10
print(module_example1.add(5, 2)) # 7
```


## Packages

A package is another major unit of a Python program, and become important as a program grows in scale. A package is simply a collection of modules and other packages, and is represented by a folder several containing `.py` files. A package must also contain a blank file with the name `__init__.py`.


