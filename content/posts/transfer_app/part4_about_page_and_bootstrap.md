Title: Oregon Engineering College Transfer App - Part 4: About Page and Bootstrap
Date: 2018-10-16 12:40
Modified: 2018-10-16 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-4-about-page-bootstrap
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 4
Summary: This is the four part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this four post, I'll review building the about page and using bootstrap to stype the pages. This includes creating a view, and creating a urlpattern. Then we'll create a template and use django's template engine and boostrap to build the page. Finally we'll run the server locally and see if the about works and is styled correctly.

This is the four part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this four post, I'll review building the about page and using bootstrap to stype the pages. This includes creating a view, and creating a urlpattern. Then we'll create a template and use django's template engine and boostrap to build the page. Finally we'll run the server locally and see if the about works and is styled correctly.

## Bootstrap

What is Bootstrap and why add it to the django project? Bootstrap is a collection of html, javascript and css that produces mobile-responsive web wages.

## Create about page URL in the pages app and in the overall project

Need to make sure both the overall project urls and the page app urls are set up for the new views (the new home page and about page)

### project urls

```
# transfer_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```

### page app urls

```
# pages/urls.py

from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
```


## Create the view for the home and about pages

```
# pages/views.py

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

```

## Create the templates for the home and about pages

Build 3 templates to make the about pages. There will be a base template and then the home and about templates will build upon the base template. Before the templates render, a templates dir needs to be created in the base project directory. All three templates will be saved in this basedir/templates directory. In the

### Add template path to project settings.py

```
# transfer_project/settings.py

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
```

### Add template dir to main project dir


### Base template

```html
<!-- templates/base.html -->

{%  block doctype %}
<!DOCTYPE html>
<html lang="en">
{% endblock %}

{%  block head %}
<head>
    <meta charset="UTF-8">
    {%  block title %}
    <title>Title</title>
    {%  endblock %}
</head>
{% endblock %}

{% block header %}
<header>
  <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>
</header>
{% endblock %}

{% block content %}
{% endblock %}

```

### Home template

```html
<!-- templates/home.html -->

{% extends 'base.html' %}

{%  block title %}
    <title>Home</title>
{%  endblock %}

{% block content %}
<h1>Home page</h1>
{% endblock content %}

```

### About template

```html
<!-- templates/about.html -->

{% extends 'base.html' %}

{%  block title %}
    <title>About</title>
{%  endblock %}

{% block content %}
<h1>About page</h1>
{% endblock %}

```

### Bootstrap in templates

#### Install django-bootstrap4 with pip

```text
> conda activate transfer
(transfer)> pip install django-bootstrap4
```

####

Add 'bootstrap4' to the list of installed apps in settings.py

```python
# transfer_project/settings.py

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

    # third party
    'bootstrap4'
]
```

#### Add a static/css directory to the pages app folder

#### Add the bootswatch litera bootstrap theme css to the pages app/static/css folder

[https://bootswatch.com/4/litera/bootstrap.css](https://bootswatch.com/4/litera/bootstrap.css)

#### Modified the base template to include the new css and bootstrap content


## Run the server locally. See if the pages worked.

picture of server running

## Write and run tests for two pages

### Write tests

```
# pages/tests.py
from django.test import SimpleTestCase


class PagesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
```

### Run tests

```
> python manage.py test
```

## Summary