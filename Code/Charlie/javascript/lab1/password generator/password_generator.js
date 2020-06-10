
function passwordGenerator(letters){
    let random_pg = Math.floor(Math.random()* letters.length)
    return letters[random_pg]
}

let alpha = "abcdefghijklmnopqrstuvwxyz"
let numbers = "0123456789"
let spec_chars = "!@#$%^&*"

let user_input = parseInt(prompt("How long do you want your password to be?: "))

let password = ""
for (let i = 0; i<user_input; ++i){
    password += passwordGenerator(alpha + numbers + spec_chars)
}
alert(`Your password is: ${password}`)


