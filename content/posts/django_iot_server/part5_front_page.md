Title: Django IoT Server - Part 5 Building a Front Page
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part5-front-page
Authors: Peter D. Kazarinoff

In this post, we are going to build a front page for our Django IoT server. This front page is what students will see when they visit the site.

[TOC]

## Pull most recent version of project down from GitHub

```text
> cd Documents
> cd django_iot_project
> conda activate django_iot_project
(djangoiot)>
```

```text
(djangoiot)> git init
(djangoiot)> git remote add origin https://github.com/username/reponame.git
(djangoiot)> git pull origin master
(djangoiot)> dir
```

## Run the development server

## General Steps

 * create a pages app
 * add pages app to list of installed apps
 * modify project urls
 * modify app urls
 * add a home page view
 * makemigrations and migrate
 * test the local server

## Add pages app to list of installed apps

```python
# settings.py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # project specific apps
    'pages.apps.PagesConfig'
]

```

## modify project urls

```python
# urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
]

```

## Modify app urls

```python
# pages/urls.py

from django.urls import path
from .views import homePageView

urlpatterns = [
    path("", homePageView, name="home")
]

```

## Add a home page view

```python
# pages/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('Django IoT Server')
```

## makemigrations and migrate

```text
> cd Documents
> cd django_iot_project
> conda activate django_iot_project

(djangoiot)>pyton manage.py makemigrations
(djangoiot)>pyton manage.py migrate
```

## Test the local server

```text
(djangoiot)>pyton manage.py runserver
# [Ctrl]+[c] to exit
```

## Update the project on GitHub

```text
# .gitignore

### Django ###
*.log
*.pot
*.pyc
__pycache__/
local_settings.py

.env
db.sqlite3
```

```text
# .gitignore

### VS Code ###
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.vscode/
```

```text
(djangoiot)>git add .
(djangoiot)>git commit -m "added pages app and simple homepage"
(djangoiot)>git push origin master
```

## Summary

This post explained how to build a very simple front page

## Next Steps

In the next post, we will review how to create the homepage
