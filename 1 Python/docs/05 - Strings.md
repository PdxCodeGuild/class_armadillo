
# Strings

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

### `a + b`

- `+`, `+=` concatenation


### `a * b`

- `*`, `*=` repeat a string



- `len(s)` get the length of a string
- `s[i]` get the character at index i
- `s[i:j]` get the sub-string from `i` to `j`
- `s[i:j:k]` get every `k`th character from `i` to `j`
- `s.find(a)` returns the index of a the first occurance of `a`
- `s.upper()` convert to upper case
- `s.lower()` convert to lower case
- `s.startswith(a)` returns true if the string starts with `a`
- `s.endswith(a)` returns true if the string ends with `a`
- `s.replace(a, b)` replaces occurances of string `a` with string `b`
- `s.strip()`removes leading and trailing characters, if given no parameter, it'll strip whitespace
- `s.split(delimeter)` splits a string into a list, if no parameter is given, it'll split on whitespace
- `delimeter.join(list)` combines the elements of a list into a single string, separated by the delimeter


### `a.count(b)`

Remember that strings are **immutable** meaning their values cannot be changed. Each of these operations returns a **new** string. You can find some reasons why strings are immutable [here](https://stackoverflow.com/questions/22397861/why-is-string-immutable-in-java). Sometimes people new to programming will make a mistake such as...

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

