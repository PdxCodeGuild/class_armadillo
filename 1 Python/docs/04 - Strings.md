
# Strings

- [Strings](#strings)
  - [String Literals](#string-literals)
  - [Escape Sequences](#escape-sequences)
  - [Raw Strings](#raw-strings)
  - [Ascii Codes](#ascii-codes)
  - [String Operations](#string-operations)
    - [Concatenation: `a + b`, `a += b`](#concatenation-a--b-a--b)
    - [Multiplication: `a * b`, `a *= b`](#multiplication-a--b-a--b)
    - [Length: len(a)](#length-lena)
    - [Access: `a[i]`](#access-ai)
    - [Slicing: `a[i:j]`, `a[i:j:k]`](#slicing-aij-aijk)
    - [Find: `a.find(b)`](#find-afindb)
    - [Converting Case: `a.upper()`, `a.lower()`](#converting-case-aupper-alower)
    - [Starts-with and Ends-with: `startswith`, `endswith`](#starts-with-and-ends-with-startswith-endswith)
    - [Replace `a.replace(b, c)`](#replace-areplaceb-c)
    - [Strip `a.strip()`](#strip-astrip)
    - [Split: `a.split(b)`](#split-asplitb)
    - [Delimeter: `a.join(b)`](#delimeter-ajoinb)
    - [Count: `a.count(b)`](#count-acountb)
  - [f-strings](#f-strings)
  - [`in`](#in)
  - [`for char in text:`](#for-char-in-text)
  - [Docstrings](#docstrings)


Strings represent text in Python. Strings in Python are encoded in Unicode, which means their reach extends far beyond ASCII. You can use Chinese characters, Arabic characters, and more.

## String Literals

To define a string literal, you can enclose text in either single-quotes or double-quotes, but you should stay consistent. You can use single-quotes inside a string enclosed in double-quotes and vice-versa.

```python
'this is a string declaration'
```
> this is a string declaration
```python
'șʈȓЇиǵʂ ářƏ ūŋĭçóďę abcABC123!@#'
```
> șʈȓЇиǵʂ ářƏ ūŋĭçóďę abcABC123!@#
```python
"we can also use double quotes"
```
> we can also use double quotes
```python
'using single-quotes "allows" you to use double-quotes inside'
```
> using single-quotes "allows" you to use double-quotes inside
```python
"and 'vice versa' with double-quotes"
```
> and 'vice versa' with double-quotes

## Escape Sequences

Escape sequences allow us to define special characters within strings.

- `\'` allows you to have a single quote inside a string enclosed in single quotes
- `\"` allows you to have a double-quote inside a string enclosed in double-quotes
- `\n` represents a new-line
- `\t` represents a tab
- `\\` represents a backslash
- `\xhhhh` represents a unicode character with id 'hhhh', e.g. `\u0394`

```python
'we can use \'single quotes\' in a single-quoted string'
```
> we can use 'single quotes' in a single-quoted string
```python
"we can use \"double quotes\" in a double-quoted string"
```
> we can use "double quotes" in a double-quoted string
```python
'we can also use a line break\na\ttab\nand a backslash \\\nand this \u0394'
```
> we can also use a line break
> a    tab
> and a backslash \
> and this Δ


## Raw Strings

Prefixing a string with 'r' will ignore any escape sequences and interpret the string **literally**.

```python
r'this is a raw string \n\t\\'
```
> this is a raw string \n\t\\\\


## Ascii Codes

There are two built-in functions for switching back and forth between characters and their ascii codes: `chr` and `ord`. You can find more information about these in the official docs for [chr](https://docs.python.org/3.6/library/functions.html#chr) and [ord](https://docs.python.org/3.6/library/functions.html#ord). You can view the ASCII table [here](https://en.wikipedia.org/wiki/ASCII#Character_set)

```python
ord('a')
```
> 97
```python
chr(97)
```
> a

## String Operations


Remember that strings are **immutable** meaning their values cannot be changed. Each of these operations returns a **new** string. You can find some reasons why strings are immutable [here](https://stackoverflow.com/questions/22397861/why-is-string-immutable-in-java).

### Concatenation: `a + b`, `a += b`

Combine two strings into one

```python
'hello' + ' ' + 'world'
```
> hello world
```python
s = 'hello'
s += ' world'
print(s)
```
> hello world



### Multiplication: `a * b`, `a *= b`

Repeat a string

```python
s = 'hello! '
'hello! ' * 4
```
> hello! hello! hello! hello! 

### Length: len(a)

Get the length of a string

```python
s = 'hello world!'
len(s)
```
> 12


### Access: `a[i]`

Get the character at index `i`, indices start at 0

```python
 #   012345
s = 'hello!'
print(s[0])
print(s[4])
```
> h
> o

### Slicing: `a[i:j]`, `a[i:j:k]`

Get the sub-string from `i` to `j`.

```python
s = 'hello world!'
print(s[3:9])
```
> lo wor

If you leave out the starting index, it's implied to be the start of the string.

```python
print(s[:9])
```
> hello wor

If you leave out the ending index, it's implied to be the end of the string.

```python
print(s[9:])
```
> ld

You may optionally add a third number, the increment. The code below will yield every other character.

```python
print(s[::2])
```
> hlowrd

You can use the increment to reverse a string.

```python
print(s[::-1])
```
> dlrow olleh




```python

```
> 

### Find: `a.find(b)`

`s.find(a)` returns the index of a the first occurance of `a`

```python
```
> 

### Converting Case: `a.upper()`, `a.lower()`

`s.upper()` convert to upper case

```python
```
> 
`s.lower()` convert to lower case

```python
```
> 



### Starts-with and Ends-with: `startswith`, `endswith`

`a.startswith(b)` returns true if `a` starts with `b`

```python
print('hello world'.startswith('hello'))
print('hello world'.startswith('world'))
```
> True
> False


`a.endswith(b)` returns true if the string ends with `b`

```python
print('hello world'.endswith('hello'))
print('hello world'.endswith('world'))
```
> False
> True


### Replace `a.replace(b, c)`

`a.replace(b, c)` replaces occurances of string `a` with string `b`

```python
```
> 

### Strip `a.strip()`

`s.strip()`removes leading and trailing characters, if given no parameter, it'll strip whitespace

```python
```
> 

### Split: `a.split(b)`


`s.split(delimeter)` splits a string into a list, if no parameter is given, it'll split on whitespace

```python
```
> 

### Delimeter: `a.join(b)`

`delimeter.join(list)` combines the elements of a list into a single string, separated by the delimeter

```python
```
> 


### Count: `a.count(b)`


```python
s = ' Hello! '
s.lower() # this returns a new string, use s = s.lower()
s.strip() # this returns a new string, use s = s.strip()
print(s) # ' Hello! ' original value is unchanged
```
`strip` and `split` can take arguments or not:
```python
s = " Hello there"
a = s.strip()
b = s.strip('e')
c = s.split()
d = s.split('e')
print(a)
>>> 'Hello there' #Stripped it of the whitespace at the beginning
print(b)
>>> ' Hello ther' #Stripped it of the 'e' at the end
print(c)
>>> ['Hello', 'there'] #Split it into a list, getting rid of and splitting at the whitespace
print(d)
>>> [' H', 'llo th', 'r', ''] #Split it into a list, this time getting rid of and splitting at the 'e'
```


## f-strings

We can use **f-strings** to quickly format text with variables, `f-strings` are prefixed with an `f`, and contain curly braces `{}` to include variables or even expressions.


```python
a = 'one'
b = 2
print(f'a is {a} and b is {b}')
print(f'1+1={1+1})
```
> a is one and b is 2
> 1+1=2

## `in`

```python
if 'h' in 'hello world!':
  print('success!')
```
> success!

## `for char in text:`

```python
text = 'Hey!'
if char in text:
  print(char)
```
> H
> e
> y
> !

## Docstrings

Docstrings are a special kind of multi-line string that's used for generating documentation. You can read more [here](Docstrings.md)

