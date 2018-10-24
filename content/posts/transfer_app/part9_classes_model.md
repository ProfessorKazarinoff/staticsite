Title: Oregon Engineering College Transfer App - Part 9: Classes Model
Date: 2018-10-24 12:40
Modified: 2018-10-24 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-8-user-profile
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




## Create a courses URL

## Create a courses View

## Create a courses template

```html
<!-- templates/logged_in_nav_dropdown.html -->

<ul class="nav justify-content-end">
    <li class="nav-item dropdown">
        <a class="btn btn-secondary dropdown-toggle" href="https://example.com" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Logged in as: {{ user.username }}</a>
        <div class="dropdown-menu" aria-labelledby="dropdown01">
            <a class="dropdown-item" href="{% url 'logout' %}">Logout</a>
            <a class="dropdown-item" href="#">Administrator Dashboard</a>
            <a class="dropdown-item" href="{% url 'profile' %}">Profile</a>
            <a class="dropdown-item" href="#">Change Password</a>
        </div>
    </li>
</ul>

```

## Run the local server to see the results

OK. We should be able to see the profile page now. Let's start the local server, login and browse to the profile page using the dropdown menu on the righthand side of the nav bar.

```text
(transfer) > python manage.py runserver
``` 

## Build tests for courses page

Since we have a new page, we need to write some new tests. We already have a couple tests. There is a test for the homepage, about page, login page and logoutpage. We can improve our test coverage by adding tests for the new profile page.

```python
# courses/tests.py

...

class ProfilePageTests(TestCase):
        def test_profile_page_status_code(self):
        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_view_uses_correct_template(self):
        response = self.client.get(reverse('users/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/users/profile.html')

```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer) > python manage.py test
```

The tests passed! Now our Django app has a working profile page.

## Summary

In this post we created a courses model and added a course using the Django admin. Then we built a set of url patterns and views for the courses pages. We built a couple templates to display our courses. Finally we constructed and ran some tests on our course pages.

## Future Work

Next, we'll build some authorization into the courses pages so that only 4-year University Administrators can add classes and access the course pages for their University.
