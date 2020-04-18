// Guess the number game

const userNum = 5;
let guesses = 0;

console.log('Computer has 10 tries to guess the number.')
while(guesses <= 10) {
    const computerNum = Math.round(Math.random() * 11);
    if(userNum != computerNum) {
        console.log(`Computer guessed [${guesses}]: ${computerNum}`);
        guesses++;
        continue;
    } else {
        console.log(`Computer guessed [${guesses}]: ${computerNum}`);
        console.log(`Computer guessed the Secret Number in ${guesses}`);
        break;
    }
};