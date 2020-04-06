
# Lab: Quiz

Using the object below, construct a GUI for the quiz.
- show the quiz title and first question with radio buttons
- add a button for going to the next question
- keep track of the user's score

```html

<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Quiz</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
      /* todo */
    </style>
  </head>
  <body>
    <!-- todo -->
    <script type="text/javascript">

      let quiz = {
        title: 'JavaScript Quiz',
        questions: [{
          text: 'How do you increment a number in JavaScript?',
          answers: [{
            text: 'i = i + 1',
            correct: false
          },{
            text: 'i += 1',
            correct: false
          },{
            text: 'i++',
            correct: false
          },{
            text: '++i',
            correct: false
          },{
            text: 'i -= -1',
            correct: false
          },{
            text: 'all of the above',
            correct: true
          }]
        },{
          text: 'In what order are the parts of a for loop?',
          answers: [{
            text: 'initialization, condition, increment',
            correct: true
          },{
            text: 'condition, initialization, increment',
            correct: false
          },{
            text: 'initialization, increment, condition',
            correct: false
          },{
            text: 'condition, initialization, increment',
            correct: false
          }]
        },{
          text: 'What\'s the difference between == and ===?',
          answers: [{
            text: 'nothing',
            correct: false
          },{
            text: '== coerces types, === does not'
            correct: true
          },{
            text: '=== coerces types, == does not',
            correct: false
          }]
        }]
      }


      // todo


    </script>
  </body>
</html>

```
