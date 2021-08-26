Title: Oregon Engineering College Transfer App - Part 8: Courses App
Date: 2021-08-26 12:40
Modified: 2021-08-26 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-8-courses-app
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 8
Summary: This is the 8th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The website will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 8th part of the series, we will create a new Django App to house our courses model. Then we'll build course list and detail pages and write some tests.

This is the 8th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The website will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 8th part of the series, we will create a new Django App to house our courses model. Then we'll build course list and detail pages and write some tests.

[TOC]

## Our project so far

So far, the files we have in our website project are shown below:

![dir_structure_before_courses_model.png]({static}/posts/transfer_app/images/dir_structure_before_courses_model.png]

We have created a Django project called ```transfer_project``` and created three Django Apps, a ```pages``` app, a ```user``` app and a ```colleges``` app. We've created a few html templates and url routes that produces web pages. We also created a Colleges model and populated the college model with two colleges using the Django admin.

Next we will create a ```courses``` app that will house our Course model.

## The general django app flow

So far we have created three Django apps. The process of creating new web pages for courses are the same steps we used to create our college pages.

 * create courses app
 * add courses app to settings.py
 * create a courses model
 * create courses page templates
 * modify project urls
 * create courses urls
 * create a courses view

## Create a courses app

Our courses app will house all of the courses functionality of our website. Create the courses app using the commands below.

```text
> cd Documents
> cd transfer
> conda activate transfer
(transfer) > python manage.py startapp courses 
```

This command adds a new app to our project. The directory structure now looks like the file structure below:

![dir_structure_after_courses_app.png]({static}/posts/transfer_app/images/dir_structure_after_courses_app.png]

## Add courses app to the list of installed apps

Just like what we did with our users, pages and colleges apps, we need to add our new courses app to the list of installed apps in our project ```settings.py``` file. Open ```settings.py``` and see the addition below.

```python
# transfer_project/settings.py
...

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
    "accounts",
]

```

## Create a Courses model

Now we need to create the Courses model. This is defined within the courses app in the ```models.py``` file. Each course has a couple specific properties that we want to keep track of:

 * Course number: Example ENGR114

 * Course name: Example Engineering Programming

 * Credits: Example 4

 * Course description: Example A 2nd year engineeirng course for students to learn computer programing to solve engineering problems

 * college: Example Portland Community College (this comes from our College model)

 * Prereqs: Example ENGR101 (optional)

 * Course outcomes: Example 1. Demonstrate ability to use programming to solve engineering problems (optional)

 * Date added: Example Aug 24, 2021

 * Added by: Example Kendra Lowry

 * Possibly others?

As far the relationship between courses and colleges goes, each course only belongs to one college and each college contains many courses. 

```python
# courses/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from colleges.models import College


class Course(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    credits = models.FloatField(null=True, blank=True)
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

## Add Course model to the Django Admin

Next, we'll add our Course model the the Django admin. That way, when we log into the admin side of our site, we'll be able to add a new course. Open ```admin.py``` in the courses app.

```python
# courses/admin.py

from django.contrib import admin

from .models import Course

admin.site.register(Course)

```

## Migrate new courses model to the database

Now that the new Course model is added, we need to migrate the database.

```text
(transfer) $ python manage.py makemigrations
(transfer) $ python manage.py migrate
```

## Add a course using the Django Admin

Now that our course model is created, and the course Model is added to the admin, we should be able to add a new courses in the Django admin. Start the local development server with the command below:

```
(transfer-app) > python manage.py runserver
```

Browse to the Django admin at the URL below

```
localhost:8000/admin
```

Log in with your super user credentials and add a couple courses. We'll add four courses so that each college can have two courses listed.

## Create a courses template

Next, we'll build a courses page that shows all the courses we added to the database in the Django admin. That means we need to create a courses template. Let's put this tempate in the ```templates/``` directory.

The html below needs to be pasted into the ```course_detail.html``` file in the ```templates/``` directory.

```html
<!-- templates/course_detail.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
    <link href="{% static 'css/home.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}

