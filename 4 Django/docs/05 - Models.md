

# Models

- [Models](#models)
  - [Overview](#overview)
  - [Field Types](#field-types)
    - [Nullable Fields](#nullable-fields)
    - [Default Values](#default-values)
  - [Database Relationships](#database-relationships)
      - [Users](#users)
      - [Cities](#cities)
    - [One-to-One](#one-to-one)
    - [Many-to-One](#many-to-one)
    - [Many-to-Many](#many-to-many)
    - [on_delete](#on_delete)
  - [ORM Operations](#orm-operations)
    - [Example Model](#example-model)
    - [Create an Instance](#create-an-instance)
    - [Changing a Property on an Instance](#changing-a-property-on-an-instance)
    - [Save an Instance](#save-an-instance)
    - [Get All Rows](#get-all-rows)
    - [Get a Particular Row](#get-a-particular-row)
    - [Check if a Record Exists](#check-if-a-record-exists)
    - [Filter Rows](#filter-rows)
    - [Specify an Order](#specify-an-order)
    - [Specify the Number of Rows to Return](#specify-the-number-of-rows-to-return)
    - [Get the Number of Rows](#get-the-number-of-rows)


## Overview

Models are Python classes that parallel tables in the database. The ORM manages this dual representation, translating statements in Python to queries on the database. You can read more about models [here](https://docs.djangoproject.com/en/2.2/topics/db/models/), and more about the ORM [here](https://docs.djangoproject.com/en/2.2/ref/models/querysets/).

- [Polls Tutorial - Part 2](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)

Database tables are like excel spreadsheets: they have headers and rows. Tables can also be thought of as Python classes, where the headers are class attributes, and the rows are instances. All models are automatically given an `id` field as a primary key, which uniquely identifies a row.

| id | email_address | first_name | last_name |
| --- | --- | --- | --- |
| 1 | wendy@gmail.com | Wendy | Carson |
| 2 | alyssa@gmail.com | Alyssa	 | Lyons |
| 3 | brian@gmail.com | Brian | Barber |

```python
from django.db import models
class Contact(models.Model):
    email_address = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
contact1 = Contact(email='wendy@gmail.com', first_name='Wendy', last_name='Carson')
contact2 = Contact(email='alyssa@gmail.com', first_name='Alyssa', last_name='Lyons')
contact3 = Contact(email='brian@gmail.com', first_name='Brian', last_name='Barber')
```

## Field Types

You can read more about the field types [here](https://docs.djangoproject.com/en/2.2/ref/models/fields/).

- `BooleanField` represents a boolean (true/false) value
- `IntegerField` represents an integer
- `FloatField` represents a floating-point number
- `CharField` represents a string, requires `max_length` parameter indicating the number of characters
- `TextField` like `CharField` but has unlimited length
- `DateTimeField` represents a datetime (more [here](https://docs.djangoproject.com/en/2.2/topics/i18n/timezones/))
- `OneToOneField` represents a [one-to-one relationship](https://docs.djangoproject.com/en/2.2/topics/db/examples/one_to_one/)
- `ForeignKey` represents a [many-to-one relationship](https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_one/)
- `ManyToManyField` represents a [many-to-many relationship](https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_many/)

### Nullable Fields

Fields can be 'null' or absent. In Python, the attributes of the instances will be `None`. To declare these fields to be 'nullable', you must specify both `null=True` for the database, and `blank=True` to be able to leave an input field blank in the admin panel.

```Python
date_completed = models.DateTimeField(null=True, blank=True)
```

### Default Values

You can specify a default value for a field by adding `default=<value>`. That way, you can leave the value out when creating and saving an instance.

```python
class Person(models.Model):
    # ...
    age = models.IntegerField(default=0)

person = Person(name="mike") # no need to specify age
person.save()
```


## Database Relationships

The three types of database relationships: one-to-one, many-to-one, and many-to-many. The `id` field of a table is called the **primary key** because it uniquely identifies a row. When another table contains a reference to that `id` field, it's called a **foreign key**. In the following example, `city_id` on `Users` is a **foreign key**, `id` on Users and `id` on Cities are **Primary Keys**. This is an example of a **many-to-one relationship**.

#### Users
| id | email_address | first_name | last_name | city_id |
| --- | --- | --- | --- | --- |
| 1 | wendy@gmail.com | Wendy | Carson | 1 |
| 2 | alyssa@gmail.com | Alyssa	 | Lyons | 1 |
| 3 | brian@gmail.com | Brian | Barber | 2 |

#### Cities
| id | name |
| --- | --- |
| 1 | Portland |
| 2 | Eugene |

This relationship would be represented in Python as thus:

```python
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)

class User(models.Model):
    email_address = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
```

### One-to-One

A one-to-one relationship means that for every row in table A, there will be a single corresponding row in table B. An example might be between [counties and capital cities](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/CPT-Databases-OnetoOne.svg/460px-CPT-Databases-OnetoOne.svg.png). Any country only has one capital. Any capital only pretains to one country. You can read more about one-to-one relationships [here](https://docs.djangoproject.com/en/2.2/topics/db/examples/one_to_one/). Normally a one-to-one relationship is unnecessary, because one could just take the fields from both models and put them onto one model. But you may have to associate new fields with an old model without changing the old model, or need to restrict access to certain data [more info](https://stackoverflow.com/questions/25206447/when-to-use-one-to-one-relationships-in-django-models).


```python
from django.db import models

class CapitalCity(models.Model):
    name = models.CharField(max_length=200)

class Country(models.Model):
    name = models.CharField(max_length=200)
    capital = models.OneToOneField(CapitalCity, on_delete=models.CASCADE)
```

```python
capital_city = CapitalCity(name='Canberra')
capital_city.save()

country = Country(name='Australia', capital=capital_city)
country.save()

print(country.capital.name) # Canberra
print(capital_city.country.name) # Australia
```

### Many-to-One

A many-to-one relationship means that for every row in table A, there may be multiple rows in table B connected to it. An example might be between a [mother and her children](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/CPT-Databases-OnetoMany.svg/460px-CPT-Databases-OnetoMany.svg.png). A mother may have multiple children, but any child only has one mother. You can read more about many-to-one relationships [here](https://docs.djangoproject.com/en/2.1/topics/db/examples/many_to_one/).


```python
from django.db import models

class Mother(models.Model):
    name = models.CharField(max_length=200)

class Child(models.Model):
    name = models.CharField(max_length=200)
    mother = models.ForeignKey(Mother, on_delete=models.PROTECT)
```


### Many-to-Many

An example might be between [authors and books](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/CPT-Databases-ManytoMany.svg/460px-CPT-Databases-ManytoMany.svg.png). One book may have multiple authors. One author may have multiple books. To define such a relationship, you can create a [junction table](https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Databases-ManyToManyWJunction.jpg/800px-Databases-ManyToManyWJunction.jpg) with two many-to-one relationships. Or you can use a `ManyToManyField`
You can read more about many-to-many relationships [here](https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_many/).


### on_delete

The `on_delete` parameter lets you control what to do with other rows when a connected row is deleted. You can read more about `on_delete` [here](https://docs.djangoproject.com/en/2.2/ref/models/fields/#arguments). The important options are:

- `CASCADE` deleted this row when the other is deleted
- `PROTECT` throws an exception when the other is deleted, this forces the developer re-assign the relationship when they want to delete a row
- `SET_NULL` sets the field containing the relationship to null (the field must also be nullable)
- `SET_DEFAULT` sets the field containing the relationship to its default value (a default must be specified)


## ORM Operations

The ORM 'object relational mapping' provides functions in Python that perform operations on the database. To read more about ORM operations, look [here](https://docs.djangoproject.com/en/2.2/topics/db/queries/). Note that `__init__`, `get`,  and `filter` take `**kwargs` (which turns named parameters into a dictionary), whereas `order_by` takes `*args` (which turns arguments into a list).

### Example Model

```python
class TodoItem(models.Model):
    todo_text = models.CharField(max_length=200)
    date_entered = models.DateTimeField()
    date_completed = models.DateTimeField(null=True, blank=True)
```


### Create an Instance

```python
from django.utils import timezone
...
todo_text = "wash the dishes"
todo_item = TodoItem(todo_text=todo_text, date_entered=timezone.now(), date_completed=None)
```

### Changing a Property on an Instance

```python
todo_item.todo_text = 'walk the dog'
```

### Save an Instance

Just call `save()` on an instance.

```python
todo_item.save()
```


### Get All Rows

To get all the rows in a table use `all()`.

```python
todo_items = TodoItem.objects.all()
```


### Get a Particular Row

To get a particular row, use `get()`. Here we're getting the item with a given primary key (pk), but you can use any attribute.

```python
item_id = 5
item = TodoItem.objects.get(pk=item_id)
```

This will raise an exception if the record is not found. A safer way is like this.

```python
item = TodoItem.objects.filter(pk=item_id).first()
```

### Check if a Record Exists

```python
if TodoItem.objects.filter(pk=item_id).exists():
    ...
```

### Filter Rows

You can `filter` particular rows by specifying a particular field's value. This is like `get` but you get multiple results instead of the first matching one.

```python
todo_items = TodoItem.objects.filter(todo_text='water the roses')
```

To filter variables by whether or not a field is null, use `<field_name>__isnull`
```python
completed_items = TodoItem.objects.filter(date_completed__isnull=False)
```

### Specify an Order

To specify an order, use `order_by`, which takes any number of strings containing the names of the fields to sort by. By default sort is ascending, use a negative symbol `-` to sort in the descending order.

```python
todo_items = TodoItem.objects.order_by('-date_entered', '-date_completed')
```


### Specify the Number of Rows to Return

To limit the number of items returned, use slicing.

```python
# only get the first 5 results
todo_items = TodoItem.objects.all()[:5]
```

### Get the Number of Rows