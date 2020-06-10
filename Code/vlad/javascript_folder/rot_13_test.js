// let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
//         let index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
//         let rot13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
//         let rotation = parseInt(prompt('what is the rotation amount? ')) // make sure to put in integer around the rotations parseInt()
//         let user_input = prompt('Enter any word: ')
//         let word = ''

//         for (let i = 0; i < user_input.length; i++) {
//             // console.log(user_input[i])
//             let letter = user_input[i]
//             let x = (alphabet.indexOf(letter) + rotation) % 26
//             word += alphabet[x]

//         }
//         alert(word)
let sentenceOriginal = "The NBA is Back! on Jul 31 2020"
let sentenceLower = sentenceOriginal.toLowerCase()

sentenceOriginal
sentenceLower