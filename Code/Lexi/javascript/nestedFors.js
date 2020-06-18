// Let's get some practice working with complex data structures. Copy-paste the data structure below into a minilab.html file and extract the relevant information from it. The books on each of the users is an array of integers representing the indices of their favorite books in the books array.

// Problem 1: What is the name of the library?

// Problem 2: How many library users are there?

// Problem 3: What is the average age of the library users?

// Problem 4: What is the oldest book? (print the name and year)

// Problem 5: What is the most favorited book? (print the name and the number of users that like it)



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
};

// Problem 1: What is the name of the library?
// Querying the first object to get the name of the library
// id=problem1
let libraryName = library['meta']['name'];
let problem1 = document.querySelector('#problem1');
problem1.innerHTML = libraryName;

// Problem 2: How many library users are there?
// 'users' object gives back an array of 'user' objects
// Querying the 'Users' object and using .length method on the array
// id=problem2
let userLength = library['users'].length;
let problem2 = document.querySelector('#problem2');
problem2.innerHTML = userLength;

// Problem 3: What is the average age of the library users?

// Initializing variable for adding ages together
let average = 0;
// Iterate over 'users' object and query the 'age' in each object and adding it to averaeg
for(let user of library['users']) {
    // user['age'] -> 5
    average += (user['age']);
}
// find the average of the counter variable, and using .length method on the 'users' array to find the length to divide by
let ageAverage = Math.floor(average / library['users'].length);
let problem3 = document.querySelector('#problem3');
problem3.innerText = ageAverage;

// Problem 4: What is the oldest book? (print the name and year)

// initializing empty array to add the years to
let publishedDate = [];

// Iterating over books object -> each 'book' is an object
for(let book of library['books']) {
    // book['published'] -> Book object year -> 1354
    // publishedDate is an empty array that we are adding the year to -> adding an additional year
    publishedDate.push(book['published']);
};
// using sort() method on the array
publishedDate.sort()
// declaring variable to be the first index of the publishedDate array -> this gives us the earliest year
let oldestPublishedBook = publishedDate[0]
let problem4 = document.querySelector('#problem4');
problem4.innerText = oldestPublishedBook;


// Problem 5: What is the most favorited book? (print the name and the number of users that like it)
// create a new array and initialize elements
let mostFavoriteBook = new Array(library['books'].length)
console.log(mostFavoriteBook)
// (4) [0, 0, 0, 0]
// 0: 0
// 1: 0
// 2: 0
// 3: 0


for(let i = 0; i < mostFavoriteBook.length; i++) {
    mostFavoriteBook[i] = 0;
};


// i is the user
for(let i = 0; i < library['users'].length; i++) {
    // j is each favorited book
    // iterating over each users favorite_book
    for(let j = 0; j < library['users'][i]['favorite_books'].length; j++) {
        // if users like is for the book
        // adding the likes from 'favorite_book' TO the mostFavoriteBook array.
        mostFavoriteBook[library['users'][i]['favorite_books'][j]] += 1;
    }
};
// results
// (4) [2, 3, 2, 1]
// 0: 2
// 1: 3
// 2: 2
// 3: 1
// length: 4
let book = 0;
// iterating over mostFavoriteBook array -> checking to see if element of mostFavoriteBook is greater/equal than book which is holding who has the most
for(let i = 0; i < mostFavoriteBook.length; i++) {
    if(mostFavoriteBook[i] >= mostFavoriteBook[book]) {
        // setting the counter to equal the new highest book
        book = i;
    }
};

let favoriteBookTitle = library['books'][book]['title']
let favoriteBook = mostFavoriteBook[book]

let problem5 = document.querySelector('#problem5');
problem5.innerText = `Title: ${favoriteBookTitle}  -  Likes: ${favoriteBook}`;