

# Lab 10: Quiz

Let's build a quiz using the [Open Trivia DB](https://opentdb.com/) Using the code below, construct a GUI for the quiz.
- Show each question and answers with radio buttons
- Allow the user to select answers and go to the previous/next question
- At the end, show the user's score
- (optional) Highlight the correct answer and the incorrect answer the user selected
- (optional) Show controls for picking the quiz parameters (amount, category, difficulty)

```javascript
axios({
  method: 'get',
  url: 'https://opentdb.com/api.php',
  params: {
    amount: 10,
    category: 18,
    difficulty: 'easy'
  }
}).then(response => {
  let questions = response.data.results
  console.log(questions)
})
```