

# Vanilla vs Vue

- [Vanilla vs Vue](#vanilla-vs-vue)
  - [Setting Inner Text](#setting-inner-text)
  - [Setting Inner HTML](#setting-inner-html)
  - [Handling Events](#handling-events)
  - [Getting Input](#getting-input)


## Setting Inner Text

**Vanilla**
```html
<div id="mydiv"></div>
<script>
    let mydiv = document.querySelector('#mydiv')
    mydiv.innerText = 'hello world!'
</script>
```

**Vue**
```html
<div id="app">
    <div>{{message}}</div>
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

## Setting Inner HTML

**Vanilla**
```html
<div id="mydiv"></div>
<script>
    let mydiv = document.querySelector('#mydiv')
    mydiv.innerHTML = '<b>hello world!</b>'
</script>
```

**Vue**
```html
<div id="app">
    <div v-html="message"></div>
</div>
<script>
    let app = new Vue({
        el: '#app',
        data: {
            message: '<b>hello world!</b>'
        }
    })
</script>
```

## Handling Events

**Vanilla**
```html
<button id="mybutton">click</button>
<script>
    let mybutton = document.querySelector('#mybutton')
    mybutton.addEventListener('click', function() {
        alert('hello world!')
    })
</script>
```

**Vue**
```html
<div id="app">
    <button v-on:click="sayHello">click</button>
</div>
<script>
    let app = new Vue({
        el: '#app',
        methods: {
            sayHello: function() {
                alert('hello world!')
            }
        }
    })
</script>
```

## Getting Input

**Vanilla**
```html
<input id="myinput" type="text"/>
<button id="mybutton">click</button>
<script>
    let mybutton = document.querySelector('#mybutton')
    let myinput = document.querySelector('#myinput')
    mybutton.addEventListener('click', function() {
        alert(myinput.value)
    })
</script>
```

**Vue**
```html
<div id="app">
    <input type="text" v-model="messasge"/>
    <button v-on:click="sayHello">click</button>
</div>
<script>
    let app = new Vue({
        el: '#app',
        data: {
            message: 'hello world!'
        },
        methods: {
            sayHello: function() {
                alert(this.message)
            }
        }
    })
</script>
```


