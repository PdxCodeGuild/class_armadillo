
# Lab 13: Simple Calculator

## Version 1

Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that `input` returns a `string`, which you can convert to a float using `float(user_input)` where `user_input` is the string you got from `input`. Below is some sample input/output.


```
> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!
```


## Version 2

Allow the user to enter a running menu

```
> what is the starting number? 34
> enter operation: + 10
> 44
> enter operation: * 3
> 132
```

## Version 3 (optional)

Allow the user to write an expression, alternating numbers and operators. Evaluate the expression left-to-right.

```
> what is the expression? 5 + 6 * 2
> 22
```

## Version 4 (optional)

Allow the user to write an expression, alternating numbers and operators. Follow the proper [order of operations](https://en.wikipedia.org/wiki/Order_of_operations), evaluating first exponentiation, then multiplication and division, then addition and subtraction.

```
> what is the expression? 5 + 6 * 2
> 17
```

## Version 5 (optional)

Allow the user to write an expression including parantheses.

```
> what is the expression? 5*(6 + 2)
> 40
```

