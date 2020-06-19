let user_input = document.querySelector('#user_input')
let btn_submit = document.querySelector('#btn_submit')
let output = document.querySelector('#output')

btn_submit.addEventListener('click', function(){
    let user_input2 = user_input.value
    let choices = ["rock", "paper", "scissors"]
    // let user_choice = prompt(` choose: rock, paper, scissors`) 
    let index = Math.floor(Math.random() * choices.length)
    let computer_choice = choices[index]
    let result = ""
    
    
    if (user_input2 == computer_choice){
        result = (`its a tie you chose ${user_input2} and computer chose ${computer_choice}`)
    }else if (user_input2 == 'rock' && computer_choice == 'paper'){
        result = (`you lose: you chose ${user_input2} and computer chose ${computer_choice}`)
    }else if (user_input2 == 'rock' && computer_choice == 'scissors'){
        result = (`you win: you chose ${user_input2} and computer chose ${computer_choice}`)
    }else if (user_input2 == 'paper' && computer_choice == 'scissors'){
        result = (`you lose: you chose ${user_input2} and computer chose ${computer_choice}`)
    }else if (user_input2 == 'scissors' && computer_choice == 'rock'){
        result = (`you lose: you chose ${user_input2} and computer chose ${computer_choice}`)
    }else if (user_input2 == 'scissors' && computer_choice == 'paper'){
        result = (`you win!: you chose ${user_input} and computer chose ${computer_choice}`)
    }
    output.innerText = `${(result)}`
})    