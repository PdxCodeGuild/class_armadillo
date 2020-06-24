

# Vue - Guess the Number

## Version 1

1. In your app's data, add a property `num_to_guess` to represent the number the user will guess, the initial value should be a random integer 1-10.
2. Use a `v-for` to generate 10 html buttons for the numbers 1-10.
3. Add a `v-on:click` to each button which calls an app method `guessNumber` and passes the selected number as a parameter.
4. In `guessNumber` detemine whether they've guessed the correct number. If it's incorrect, tell the user. If it's correct, tell the user and choose a new random number

## Version 2

Keep track of the number of guesses using another app property `num_guesses`. If the user gets 10 wrong guesses, tell them they've lost and restart the game.

## Version 3 (optional)

Disable the buttons as the user clicks them so they cannot click them again. Once the game is over, re-enable all the buttons.

