
# Strings

Strings represent text, and can be enclosed in either double-quotes or single-quotes. You can read more about strings [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) and [here](https://www.w3schools.com/js/js_string_methods.asp).

```javascript
let s = 'hello world!';
let t = "hello world!";
```

Below are some common operations that can be performed on strings, you can also find a list [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Useful_string_methods) and [here](https://www.w3schools.com/js/js_string_methods.asp).

|Method|Description|
|--- |--- |
|`charAt(index)` and `[index]`| returns the character at the given index [more info](https://stackoverflow.com/questions/5943726/string-charatx-or-stringx)|
|`charCodeAt(index)`| returns the code of the character at the given index |
|`fromCharCode(char_code)`| converts character codes to characters |
|`indexOf(str)`| returns the index of the first occurance of `str`, starting from the beginning|
|`lastIndexOf(str)`|returns the index of the first occurance of `str`, starting from the end|
|`+` and `concat(str1, str2, ...)`| concatenates strings together |
|`repeat(count)`|repeats a string the given number of times|
|`startsWith(str)`|returns true if the string starts with the given sub-string|
|`endsWith(str)`|returns true if the string starts with the given sub-string|
|`includes(str)`|returns true if the string contains the given sub-string|
|`trim()`|removes whitespace from the beginning and end|
|`toLowerCase()`|converts a string to lowercase|
|`toUpperCase()`|converts a string to uppercase|
|`localeCompare(str)`|compares two strings in the host's locale|
|`match(regex)`|finds and returns matches in the string|
|`search(regex)`|finds a match in the string, returns the position of the match|
|`replace(str_find, str_replace)`|searches the string for a specified string or regex, and returns a new string with the matches replaced|
|`split(delimeter)`|returns an array of substrings, split by the delimeter|
|`substring(start, end)` and `slice(start, end)`|returns a sub-string between the the given indices [more info](https://stackoverflow.com/questions/2243824/what-is-the-difference-between-string-slice-and-string-substring)|
|`substr(start, length)`|returns a sub-string starting from the given index, and containing the given number of characters|
|`toLocaleLowerCase()`|converts a string to lowercase, according to the host's locale|
|`toLocaleUpperCase()`|converts a string to uppercase, according to the host's locale|




## Escape Sequences

Escape sequences allow us to enter special characters into our strings.


| Escape Sequence | Description |
| --- | --- |
| `\n` | newline |
| `\t` | tab |
| `\'` | single-quote |
| `\"` | double-quote |
| `\\` | backslash |
| `\0` | begins an octal character |
| `\x` | begins a hexidecimal character |
| `\u` | begins a unicode character (e.g. `\u2665` is `♥`) |





## Template Literals

Template Literals allow us to more easily inject variables into strings. Template Literals are defined via back-ticks `. More info [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).


```javascript
function getFullName(title, fname, lname, degree) {
    return `${title} ${fname} ${lname}, ${degree}`
}
// returns 'Rear Admiral Grace Hopper, PhD'
getFullName('Rear Admiral', 'Grace', 'Hopper', 'PhD')
```

You can even write expressions inside the template:
```javascript
function showYourWork(num1, num2) {
    return `${num1} + ${num2} = ${num1 + num2}`
}
// returns '3 + 4 = 7'
showYourWork(3, 4)
```



## Line Continuation

A backslash followed by a newline in a string literal will continue that string. The resulting string won't contain a backslash or a newline.

```javascript
let s = 'this is a really long\
string, so long that we had to\
write it on multiple lines'
```

You may also use a template literal to get a multi-line string, which **will** contain new-line characters.

```javascript
let s = `this is a really long
string, so long that we had to
write it on multiple lines`
```
