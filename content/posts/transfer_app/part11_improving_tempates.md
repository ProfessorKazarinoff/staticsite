Title: Oregon Engineering College Transfer App - Part 11: Improving the Templates
Date: 2021-08-23 12:40
Modified: 2021-08-23 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-11-improve-templates
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 11
Summary: This is the 11th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 11th part of the series, we are going to improve the templates so that the website is useful for college students that want to transfer.

This is the 11th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this 11th part of the series, we are going to improve the templates so that the website is useful for college students that want to transfer.

[TOC]

## Our project so far

We kind of have the whole website scaffolded out now. Our site has colleges, majors, courses and articulations in it. The file structure built so far is below:

```text

```

What we need to do now is improve the templates so that the pages on the website are useful for students.

## Add the articulated classes to each course detail view


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

## Write tests for the course detail page

We've made a change to the couse detail page, so let's write some new tests. These new tests can be in the courses app.

```python
# courses/tests.py

from django.test import SimpleTestCase, TestCase

class CoursesDetailPageTest(SimpleTestCase)

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

Browse to a course page and see if that couse shows what it counts for at other colleges.

```text
localhost:8000/courses1
```

## Summary

In this post we modified the course detail view so that it showed which courses a particular course transfers to.

## Future Work

Next, we can put in a new collumn on the majors page that shows all the courses that articulate.
