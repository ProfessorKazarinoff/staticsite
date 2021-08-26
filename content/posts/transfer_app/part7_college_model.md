Title: Oregon Engineering College Transfer App - Part 7: College Model
Date: 2021-08-26 12:40
Modified: 2021-08-26 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-7-college-model
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 7
Summary: This is the 7th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 7th part of the series, we'll create a college model and add a few colleges to our database using the Django admin. We will also create a college list page and a college detail page.

This is the 7th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 7th part of the series, we'll create a college model and add a few colleges to our database using the Django admin. We will also create a college list page and a college detail page.

[TOC]

## Databse Design

So far our website is made up of static pages. These pages won't change unless we change the html in our templates. But we are building a dynamic website. Our website should change when a new course is added, or a course is removed, or a change in how a course transfers. In order to make our website dynamic, we need to create a database and that means we need to think about database design.

How are we going to structure our database for our website?

Our website is going to list courses at different colleges, so we have a couple relationships:

 * A College can have many courses
 * A course belongs to a specific college
 * A major belongs to a specific college and contains many courses
 * A course at one college is equivalent to a course at another college

## Why a College model?

The purpose of the Oregon Transfer App is to design a website that students can visit to see which classes transfer from Community College Engineering programs to 4-year University Engineering Programs. A college is the biggest "bucket" in our website. A college contains many majors and each major contains many courses. Since a major belongs to a college and a course belongs a college, we'll make our college model first so that when we make our majors and courses models there will be a college to associate them with.

## Create a College model

We need to build a colleges app to contain our colleges model. New Django apps, which are the components that make up Django projects are created with the ```manange.py startapp``` command. 

```text
$ conda activate transfer
(transfer) $ python manage.py startapp colleges
```

Now we need to add the new colleges app to the list of installed apps in our Django project. Open ```settings.py``` in the ```transfer_project``` directory and make sure the list of ```INSTALLED_APPS``` is up to date.

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
    "pages.apps.PagesConfig",
    "accounts",
]
```

We'll also add a time zone to the project settings so we can mark a time when each new course is added to the website.

```python
# transfer_project/settings.py
...

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Los_Angeles"
```

## Create the College model

Now we need to create the College model. This is defined within the colleges app in the ```models.py``` file. Each college has a couple specific properties that we want to keep track of:

 * College name: Example Portland Community College

 * College abbreviation: Example PCC

 * College URL: Example https://pcc.edu

 * Date added: Example Aug 24, 2021 (we'll make this automatic)

 * Added by: Example Kendra Lowry (we'll make this automatic based on who is logged in)

 * Possibly others? Like manybe the location or a description? We can add these later if we need to.

```python
# colleges/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class College(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    URL = models.URLField()
    slug = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('college_detail', args=[str(self.slug)])

```

## Migrate new College model to the database

Now that the College model is added, we need to migrate the model to the database.

```text
(transfer) $ python manage.py makemigrations
(transfer) $ python manage.py migrate
```

## Add courses model to the Django admin

Now let's add our colleges model to the Django admin so that we can test it's functionality.

```python
# colleges/admin.py

from django.contrib import admin

from .models import College


admin.site.register(College)

```

Start the development server and bring up the Django admin.

```text
(transfer) $ python manage.py runserver
```

browse to:

 > localhost:8000/admin

Login with the superuser account

![Django Admin Login]({static}/posts/transfer_app/images/django_admin_login.png)

Add a new college with the [+] button

![Django Admin add course]({static}/posts/transfer_app/images/django_admin_add_course.png)

Add details to the new college entry

![Django Admin add course details]({static}/posts/transfer_app/images/django_admin_add_course_details.png)

![Django Admin add course details]({static}/posts/transfer_app/images/django_admin_save_course_details.png)

Afer we save the college entry, we can see the college in the list of colleges on the Django admin pannel.

![Django Admin add course details]({static}/posts/transfer_app/images/django_admin_add_course_details.png)

Now that the college model is running and we have one college added, let's add one more college to the Django admin. With two college we will be able to see what a college page looks like with more than one college and how we can iterate over the colleges to build the colleges list page. Up next is creating url routes so we have a destinations for our college pages.

## Create a colleges urls

We want to create a url for our colleges page. This needs to be accomplished in two steps. First we need to add a url to the over-all project urls, second we need to add a url to the colleges app ```urls.py``` file.

### Add a college URL to the project urls

We'll add the sub-url ```/colleges``` to proceed any url's that display college pages. In the project url's, we'll add a url route to go to our college app url's.

```python
# transfer_project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("colleges/", include("colleges.urls")),
    path("", include("pages.urls")),
]

```

Any url that starts with ```/colleges``` is now routed to the colleges app urls. Create a new ```urls.py``` file in the ```colleges/``` app directory.

```python
# colleges/urls.py

from django.urls import path
from .views import (
    CollegeDetailView,
    CollegeListView,
)

urlpatterns = [
    path("college_list/", CollegeListView.as_view(), name="college_list"),
    path("college/<slug:slug>/", CollegeDetailView.as_view(), name="college_detail"),
]

