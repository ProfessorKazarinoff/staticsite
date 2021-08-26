Title: Oregon Engineering College Transfer App - Part 9: Majors Model
Date: 2021-08-26 12:40
Modified: 2021-08-26 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-9-majors-model
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 9
Summary: This is the 9th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 9th part of the series, we are going to create a new Django app and model for majors. An example of a major is Civil Engineering or Mechanical Engineering.

This is the 9th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 9th part of the series, we are going to create a new Django app and model for majors. An example of a major is Civil Engineering or Mechanical Engineering.

[TOC]

## Our project so far

Our Django site has grown in size. We started out with just a home page and about page, and now we have pages for colleges and courses. The files in our project so far are shown below

```text

```

We have created a Django project called ```transfer_project``` and created four Django apps, a ```pages``` app, a ```user``` app, a ```colleges``` app and a ```courses app```. We've created a few html templates and url routes that produces a few web pages. We also created two models, a college model and a course model. We linked our college model to our course model so that every course was associated with the college where it was taught. So far we have 3 courses on our site that we entered into the Django admin.

Next we will create a majors model to save the different engineering majors at each college.

## The general django programming pattern flow

So far we have created three Django apps. The process of creating a new web page that we used to build our home and about pages is the same steps that we'll use to create our courses page.

 * create app
 * model
 * admin
 * templates
 * project urls
 * app urls
 * views

## Create a Majors app

```text
> cd Documents
> cd transfer
> conda activate transfer
(transfer) > python manage.py startapp majors
```

## Add to majors to the list of installed apps

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
]

```

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

As far the relationship between majors and colleges goes, each major only belongs to one college and each college contains many majors. As far as the relationship between majors and courses goes, each major contains many courses and each course can be part of many majors. We'll create two models in the ```majors/models.py``` file. One model ```Major``` will be for the "generic" major like Mechanical Engineering or Electrical Engineering. Then we'll have a more specific model for a major at a particular college, such as Mechanical Engineering at Portland State University.

```python
# majors/models.py

from django.db import models
from django.urls import reverse
from colleges.models import College
from courses.models import Course

class Major(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)

    class Meta:
        ordering = ["abbreviation"]

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"

    def get_absolute_url(self):
        return reverse("major_detail", args=[str(self.id)])
    

class CollegeMajor(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    courses = models.ManyToManyField(Course, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["major"]

    def __str__(self):
        return f"{self.major.abbreviation} - {self.major.name} at {self.college.abbreviation}"

    def get_absolute_url(self):
        return reverse("college_major_detail", args=[str(self.id)])

```
## Add majors to the Django admin

```python
# majors/admin.py

from django.contrib import admin

from .models import Major, CollegeMajor

admin.site.register(Major)
admin.site.register(CollegeMajor)

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

The html below needs to be pasted into the ```major_list.html``` and ```major_detail``` files in the ```templates/``` directory.

```html
<!-- templates/major_list.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
    <link href="{% static 'css/home.css' %}" rel="stylesheet">
    <link href="{% static 'css/majors_list.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}
  <div class="container">
    <!-- Example row of columns -->
    <div class="row">
      {% for major in object_list %}
      <div class="col-md-4">
        <h2>{{ major.name }}</h2>
        <p>{{ major.description }}</p>
        <p><a class="btn btn-secondary" href="{% url 'major_detail' major.id %}" role="button">View Courses &raquo;</a></p>
      </div>
      {% endfor %}
    <hr>

  </div> <!-- /container -->
</div>

{% endblock content %}

```

```html
<!-- templates/major_detail.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
    <link href="{% static 'css/advising_guide.css' %}" rel="stylesheet">
    <link href="{% static 'css/course_list.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}
<div class="container">
    <h3>{{ object.name }} Advising Guide</h3>
    <hr>
    <h4>Engineering Majors</h4>

    <table class="table">
        <thead class="thead-light">
            <tr>
                <th scope="col">Major</th>
                <th scope="col">Abbreviation</th>
                <th scope="col">Colleges</th>
            </tr>
        </thead>
        <tbody>
            {% for major in object.majors.all %}
            <tr>
                <td><a class="course-link-color" href="{% url 'major_detail' major.id %}">{{ major.name }}</a></td>
                <td>{{ major.abbreviation }}</td>
                <td>PCC, PSU, OSU</td>
            </tr>
            {% endfor %}
        </tbody>
      </table>

      <hr>

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
    path("colleges/", include("colleges.urls")),
    path("courses/", include("courses.urls")),
    path("majors/", include("majors.urls")),
    path("", include("pages.urls")),
]

```

## Create the majors url routes

```python
# majors/urls.py

from django.urls import path

from .views import MajorDetailView, MajorListView

urlpatterns = [
    path("major_list/", MajorListView.as_view(), name="major_list"),
    path("major/<int:pk>/", MajorDetailView.as_view(), name="major_detail"),
]

```

## Create two Views

In our ```majors/urls.py``` file we used two views: ```MajorListView``` and the ```MajorDetailView```. Both of these views need to be created in ```majors/views.py```.

```python
# majors/views.py

from django.views.generic import DetailView, ListView

from .models import Major


class MajorDetailView(DetailView):
    model = Major
    template_name = "major_detail.html"


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

## Format, add, commit and push to github

```text
(transfer) > isort .
(transfer) > black .
(transfer) > git add .
(transfer) > git commit -m "commit message"
(transfer) > git push origin main
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
