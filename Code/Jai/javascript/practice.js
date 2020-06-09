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
}
console.log(is_even(5))  //False
console.log(is_even(6)) //True


// Problem 2 ------------------------------------------------------
// Write a function that takes two integers, 'a' and 'b', and returns 'true' if one is positive and the other is negative, and return 'false' otherwise.
function opposite(a, b) {
    if ((a > 0 && b > 0) || (a < 0 && b < 0)) {
        return false
    } else {
        return true
    } 
}
console.log(opposite(10, -1)) // True
console.log(opposite(2, 3)) // False
console.log(opposite(-1, -1)) // False

// Problem 3 ------------------------------------------------------
// Write a function that returns the maximum of 3 parameters.
function maximum_of_three(a, b, c) {
    // your code here
}
//console.log(maximum_of_three(5,6,2)) // 6
//console.log(maximum_of_three(-4,3,10)) // 10



// strings ========================================================
// ================================================================

// Problem 4 ------------------------------------------------------
// Get a string from the user, print out another string, doubling every letter.
function double_letters(word) {
    // your code here
}
//console.log(double_letters('hello')) // hheelllloo

// Problem 5 ------------------------------------------------------
// Return the number of letter occurances in a string.
function count_letter(letter, word) {
    // your code here
}
//console.log(count_letter('i', 'antidisestablishmentterianism')) // 5
//console.log(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) // 2

// Problem 6 ------------------------------------------------------
// Return the letter that appears the latest in the english alphabet.
function latest_letter(word) {
    // your code here
}
//console.log(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) // v

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
    // your code here
}
//console.log(extract_less_than_ten([2, 8, 12, 18])) // [2, 8]

// Problem 9 --------------------------------------------------------------
// Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
function eveneven(nums) {
    // your code here
}
//console.log(eveneven([5, 6, 2])) // true
//console.log(eveneven([5, 5, 2])) // false

// Problem 10 --------------------------------------------------------------
// Return a new array containing a every ither number
function every_other(nums) {
    // your code here
}
//console.log(every_other([0, 1, 2, 3, 4, 5, 6, 7, 8])) // 0, 2, 4, 6, 8

// Problem 11 --------------------------------------------------------------
// Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.
function find_pair(nums, target) {
    // your code here
}
//console.log(find_pair([5, 6, 2, 3], 7)) // [5, 2]


// Problem 12 --------------------------------------------------------------
// Write a function that takes `n` as a parameter, and returns a list containing the first n Fibonacci Numbers - https://en.wikipedia.org/wiki/Fibonacci_number.
function fibonacci(n) {
    // your code here
}
// console.log(fibonacci(8)) // [1, 1, 2, 3, 5, 8, 13, 21]