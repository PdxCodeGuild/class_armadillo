
# Lab 3: Contacts

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

## Views

The application will have the following views:

- `/contacts/` will render a template containing a `new contact` button, as well as a list of contacts each with a `view contact` button
- `/contacts/<id>/` will be a detail page for a contact with the given `id`
- `/contacts/new/` will render a template containing a form for creating a new contact
- `/contacts/new/submit/` will receive the form submission from `/contacts/new/`, create a new contact in the database, and redirect to the detail page for the newly created contact

## Version 2 (optional)

Add the ability to delete a contact, and a separate page for editing a contact (basically the same form as the new contact, but with all the fields pre-populated with a given contact's info).
