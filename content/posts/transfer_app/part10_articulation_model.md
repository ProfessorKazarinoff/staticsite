Title: Oregon Engineering College Transfer App - Part 10: Articulation Model
Date: 2021-08-28 12:40
Modified: 2021-08-28 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-10-articulation-model
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 10
Summary: This is the 10th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 10th part of the series, we are going to create a new Django articulation model.

This is the 10th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 10th part of the series, we are going to create a new Django articulation model and figure out how to do reverse lookups.

[TOC]

## Our project so far

Our Django site has grown in size. We have a main transfer_project and three main parts of our website: colleges, majors and classes. We also have a pages app for our about page. The directory structure so far is below.

```text

```

Next we'll create an articulations app and model to hold the information about which courses are equivalent to which other courses.

## The general django programming pattern flow

We are going to use the same general coding steps that we used when we created the college app, the courses app and the majors app.

 * create a new app
 * add the app to the admin 
 * create a model
 * create an html template
 * project urls
 * app urls
 * views
 * tests

## Create a new articulations app

```text
> cd Documents
> cd tranfer
> conda activate transfer
> (transfer) > python manage.py startapp articulations
```

## add the new app to the project settings

In the ```transfer_project/``` directory modify the ```settings.py``` file.

```python
INSTALLED_APPS = [
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # 3rd party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # project specific
    "colleges.apps.CollegesConfig",
    "courses.apps.CoursesConfig",
    "pages.apps.PagesConfig",
    "majors.apps.MajorsConfig",
    "accounts",
    "articulations.apps.ArticulationsConfig",
]

```

## Create an Articulation model

Now we are going to create an Articulation model. The Articulation model is going to be defined within the articulations app. Each articulation is made up of two courses. One course is from a community college and one other course is from a 4-year college. Each course can be part of many Articulation Agreements. Our Articulation model is defined within the articulations app in the ```models.py``` file. Each articulation as a couple specific properties that we want to keep track of:

 * Course 1: Example ENGR211 at Portland Community College

 * Course 2: Example ENGR211 at Portland State University

 * Notes: this agreement is between PCC and PSU

 * URL: webpage which shows the courses are equivalent

 * Date added: Example Aug 24, 2021

 * Added by: Example Kendra Lowry

 * Possibly others?

As far the relationship between articulations and courses goes, each articulation is between two courses. Those two courses are at different colleges. 

```python
# articulations/models.py

from django.db import models
from django.urls import reverse
from courses.models import Course

class Articulation(models.Model):
    course1 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course1")
    course2 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course2")
    URL = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.course1.number} at {self.course1.college.abbreviation} --> {self.course2.number} at {self.course2.college.abbreviation}"

    def get_absolute_url(self):
        return reverse("articulation_detail", args=[str(self.id)])

```

## Add Articulatoin model to the Django admin

```python
# articulations/admin.py

from django.contrib import admin

from .models import Articulation

admin.site.register(Articulation)

```

## Migrate new Articulation model to the database

Make a new app and a new model, so we need to migrate the database.

```text
(transfer) $ python manage.py makemigrations
(transfer) $ python manage.py migrate
```

## Add an articulation between two classes using the Django Admin

Now that our Articulation model is created, we should be able to add a new class equivalency using the Django admin. Start the local development server with the command below:

```text
(transfer) > python manage.py runserver
```

Browse to the Django admin at the URL below

 > localhost:8000/admin

Log in with your super user credentials and an articulation. Let's link a course at Portland Community College with the equivalent course at Portland State and Oregon State.

## Create an artiulation template

Next, we'll build an articulation detail and articulations list page that shows which two courses match up. That means we need to create an two templates. Let's put these tempates in the ```templates/``` directory. The directory strucutre of the entire Django project is below:

```text
├───articulations
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

The html below needs to be pasted into the ```articulation_detail.html``` and ```articulation_list.html``` file in the ```templates/``` directory.

```html
<!-- templates/articulation_detail.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
    <link href="{% static 'css/home.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}

<div class="container">
    <h3>{{ object.course1.abbreviation }} - {{ object.course2.abbreviation }}</h3>
    <hr>
    <p>Description: {{ object.descrition}} </p>
    <p>Reference: {{ object.url }}</p>
    <hr>
</div>

{% endblock content %}

```

```html
<!-- templates/articulation_list.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
    <link href="{% static 'css/home.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}
<div class="container">
    <h2>All Course Equivalency Listing</h2>
    <hr>
    <h4>Engineering courses</h4>

    <table class="table">
        <thead class="thead-light">
            <tr>
                <th scope="col">Course number</th>
                <th scope="col">Course name</th>
                <th scope="col">College</th>
                <th scope="col">Equivalent Course number</th>
                <th scope="col">Equivalent Course name</th>
                <th scope="col">College</th>
            </tr>
        </thead>
        <tbody>
            {% for articulation in object_list %}
            <tr>
                <td><a class="course-link-color" href="{% url 'course_detail' articulation.course1.id %}">{{ articulation.course1.number }}</a></td>
                <td>{{ articulation.course1.name }}</td>
                <td>{{ articulation.course1.college }}</td>
                <td><a class="course-link-color" href="{% url 'course_detail' articulation.course2.id %}">{{ articulation.course1.number }}</a></td>
                <td>{{ articulation.course2.name }}</td>
                <td>{{ articulation.course2.college }}</td>
            </tr>
            {% endfor %}
        </tbody>
      </table>
    </div>

