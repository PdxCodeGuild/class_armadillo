# Lab 2: Todo

## Version 1

Let's create a simple todo app. This can be done with a single model **TodoItem** which contains a text **description**, a **created date**, a **completed date**, and a boolean representing whether it was **completed**. The index page should list all the todo items, and a text field and a button (in a form). When the clicks the button, it should saves a new todo item to the server and shows the newly-added item in the list. Use one view to render the template, and another view to receive the form submission and redirect back to the first view.


## Version 2

Add a button next to each todo item to complete it. Show completed items in a separate list (or at the bottom of the existing list) with grey color and maybe a line through them.

## Version 3 (optional)

Let's add a **Priority** model with a **name** field (e.g. low, medium, high). Then add a **foreign key** to the **TodoItem** linking it to a **Priority**. The form for creating a todo item should also have a dropdown list for selecting the priority. Display the priority in the list of todo items.

## Version 3 (optional)

Let's add a separate form for deleting a todo item. It should contain a drop-down list of items, and a submit button to delete one. This should also use a separate view for receiving the form submission.



