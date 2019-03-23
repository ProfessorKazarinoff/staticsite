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

There are three basic steps to building a page on a Django site (if a databse isn't involved):

 * Create a docs page template
 * Create a docs page View
 * check project urls and modify pages app urls

These steps can be completed in any order, but I like to build the template first (that's what the user sees). Then build the View next (that's what calls the template). And finally modify the URL's (that's what triggers the View). The code editor I use is most helpful when the page is built in this order.

## docs page template

First we'll create a ```docs.html``` file in the ```templates``` directory. The docs template inherits from the base template just like the homepage template did. 

```html
<!-- docs/home.html -->

{% extends 'base.html' %}

{% block content %}
    <div>
        <h1> Docs for Django IoT Server </h1>
    </div>
{% endblock content %}

```

## Create a docs page view

Next we'll create a docs page view that calls our docs.html template. The docs page view inherits from Django's ```TemplateView``` class just like the homepage view did. 

```python
# pages/views.py

from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class DocsPageView(TemplateView):
    template_name = 'docs.html'

```


## project urls

Now, we'll check the project-level urls and make sure we don't have to add an additional route. We already included the ```pages.urls``` path, so the project-level urls can stay the same.

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

We do need to modify the pages app urls. We need to add one additional path to point to our docs page view. Note that we need to import the ```DocsPageView``` class we created earlier.

```python
# pages/urls.py

from django.urls import path
from .views import HomePageView, DocsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("docs/", DocsPageView.as_view(), name="docs")
]

```

Now that the template, view, and urls are finished we can test our handywork.

### test the server

Open the Anaconda Prompt and cd into the project directory. Activate the ```djangoiot``` virtual environment and run the local development server.

```text
> cd Documents
> cd django-iot-project
> conda activate djangoiot
(djangoiot)> python manage.py runserver
```

browse to:

 > http://localhost:8000/docs

You should see the simple docs page in all it's glory.

## Summary

This post, we built our second webpage. First we created a new template, then constructed a class-based view. Next we modified our urls and finally ran the local development server to see the results.

## Next Steps

In the next post, we will add bootstrap4 styling to our site. We will also build out our html templates so that our webpages look a little more professional. 
