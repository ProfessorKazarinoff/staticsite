Title: How I Build This Site - Part 6
Date: 2017-12-18 18:50
Modified: 2017-12-18 18:50
Status: draft
Category: This site
Tags: python, pelican, blog, css, javascript
Slug: how-i-built-site-5
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 6
Summary: This is the sixth part in a multi-part series on how I built this site. In the [last post]({filename}how_I_built_this_site5.md), we put a search bar at the top right of each page and some css and javascript in order to make tables on the site look better. In this post we are going to add two new _pages_ to our static site. An **About** page and a **Book* page. These new pages will have menu entries at the top of our site.

This is the sixth part in a multi-part series on how I built this site. In the [last post]({filename}how_I_built_this_site5.md), we put a search bar at the top right of each page and some css and javascript in order to make tables on the site look better. In this post we are going to add two new _pages_ to our static site. An **About** page and a **Book* page. These new pages will have menu entries at the top of our site.


### Steps in this post

We are going to accomplish the following in this post. By the end of the post we are going to have a site with two new pages and two menu entries.

1. Activate our ```staticsite``` virtual environment
2. Pull the most recent version of our site from github
3. Add two new _pages_  (**_.md_** files) to our **content** folder
4. Modify the **_pelicanconf.py_** file to use the new pages
5. Build and preview the site with Pelican
6. Add, commit and push the changes to github


Let's get started.


### Activate our virtual environment and pull the most recent version of the site down from github


```
$ cd ~/Documents/staticsite
$ source activate staticsite
(staticsite) $ git pull origin master
```

The **staticsite** directory should look something like this:

```
staticsite/
├── LICENSE
├── Makefile
├── README.md
├── __pycache__
├── content
│   ├── posts
│       ├── first_post.md
│       ├── second_post.md
│       ├── third_post.md
│   ├── code
│       ├── sample_notebook.ipynb
├── develop_server.sh
├── fabfile.py
├── output
├── pelican-plugins
│   ├── i18n_subsites
│   ├── liquid_tags
│   ├── pelican-ipynb
│   ├── tipue_search
├── pelican-themes
│   ├── pelican-bootstrap3
├── pelican.pid
├── pelicanconf.py
├── publishconf.py
└── srv.pid
```

### Create two new _pages_ (**_.md_** files)

Up to this point, the top of our site has a menu item for [This site], which isn't very useful.  

![simple_pelican-bootstrap3_theme.png]({filename}/images/simple_pelican-bootstrap3_theme.png)

We are going to add two new menu items that link to two new _pages_. These are [About] and [Book]. First we will create a new **pages** folder in the **staticsite/content** directory

```
(staticsite) $ cd ~/Documents/staticsite/content
(staticsite) $ mkdir pages
(staticsite) $ cd pages
(staticsite) $ pwd
```
Now we create two new **_.md_** files. Note that this file is different from the posts we've been writing. It has a very simple header, with just one line: Title. We don't need to put in a date or a slug in the header. The first file is for the **about** page

**_about.md_**
```
Title: About

Why I started this blog


My background


My family


My hobbies
```

The second page is for the book I am writing, Python Programming for Undergraduate Engineers. The text for the page is going to look something like:

book.md
```
Title: Book

### Coming in Fall 2018

Book: **Python Programming for Undergraduate Engineers**

This books is for undergraduate engineers learning programming. It is focused on using Python and programming to solve engineering problems. 

### Chapter List

* Preface
* Chapter 1: Orientation
* Chapter 2: Engineering 101
* Chapter 3: Statics
* Chapter 4: Circuits I
* Chapter 5: Strengths
* Chapter 6: Circuits II
* Chapter 7: Dynamics
* Chapter 8: Circuits III
* Chapter 9: Capstone
* Appendix

### Pre-order will be available soon
```
After the pages are is saved, our **staticsite directory** should look something like this:

```
staticsite/
├── LICENSE
├── Makefile
├── README.md
├── __pycache__
├── content
│   ├── posts
│       ├── about.md
│       ├── book.md
│   ├── posts
│       ├── first_post.md
│       ├── second_post.md
│       ├── third_post.md
│       ├── fourth_post.md
│   ├── code
│       ├── sample_notebook.ipynb
├── develop_server.sh
├── fabfile.py
├── output
├── pelican-plugins
│   ├── i18n_subsites
│   ├── liquid_tags
│   ├── pelican-ipynb
│   ├── tipue_search
├── pelican-themes
│   ├── pelican-bootstrap3
├── pelican.pid
├── pelicanconf.py
├── publishconf.py
└── srv.pid
```


### Modify **_pelicanconf.py_** to include the two new pages.

Pelican needs to know about the two "pages" files. Modify the **_pelicanconf.py_** file to include the lines:

```
#pelicanconf.py

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
```

### Build and preview the site with Pelican

With the two new page .md files created and the changes to **_pelicanconf.py_** in place, let's preview the site again.  We build the site and serve up the contents in the **output** folder with:

```
make html
make serve
```

To view the site, point a browser to _localhost:8000_

[localhost:8000](localhost:8000)

use ```ctrl-c``` to stop the server.

### Add and commit the changes then push them to github

When we are done editing the the site, we add **all of the changes** to our local git repo using ```git add .```. Commit those changes with ```git commit``` and add the ``` -m "added about and book pages" ``` flag to supply a commit message (make sure to use double quotes "commit message"). Push the changes up to github with ```git push origin master```

```
git add .
git commit -m "added about and book pages"
git push origin master
```

In the next post we will publish the site to github pages. Once the site is published, it will be live and public. Available to any one with an internet connection. An actual, real, published, live static site!






