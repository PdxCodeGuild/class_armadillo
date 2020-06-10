


// thisIsCamelCase
// this_is_snake_case
// ThisIsPascalCase
// this-is-kebab-case


function getCardValue(card) {
    card = card.toLowerCase()
    if (!isNaN(card)) {
        return parseInt(card)
    } else if (card == 'a') {
        return 1
    } else if (card == 'j' || card == 'q' || card == 'k') {
        return 10
    }
    return null

    // let card_values = {
    //     'a': 1,
    //     '2': 2,
    //     '3': 3,
    //     // ...
    //     'j': 10
    // }
    // return card_values[card]
}

let card1 = prompt('Enter card 1')
let card2 = prompt('Enter card 2')
let card3 = prompt('Enter card 3')

let total = getCardValue(card1) + getCardValue(card2) + getCardValue(card3)
alert('The total is ' + total)
if (total < 17) {
    alert('hit')
} else if (total < 21) {
    alert('stay')
} else if (total == 21) {
    alert('blackjack')
} else {
    alert('busted')
}


