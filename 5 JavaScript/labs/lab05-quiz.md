

# Lab: Quiz

Using the code below, construct a GUI for the quiz.
- Show controls for picking the quiz parameters and a button for starting the quiz
- Allow the user to select answers and go to the previous/next question
- At the end, show the user's score
- (optional) Highlight the correct answer and the incorrect answer the user selected

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  </head>
  <body>
    <div id="app">
      <input type="number" v-model="input_amount"/>
      <button v-on:click="startQuiz">start</button>
      <div v-for="question in questions" v-html="question.question"></div>
    </div>
    <script type="text/javascript">
      let app = new Vue({
        el: '#app',
        data: {
          input_amount: 10,
          questions: []
        },
        methods: {
          startQuiz: function() {
            axios({
              method: 'get',
              url: 'https://opentdb.com/api.php',
              params: {
                amount: this.input_amount,
                category: 18,
                difficulty: 'easy'
              }
            }).then((response) => {
              this.questions = response.data.results
            })
          }
        }
      })
    </script>
  </body>
</html>
```