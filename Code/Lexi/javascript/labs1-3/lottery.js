
// write a function to match numbers
function numMatches(winning, ticket){
    // 'let' is implicitly done on function declaration line (params)
    let matches = 0

    //this if -else statement is checking if the user entered integers
    if (Number.isInteger(winning)){
    winning = winning.toString()
    }
    // break (exits block) vs return (exits whole f(x))

    //this for-of loop iterates through an obj
    for(let w of winning){
        console.log(w)
        if (Number.isInteger(w)) {
            return w
        }

    }
    // this if -else statement is checking if the user entered integers
    if (Number.isInteger(ticket)){
        ticket = ticket.toString()

    } //this for-of loop iterates through an obj
    for(let t of ticket){
        console.log(t)
    }
    //method on the number prototype === stands alone
    // Famous words from Freya
    // winning = toString(winning)
    console.log(winning)
    winning = winning.split("")
    //convert ticket into array
    // ticket = toString(ticket)
    ticket = ticket.split("")
    console.log(ticket)
    // value of item at index is the 1st para
    ticket.forEach(function(i){
        // two params not needed https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
        if (ticket[i] === winning[i]){
            matches++
            console.log(`Your ticket matches the winnning ticket!`)
        }else{
            alert(`This ticket is not a winner`)
        }
    })
    return matches
}
numMatches('123456','123456')
