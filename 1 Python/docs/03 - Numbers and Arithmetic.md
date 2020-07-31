
# Numbers and Arithmetic


- [Numbers and Arithmetic](#numbers-and-arithmetic)
  - [Ints](#ints)
  - [Floats](#floats)
  - [Arithmetic Operators](#arithmetic-operators)
    - [Addition: `a + b`](#addition-a--b)
    - [Subtraction: `a - b`](#subtraction-a---b)
    - [Multiplication: `a * b`](#multiplication-a--b)
    - [Division: `a / b`](#division-a--b)
    - [Floor Division: `a // b`](#floor-division-a--b)
    - [Modulus: `a % b`](#modulus-a--b)
  - [Functions](#functions)
    - [Type Conversions](#type-conversions)
    - [Absolute Value](#absolute-value)
    - [Round](#round)
    - [](#)

## Ints

'Ints' represent integers, or 'whole numbers', and they can be positive or negative.

```python
x = 5
print(x)
print(type(x))
```
> 5
> <class 'int'>


## Floats

'Float' is stort for 'floating-point number', which represents an approximation of a real number. Floats may also be written with an exponent, designated by `e`: `3.12e6` is 3,120,000.

```python
x = 5.23
print(x)
print(type(x))
```
> 5.23
> <class 'float'>

There are also three special values floats may take: positive infinity, negative infinity, and NaN. NaN is short for 'not a number', it's the result of some mathematical operations, particularly in `numpy`. You can check for these values with the `math` module.

```python
import math

x = float('nan')
print(math.isnan(x))

y = float('inf')
print(math.isinf(y))

z = float('-inf')
print(math.isinf(z))
print(math.isfinite(z))
```

The `math` module has many other specialized math functions you can utilize, a full list of them can be found [here](https://docs.python.org/3/library/math.html). For each of the arithmetic operators, there are short-hand versions, which compute a result and store it as the original variable: `x += 2` is equivalent to `x = x + 2`.


## Arithmetic Operators

- `+`, `+=` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `//` floor division, results in an `int`
- `%` modulus, a%b is the remainder of a/b
- `**` exponentiation


### Addition: `a + b`

### Subtraction: `a - b`

### Multiplication: `a * b`

### Division: `a / b`

### Floor Division: `a // b`

### Modulus: `a % b`

Modulus is the 'remainder function' for example, 5%2 is 1, 6%2 is 0, 23%5 is 3, etc. It's also useful for containing the range of a variable.

```python
i = 0
while i < 100:
    print(i%3)
    i = i + 1
```
> 0
> 1
> 2
> 0
> 1
> 2
> 0
> ...

## Functions

### Type Conversions

```python
int('5')
```
> 5
```python
int(5.23)
```
> 5
```python
float('5.0')
```
> 5


### Absolute Value

### Round


### 
    - abs() returns the absolute value of a number
    - round() rounds a number, an optional second argument can specify how many decimal places the output should have
    - min() returns the minimum of the values passed to it
    - max() returns the maximum of the values passed to it
    - sum() returns the sum of the values passed to it



