 let choices = ["rock", "paper", "scissors"]
 
 let user_choice = prompt(" choose rock, paper, scissors") 
alert("you have entered " + user_choice)

let index = Math.floor(Math.random() * choices.length)



let computer_choice = choices[index]
alert("computer chose " + computer_choice)

if (user_choice == computer_choice){
    alert('tie')
}else if (user_choice == 'rock' && computer_choice == 'paper'){
    alert('you lose')
}else if (user_choice == 'rock' && computer_choice == 'scissors'){
    alert('you WIN')
}else if (user_choice == 'paper' && computer_choice == 'scissors'){
    alert('you lose')
}else if (user_choice == 'scissors' && computer_choice == 'rock'){
    alert('you lose')
}else if (user_choice == 'scissors' && computer_choice == 'paper'){
    alert('you win!')
}


