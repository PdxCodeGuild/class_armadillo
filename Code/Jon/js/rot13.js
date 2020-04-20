const abcList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

let rotation = parseInt(prompt('Please enter in a rotation'));
let user_input = prompt('Please enter in a code to encrypt');


for(let letter of user_input) {
    let letterIndex = abcList.indexOf(letter)
    let encryptedLetter = ((letterIndex + rotation) % 26)
    user_input = user_input.replace(letter, abcList[encryptedLetter])
}
console.log(user_input)



