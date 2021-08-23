Title: Oregon Engineering College Transfer App - Part 8: Courses App
Date: 2021-08-23 12:40
Modified: 2021-08-23 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-8-courses-app
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 8
Summary: This is the 8th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 8th part of the series, we are going to create a new Django App to house our courses model.

This is the 8th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 8th part of the series, we are going to create a new Django App to house our courses model.

[TOC]

## Our project so far

So far, the files we have in our website project are shown below:

```text

```

We have created a Django project called ```transfer_project``` and created three Django Apps, a ```pages``` app, a ```user``` app and a ```colleges``` app. We've created a few html templates and url routes that produces a few web pages. We also created a Colleges model and populated the college model with two colleges using the Django admin.

Next we will create a ```courses``` app that will house our Course model.

## The general django app flow

So far we have created three Django apps. The process of creating a new web page that we used to build our home and about pages is the same steps that we'll use to create our courses page.

 * create courses app
 * add courses app to settings.py
 * create a courses model
 * create a courses page template
 * modify project urls
 * create courses urls
 * create a courses view

## Create a courses app

Our courses app will house all of the courses functionality of our website. Create the courses app using the commands below.

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

Just like what we did with our users, pages and colleges apps, we need to add our new courses app to the list of installed apps in our ```settings.py``` file. Open ```settings.py``` and see the addition below.

```python
# transfer_project/settings.py

# Application definition

INSTALLED_APPS = [
    # project specific
    'pages.apps.PagesConfig',
    'users.apps.UsersConfig',
    'colleges.apps.CollegesConfig',
    'courses.apps.CoursesConfig',
    
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

## Create a Courses model

Now we need to create the Courses model. This is defined within the courses app in the ```models.py``` file. Each course has a couple specific properties that we want to keep track of:

 * Course number: Example ENGR114

 * Course name: Example Engineering Programming

 * Credits: Example 4

 * Course description: Example A 2nd year engineeirng course for students to learn computer programing to solve engineering problems

 * college: Example Portland Community College

 * Prereqs: Example ENGR101

 * Course outcomes: Example 1. Demonstrate ability to use programming to solve engineering problems

 * Date added: Example Aug 24, 2021

 * Added by: Example Kendra Lowry

 * Possibly others?

As far the relationship between courses and colleges goes, each course only belongs to one college and each college contains many courses. 

```python
# courses/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from colleges.models import College


class Course(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    pre_reqs = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=200, blank=True)
    course_outcomes = models.TextField(max_length=200, blank=True)
    URL = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number} {self.name} at {self.college}'

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])

```

## Migrate new courses model to the database

Now that the courses model is added, we need to migrate the model to the database.

```text
(transfer) $ python manage.py makemigrations
(transfer) $ python manage.py migrate
```

## Add a course using the Django Admin

Now that our course model is created, we should be able to add a new courses in the Django admin. Start the local development server with the command below:

```
(transfer-app) > python manage.py runserver
```

Browse to the Django admin at the URL below

```
localhost:8000/admin
```

Log in with your super user credentials and add a couple courses. We'll add four courses so that each college can have two courses listed.

## Create a courses template

Next, we'll build a courses page that shows all the courses we added to the database in the Django admin. That means we need to create a courses template. Let's put this tempate in the ```templates/courses/``` directory. The directory strucutre of the entire Django project is below:

```text
├───pages
│   ├───migrations
│   │   └───__pycache__
│   ├───static
│   │   └───css
│   └───__pycache__
├───templates
│   ├───pages
│   ├───colleges
│   ├───courses
│   │   └───courses.html
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

Now that the course html template is created, we need to create a url pattern that points to the template. When a user browses to https://domain.com/courses, the courses template should pop up. Edit the transfer_project/urls.py file to include a new route for the courses template. 

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
# courses/urls.py

from django.urls import path
from .views import (
    CourseDetailView,
    CourseListView,
)

urlpatterns = [
    path("course_list/", CourseListView.as_view(), name="course_list"),
    path("course/<slug:slug>/", CourseDetailView.as_view(), name="course_detail"),
]

```

## Create a courses view

In our ```courses/urls.py``` file we all the ```CourseListView``` and the ```CourseListView```. Both of these views need to be created in ```courses/views.py```.

```python
# courses/views.py

from django.views.generic import ListView, DetailView

from .models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"


class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"
```


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

## Run the development server

## Summary

In this post we created a courses app. We followed the general Django pattern to create a courses page on our website
 * courses model
 * project urls
 * courses urls
 * courses template
 * courses view

## Future Work

Next, we are going to think about how to build the database for the website and how our database models are going to work.
