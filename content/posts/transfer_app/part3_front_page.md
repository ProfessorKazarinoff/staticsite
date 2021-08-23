Title: Oregon Engineering College Transfer App - Part 3: Front Page
Date: 2018-10-16 12:40
Modified: 2018-10-16 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-3-front-page-app
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 3
Summary: This is the third part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this third post, I'll review building the first pages app. The first app to add to the django project. This includes creating the app at the command line, adding the app to the project, creating a view, and creating a urlpattern. Then we'll run the server locally and see if the pages app works.

This is the third part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this third post, I'll review building the first pages app. The first app to add to the django project. This includes creating the app at the command line, adding the app to the project, creating a view, and creating a urlpattern. Then we'll run the server locally and see if the pages app works.

## Django Apps

What is a django app and how is it different from a django project? A djano app is part of a django project. One django project can have many apps.

## Create the pages app

## Add the pages app to the list of installed apps

```python
# Application definition

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # project specific
    'pages.apps.PagesConfig',
]

```

## Define a homepage view

in pages/views.py

```python
# pages/views.py

from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('College Transfer App')
```

## Configure the homepage URL pattern in the pages app

## Configure the homepage URL pattern in the overall transfer project

## Test the server locally

## Summary

## Next Steps
