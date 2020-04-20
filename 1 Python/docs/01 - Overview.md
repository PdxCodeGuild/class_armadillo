
# Overview

Python is a popular general-purpose multi-paradigm programming language. General purpose means it can be used for a variety of purposes: desktop applications, [games](https://wiki.python.org/moin/GameProgramming), [embedded systems](https://micropython.org/), web development (Flask and Django), [data science](https://www.upwork.com/hiring/data/15-python-libraries-data-science/), [artificial intelligence](https://wiki.python.org/moin/PythonForArtificialIntelligence) and more. It also means that its core principles carry over to other languages, so you'll be able to more easily broaden your horizon. Python always has an active community with plenty of learning resources, conferences, and libraries. For more information, check out the [Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index) and [Python Standard Library](https://docs.python.org/3/library/index.html). The [wikipedia article](https://en.wikipedia.org/wiki/Python_(programming_language)) offers a decent overview.


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


## Common Built-in Types

For all the built-in types, check the [official docs](https://docs.python.org/3.2/library/stdtypes.html). To check an object's type, use the `type` function.

- `None` the absence of a value, [null](https://en.wikipedia.org/wiki/Null_pointer)
- `int` integer number
- `float` floating-point number
- `string` text
- `bool` `True` or `False`
- `list` an ordered list of objects
- `set` an unordered collection of unique objects
- `dict` a collection of key-value pairs
- `range` represents a range of numbers



## Common Built-in Functions

For all the built-in functions, check the [official docs](https://docs.python.org/3/library/functions.html)


- I/O
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



## Running Python

The python interpreter is run through the terminal, and can be used interactively, or to run a `.py` file. You can find more info in the [official docs](https://docs.python.org/3/using/cmdline.html).


- `python` start the interactive interpreter, use `quit()` to close it
- `python <file>` execute the python source code in the given file
- `python <file> <arguments>` execute a python file and [pass arguments](https://docs.python.org/3/howto/argparse.html)
- `python --help` print out all command-line options
- `python --version` show which version of python you're using

## Installing Packages with `pip`

[Pip](https://pip.pypa.io/en/stable/) stands for 'pip installs python', and is used to manage packages.

- `pip install <package>` install a package
- `pip freeze` list installed packages
- `pip freeze > requirements.txt` save installed package names into a file
- `pip install -r requirements.txt` install packages from names in a file
- `pip uninstall <package>` uninstall a package


## Common Built-in Modules

- [math](https://docs.python.org/3/library/math.html) additional math functions like cos, sin, 
- [decimal](https://docs.python.org/3/library/decimal.html) more advanced floating point arithmetic
- [random](https://docs.python.org/3/library/random.html) generate random numbers
- [datetime](https://docs.python.org/3/library/datetime.html), [time](https://docs.python.org/3/library/time.html), [calendar](https://docs.python.org/3/library/calendar.html) working with dates and times
- [re](https://docs.python.org/3/library/re.html) regular expressions
- [os](https://docs.python.org/3/library/os.html) file operations
- [itertools](https://docs.python.org/3/library/itertools.html), [functools](https://docs.python.org/3/library/functools.html) advanced operations on iterables and functions
- [collections](https://docs.python.org/3/library/collections.html) data structures
- [csv](https://docs.python.org/3/library/csv.html) csv file parsing


## Other Popular Modules

These can be installed using `pip install <module>`. You can find more libraries [here](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/), [here](https://tryolabs.com/blog/2017/12/19/top-10-python-libraries-of-2017/), and [here](http://www.pythonforbeginners.com/api/list-of-python-apis)

- [pillow](https://python-pillow.org/): image manipulation
- [requests](http://requests.readthedocs.io/en/master/): http requests
- [twisted](http://twistedmatrix.com/trac/): networking engine
- [scrapy](https://scrapy.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): web scraping
- [nltk](http://www.nltk.org/): natural language processing
- [numPy](http://www.numpy.org/): advanced mathematics
- [scipy](https://www.scipy.org/): scientific computing
- [pygame](http://www.pygame.org/news.html): game framework
- [matplotlib](http://matplotlib.org/): 2D/3D plotting
- [tkinter](https://wiki.python.org/moin/TkInter), [wxPython](https://www.wxpython.org/), [PyQT](https://sourceforge.net/projects/pyqt/), [PyGTK](https://wiki.python.org/moin/PyGtk): GUI


## Terms

- argument
    - snyonymous with 'parameter', the values passed into a function
- boolean
	- True or False, the result of == != < <= > >=
- class
    - a way to define a type, a 'class of objects'
- comment
	- a way of writing text in code that's ignored by the interpreter
	- e.g. `# this is a comment`
- comparison
    - == != < <= > >=
- conditional
    - if, elif
- declaration
    - to 'declare' a value, to say that it exists (often with a given value, e.g. `x = 5`)
- dunder
	- double underscore '__'
- element
    - an element of a list
    - e.g. in `[1, 2, 3]` `1` is the 'first element'
- escape sequence
    - a way to specify special characters in a string literal
    - e.g. `\n` is a newline, `\t` is a tab, `\'` is a single-quote, `\"` is a double-quote, `\\` is a backslash.
- exception
    - a way in python to indicate that an error occurred, e.g. accessing an element of a list beyond its end, trying to divide by zero
- expression
    - a section of code that evaluates to a value
- float
	- a floating point number, e.g. 5.6
- function
    - an isolated section of code that's supposed to perform a specific operation
- index
    - an integer representing the position of an element in a list, or a character in a string
- instance
    - as opposed to 'type', an actual object, not just a 'blueprint'
- int
	- an integer, e.g. 5, 12, -231
- iteration
	- repeating a block of code by looping
- list
	- an ordered collection of elements, denoted by []
	- `nums = [5, 6, 7]`
	- `names = ['jack', 'jill', 'jane']`
- literal
	- a value put directly into source code
- loop
    - repeatly executing a section of code
    - `for` and `while` are the kinds of loops in python
- method
    - a special type of function, associated with the instance of a type
    - e.g. `'hello world'.split(' ')`
- module
    - an organization unit in Python, a `.py` file represents a module
- modulus ('mod')
	- the 'remainder function' e.g. 5%3=2
	- it's useful for wrapping past the end of an array, or confining an int to a range
- parameter
    - snyonymous with 'argument', the values passed into a function
- statement
    -  a section of code that performs a complete operation
- type
    - synonymous with 'class', general characteristics shared among different instances
    - e.g. string, int, float, list
    - you can access an object's type with `type(o)`, e.g. `print(type(5))` will print `int`
- variable
	- e.g. algebra, a name that stands for a value 
    - the name can be made with letters, numbers, and underscores, it just can't start with a number
