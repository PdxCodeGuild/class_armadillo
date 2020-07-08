

# Forms

- [Forms](#forms)
  - [Using Forms Without the Form Class](#using-forms-without-the-form-class)
  - [The Form Class](#the-form-class)
  - [The ModelForm Class](#the-modelform-class)
  - [Using Forms with CSS Frameworks](#using-forms-with-css-frameworks)


## Using Forms Without the Form Class

Let's take a look back at [HTML forms](../../2%20HTML+CSS/docs/03%20-%20HTML%20Forms.md). You don't have to do anything special to use forms in Django. The `input` elements need `name` attributes, the `action` attribute of the form needs to point to a view. When you submit the data, the form will gather all the `name` attributes from the `input` fields and associate them with each `input`'s `value`.

```html
<form action="{% url 'contacts:save_contact' %}" method="post">
    {% csrf_token %}
    <input type="text" name="contact_name"/>
    <input type="number" name="contact_age"/>
    <button type="submit">save contact</button>
</form>
```

Django will take the name-value pairs from the request and put them into a dictionary-like object `request.POST`. You can then access those values from the view using the value of the `name` attribute as a key.

```python
# a view for receiving a form submission
def save_contact(request):
    # verify we received the form data
    print(request.POST)
    # get the form data out of request.POST
    contact_name = request.POST['contact_name']
    contact_age = request.POST['contact_age']
    # create an instance of our model
    contact = Contact(name=contact_name, age=contact_age)
    # save a new record to the database
    contact.save()
    # redirect the the index page
    return HttpResponseRedirect(reverse('contacts:index'))
```

## The Form Class

Django has a special Form class to make the creation of forms easier. These also do input validation on the front-end and the back-end for you. You can read in the official docs: [Working with Forms](https://docs.djangoproject.com/en/3.0/topics/forms/), [Forms API](https://docs.djangoproject.com/en/3.0/ref/forms/api/#django.forms.Form). You can put your forms in a `forms.py` inside your app.


**forms.py**
```python
from django import forms
class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Contact Name', max_length=100)
    contact_age = forms.IntegerField(label='Contact Age')
```

**views.py**
```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
def index(request):
    if request.method == 'POST': # receiving a form submission
        # create an instance of our form from the form data
        form = ContactForm(request.POST)
        if form.is_valid():
            # get the data out of the form
            contact_name = form.cleaned_data['contact_name']
            contact_age = form.cleaned_data['contact_age']
            # create an instance of our model from the data
            contact = Contact(name=contact_name, age=contact_age)
            # save a new record to the database
            contact.save()
            # create a new blank form for the template
            form = ContactForm()
        # if the form is invalid, we just send it back to the template
    else: # receiving a GET request
        form = ContactForm() # create a new blank form
    return render(request, 'contacts/index.html', {'form': form}) # pass the form to the template
```

**index.html**
```html
<form action="{% url 'contacts:index' %}" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>
```


## The ModelForm Class

ModelForms allow us to generate a form directly from a model. You can read more about ModelForms in the [official docs](https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/).

**models.py**
```python
from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

**forms.py**
```python
from django.forms import ModelForm
from .models import Contact
class TodoForm(ModelForm):
    class Meta:
        # the model to associate with the form
        model = Contact
        # a list of all the models' fields you want in the form
        # fields = ['text']
        # or just use all of them
        fields = '__all__'
```

**views.py**
```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
def index(request):
    if request.method == 'POST': # receiving a form submission
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # save the todo item associated with the form
            form = ContactForm() # create a new blank form
        # if the form is invalid, we just send it back to the template
    else: # receiving a GET request
        form = ContactForm() # create a new blank form
    return render(request, 'contacts/index.html', {'form': form}) # pass the form to the template
```

**index.html**
```html
<form action="{% url 'contacts:index' %}" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>
```

## Using Forms with CSS Frameworks

CSS Frameworks like Boostrap and Materialize have specific ways their forms are structures, and don't work with the default forms very well. [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) allow you to better control how forms are rendered.

- [tutorial on using bootstrap w/ django forms](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)
- [library for using materialize w/ django forms](https://pypi.org/project/crispy-forms-materialize/)
