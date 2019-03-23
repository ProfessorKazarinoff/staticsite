Title: Django IoT Server - Part 6 Front Page Templates
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part7-deployment-intro
Authors: Peter D. Kazarinoff

In this post, we are going to go over the steps to use a template to build our front page
[TOC]

## Why use tempates?

## Class-based frontpage view

```python
# pages/views.py

from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

```

## project urls

```python
# urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
]

```

## pages app urls

```python
# pages/urls.py

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home")
]

```

## specify a templates dir in project settings

```python
# settings.py

...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

...

```

## base tempate

Create a ```templates``` dir in the main project dir.

```html
<!-- templates/base.html -->

{% block doctype %}
    <!DOCTYPE html>
    <html lang="en">
{% endblock %}

{% block head %}
    <head>
        <meta charset="UTF-8">
        {% block title %}
            <title>Django IoT Server</title>
        {% endblock %}
    </head>
{% endblock head %}

{% block header %}
{% endblock header %}

{% block content %}
{% endblock content %}

```

## front page template

create a ```home.html``` file in the ```templates``` directory

```html
<!-- templates/home.html -->

{% extends 'base.html' %}

{% block content %}
    <div>
        <h1> Django IoT Server </h1>
    </div>
{% endblock content %}

```


## test the server

```text
> cd Documents
> cd django-iot-project
> conda activate djangoiot
(djangoiot)> python manage.py runserver
```

## Summary

This post, we created an HTML tempate base and an HTML template for our home page. We also 

## Next Steps

In the next post, we will add a docs page (documentation page) to our Django IoT server. We will use the same set of steps we used in this post: first create a template, then create a Class-based view, then modify our urls.
