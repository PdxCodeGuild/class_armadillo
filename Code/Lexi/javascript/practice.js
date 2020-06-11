// problem 1

function haha(x, y){
   return x + y
}


// read up on 'closure' which is defining a f(x) within a f(x)
var counter = 0
function ohno(){
    return counter +=2
    
}

console.log(ohno()) // 2
console.log(ohno()) // 4

//This is a closure almost

//hw read: https://nodejs.org/api/repl.html node repl