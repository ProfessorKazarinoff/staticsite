Title: Oregon Engineering College Transfer App - Part 9: Majors Model
Date: 2021-08-23 12:40
Modified: 2021-08-23 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-9-majors-model
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 9
Summary: This is the 9th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 9th part of the series, we are going to create a new Django majors model.

This is the 9th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 9th part of the series, we are going to create a new Django majors model.

[TOC]

## Our project so far

Our Django site has grown in size. We started out with just a home page and about page, and now we have pages for colleges and courses. The files in our project so far are shown below

```text

```

We have created a Django project called ```transfer_project``` and created four Django apps, a ```pages``` app, a ```user``` app, a ```colleges``` app and a ```courses app```. We've created a few html templates and url routes that produces a few web pages. We also created two models, a college model and a course model. We linked our college model to our course model so that every course was associated with the college where it was taught. So far we have 4 courses on our site that we entered into the Django admin.

Next we will create a majors model to save the different engineering majors at each college.

## The general django programming pattern flow

So far we have created three Django apps. The process of creating a new web page that we used to build our home and about pages is the same steps that we'll use to create our courses page.

 * create a model
 * create a page templates
 * project urls
 * app urls
 * create views

## Create a Majors model

Now we are going to create a Majors model. The major's model is going to be defined within the colleges app. Each college has a couple majors. We could create a whole new app for majors. But for right now, I think we'll keep it in the college app. Our majors model is defined within the colleges app in the ```models.py``` file. Each major as a couple specific properties that we want to keep track of:

 * Major name: Example Mechanical Engineering

 * Major abreviation: Example ME

 * College: Portland State University

 * Major description: Mechanical Engineering is the engineering of moving mechanical components

 * Courses: Which courses are part of the major

 * Date added: Example Aug 24, 2021

 * Added by: Example Kendra Lowry

 * Possibly others?

As far the relationship between majors and colleges goes, each major only belongs to one college and each college contains many majors. As far as the relationship between majors and courses goes, each major contains many courses and each course can be part of many majors. 

```python
# majors/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from colleges.models import College
from courses.models import Course


class Major(models.Model):
    name = models.CharField(max_length=50)
    abreviation = models.CharField(max_length=10)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    slug = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    courses = models.ManyToManyField(Course, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["abbreviation"]

    def __str__(self):
        return f"{self.abbreviation} - {self.name} at {self.college.abreviation}"

    def get_absolute_url(self):
        return reverse("major_detail", args=[str(self.slug)])

    def __str__(self):
        return f'{self.number} {self.name} at {self.college}'

```

## Migrate new majors model to the database

Now that the majors model is added, we need to migrate the model to the database.

```text
(transfer) $ python manage.py makemigrations
(transfer) $ python manage.py migrate
```

## Add a major using the Django Admin

Now that our major model is created, we should be able to add a new major in the Django admin. Start the local development server with the command below:

```text
(transfer-app) > python manage.py runserver
```

Browse to the Django admin at the URL below

```text
localhost:8000/admin
```

Log in with your super user credentials and add two majors. Let's have one major belong to one college and the another major belong to the other college in the database. 

## Create a majors template

Next, we'll build a majors page that shows all the majors we added to the database in the Django admin. That means we need to create a majors list template. Let's put this tempate in the ```templates/majors/``` directory. The directory strucutre of the entire Django project is below:

```text
├───pages
├───templates
│   ├───pages
│   ├───colleges
│   ├───courses
│   ├───majors
│   │   └───majors.html
│   └───users
├───transfer_project
└───users
```

The html below needs to be pasted into the ```majors.html``` file in the ```templates/majors/``` directory.

```html
<!-- templates/majors/majors.html -->

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
    path('majors/', include('majors.urls')),
    path('', include('pages.urls')),
]

```

## Create the majors url routes

```python
# majors/urls.py

from django.urls import path
from .views import (
    MajorDetailView,
    MajorListView,
)

urlpatterns = [
    path("major_list/", MajorListView.as_view(), name="major_list"),
    path("major/<slug:slug>/", MajorDetailView.as_view(), name="major_detail"),
]

```

## Create two Views

In our ```majors/urls.py``` file we used two views: ```MajorListView``` and the ```MajorDetailView```. Both of these views need to be created in ```majors/views.py```.

```python
# majors/views.py

from django.views.generic import ListView, DetailView

from .models import Major


class MajorDetailView(DetailView):
    model = Major
    template_name = "course_detail.html"


class MajorListView(ListView):
    model = Major
    template_name = "major_list.html"
```


## Build tests for the majors page

Since we have two new pages, we need to write some new tests. We already have a couple tests. Each time we added a page to our website, we added a new test. These tests are for the majors pages.

```python
# majors/tests.py

from django.test import SimpleTestCase, TestCase

class MajorsListPageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class MajorsDetailPageTest(SimpleTestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer-app) > python manage.py test
```

Everything passes! Great. Another part of the Django project down.

## Run the development server

Run the development server and see our major pages in action. 

```text
(transfer-app) > python mange.py runserver
```

browse to the list of majors

```text
localhost:8000/major_list/
```

## Summary

In this post we created a majors model. We followed the general Django pattern to create a majors list page and a majors detail page on our website
 * majors model
 * project urls
 * majors urls
 * major list template
 * major detial template
 * major list view
 * major detail view
 * tests of our majors pages

## Future Work

Next, we are going to link our classes together with an articuluation model. This model will give us the relationship between a course at a community college and a course at a 4-year university. This is the main business logic of our app.
