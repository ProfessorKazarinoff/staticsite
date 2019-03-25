Title: Django IoT Server - Part 9 Data Model
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part9-data-model
Authors: Peter D. Kazarinoff

In this post, we are going add a second app to our Django project, a data app. This data app will deal with the data pushed and pulled to the server from users. We will also create our first _model_. I think of a model in Django as a database table or microsoft excel sheet. I know that web-design and database professionals probably don't agree with this characterization. But when I think of a Django model, what comes into my mind is the column headers on an Excel sheet.

[TOC]

## Run migrations before creating the data app or data model

```text
(djangoiot)> python manage.py makemigrations
(djangoiot)> python manage.py migrate
```

## Create the data app

New apps are created by running ```manage.py```, not by running the ```django-admin``` from the command line.

```text
(djangoiot)> python manage.py startapp data
```

This creates a new directory and a bunch of new files.

## Add the new data app to the list of installed apps

```python
# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # project specific apps
    'pages.apps.PagesConfig',
    'data.apps.DataConfig',

    # 3rd party packages

]
```

## Create the data model

```python
# data/models.py

from django.db import models

# Create your models here.

class Data(models.Model):
    DATA_TYPE_CHOICES = (('flt', "Float"), ('str', "string"))
    created_at = models.DateTimeField(auto_now_add=True)
    channel_num = models.PositiveSmallIntegerField()
    field_num = models.PositiveSmallIntegerField()
    data_flt = models.DecimalField(max_digits=19, decimal_places=10)
    data_str = models.CharField(max_length=20)
    uploaded_by = models.CharField(max_length=30)
    data_pt_num = models.PositiveIntegerField()
    data_pt_type = models.CharField(max_length=3, choices=DATA_TYPE_CHOICES, default='flt')

    def __str__(self):
        return f'{self.created_at} channel: {self.channel_num} field: {self.field_num} data: {self.data_flt}'

```

Next, we will add a data point using the Django admin. To log into the Django admin, we need a username and password. So first we'll create a superuser who can log into the Django admin.

## Makemigrations and migrate

```text
(djangoiot)> python manage.py makemigrations
(djangoiot)> python manage.py migrate
```

## Create a Superuser

```text
(djangoiot)> python manage.py createsuperuser
```

## Add data model to the django admin

```python
# data/admin.py

from django.contrib import admin

# Register your models here.

from .models import Data


admin.site.register(Data)
```

## Run the local server and browse to the Django admin

```text
(djangoiot)> python manage.py runserver
```

 > https://localhost/admin


log in and add some data points


## Summary

This post, we created a data app and a data model. Then we logged into the Django admin and added a couple of data points.

## Next Steps

In the next post, we will modify our pages template to show data from the data model. 
