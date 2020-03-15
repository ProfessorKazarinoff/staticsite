Title: Deploy a Django Web App on Heroku
Date: 2020-03-15 14:36
Modified: 2020-03-15 14:36
Status: draft
Category: django
Tags: python, django, heroku
Slug: deploy-django-on-heroku
Authors: Peter D. Kazarinoff
Summary: In this post, we are going to deploy a Django Web App on Heroku.

In this post, we are going to deploy a Django App on Heroku.

pip install the heroku django package

at the bottom of settings.py add the heroku locals line

Create:

 * requirements.txt (pip freeze > requirements.txt)
 * runtime.txt (python-3.7.6)
 * Procfile (web: gunicorn my_project_name.wsgi --log-file -)

```
git push origin master
```

install heroku cli

```
heroku login
heroku create my-app-name
git push heroku master
heroku open
```

But... you probably need to migrate the database on heroku

```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```
