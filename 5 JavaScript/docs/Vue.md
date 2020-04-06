


# Vue.js


Front-end frameworks like **Vue**, **React** (Facebook), and **Angular** (Google) can be used to create complex, interactive web pages. The principle advantage they offer is the separation of *display* and *data*. Developing complex pages in [vanilla JavaScript](http://vanilla-js.com/) becomes cumbersome and messy, every time an value is updated, certain HTML elements must be created or hidden, have its style changed, have its inner text changed, etc. Libraries like **Vue.js** allows  the HTML section to decide how things are displayed and allows the JavaScript section to decide how data is processed.


## 1 Rendering Values

Render variables in the HTML using `{{}}`.

```html
<div id="app">
  <span>{{ message }}</span>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      message: 'hello world!'
    }
  })
</script>
```

## 2 Setting Attributes

Set attribute values using `v-bind`.

```html
<div id="app">
  <img v-bind:src="image_url"/>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      image_url: 'https://placekitten.com/200/200'
    }
  })
</script>
```

## 3 Conditionals


There are two directive for controlling the visibility of an HTML element, `v-if` and `v-show`. If the variable they're associated with is `true`, the element will be shown, if it is `false`, it won't be. `v-if` actually removes the element, while `v-show` simply hides it. `v-if` has a higher toggle cost, but `v-show` has a higher initial cost (if the value is initially `false`). [link](https://vuejs.org/v2/guide/conditional.html#v-if-vs-v-show)

```html
<div id="app">
  <span v-if="seen">some text</span>
  <span v-show="seen">some text</span>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      seen: true
    }
  })
</script>
```

## 4 Loops

Loop over a list using `v-for`, repeatedly generating elements. Just like with Python, the variable name is arbitrary. You can optionally add an index.

```html
<div id="app">
  <ul>
    <li v-for="color in colors">{{ color }}</li>
  </ul>
  <ul>
    <li v-for="(color, index) in colors">{{ index }}) {{ color }}</li>
  </ul>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      colors: ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    }
  })
</script>
```

## 5 Input Fields

You can bind app variables to input fields using `v-model`. If the user changes the value of the input field, the variable in the app will be updated and vice versa.


```html
<div id="app">
  <input type="text" v-model="name"/>
  <select v-model="color">
    <option value="red">red</option>
    <option value="green">green</option>
    <option value="blue">blue</option>
  </select>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      name: 'bob',
      color: 'red',
    }
  })
</script>
```

## 6 Event Listeners

Bind events on elements to methods using `v-on`.

```html
<div id="app">
  <button v-on:click="doSomething">click</button>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {},
    methods: {
      doSomething: function() {
        alert('clicked!')
      }
    }
  })
</script>
```


## 7 Lifecycle Hooks

Lifecycle hooks are special functions called throughout the lifecycle of a Vue app.

```html
```html
<div id="app">
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {},
    created: function() {
      alert('app created!')
    }
  })
</script>
```
```