// fundamentals ===================================================
// ================================================================

// Problem 1 ------------------------------------------------------
// Write a function that tells whether a number is even or odd
function is_even(a) { 
    let rem = a % 2
    if (rem > 0) {
        return false
    } 
    return true

    // return a%2 == 0
}
// console.log(is_even(5))  //False
// console.log(is_even(6)) //True


// Problem 2 ------------------------------------------------------
// Write a function that takes two integers, 'a' and 'b', and returns 'true' if one is positive and the other is negative, and return 'false' otherwise.
function opposite(a, b) {
    if ((a > 0 && b > 0) || (a < 0 && b < 0)) {
        return false
    } else {
        return true
    }
    // return (a > 0 && b < 0) || (a < 0 && b > 0)
    // return a*b < 0
}
// console.log(opposite(10, -1)) // True
// console.log(opposite(2, 3)) // False
// console.log(opposite(-1, -1)) // False

// Problem 3 ------------------------------------------------------
// Write a function that returns the maximum of 3 parameters.
function maximum_of_three(a, b, c) {
    if (a > b && a > c) {
        return a
    } else if (b > a && b > c) {
        return b
    } else {
        return c
    }

    // if (a > b) {
    //     if (a > c) {
    //         return a
    //     } else {
    //         return c
    //     }
    // } else if (b > c) {
    //     return b
    // } else {
    //     return c
    // }

    // return Math.max(a, b, c)
}
// console.log(maximum_of_three(5,6,2)) // 6
// console.log(maximum_of_three(-4,3,10)) // 10



// strings ========================================================
// ================================================================

// Problem 4 ------------------------------------------------------
// Get a string from the user, print out another string, doubling every letter.
//  01234
// 'hello'
function double_letters(word) {
    let new_word = ''
    // iterate over the indices of the string
    for (let i=0; i<word.length; i++) {
        // console.log(i)
        // console.log(word[i])
        // console.log()
        new_word += word[i] + word[i]
    }
    return new_word

    // return word.split('').map(function(e) { return e+e}).join('')
}
// console.log(double_letters('hello')) // hheelllloo

// map example
// nums = [1, 2, 3, 4]
// nums = nums.map(function(x) {
//     return x*x
// })
// console.log(nums) // [ 1, 4, 9, 16 ]




// Problem 5 ------------------------------------------------------
// Return the number of letter occurances in a string.
function count_letter(letter, word) {
    let counter = 0 // initialize a counter
    for (let i=0; i<word.length; i++) { // iterate over the indices of the characters in the word
        if (word[i] == letter) { // if the letter of the word is equal to the letter we're looking for
            counter++ // increment the counter
        }
    }
    return counter // return the counter
}
// console.log(count_letter('i', 'antidisestablishmentterianism')) // 5
// console.log(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) // 2



// Problem 6 ------------------------------------------------------
// Return the letter that appears the latest in the english alphabet.
function latest_letter(word) {

    // split the word into an array of characters
    // sort it alphabetically
    // and take the last element
    // console.log(word)
    // console.log(word.split(''))
    // console.log(word.split('').sort())
    return word.split('').sort()[word.length-1]

    // let latest_character = 'a'
    // for (let i=0; i<word.length; ++i) {
    //     if (word.charCodeAt(i) > latest_character.charCodeAt(0)) {
    //         // console.log('replacing ' + latest_character + ' with ' + word[i])
    //         latest_character = word[i]
    //     }
    // }
    // return latest_character


    // let latest_letter = 'a'
    // let alphabet = 'abcdefghijklmnopqrstuvwxyz'
    // for (let i=0; i<word.length; ++i) {
    //     if (alphabet.indexOf(word[i]) > alphabet.indexOf(letter)) {
    //         // console.log('replacing ' + latest_character + ' with ' + word[i])
    //         latest_character = word[i]
    //     }
    // }
    // return latest_character


    // let codes = []
    // for (let i=0; i<word.length; ++i) {
    //     console.log(word[i] + ' ' + word.charCodeAt(i))
    //     codes.push(word.charCodeAt(i))
    // }
    // console.log(codes)
    // codes = codes.sort(function(a, b) { return a - b })
    // console.log(codes)
    // return String.fromCharCode(codes[codes.length-1])
}
// console.log(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) // v


// sort by default sorts in alphabetical order
// let nums = [90, 105]
// nums.sort()
// console.log(nums)

// console.log(5 == '5') // true, implicitly converts both to the same type



// function min(nums) {
//     let running_min = 0
//     for (let i=0; i<nums.length; ++i) {
//         if (nums[i] < running_min) {
//             running_min = nums[i]
//         }
//     }
//     return running_min
// }

