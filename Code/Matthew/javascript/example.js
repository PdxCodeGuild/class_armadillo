

// declaring variables

// python
// x = 10 // declaration and assignment
// x = 20 // just assignment

// javascript
let x = 10
x = 20
x = x + 10
x += 10
x++ // x += 1, x = x + 1
x-- // x -= 1, x = x - 1
++x
--x
console.log(x)
console.log(typeof x)


// x++ vs ++x
x = 10
console.log('x is ' + x++) // post-increment "x is 10"
x = 10
console.log('x is ' + ++x) // pre-increment "x is 11"

let fruits2 = ['apples', 'bananas', 'pears']
let i = 0
let j = 0
while (i < fruits2.length) {
    console.log(fruits2[++i])
    console.log(fruits2[j++])
}

// strings
let text = 'hello world'
console.log(text.toUpperCase())

// arrays
let fruits = ['apples', 'bananana', 'pears']
fruits.push('cherries')
console.log(fruits)

let obj = {
    'mykey': 5,
    'my-key': 5,
    myprop: 5,
}
console.log(obj)
console.log(obj.mykey)
// console.log(obj.my-key) // crash!
console.log(obj['my-key'])
console.log(obj['myprop'])

// conditionals
temperature = Math.floor(50+Math.random()*50)
console.log(temperature)
if (temperature < 60) {
    console.log('cold')
} else if (temperature < 80) {
    console.log('warm')
} else {
    console.log('hot')
}

// loops
i = 0
while (i < 10) {
    console.log(i)
    i++
}

// for i in range(10): i would go 0...9
// for (initialization; condition; increment)
for (let i=0; i<10; i++) {}

// python
// def add(a, b):
//     return a + b



// two ways to define functions
function add(a, b) {
    return a + b
}
console.log(add(5, 2))

let add = function(a ,b) {
    return a + b
}
console.log(add(5, 2))


// "function x" will get 'hoisted', "let x = function" will not
console.log(add(5, 2))
function add(a, b) { // this will get 'hoisted' - moved to the top of the file
    return a + b
}
// console.log(add(5, 2)) // crash
let add = function(a, b) {
    return a + b
}
console.log(add(5, 2))




