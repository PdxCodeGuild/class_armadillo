
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
// write a function that generates 6 random nums
// function pick_6(){
//     let list_of_6 = 0
// }

//take input

// split into list

// 6 elems at end

// go through spans (with numbered ids) number_1

// then do doc.q...All <--creates array of all elems it finds

// or common class amongs spans

// since they're in order, you could match 'em

// go through array, do item at index[0] and put that item in the element

//in the array of elems

//qu...all

//console.log output

//common class on all spans

//nesting

//querySel all send it # and id for parent div

// tag for each of the child divs

// just like targeting all spans within a div

// send same querySelall

//loop through one -for one