let user_input = document.querySelector('#user_input')
let btn_submit = document.querySelector('#btn_submit')
let output = document.querySelector('#output')


function random_pw(array){
    let random = Math.floor(Math.random()*array.length)
    return array[random];
}



btn_submit.addEventListener('click', function(){
    let user_input1 = user_input.value
    let characters ='abcdefghijklmnopqrstuvwxyz'
        characters += characters.toUpperCase()
        characters += characters.toLowerCase()
        characters += '0123456789'
        characters += '@#$%&*_-+=/?><'
    let results = ''

    let password = ''
    for (let p=0; p<user_input1; ++p){
        let g = random_pw(characters)
        password += g
    }
    console.log(password)
    result = (`Your password is: ${password}`)
    output.innerText = `${(result)}`
});
