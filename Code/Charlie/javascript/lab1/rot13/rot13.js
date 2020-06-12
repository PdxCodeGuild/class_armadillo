let user_input = document.querySelector('#user_input')
let btn_submit = document.querySelector('#btn_submit')

btn_submit.addEventListener('click', function(){
    let user_input2 = user_input.value

    let alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    let rotate = 13
    
    let word = ""

    for (let i=0; i<user_input2.length; ++i) {
        let letters = user_input2[i]
        let x = (alpha.indexOf(letters) + rotate) % 26
        word += alpha[x]
    }
    console.log(word)
    alert(`Your rotated word is: ${word}`)
})