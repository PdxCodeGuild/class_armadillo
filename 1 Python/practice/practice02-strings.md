
# Practice: Strings

For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

```python
def add(a, b):
    return a + b
#print(add(5, 2))
#print(add(8, 1))
```


## Problem 1

Get a string from the user, print out another string, doubling every letter.

```python
def double_letters(word):
  ...
print(double_letters('hello')) # hheelllloo
```

## Problem 2

Write a function that takes a string, and returns a list of strings, each missing a different character.

```python
def missing_char(word):
  ...
print(missing_char('kitten')) # ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']
```

## Problem 3
Return the letter that appears the latest in the english alphabet.

```python
def latest_letter(word):
  ...
print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v
```

## Problem 4

Write a function that returns the number of occurances of 'hi' in a given string.

```python
def count_hi(text):
  ...
print(count_hi('hihi')) # 2
```

## Problem 5

Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

```python
def cat_dog(text):
  ...
print(cat_dog('catdog')) # True
print(cat_dog('catcat')) # False
print(cat_dog('catdogcatdog')) # True
```

## Problem 6

Return the number of letter occurances in a string.
```python
def count_letter(letter, word):
    ...
print(count_letter('i', 'antidisestablishmentterianism')) # 5
print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2
```

## Problem 7

Convert input strings to lowercase without any surrounding whitespace.

```python
def lower_case(text):
  ...
print(lower_case("SUPER!")) # 'super!'
print(lower_case("        NANNANANANA BATMAN        ")) # 'nannananana batman'
```
