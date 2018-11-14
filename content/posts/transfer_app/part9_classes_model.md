Title: Oregon Engineering College Transfer App - Part 9: Classes Model
Date: 2018-10-24 12:40
Modified: 2018-10-24 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-9-classes-model
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 9
Summary: This is the 9th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this nineth post, we'll create a new classes model and create a page where 4-year University Administrators can add classes to the site.

This is the 9th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this nineth post, we'll create a new classes model and create a page where 4-year University Administrators can add classes to the site.

[TOC]

## Why a classes model?

The purpose of the Oregon Transfer App is to have a website that students can visit to see which classes transfer from Community College Engineering programs to 4-year University Engineering Programs. The classes at the 4-year Universities has to be part of the site. We need to add a way for 4-year University administrators to add, modify and delete classes taught at their University.

## Create a courses app

We need to build a courses app to contain our courses model. New Django apps, which are the components that make up Django projects are created with the ```manange.py startapp``` command. 

```text
$ conda activate transfer
(transfer) $ python manage.py startapp courses
```

Now we need to add the new courses app to the list of installed apps in our Django project

```python
# transfer_project/settings.py

INSTALLED_APPS = [
    # project specific
    "pages.apps.PagesConfig",
    "users.apps.UsersConfig",
    "courses.apps.CoursesConfig",
    # 3rd party
    "crispy_forms",
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

We'll also add a time zone to the project settings so we can mark a time when each new course is added to the website.

```python
# transfer_project/settings.py

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Los_Angeles"
```

## Create the courses model

Now we need to create the courses model. This is defined within the courses app in the models.py file. Each class has a couple specific properties that we want to keep track of:

 * Course number: Example ENGR114

 * Course name: Example Engineering Programming

 * Credits: Example 4

 * Course description: Example A 2nd year engineeirng course for students to learn computer programing to solve engineering problems

 * University name: Example PSU

 * Department name: Example ECS

 * Prereqs: Example ENGR101 and ENGR112

 * Course outcomes: Example 1. Demonstrate ability to use vectors

 * Course page URL: Example https://pdx.edu/ECE112.html

 * Date added: Example Oct 24, 2018

 * Added by: Example Kendra Lowry

 * Possibly others?

```python
# courses/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Course(models.Model):
    course_number = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    college = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    pre_reqs = models.CharField(max_length=50)
    course_description = models.TextField()
    course_outcomes = models.TextField()
    course_URL = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course_number} {self.course_name} {self.college}'

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])

```

## Migrate new courses model to the database

Now that the courses model is added, we need to migrate the model to the database.

```text
(transfer) $ python manage.py makemigrations courses
(transfer) $ python manage.py migrate
```

## Add courses model to the Django admin and test

Now let's add our courses model to the Django admin so that we can test it's functionality.

```python
# courses/admin.py

from django.contrib import admin

from .models import Course


admin.site.register(Course)
```

Start the development server and bring up the Django admin.

```text
(transfer) $ python manage.py runserver
```

browse to:

 > localhost:8000/admin

Login with the superuser account

![Django Admin Login]({filename}/posts/transfer_app/images/django_admin_login.png)

Add a new course with the [+] button

![Django Admin add course]({filename}/posts/transfer_app/images/django_admin_add_course.png)

Add course details

![Django Admin add course details]({filename}/posts/transfer_app/images/django_admin_add_course_details.png)

![Django Admin add course details]({filename}/posts/transfer_app/images/django_admin_save_course_details.png)

Afer we save the course, we can see the course in the list of courses on the Django admin pannel. We can see the course number, course name and college as we specificed in the courses model

![Django Admin add course details]({filename}/posts/transfer_app/images/django_admin_add_course_details.png)

Now that the courses model is running and we have a course added, let's add one more course through the Django admin. With two courses added we will be able to see what a course page looks like with more than one course and how we can iterated over the courses to build the courses page. Up next is creating a url route so we have a destination for our course page.


## Create a courses URL

We want to create a url for our courses page. This needs to be accomplished in two steps. First we need to add a url to the over-all project urls, second we need to add a url to the courses app urls

### Add a courses URL to the project urls

We'll add the sub-url ```/courses``` to proceed any url's that display course pages. In the project url's, we'll add a url route to go to our courses app url's

```python
# transfer_project/urls.py

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path('courses/', include('courses.urls')),
    path("", include("pages.urls")),
]

```

Any url that starts with ```/courses``` is now routed to the courses app urls. So now we need to modify the courses app urls. Create a new url.py file in the courses app directory.

```python
# courses/urls.py

from django.urls import path

from .views import CourseListView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
]
```

We named the ```CourseListView``` as the view called when the ```/courses``` url is requested. This view needs to be constructed.

## Create a courses View

To create the ```CourseListView```, we'll create a custom class-based view from Django's generic ```ListView``` class. We'll assign the view to use the course_list.html template, which we'll put in the tempates/courses directory

```python
# courses/views.py

from django.shortcuts import render
from django.views.generic import ListView

from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'

```

## Create a courses template

Our course list view is pointing to the template ```ourses/course_list.html``` so that's the template we'll construct next. We'll use bootstrap cards for each course in the template. Django's generic ListView class provides an object called object_list. Since our CourseListView is daughter class of the ListView class, our CourseListView also provides an object called object_list. When we iterate over object_list, we'll iterate over the two courses we created in the Django admin.

```html
<!-- templates/courses/course_list.html -->

{% extends 'bootstrap_base.html' %}

{% block content %}
    
    <div class="card-deck">
    {% for course in object_list %}
        <div class="card text-white bg-info mb-3" style="max-width: 18rem;">
            <div class="card-header"> {{ course.college }}</div>
            <div class="card-body">
                <h5 class="card-title">{{ course.course_number }} {{ course.course_name }}</h5>
                <p class="card-text">{{ course.course_description }}</p>
            </div>
            <div class="card-footer bg-transparent text-center text-muted text-white-50">
                <a href="#" class="badge badge-secondary">Edit</a> | <a href="#" class="badge badge-secondary">Delete</a>
            </div>
        </div>
    {% endfor %}
    </div>

{% endblock content %}

```


## Run the local server to see the results

OK. We should be able to see the course page list now. Let's run the local server and browse to the /courses page.

```text
(transfer) > python manage.py runserver
``` 

 > localhost:8000/courses

 ![courses list page]({filename}/posts/transfer_app/images/courses_list_page.png)

It works! We see the two courses we added to the Django admin.

## Build tests for courses page

Since we have a courses list page, we need to write a new test. We already have a couple tests. We can continue to improve our test coverage by adding tests for the new courses list page.

```python
# courses/tests.py

...

class CoursesListPageTests(TestCase):
        def test_courses_list_page_status_code(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)

    def test_courses_view_uses_correct_template(self):
        response = self.client.get(reverse('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/courses/course_list.html')

```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer) > python manage.py test
```

The tests passed! Now our Django app has a working profile page.

## Summary

In this post we created a courses model and added a course using the Django admin. Then we built a set of url patterns and views for the courses pages. We built a couple templates to display our courses. Finally we constructed and ran some tests on our course pages.

## Future Work

Next, we'll build some authorization into the courses pages so that only 4-year University Administrators can add classes and access the course pages for their University. We also need to build in functionality for courses to be added using the site, instead of courses added using the Django admin.
