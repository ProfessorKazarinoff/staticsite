Title: Django IoT Server - Part 10 Showing Data
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part10-showing-data
Authors: Peter D. Kazarinoff

In this post, we are going show the data from our data model on the homepage. In the previous post, we created a data model and then used the django admin to add a couple of data points. We can see our data points in the Django admin, but we can't see data points on the public facing site. To show our data on the homepage, we will call data points from our database and pass them to the homepage view and template.

[TOC]

## View the frontpage using the development server

```text
(djangoiot)> python manage.py startserver
```

## Modify the homepage view

We need to modify our homepage view so that we bring in our data model. With the data model brought into our homepage view, we can pass off the data stored in the database to our homepage template.


```python
# pages/views.py

from django.views.generic import ListView

from .models import Data

class DataListView(ListView):
    
    model = Data

    template_name = 'home.html'

```

## Modify the pages urls to call our new view

```python
pages/urls.py

from django.urls import path

from .views import DataListView

urlpatterns = [
    path('', DataListView.as_view(), name='home')
    path('liveplot/', LivePlotView.as_view(), name='liveplot')

]
```

## Modify the homepage template to accept data from the database

Note that ```object_list``` is a built-in attribute that comes from Django's ```ListView``` class. Since we sub-classed ```Listview``` to make our ```DataListView```, we have the ```object_list``` attribute available in our ```home.html``` template. 

```html

{% block datatable }
    {% for data_pt in object_list %}
        <ul>
            <li> data_pt.datetime_added</li>
            <li> data_pt.channel_num</li>
            <li> data_pt.field_num</li>
            <li> data_pt.data</li>
        </ul>
    {% endfor }
{% endblock datatable }

```

## View the homepage using the development server

```text
(djangoiot)> python manage.py startserver
```

## Add a new data point using the Django admin and see the datapiont on the homepage

Let's add a new data point and see if that datapoint comes up in our homepage.

Browse to:

 > localhost:8000/admin

Log in using the super-user credentials we set up earlier. Create a new data point.

Then go back to the main page

 > localhost:8000

We see our new data point on the homepage!

## Summary

This post, we put our data points on the sites main page. We accomplished this by creating a new view in the pages app and then modifying our pages app urls to point to the new view. Next we modified the template that produces the homepage and brought data from the database onto the homepage. Finally we used the Django admin to add a data point and then viewed the result on the homepage.

## Next Steps

In the next post, we will create a new channels app that will display data only from a specific channel on each channel page.
