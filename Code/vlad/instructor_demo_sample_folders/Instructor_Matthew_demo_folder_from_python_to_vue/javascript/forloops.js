
//              0          1          2         3          4
let fruits = ['apples', 'bananas', 'pears', 'cherries', 'avocado']
// iterate over the indices
// in python: for i in range(len(fruits)):
for (let i=0; i<fruits.length; ++i) {
    console.log(i + ' ' + fruits[i])
}

// let i=0
// while (i < fruits.length) {
//     console.log(i + ' ' + fruits[i])
//     i++
// }

// iterate over the elements of an array
// in python: for fruit in fruits:
for (let fruit of fruits) {
    console.log(fruit)
}

// another way to iterate over the elements of an array
// in python: for fruit in fruits:
fruits.forEach(function(e) {
    console.log(e)
})


// iterate over the properties of an object (the keys of a dictionary)
let contact = {
    first_name: 'Jane',
    last_name: 'Doe',
    age: 56
}
for (let key in contact) {
    console.log(key + ' ' + contact[key])
}

