Title: How to use PyScript
Slug: how-to-use-pyscript
Date: 2022-05-26 09:30
Modified: 2022-05-26 09:01
Status: draft
Category: web
Tags: python, pyscript, matplotlib
Author: Peter D. Kazarinoff
Summary: Pyscript is a Python library that allows you to write Python code in webpages. Instead of writting web pages in HTML, Javascript and CSS, PyScript allows you to write Python code to construct a web page. In this post, you'll learn how to use PyScript to make a web page with plots.
 

## What is PyScript

PyScript is a Python library that allows you to write Python code to build web pages. Instead of writting web pages in HTML, Javascript and CSS, PyScript allows you to write Python code to construct a web page. The PyScript project is open source and is supported by Anaconda, the company that makes the Anaconda distribution of Python.

You can find the PyScipt documentation here: ![PyScript Docs](https://pyscript.net/)

A great webpage of PyScript Examples can be found here: ![PyScript Examples](https://pyscript.net/examples/)

## How do you use PyScript?

Using PyScript is pretty easy. Below are the pieces needed to construct a webpage with Pyscript:

 * html page
 * PyScript library sourced in the html header
 * a ```<div>``` on the html page that denotes a PyScript section
 * Python code within the PyScript ```<dev>```
 * Optional: a section on the html page to show your imports

## A simple Web Page

Let's start out by making a simple webpage in html. Create a new file called ```index.html```. Use a code editor like VS Code or Notepad and paste in the following:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />

    <title>PyScript for Undergraduate Engineers</title>
  </head>

  <body>
    Pyscript for Undergraduate Engineers
  </body>
</html>

```

To view the html page we just created, use your computer's file browser to navigate to where you saved ```index.html``` and open it by double clicking. This should open a web browser tab with your rendered html.

## Build a simple PyScript Webpage

Next, we'll modify our html page to use PyScript. We don't need to make very many modifications to the page to make this work.

The additions to our html page are:

 * PyScript script linked in header
 * PyScript css linked in header
 * A ```<div>``` for PyScript in the ```<body>``` of the html page
 * Python code within the PyScript ```<div>```

Copy the code below into at file called ```pyscript_page.html```. Note the two new lines in the ```<head>``` section of the html page. One line is for the PyScript CSS and the other line is for the PyScript javascript script.

```html
<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
<script defer src="https://pyscript.net/alpha/pyscript.js"></script>
```

Within the ```<body>``` of the html page, not how we add a tag for ```<py-script>``` and put our Python code between the ```<py-script>``` and ```</py-script>``` tags.

```html
  <body>
    <py-script>
    print("PyScript for Undergraduate Engineers")
    </py-script>
  </body>
```

The complete html source is below:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />

    <title>PyScript for Undergraduate Engineers</title>

    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />

    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  </head>

  <body>
    <py-script>
    print("PyScript for Undergraduate Engineers")
    </py-script>
  </body>
</html>

```

Browse to the html file you just created on your computer and open it. This should open a web brower tab like the image below:

![#](#)

## Use PyScript to build a webpage with a plot

## Summary
