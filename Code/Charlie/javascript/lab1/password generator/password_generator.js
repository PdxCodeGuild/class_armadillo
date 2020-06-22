let user_input = document.querySelector('#user_input')
let btn_submit = document.querySelector('#btn_submit')
let output = document.querySelector('#output')


function passwordGenerator(letters){
    let random_pg = Math.floor(Math.random()* letters.length)
    return letters[random_pg]
}
btn_submit.addEventListener('click', function(){
    let user_input2 = user_input.value
    let alpha = "abcdefghijklmnopqrstuvwxyz"
    let numbers = "0123456789"
    let spec_chars = "!@#$%^&*"
    let result = ""

    let password = ""
    for (let i=0; i<user_input2; ++i){
        let x = passwordGenerator(alpha + numbers + spec_chars)
        password += x
    }
    console.log(password)
    result = (`Your password is: ${password}`)
    output.innerText = `${(result)}`
})
