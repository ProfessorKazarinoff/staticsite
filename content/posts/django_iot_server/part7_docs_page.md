Title: Django IoT Server - Part 7 Docs Page
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part7-docs-page
Authors: Peter D. Kazarinoff

In this post, we are going to add a second page to our Django IoT server. We are going to add a docs page.

[TOC]

## Basic Steps

 * check project urls
 * modify pages app urls
 * create a view in the pages app
 * create a docs template

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

## modify pages app urls

```python
# pages/urls.py

from django.urls import path
from .views import HomePageView, DocsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("docs/", DocsPageView.as_view(), name="docs")
]

```

## Create a docs page view

```python
# pages/views.py

from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class DocsPageView(TemplateView):
    template_name = 'docs.html'

```


## docs page template

create a ```docs.html``` file in the ```templates``` directory

```html
<!-- docs/home.html -->

{% extends 'base.html' %}

{% block content %}
    <div>
        <h1> Docs for Django IoT Server </h1>
    </div>
{% endblock content %}

```


### test the server

```text
> cd Documents
> cd django-iot-project
> conda activate djangoiot
(djangoiot)> python manage.py runserver
```

browse to:

 > http://localhost:8000/docs

## Summary

This post, we reviewed how we are going to deploy our Django IoT server out in the wild.

## Next Steps

In the next post, we will start the server deployment by creating a set of public and private SSH keys.