```

We named the ```CollegesListView``` as the view called when the ```/colleges/college_list``` url is requested. This view needs to be constructed. We name ```CollegeDetailView``` as the view called when an individual college is selected. This view also needs to be constructed.

## Create two college views

To create the ```CollegesListView```, we'll create a custom class-based view from Django's generic ```ListView``` class. We'll assign the view to use the ```college_list.html``` template, which we'll put in the ```tempates/colleges/``` directory.

```python
# colleges/views.py

from django.views.generic import ListView, DetailView

from .models import College


class CollegeDetailView(DetailView):
    model = College
    template_name = "college_detail.html"


class CollegeListView(ListView):
    model = College
    template_name = "college_list.html"

```

## Create college page templates

Our college list view is pointing to the template ```colleges/college_list.html``` so that's the template we'll construct next. We'll use bootstrap cards for each college in the template. Django's generic ```ListView``` class provides an object called ```object_list```. Since our ```CollegeListView``` is a daughter class of the ```ListView``` class, our ```CollegeListView``` also provides an object called ```object_list```. When we iterate over ```object_list```, we'll iterate over the two colleges we created in the Django admin.

```html
<!-- templates/college_list.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
    <link href="{% static 'css/home.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}
<div class="container">
  <!-- Example row of columns -->
  <div class="row">
    {% for college in object_list %}
    <div class="col-md-4">
      <h2>{{ college.name }}</h2>
      <p>{{ college.description }}</p>
      <p><a class="btn btn-secondary" href="{% url 'college_detail' college.slug %}" role="button">View College &raquo;</a></p>
    </div>
    {% endfor %}
  <hr>

  </div> <!-- /row -->
</div> <!-- /container -->

{% endblock content %}

```

The other template is the college detail template. Create a new file in ```templates/``` called ```college_detail.html```. 

```html
<!-- templates/college_detail.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
  <link href="{% static 'css/home.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}
<div class="container">
    <h2>{{ college.name }} - {{ college.abbreviation }}</h2>
    <hr>
    <p>{{ college.description }}</p>
    <hr>
    <h3>{{ college.abbreviation }} offers the following majors: </h3>
</div>

<div class="container">
    <!-- Example row of columns -->
    <div class="row">
      {% for major in college.majors.all %}
      <div class="col-md-4">
        <h2>{{ major.name }}</h2>
        <p>{{ major.description }}</p>
        <p><a class="btn btn-secondary" href="{% url 'major_detail' major.slug %}" role="button">View Courses &raquo;</a></p>
      </div>
      {% endfor %}
    <hr>

  </div> <!-- /container -->
</div>

{% endblock content %}

```


## Run the local server to see the results

OK. We should be able to see the course page list now. Let's run the local server and browse to the /courses page.

```text
(transfer) > python manage.py runserver
``` 

 > localhost:8000/colleges/college_list

 ![courses list page]({static}/posts/transfer_app/images/courses_list_page.png)

It works! We see the two courses we added to the Django admin.

## Build tests for the colleges page

Since we have a college list page, we need to write a new test. We already have a couple tests. We can continue to improve our test coverage by adding tests for the new colleges list page.

```python
# colleges/tests.py

from django.test import TestCase
from django.urls import reverse

from .models import College
from accounts.models import CustomUser


class CollegesListPageTests(TestCase):
    def test_colleges_list_page_status_code(self):
        response = self.client.get('/colleges/college_list/')
        self.assertEqual(response.status_code, 200)

    def test_colleges_list_view_uses_correct_template(self):
        response = self.client.get(reverse('college_list'))
        self.assertTemplateUsed(response, 'college_list.html')

class CollegeTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='peter', email='peter@peter.com', password='top_secret')
        College.objects.create(
            name ="Mt. Hood Community College",
            abbreviation = "MHCC",
            URL = "https://mhcc.edu/",
            slug = "mhcc",
            description = "Mt. Hood Community College is in Gresham, OR",
            added_by = self.user
            )

    def test_text_content(self):
        college = College.objects.get(id=1)
        expected_object_name = f'{college.name} - {college.abbreviation}'
        self.assertEquals(expected_object_name, 'Mt. Hood Community College - MHCC')

    def test_college_list_view(self):
        response = self.client.get(reverse('college_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'is in Gresham, OR')
        self.assertTemplateUsed(response, 'college_list.html')

    def test_college_detail_view(self):
        college = College.objects.get(id=1)
        response = self.client.get(reverse('college_detail', args=[str(college.slug)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mt. Hood Community College')
        self.assertTemplateUsed(response, 'college_detail.html')

```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer) > python manage.py test
```

The output should look something like:

```text
----------------------------------------------------------------------
Ran 15 tests in 0.474s

OK
Destroying test database for alias 'default'...
```

The tests passed! Now our Django app has a working profile page.

## Format and push our code up to GitHub

We are at a good point in our project to make sure all the code we've written so far is saved on our computer and synched up with github.com. Type the commands below to add all the new files in our project, commit the changes and push the changes up to our remote repo on github.com

```text
(transfer) > isort .
(transfer) > black .
(transfer) > git add .
(transfer) > git commit -m "commit message"
(transfer) > git push origin main
```

## Summary

In this post we created a colleges model and added to colleges to our website using the Django admin. Then we built a set of url patterns and views for the colleges pages. We built a couple templates to display our colleges. Finally we constructed and ran some tests on our college pages.

## Future Work

Next, we'll create a course model and course pages that will house individual courses at community colleges and 4-year colleges which are in our database.
