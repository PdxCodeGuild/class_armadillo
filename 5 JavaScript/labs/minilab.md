

# Minilab

Let's get some practice working with complex data structures. Copy-paste the data structure below into a `minilab.html` file and extract the relevant information from it. The `books` on each of the `users` is an array of integers representing the indices of their favorite books in the `books` array.


Problem 1: What is the name of the library?

Problem 2: How many library users are there?

Problem 3: What is the average age of the library users?

Problem 4: What is the oldest book? (print the name and year)

Problem 5: What is the most favorited book? (print the name and the number of users that like it)

```javascript
let library = {
    meta: {
        name: 'A Little Library',
        description: 'practice for working with complex data'
    },
    users: [{
        first_name: 'Jane',
        last_name: 'Smith',
        age: 24,
        favorite_books: [0, 2, 3]
    },{
        first_name: 'Wendy',
        last_name: 'Carson',
        age: 56,
        favorite_books: [0, 1]
    },{
        first_name: 'Brian',
        last_name: 'Barber',
        age: 12,
        favorite_books: [1]
    },{
        first_name: 'Alyssa',
        last_name: 'Lyons',
        age: 34,
        favorite_books: [1, 2]
    }],
    books: [{
        title: 'A Wrinkle in Time',
        author: 'Madeleine L\'Engle',
        published: 1962
    },{
        title: 'The Giving Tree',
        author: 'Shel Silverstein',
        published: 1964
    },{
        title: 'The Odyssey',
        author: 'Homer',
        published: -800
    },{
        title: 'The Divine Comedy',
        author: 'Dante Alighieri',
        published: 1320
    }]
}
```