{% endblock content %}

```

## Modify project urls

Now that the course html template is created, we need to create a url pattern that points to the template. When a user browses to https://domain.com/courses, the courses template should pop up. Edit the transfer_project/urls.py file to include a new route for the courses template. 

```python
# transfer_project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("articulations/", include("articulations.urls")),
    path("colleges/", include("colleges.urls")),
    path("courses/", include("courses.urls")),
    path("majors/", include("majors.urls")),
    path("", include("pages.urls")),
]

```

## Create the articulation url routes

Create a new file in the ```articulations``` directory called ```urls.py```. Paste in the code below.

```python
# articulations/urls.py

from django.urls import path
from .views import (
    ArticulationDetailView,
    ArticulationListView,
)

urlpatterns = [
    path("articulation/<slug:pk>/", ArticulationDetailView.as_view(), name="articulation_detail"),
    path("articulation_list", ArticulationListView.as_view(), name="articulation_list"),
]

```

## Create two Views

In our ```articulations/urls.py``` file we used two new views: ```ArticulationDetailView``` and ```ArticulationListView```. These views needs to be created in ```articulations/views.py```.

```python
# articulations/views.py

from django.views.generic import ListView, DetailView

from .models import Articulation

class ArticulationListView(ListView):
    model = Articulation
    template_name = "articulation_list.html"

class ArticulationDetailView(DetailView):
    model = Articulation
    template_name = "articulation_detail.html"

```


## Build tests for the articulation page

Since we have a new pages, we need to write some new tests. These new tests can be in the articulations app in a ```tests.py``` file.

```python
# courses/tests.py

from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from colleges.models import College
from courses.models import Course
from .models import Articulation


class ArticulationListPageTests(TestCase):
    def test_articulations_list_page_status_code(self):
        response = self.client.get("/articulations/articulation_list/")
        self.assertEqual(response.status_code, 200)

    def test_articulations_list_view_uses_correct_template(self):
        response = self.client.get(reverse("articulation_list"))
        self.assertTemplateUsed(response, "articulation_list.html")


class ArticulationTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="peter", email="peter@peter.com", password="top_secret"
        )
        College.objects.create(
            name="Mt. Hood Community College",
            abbreviation="MHCC",
            URL="https://mhcc.edu/",
            slug="mhcc",
            description="Mt. Hood Community College is in Gresham, OR",
            added_by=self.user,
        )
        College.objects.create(
            name="Portland State University",
            abbreviation="PSU",
            URL="https://pdx.edu/",
            slug="psu",
            description="Portland State University is in Portland, OR",
            added_by=self.user,
        )
        college1 = College.objects.get(id=1)
        college2 = College.objects.get(id=2)
        Course.objects.create(
            number="ENGR 211",
            name="Engineering Statics",
            credits=4.0,
            college=college1,
            pre_reqs="ENGR 101",
            description="An engineering statics course",
            course_outcomes="test outcomes",
            URL="https://www.pcc.edu/ccog/engr/211/",
            added_by=self.user,
        )
        Course.objects.create(
            number="ENGR 211",
            name="Statics",
            credits=4.0,
            college=college2,
            pre_reqs="MTH 251",
            description="A course on engineering statics",
            course_outcomes="test outcomes",
            URL="https://www.pcc.edu/ccog/engr/211/",
            added_by=self.user,
        )
        course1 = College.objects.get(id=1)
        course2 = College.objects.get(id=2)
        Articulation.objects.create(
            course1 = course1,
            course2 = course2,
            URL = "https://pcc.edu/engineering",
            description = "Mt Hood class transfers to PSU",
        )
    def test_text_content(self):
        articulation = Articulation.objects.get(id=1)
        expected_object_name = f"{articulation.course1.number} at {articulation.course1.college.abbreviation} --> {articulation.course2.number} at {articulation.course2.college.abbreviation}"
        self.assertEquals(
            expected_object_name,
            "ENGR 211 at MHCC --> ENGR 211 at PSU",
        )

    def test_articulation_list_view(self):
        response = self.client.get(reverse("articulation_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ENGR 211")
        self.assertTemplateUsed(response, "articulation_list.html")

    def test_course_detail_view(self):
        articulation = Articulation.objects.get(id=1)
        response = self.client.get(reverse("articulation_detail", args=[str(articulation.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ENGR 211")
        self.assertTemplateUsed(response, "articulation_detail.html")

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

 > localhost:8000/articulations/articulation/1/

## Summary

In this post we created an articulations model. We followed the general Django pattern to create a model, route, view and template.

 * articulations app
 * articulation model (in the courses app)
 * courses urls
 * articulation list template
 * articulation detail view
 * tests of our articulation pages

## Future Work

Next, we need to work on the templates a bit to produce a website that is really meaningful for students who want to transfer from a community college to a 4-year college.
