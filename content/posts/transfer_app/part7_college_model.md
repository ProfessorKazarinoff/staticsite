Title: Oregon Engineering College Transfer App - Part 7: College Model
Date: 2021-08-23 12:40
Modified: 2021-08-23 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-7-college-model
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 7
Summary: This is the 7th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 7th part of the series, we'll create a new College model and add a few colleges to our database using the Django admin. 

This is the 7th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 7th part of the series, we'll create a new College model and add a few colleges to our database using the Django admin. 


[TOC]

## Databse Design

So far our website is made up of static pages. These pages won't change unless we change the html in the templates. But we are building a dynamic website. Our website should change when a new course is added, or a course is removed or a change in how a course transfers. In order to make our website dynamic, we need to create a database and that means we need to think about database design.

How are we going to structure our database for our website?

Our website is going to list courses at different colleges, so we have a couple relationships:

 * A College can have many courses
 * A course belongs to a specific college
 * A major belows to a specific college and contains many courses
 * A course at one college is equivalent to a course at another college

## Why a College model?

The purpose of the Oregon Transfer App is to have a website that students can visit to see which classes transfer from Community College Engineering programs to 4-year University Engineering Programs. A college is the biggest "bucket" in our website. A college contains many majors and each major contains many courses. Since a major belongs to a college and a course belongs a college, we'll make our College model first so that when we make our majors and courses models there will be a college to associate them with.

## Create a College model

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

## Create the College model

Now we need to create the College model. This is defined within the courses app in the ```models.py``` file. Each college has a couple specific properties that we want to keep track of:

 * College name: Example Portland Community College

 * College abriviation: Example PCC

 * College URL: Example https://pcc.edu

 * Date added: Example Aug 24, 2021

 * Added by: Example Kendra Lowry

 * Possibly others? Like manybe the location or a description? We can add these later if we need to.

```python
# courses/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class College(models.Model):
    name = models.CharField(max_length=50)
    abreviation = models.CharField(max_length=30)
    URL = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('college_detail', args=[str(self.id)])

```

## Migrate new College model to the database

Now that the College model is added, we need to migrate the model to the database.

```text
(transfer) $ python manage.py makemigrations
(transfer) $ python manage.py migrate
```

## Add courses model to the Django admin

Now let's add our courses model to the Django admin so that we can test it's functionality.

```python
# courses/admin.py

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

Afer we save the college, we can see the course in the list of colleges on the Django admin pannel. We can see the college name we entered into the Django admin

![Django Admin add course details]({static}/posts/transfer_app/images/django_admin_add_course_details.png)

Now that the college model is running and we have a course added, let's add one more college to the Django admin. With two college we will be able to see what a college page looks like with more than one college and how we can iterated over the colleges to build the colleges page. Up next is creating a url route so we have a destination for our course page.


## Create a colleges URL

We want to create a url for our colleges page. This needs to be accomplished in two steps. First we need to add a url to the over-all project urls, second we need to add a url to the courses app urls

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

from .views import CollegesListView

urlpatterns = [
    path('', CollegesListView.as_view(), name='college_list'),
]
```

We named the ```CollegesListView``` as the view called when the ```/courses/colleges``` url is requested. This view needs to be constructed.

## Create a colleges View

To create the ```CollegesListView```, we'll create a custom class-based view from Django's generic ```ListView``` class. We'll assign the view to use the ```college_list.html``` template, which we'll put in the ```tempates/courses/``` directory.

```python
# courses/views.py

from django.shortcuts import render
from django.views.generic import ListView

from .models import Course


class CollegesListView(ListView):
    model = Course
    template_name = 'courses/college_list.html'

```

## Create a courses template

Our college list view is pointing to the template ```ourses/college_list.html``` so that's the template we'll construct next. We'll use bootstrap cards for each college in the template. Django's generic ```ListView``` class provides an object called ```object_list```. Since our ```CollegeListView``` is a daughter class of the ```ListView``` class, our ```CollegeListView``` also provides an object called ```object_list```. When we iterate over ```object_list```, we'll iterate over the two collegews we created in the Django admin.

```html
<!-- templates/courses/college_list.html -->

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

 > localhost:8000/courses/colleges

 ![courses list page]({static}/posts/transfer_app/images/courses_list_page.png)

It works! We see the two courses we added to the Django admin.

## Build tests for the colleges page

Since we have a college list page, we need to write a new test. We already have a couple tests. We can continue to improve our test coverage by adding tests for the new colleges list page.

```python
# courses/tests.py

...

class CollegesListPageTests(TestCase):
    def test_courses_list_page_status_code(self):
        response = self.client.get('/courses/colleges')
        self.assertEqual(response.status_code, 200)

    def test_courses_view_uses_correct_template(self):
        response = self.client.get(reverse('/courses/colleges')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/courses/college_list.html')

```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer) > python manage.py test
```

The tests passed! Now our Django app has a working profile page.

## Push our code up to GitHub

We are at a good point in our project to make sure all the code we've written so far is saved on our computer and synched up with github.com. Type the commands below to add all the new files in our project, commit the changes and push the changes up to our remote repo on github.com

```text
> git add .
> git commit -m "commit message"
> git push origin main
```

## Summary

In this post we created a colleges model and added to colleges to our website using the Django admin. Then we built a set of url patterns and views for the courses pages. We built a couple templates to display our courses. Finally we constructed and ran some tests on our course pages.

## Future Work

Next, we'll build some authorization into the courses pages so that only 4-year University Administrators can add classes and access the course pages for their University. We also need to build in functionality for courses to be added using the site, instead of courses added using the Django admin.
