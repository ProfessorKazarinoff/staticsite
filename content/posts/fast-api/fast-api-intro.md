Title: Introduction to Fast API
Date: 2021-01-18 09:01
Modified: 2021-01-18 09:01
Status: draft
Category: fast-api
Tags: python, fast-api
Slug: introduction-to-fast-api
Authors: Peter D. Kazarinoff
Series: Fast-API
Series_index: 1

This post is the first part of a series on Fast API. Fast API is a Python web framework for building web API's. It is sort of the Django or Flask, except it's primary use is to create web API's instead of creating whole websites.

[TOC]

## Installation

You can install Fast API with **pip** the Python package manager. First, it's a good idea to create a Python virtual environment. Depending on what system you are using, there are different ways to create a new Python virtual environemnt. I'm writing this blog post on Linux (Ubuntu 20.04). The commands I used are below:

```text
python -m venv venv
source venv/bin/activate
python -m pip install fastapi
python -m pip install uvicorn[standard]
```

## Make a simple one-file fast-api app

In the root directory of your project, create a new file called ```main.py``` in the ```main.py``` file, copy the code below:

```python
# main.py

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

```

Same ```main.py```

## Run the one-file fast API app

Now we need to run our app. Type the command below into a terminal. Make sure the virtual environment you created earlier is active.

```text
uvicorn main:app --reload
```

You will see output in the terminal similar to the output below:

```text
INFO:     Uvicorn running on http://127.0.01:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [75881] using watchgod
INFO:     Started server process [75883]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## View Fast API in action.

Now that Fast API is running locally, we can see it working in a web browser. Open a web broswer and feed in the URL below:

```text
http://127.0.0.1:8000/items/9?q=gabby
```

If fast API is working, your browser will return:

```text
{
  "item_id": 9,
  "q": "gabby"
}
```

Now let's change the query string in the URL and view the result. Browse to the URL below:

```text
http://127.0.0.1:8000/items/7?q=maelle
```
{
  "item_id": 7,
  "q": "maelle"
}
Your browser will now return you an updated JSON response.

```text
{
  "item_id": 7,
  "q": "maelle"
}
```

But what happens when we feed in something other than an integer after ```items/``` in the URL? In our ```main.py``` file, the function ```read_item()``` specified the first arguemnt ```item_id: int``` as an integer using a type hint. Try the URL below and view the result in a browser window.

```text
http://127.0.0.1:8000/items/maelle?q=7
```

The response we get back is:

```text
{
  "detail": [
    {
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

So with only a little code, we created a very simple web API that does some url validation for us. Pretty cool right?

## Check out the auto-generated docs

FastAPI also includes auto-generated documentation. Even with our simple ```main.py``` script, which only contained two functions, API docs are auto-generated. Browse to the docs URL

```text
http://127.0.0.1:8000/docs
```

You get some pretty good looking docs that show what our web API expects. It shows us that the reason our last request didn't return output as before was that we didn't specifiy an integer in the first part of our URL.



You can run a requrest right in the docs page and see the output we got in our web browser earlier. 

## Make Fast API return a web page

Fast API can be used to return a JSON response, but it can also return server-rendered templates like Flask and Django. Jinja2 needs to be installed to use templates with fast API

```text
python -m pip install jinja2
python -m pip install aiofiles
```

### Create a new ```template-app.py``` file. 

Create new file in the root of the project along side ```main.py``` and call it ```template-app.py```. Inside of ```template-app.py``` copy the code below:

```python
# tempate-app.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})

```

### Create the template

Create a file ```templates/index.html``` copy the code below into ```templates/index.html```.

```text
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link href="{{ url_for('static', path='/styles.css') }}" rel="stylesheet">
    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
    <h1>Item ID: {{ id }}</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>

```

The key part of the html template is ```<h1>Item ID: {{ id }}</h1>``` Whatever ```id``` is specified in the URL will be printed out on the webpage.

### Add some css

Now add some css. Create a new file ```static/styles.css```. In ```static/styles.css``` copy the code below:

```text
h1 {
    color: green;
}
```

### Run the new app that contains the templates

That should be it. Now to run the new template app, open a terminal and type the command below:

```
uvicorn template-app:app --reload
```

Browse to:

```text
http://127.0.0.1:8000/items/Peter
```

And you should see the green output in the web browser. 
