
# Python Quick Reference

- [Python Quick Reference](#python-quick-reference)
  - [Types](#types)
  - [Terms](#terms)
  - [Keywords](#keywords)
  - [Booleans](#booleans)
    - [literals](#literals)
    - [`a == b`](#a--b)
    - [`a != b`](#a--b-1)
    - [`a < b`](#a--b-2)
    - [`a <= b`](#a--b-3)
    - [`a > b`](#a--b-4)
    - [`a >= b`](#a--b-5)
    - [`a and b`](#a-and-b)
    - [`a or b`](#a-or-b)
  - [Integers and Floats](#integers-and-floats)
  - [Built-in Functions](#built-in-functions)
    - [I/O](#io)
      - [`input(message)`](#inputmessage)
      - [`print(object)`](#printobject)
    - [Meta](#meta)
      - [`id(object)`](#idobject)
      - [`eval`](#eval)
      - [`exec`](#exec)
      - [`type(object)`](#typeobject)
    - [Iterable](#iterable)
      - [`sum(numbers)`](#sumnumbers)
  - [Looping](#looping)
    - [`while condition:`](#while-condition)
    - [`for element in list:`](#for-element-in-list)
    - [`for char in string:`](#for-char-in-string)
    - [`continue`](#continue)
    - [`break`](#break)
  - [Strings](#strings)
  - [Lists](#lists)
  - [Dictionaries](#dictionaries)
  - [Functions](#functions)
  - [Other Modules](#other-modules)
    - [`math`](#math)



## Types

- `None` represents the absence of a value
- `int` integer number
- `float` floating-point number
- `string` text
- `bool` a boolean, `True` or `False`
- `list` an ordered list of elements
- `tuple` an ordered and immutible list of elements
- `set` an unordered collection of unique elements
- `dict` a collection of key-value pairs



## Terms

- 
- **Class** an aggregation of data and functions which serve a common purpose
- **Iterable** something that can be iterated over with a for-loop, examples are `string`, `list`, `tuple` and `dict`
- **Method** a special type of function, associated with a type/class
- **Type** an identity associated with a data structure, python build-in types include `bool`, `int`, `float`, `string`, `list`, and `dict`



## Keywords

```python
import keyword
keyword.kwlist
```

- **and** boolean operator
- **as** used with imports
- **assert** used for debugging
- **async** 
- **await** 
- **break** used with loops, exit the current loop
- **class** blueprints of an object, including data and methods
- **continue** used for loops, skip the rest of the current iteration and go to the next
- **def** define a function
- **del** delete, used with lists and dicts
- **elif** else-if, part of a conditional
- **else** part of a conditional
- **except** part of exception handling
- **False** boolean literal
- **finally* part of exception handling
- **for** define a for-loop
- **from** used with imports
- **global** define a global variable
- **if** part of conditionals
- **import** used with imports
- **in** a boolean operator, also part of for-loops
- **is** a boolean operator, tests for equality
- **lambda** a short-hand function
- **None** a boolean literal
- **nonlocal** ???
- **not** a boolean operator
- **or** a boolean operator
- **pass** 
- **raise**
- **return**
- **True**
- **try**
- **while**
- **with**
- **yield**


## Booleans

### literals

There are two boolean literals, `True` and `False`, each of the comparison operators


### `a == b`

Returns `True` if the two given values are equal, false otherwise.

### `a != b`

### `a < b`

### `a <= b`

### `a > b`

### `a >= b`

### `a and b`

### `a or b`


## Integers and Floats


Modulus can also be used with floats.

## Built-in Functions

[Full list](https://docs.python.org/3/library/functions.html)

### I/O

#### `input(message)`

Prompt the user to enter text on the terminal.

```python
name = input('what is your name? ')
print(name)
```


#### `print(object)`

`print` will invoke the object's \_\_str__() implementation.


### Meta


#### `id(object)`

Get an identifier for the object, used by the [garbage collector](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)).

```python

```

#### `eval`

#### `exec`

#### `type(object)`

Find out what type an object is.

```python
print(type(None))
print(type(True))
print(type(5))
print(type(5.0))
print(type([]))
print(type({}))
print(type(type(5)))
```


### Iterable


#### `sum(numbers)`






## Looping

### `while condition:`

Loop on the indented block of code until the given condition is `False`.

```python
i = 0
while i < 5:
  print(i, 'hi')
  i += 1
```
```
0 hi
1 hi
2 hi
3 hi
4 hi
```

```python
while 
```

### `for element in list:`

### `for char in string:`

### `continue`

### `break`





## Strings



## Lists

## Dictionaries

## Functions




## Other Modules

### `math`



###