<div class="container">
    <h3>{{ object.number }} - {{ object.name }}</h3>
    <hr>
    <p>Credits: {{ object.credits }} </p>
    <p>Prereqs: {{ object.pre_reqs }}</p>
    <hr>
    <p>Description: {{ object.description }}</p>
</div>

{% endblock content %}

```

The html below needs to be pasted into the ```course_list.html``` file in the ```templates/``` directory.

```html
<!-- templates/course_list.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
    <link href="{% static 'css/home.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}
<div class="container">
    <h2>All Course Listing</h2>
    <hr>
    <h4>Engineering courses</h4>

    <table class="table">
        <thead class="thead-light">
            <tr>
                <th scope="col">Course number</th>
                <th scope="col">Course name</th>
                <th scope="col">Credits</th>
                <th scope="col">College</th>
                <th scope="col">Prerequisites</th>
            </tr>
        </thead>
        <tbody>
            {% for course in object_list %}
            <tr>
                <td><a class="course-link-color" href="{% url 'course_detail' course.id %}">{{ course.number }}</a></td>
                <td>{{ course.name }}</td>
                <td>{{ course.credits }}</td>
                <td>{{ course.college }}</td>
                <td>{{ course.pre_reqs }}</td>
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
    path("colleges/", include("colleges.urls")),
    path('courses/', include('courses.urls')),
    path("", include("pages.urls")),
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
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
]

```

## Create a courses view

In our ```courses/urls.py``` file we all the ```CourseListView``` and the ```CourseDetailView```. Both of these views need to be created in ```courses/views.py```.

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

Since we have two new pages, we need to write some new tests.

```python
# courses/tests.py

from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from colleges.models import College
from .models import Course


class CoursesListPageTests(TestCase):
    def test_courses_list_page_status_code(self):
        response = self.client.get("/courses/course_list/")
        self.assertEqual(response.status_code, 200)

    def test_courses_list_view_uses_correct_template(self):
        response = self.client.get(reverse("course_list"))
        self.assertTemplateUsed(response, "course_list.html")


class CourseTests(TestCase):
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
        college = College.objects.get(id=1)
        Course.objects.create(
            number = "ENGR 114",
            name = "Engineering Programming",
            credits = 4.0,
            college = college,
            pre_reqs = "ENGR 101",
            description = "An engineering programming course",
            course_outcomes = "test outcomes",
            URL = "https://www.pcc.edu/ccog/engr/114/",
            added_by = self.user,
        )

    def test_text_content(self):
        course = Course.objects.get(id=1)
        expected_object_name = f"{course.number} {course.name} at {course.college}"
        self.assertEquals(expected_object_name, "ENGR 114 Engineering Programming at Mt. Hood Community College")

    def test_course_list_view(self):
        response = self.client.get(reverse("course_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ENGR 114")
        self.assertTemplateUsed(response, "course_list.html")

    def test_course_detail_view(self):
        course = Course.objects.get(id=1)
        response = self.client.get(reverse("course_detail", args=[str(course.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ENGR 114")
        self.assertTemplateUsed(response, "course_detail.html")

```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer) > python manage.py test
```

The output should look something like below:

```text
----------------------------------------------------------------------
Ran 20 tests in 0.935s

OK
Destroying test database for alias 'default'...
```

Everything passes! Great. Another part of the Django project down.

## Run the development server

```text
(transfer) > python manage.py runserver
```

## Format, add, commit and push

```text
(transfer) > isort .
(transfer) > black .
(transfer) > git add .
(transfer) > git commit -m "commit message"
(transfer) > git push origin main
```

## Summary

In this post we created a courses app. We followed the general Django pattern to create a courses page on our website
 * courses model
 * project urls
 * courses urls
 * courses template
 * courses view

## Future Work

Next, we are going to build a model for college majors. This way, if a student knows they want to major in Mechanical Engineering, they can see all of the courses that go along with that major that are taught at each college.
