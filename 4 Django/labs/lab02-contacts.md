
# Lab 2: Contacts

Let's build a CRUD application for managing a contact list.

## Model

Our `Contact` model will have the following fields:

| field name | Django model field | html element |
| ----       | --------           | ----------   |
| `first_name` | `CharField` | `<input type="text"/>` |
| `last_name` | `CharField` | `<input type="text"/>` |
| `age` | `IntegerField` | `<input type="number"/>` |
| `birthday` | `DateField` | `<input type="date"/>` |
| `phone_number` | `CharField` | `<input type="text" pattern="?"/>`
| `is_cell` | `BooleanField` | `<input type="checkbox"/>` |
| `comments` | `TextField`| `<textarea></textarea>` |

## Pages

The application will have the following views:

- `/contacts/` will render a template containing a `new contact` button, as well as a list of contacts each with a `view contact` button and an `edit contact` button
- `/contacts/<id>/` will be a detail page for a contact with the given `id`
- `/contacts/new/` will render a template containing a form for creating a new contact
- `/contacts/new/submit/` will receive the form submission from `/contacts/new/`, create a new contact in the database, and redirect to the detail page for the newly created contact
- `/contacts/<id>/edit/` will have a form for editing a contact

## Steps

These are the recommended steps:

1. Define the model in the app's `models.py`
2. Register the model with the admin page, log in and create some records to make sure everything works
3. Create the contact detail page, which displays the different fields and their values
4. Create the new contact page
5. Create the edit contact page

