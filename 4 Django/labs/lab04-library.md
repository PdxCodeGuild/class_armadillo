
# Lab 4: Library

Let's create an application for representing a library. You should have two models (below) and a page for users to check out and check in books. You can enter the book and author information using the admin panel.

### Models

- Book
  - title (string)
  - publish date (datetime)
  - author (foreign key)
  - checked_out_by (nullable foreign key to User)
- Author
  - name (string)

### Pages

- Index
  - list all the books and whether they're checked out
  - form with drop-down list of books that haven't been checked out, and a "checkout" button

## Version 2

Add another model to keep track of who checked out a book and when. When a user checks a book back in, record that too. Add a text input on the 'checkout' page to record the name of who checked out the book. When a book is checked out, add a row to this table with the checkin date equal to null. When the book is checked back in, set the checkin date.

- BookCheckout
  - checked_out_by (foreign key to User, who checked it out)
  - book (foreign key)
  - checkout date (datetime)
  - checkin date (datetime, null until checked back in)

Add a "book detail" page

- Detail
  - Show all the book's information
  - Show all the checkout records for that book
