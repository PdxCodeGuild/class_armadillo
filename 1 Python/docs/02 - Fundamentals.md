
# Fundamentals


- [Fundamentals](#fundamentals)
  - [Common Built-in Types](#common-built-in-types)
  - [Variables, Objects](#variables-objects)
  - [Types](#types)
  - [Type Conversion](#type-conversion)
  - [Literals](#literals)
  - [Mutability](#mutability)
  - [Functions](#functions)
  - [Classes](#classes)
  - [Methods](#methods)
  - [I/O](#io)
    - [Print](#print)
    - [Input](#input)
  - [Common Built-in Functions](#common-built-in-functions)


## Common Built-in Types

For all the built-in types, check the [official docs](https://docs.python.org/3.2/library/stdtypes.html).

- `None` the absence of a value, [null](https://en.wikipedia.org/wiki/Null_pointer)
- `int` integer number
- `float` floating-point number
- `string` text
- `bool` `True` or `False`
- `list` an ordered list of objects
- `set` an unordered collection of unique objects
- `dict` a collection of key-value pairs
- `range` represents a range of numbers


## Variables, Objects

Variables are names given to objects. These allow us to specify the operations we'd like to perform on that data in our source code. Objects are collections of data stored in memory, we refer to objects using variables. You can get an identifier for an object with the function `id()`

```python
x = 5 # x is the variable, 5 is the object
print(id(x))
message = 'hello' # message is the variable, 'hello' is the object
print(id(message))
```
> 512341256
> 231661621

Everything is an object in python, including None, booleans, integers, floats, modules, classes, and functions. This means they can be assigned to variables, passes as parameters to functions, and be put into lists and dictionaries.

## Types

Every object has a type, which can be checked by using the `type()` function.

```python
print(type(None)) # <class 'NoneType'>
print(type(False)) # <class 'boolean'>
print(type(5)) # <class 'int'>
print(type(5.0)) # <class 'float'>
print(type('hello')) # <class 'str'>
print(type(type(5))) # <class 'type'>
```

We can define custom types using [classes](10%20-%20Classes.md).

```python
class Point:
    def __init__(self):
        pass
p = Point()
print(type(p)) # <class '__main__.Point'>
print(type(Point)) # <class 'type'>
```


## Type Conversion

Every class has an initializer, which can be used to create an instance of that class.

```python
print(bool('True')) # True
print(int('5')) # 5
print(float('5.0')) # 5.0
print(str(5)) # '5'
```

## Literals

The easiest way to enter data in your problem is through 'literals', which are called as such because they're *literally* written in the source code.

- bool literals: `True` and `False`
- int literals: `3`, `-20`, `294927`
- float literals: `3.2`, `3.14e-10`
- string literals: `'hello'` and `"world"`
- list literals: `[]`, `[1, 2, 3]`
- dict literals: `{}`, `{'a': 1, 'b': 2}`

## Mutability

Certain datatypes in Python are **immutable** meaning their values **cannot** be changed. Immutable types include ints, floats, strings, and tuples. This is why string methods like `lower`, `replace` and `strip` return **copies** of the given string.


```python
x = 5
y = x
y += 2
print(x)
print(y)
```
> 5
> 7

```python
x = ['apples', 'bananas', 'pears']
y = x
y.append('cherries')
print(x)
print(y)
```
> ['apples', 'bananas', 'pears', 'cherries']
> ['apples', 'bananas', 'pears', 'cherries']


## Functions


## Classes


## Methods



## I/O

### Print

Print is a function in python that allows us to print text to the terminal. Each call to `print` results in a new-line.

```python
print('hello')
print('world')
```
> hello
> world


By default, print will have a newline at the end, if you wish to 

```python
print('hello', end=' ')
print('world')
```
> hello world

If you pass multiple arguments (separated by commas), it'll print them each on a single line with spaces in between. 

```python
name = 'Jane'
score = 97
print("Total score for", name, "is", score)
```
> Total score for Jane is 97

If you want to specify a different separator character (space is default), you can write something like:

```python
name = 'Jane'
score = 97
print("Total score for ", name, " is ", score, sep='_')
```
> Total_score_for_Jane_is_97


### Input

The `input` function allows us to prompt the user for input on the terminal. The string that's passed to it determines what's displayed with the prompt.

```python
name = input('What is your name? ')
print('Hello', name, '!')

```
> What is your name? Joe
> Hello Joe !




## Common Built-in Functions

For all the built-in functions, check the [official docs](https://docs.python.org/3/library/functions.html)


- [I/O](#i/o)
    - input() prompts the user for input on the terminal
    - print() displays text to the user on the terminal
- Arithmetic
    - abs() returns the absolute value of a number
    - round() rounds a number, an optional second argument can specify how many decimal places the output should have
    - min() returns the minimum of the values passed to it
    - max() returns the maximum of the values passed to it
    - sum() returns the sum of the values passed to it
- Type Conversion
    - int() converts a value to an int
    - float() converts a value to a float
    - str() converts a value to a string
    - chr() converts an int to a string containing the character with that unicode value, for example `chr(97)` returns the string 'a'
    - ord() converts a character into an int representing the unicode value, for example `ord('a')` returns `97`
    - bool() converts a value to a boolean
    - list() converts a value to a list
    - tuple() converts a value to a tuple
    - set() converts a value to a set
    - dict() converts a value to a dict
- Iterables
    - len() returns the length of a list
    - sorted() sorts a list
    - reversed() reverses a list

