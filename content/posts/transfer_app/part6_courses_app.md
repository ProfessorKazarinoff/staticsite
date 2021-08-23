Title: Oregon Engineering College Transfer App - Part 6: Courses App
Date: 2021-08-23 12:40
Modified: 2021-08-23 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-6-Courses App
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 6
Summary: This is the 6th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this sixth post, we are going to create a new Django App to house our courses model.

This is the 6th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this sixth post, add a way for users to log into the site.

[TOC]

## Our project so far

So far, the files we have in our website project are shown below:

```text

```

We have created a Django project called ```transfer_project``` and created two Django Apps, a ```pages``` app and a ```user``` app. We've created a few html templates and url routes.

Next we will create a ```courses``` app that will house our Course model.

## The general django app flow

So far we have created two Django apps. The process of creating a new web page that we used to build our home and about pages is the same steps that we'll use to create our courses page

 * create courses app
 * add courses app to settings.py
 * create a courses page template
 * modify project urls
 * create courses urls
 * create a courses view

## Create a courses app

To help with the forms part of the login and logout pages, we'll use a Python package called django-crispy-forms. This package will help use build the login form and give some bootstrap4 styling to the form. We have bootstrap styling on the rest of the site on the home and about pages, so having bootstrap styling on the login page too helps keep the look of the site consistant. To install django-crispy-forms, we can use the Anaconda prompt and install from the conda-forge channel. Make sure to intall django-crisp-forms into the ```(transfer)``` virtual environment.

```text
> cd Documents
> cd transfer-app
> conda activate transfer-app
(transfer-app) > python manage.py startapp courses 
```

This command adds a new app to our project. The directory structure now looks like the file structure below:

```text

```

## Add courses app to the list of installed apps

Just like what we did with our users app and our pages app, we need to add our new courses app to the list of installed apps in our ```settings.py``` file. Open ```settings.py``` and see the addition below.

```python
# transfer_project/settings.py

# Application definition

INSTALLED_APPS = [
    # project specific
    'pages.apps.PagesConfig',
    'users.apps.UsersConfig',
    'courses.apps.CoursesConfig,
    
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    
]

```


## Create a courses template

Next, we'll build a courses page that shows all the courses we add to the database. That means we need to create a courses template. Let's put this tempate in the templates/courses directory. The directory strucutre of the entire Django project is below:

```text
├───pages
│   ├───migrations
│   │   └───__pycache__
│   ├───static
│   │   └───css
│   └───__pycache__
├───templates
│   ├───pages
│   ├───courses
│   └───users
├───transfer_project
│   └───__pycache__
└───users
```

The html below needs to be pasted into the ```courses.html``` file in the ```templates/courses/``` directory.

```html
<!-- templates/courses/courses.html -->

{% extends 'bootstrap_base.html' %}
{% load crispy_forms_tags %}

{% block content %}
    <div class="jumbotron">
        <div class="content-section">
            <form method="POST">
                {% csrf_token %}
                <fieldset class="form-group">
                    <legend class="border-bottom mb-4"><h1>Log In</h1></legend>
                    {{ form|crispy }}
                </fieldset>
                <div class="form-group">
                    <button class="btn btn-lg btn-success" type="submit">Login</button>
                </div>
            </form>
            <div class="border-top pt-3">
                <small class="text-muted">
                    Need An Account? <a class="ml-2" href="{% url 'home' %}">Sign Up Now</a>
                </small>
            </div>
        </div>
    </div>
{% endblock content %}
```

## Modify project urls

Now that the login template is created, we need to create a url pattern that points to the template. When a user browses to https://domain.com/login, the login template should pop up. Edit the transfer_project/urls.py file to include a new route for the login template. We'll use Djangos build in ```django.contrib.auth.views.LoginView``` as the view function. Note the import line ```from django.contrib.auth import views as auth_views```. There are going to end up being a lot of functions in this urls.py file with the name ```views```, so we create the alias ```auth_views``` to prevent function name duplication.

```python
# transfer_project/urls.py

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', include('pages.urls')),
]

```

## Create the courses url routes

```python


```

## Create a courses view



## Build tests for courses page

Since we have two new pages, we need to write some new tests. We already have a couple tests. There is a test for the homepage and a test for the about page. We can improve these tests by adding an ```assertTemplateUsed()``` test for both pages.

```python
# pages/tests.py

from django.test import SimpleTestCase, TestCase

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class AboutPageTests(SimpleTestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

class LoginPageTests(SimpleTestCase):

        def test_login_page_status_code(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_login_view_uses_correct_template(self):
        response = self.client.get(reverse('logout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/users/login.html')

```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer) > python manage.py test
```

Everything passes! Great. Another part of the Django project down.

## Summary

In this post we created a courses app. We followed the general Django pattern to create a courses page on our website

 * project urls
 * courses urls
 * courses template
 * courses view

## Future Work

Next, we are going to think about how to build the database for the website and how our database models are going to work.
