let user_input = document.querySelector('#user_input')
let btn_submit = document.querySelector('#btn_submit')
let div_output = document.querySelector('#div_output')

btn_submit.addEventListener('click', function(){
    let user_input2 = user_input.value
    let submit2 = btn_submit.value

    let alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    let rot13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']


    let index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
    let rotate = 13
    // let user_input = prompt("Enter word to rotate: ")
    let word = ""

    for (let i = 0; i < user_input2.length; ++i) {
        let letters = user_input2[i]
        let x = (alpha.indexOf(letters) + rotate) % 26
        word += alpha[x]
    }
    console.log(word)
    // alert(`Your rotated word is: ${word}`)
})