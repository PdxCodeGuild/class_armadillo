let user_input = document.querySelector('#user_input')
let btn_submit = document.querySelector('#btn_submit')
let div_output = document.querySelector('#div_output')

function passwordGenerator(letters){
    let random_pg = Math.floor(Math.random()* letters.length)
    return letters[random_pg]
}
btn_submit.addEventListener('click', function(){
    let user_input2 = user_input.value
    let submit2 = btn_submit.value
    let alpha = "abcdefghijklmnopqrstuvwxyz"
    let numbers = "0123456789"
    let spec_chars = "!@#$%^&*"

    // let user_input = parseInt(prompt("How long do you want your password to be?: "))

    let password = ""
    for (let i = 0; i<user_input; ++i){
        password += passwordGenerator(alpha + numbers + spec_chars)
    }
    console.log(password)
    alert(`Your password is: ${password}`)
})
