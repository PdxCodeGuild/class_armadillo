
# Variables and I/O


## Variables & Objects

Variables are names given to objects. These allow us to specify the operations we'd like to perform on that data in our source code. Objects are collections of data stored in memory, we refer to objects using variables. You can get an identifier for an object with the function `id()`

```python
x = 'hello' # x is the variable, 'hello' is the object
print(id(x))
y = 5
print(id(5))
```
> 512341256
> 231661621


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



