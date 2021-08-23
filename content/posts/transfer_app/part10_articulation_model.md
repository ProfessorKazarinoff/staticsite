Title: Oregon Engineering College Transfer App - Part 10: Articulation Model
Date: 2021-08-23 12:40
Modified: 2021-08-23 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-10-articulation-model
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 10
Summary: This is the 10th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 10th part of the series, we are going to create a new Django articulation model.

This is the 10th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 10th part of the series, we are going to create a new Django articulation model.

[TOC]

## Our project so far

Our Django site has grown in size. We have a main transfer_project and three main parts of our website: colleges, majors and classes. We also have a pages app for our about page. The directory structure so far is below.

```text

```

Next we'll create an articulations model in our courses app to show which classes transfer to which universitiess.

## The general django programming pattern flow

We are going to use the same general programing steps that we used when we created the college app, the courses app and the majors app. But our articulation model is going to be inside our courses app. To me this makes sense because an articulation is between two courses.

 * create a model
 * create an html template
 * project urls
 * app urls
 * create views

## Create an Articulation model

Now we are going to create an Articulation model. The articulation model is going to be defined within the courses app. Each articulation has two courses. One course from a community college and one course from a 4-year college. Each class can be part of many articulation agreements. Our articulations model is defined within the courses app in the ```models.py``` file. Each articulation as a couple specific properties that we want to keep track of:

 * Course 1: Example ENGR211 at Portland Community College

 * Course 2: Example ENGR211 at Portland State University

 * Notes: this agreement is between PCC and PSU

 * URL: webpage which shows the courses are equivalent

 * Date added: Example Aug 24, 2021

 * Added by: Example Kendra Lowry

 * Possibly others?

As far the relationship between articulations and courses goes, each articulation is between two courses. Those two courses are at different colleges 

```python
# courses/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from colleges.models import College

class Course(models.Model):
    ...

class Articulation(models.Model):
    course1 = models.ForeignKey(Course, on_delete=models.CASCADE)
    course2 = models.ForeignKey(Course, on_delete=models.CASCADE)
    URL = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.course1.course_number} at {self.course1.college.abreviation} --> {self.course2.course_number} at {self.course2.college.abreviation}"

    def get_absolute_url(self):
        return reverse("articulation_detail", args=[str(self.slug)])

```

## Migrate new Articulation model to the database

Now that the majors model is added, we need to migrate the model to the database.

```text
(transfer) $ python manage.py makemigrations
(transfer) $ python manage.py migrate
```

## Add an articulation between two classes using the Django Admin

Now that our articulation model is created, we should be able to add a new class equivalency in the Django admin. Start the local development server with the command below:

```text
(transfer-app) > python manage.py runserver
```

Browse to the Django admin at the URL below

```text
localhost:8000/admin
```

Log in with your super user credentials and add two majors. Let's link two courses at PCC with two courses at PSU. 

## Create an artiulation template

Next, we'll build an articulation detail page that shows which two courses match up. That means we need to create an articulations detail template. Let's put this tempate in the ```templates/courses/``` directory. The directory strucutre of the entire Django project is below:

```text
├───courses
├───majors
├───pages
├───templates
│   ├───pages
│   ├───colleges
│   ├───courses
│   │   ├───course_detail.html
│   │   ├───course_list.html
│   │   └───articulation_detail.html
│   ├───majors
│   └───users
├───transfer_project
└───users
```

The html below needs to be pasted into the ```articulation_detial.html``` file in the ```templates/courses/``` directory.

```html
<!-- templates/courses/articulation_detail.html -->

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

## Create the articulation url routes

```python
# majors/urls.py

from django.urls import path
from .views import (
    ArticulationDetailView,
)

urlpatterns = [
    path("course_list/", CourseListView.as_view(), name="course_list"),
    path("course/<slug:slug>/", CourseDetailView.as_view(), name="course_detail"),
    path("articulation/<slug:pk>/", ArticulationDetailView.as_view(), name="articulation_detail"),
]

```

## Create a View

In our ```courses/urls.py``` file we used one new view: ```ArticulationDetailView```. This view needs to be created in ```courses/views.py```.

```python
# courses/views.py

from django.views.generic import ListView, DetailView

from .models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"


class CourseListView(ListView):
    model = Course
    template_name = "major_list.html"

class ArticulationDetailView(DetailView):
    model = Articulation
    template_name = "articulation_detail.html"
```


## Build tests for the articulation page

Since we have a new page, we need to write some new tests. These new tests can be in the courses app.

```python
# courses/tests.py

from django.test import SimpleTestCase, TestCase

class CoursesListPageTests(SimpleTestCase):
...


class CoursesDetailPageTest(SimpleTestCase):
...


class ArticulationDetailPageTest(SimpleTestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('courses/articulations/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articulation_detail.html')
```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer-app) > python manage.py test
```

If all our tests pass, that means we can run the development server

## Run the development server

Run the development server and see our major pages in action. 

```text
(transfer-app) > python mange.py runserver
```

browse to an articulation agreement

```text
localhost:8000/courses/articulation/1
```

## Summary

In this post we created an articulations model. We followed the general Django pattern to create a model, route, view and template.

 * articulation model (in the courses app)
 * courses urls
 * articulation list template
 * articulation detail view
 * tests of our articulation pages

## Future Work

Next, we need to work on the templates a bit to produce a website that is really meaningful for students who want to transfer from a community college to a 4-year college.