// let s = 'hello world'
// console.log(s.charCodeAt(0)) // code of 'h' is 104
// console.log(s.charCodeAt(1)) // code of 'e' is 101
// console.log(String.fromCharCode(101)) // e

// let alphabet = 'abcdefghijklmnopqrstuvwxyz'
// console.log(alphabet.indexOf('o'))

// console.log('hello world 123'.split(' '))
// console.log('hello world'.split(''))
// console.log('hello world'.split('').sort())


// Problem 7 ------------------------------------------------------
// Write a function that returns the number of occurances of 'hi' in a given string.
function count_hi(text) {
    // your code here
}
//console.log(count_hi('hihi')) // 2



// arrays =====================================================
// ============================================================

// Problem 8 --------------------------------------------------------------
// Write a function to move all the elements of a list with value less than 10 to a new list and return it.
function extract_less_than_ten(nums) {
    let new_list = []
    for (let i=0; i<nums.length; i++) {
        console.log(i + ' ' + nums[i])
        if (nums[i] < 10) {
            new_list.push(nums[i])
        }
    }
    return new_list

    // let new_list = []
    // let i = 0
    // while (i < nums.length) {
    //     if (nums[i] < 10) {
    //         new_list.push(nums[i])
    //     }
    //     i++
    // }
    // return new_list
}
// console.log(extract_less_than_ten([2, 8, 5, 12, 18])) // [2, 8, 5]




// Problem 9 --------------------------------------------------------------
// Write a function that takes an array of numbers, and returns True if there is an even number of even numbers.
function eveneven(nums) {
    let evens = []
    for (let i=0; i<nums.length; i++) {
        if (is_even(nums[i])) {
            evens.push(nums[i])
            console.log(evens)
        }
    }
    return is_even(evens.length)

    // let counter = 0
    // for (let i=0; i<nums.length; ++i) {
    //     if (is_even(nums[i])) {
    //         counter++
    //     }
    // }
    // return is_even(counter)
}
// console.log(eveneven([5, 6, 2])) // true
// console.log(eveneven([5, 5, 2])) // false

// Problem 10 --------------------------------------------------------------
// Return a new array containing a every other element
function every_other(nums) {
    let odds = []
    for (let i=0; i<nums.length; ++i) {
        if (is_even(i)) {
            console.log(i + ' ' + nums[i])
            odds.push(nums[i])
        }
    }
    return odds

    // let r = []
    // for (let i=0; i<nums.length; i+=2) { // for i in range(0, len(nums), 2):
    //     r.push(nums[i])
    // }
    // return r
}
//                        0    1    2    3    4
// console.log(every_other(['a', 'b', 'c', 'd', 'e'])) // ['a', 'c', 'e']



// let fruits = ['apples', 'bananas', 'pears']
// // for i in range(len(fruits))
// for (let i=0; i<fruits.length; ++i) {}
// // for i in range(0, len(fruits), 3)
// for (let i=0; i<fruits.length; i+=3) {}
// // for i in range(2, len(fruits), 2)
// for (let i=2; i<fruits.length; i+=2) {}
// // for i in range(len(fruits)-1, -1, -1)
// for (let i=fruits.length-1; i>-1; i--) {}


// def every_other(mylist):
//     r = []
//     for i in range(len(mylist)):
//         if i%2 == 0:
//             r.append(mylist[i])
//     return r



// Problem 11 --------------------------------------------------------------
// Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.
function find_pair(nums, target) {
    let output = []
    for (let i=0; i<nums.length; i++) {
        for (let j=i+1; j<nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                output.push([nums[i], nums[j]])
            }
            // if (i != j) {
            //     console.log(nums[i] + ' ' + nums[j])
            //     if (nums[i] + nums[j] == target) {
            //         output.push([nums[i], nums[j]])
            //     }
            // }
        }
    }
    return output
}
// console.log(find_pair([5, 6, 2, 3, 1], 7)) // [5, 2]

// nested for loop
let letters = ['a', 'b', 'c', 'd']
for (let i=0; i<letters.length; ++i) {
    // console.log(letters[i])
    for (let j=i+1; j<letters.length; ++j) {
        console.log(letters[i] + ' ' + letters[j])
    }
}

// let matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
// for (let i=0; i<matrix.length; ++i) {
//     for (let j=0; j<matrix[i].length; ++j) {
//         console.log(matrix[i][j])
//     }
// }



// Problem 12 --------------------------------------------------------------
// Write a function that takes `n` as a parameter, and returns a list containing the first n Fibonacci Numbers - https://en.wikipedia.org/wiki/Fibonacci_number.
function fibonacci(n) {
    // your code here
}
// console.log(fibonacci(8)) // [1, 1, 2, 3, 5, 8, 13, 21]