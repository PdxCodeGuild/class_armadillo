let choices = ["rock", "paper", "scissors"]
 
let user_choice = prompt(` choose: rock, paper, scissors`) 

let index = Math.floor(Math.random() * choices.length)
let computer_choice = choices[index]


if (user_choice == computer_choice){
    alert(`its a tie you chose ${user_choice} and computer chose ${computer_choice}`)
}else if (user_choice == 'rock' && computer_choice == 'paper'){
    alert(`you lose: you chose ${user_choice} and computer chose ${computer_choice}`)
}else if (user_choice == 'rock' && computer_choice == 'scissors'){
    alert(`you win: you chose ${user_choice} and computer chose ${computer_choice}`)
}else if (user_choice == 'paper' && computer_choice == 'scissors'){
    alert(`you lose: you chose ${user_choice} and computer chose ${computer_choice}`)
}else if (user_choice == 'scissors' && computer_choice == 'rock'){
    alert(`you lose: you chose ${user_choice} and computer chose ${computer_choice}`)
}else if (user_choice == 'scissors' && computer_choice == 'paper'){
    alert(`you win!: you chose ${user_choice} and computer chose ${computer_choice}`)
}