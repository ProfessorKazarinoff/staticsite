Title: How I Build This Site - Part 7
Date: 2017-12-14 12:40
Modified: 2017-12-14 12:40
Status: published
Category: This site
Tags: python, pelican, blog, git, github, github pages
Slug: how-i-built-this-site-7
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 7
Summary: This is the seventh part of a multi-part series on how I built this site. In [last post]({filename}how_I_built_this_site6.md), we added two new _pages_ to our site. An **About** page and a **Book** page.  In this post, we are going to deploy the site to [github pages](https://pages.github.com/). Github pages is a place on github were documentation and static sites can be hosted.

This is the seventh part of a multi-part series on how I built this site. In [last post]({filename}how_I_built_this_site6.md), we added two new _pages_ to our site. An **About** page and a **Book** page.  In this post, we are going to deploy the site to [github pages](https://pages.github.com/). Github pages is a place on github were documentation and static sites can be hosted.


### Steps in this post

By the end of the post we are going to have a working static website hosted on github pages. To accomplish this, we will complete the following steps:

1. Pull the most recent version of the site from gitub
2. Run pelican's ```make html``` command to build the site and preview it with ```make serve```
3. Modify the **_publishconf.py_** file to include our github pages url and relative links
4. Use ```pelican content -s publishconf.py``` to build a published version of the site in the **output** directory
5. Add, commit and push the published contents to our **master** branch on github
6. Make a **gh-pages** branch in our **staticsite** repo on github
7. Use ```ghp-import output``` and ```git push origin gh-pages``` to push the **output** directory to the **gh-pages** branch
8. View the freshly published site! 


OK, let's get started. Can't wait to see the published site live on github pages.

<br>

### Pull to the most recent version of the site from github

Open a terminal and ```cd``` to the ```staticsite``` directory. Then activate the ```(staticsite)``` virtual environment with ```source activate staticsite```. Once in the ```(staticsite)``` environment, pull the most recent version of the site down from github with ```git pull origin master```.

```text
$ cd ~/Documents/staticsite
$ conda activate staticsite
(staticsite) $ git pull origin master
```

The **staticsite directory** should look something like this:

```text
staticsite
├── LICENSE
├── Makefile
├── README.md
├── __pycache__
├── _nb_header.html
├── content
├── develop_server.sh
├── fabfile.py
├── output
├── pelican-plugins
├── pelican-themes
├── pelican.pid
├── pelicanconf.py
├── publishconf.py
└── srv.pid
```


Now we use the ```make html``` command to build a demo version of the site. This will place the static files (_html_, _css_, _javascript_) that forms the site in the **output** folder.  We preview the site with ```make serve```.

On MacOS and Linux:

```text
(staticsite) $ make html
(staticsite) $ make serve
```

On Windows:

```text
(staticsite) $ fab build
(staticsite) $ fab serve
```

The demo version of our site can now be viewed by pointing a browser to:

[localhost:8000](localhost:8000)

Press ```ctr-c``` to stop the server.

<br>

### Modify the **_publishconf.py_** file to use the github pages url

We need to edit the **_publishconf.py_** file to add our github pages url to ```SITEURL``` and set ```RELATIVE_URLS``` to True. The lines to change are:

```text
#publishconf.py
SITEURL = 'https://username.github.io/staticsite'
RELATIVE_URLS = True
```

Make sure to set ```username``` to your github user name. Setting ```RELATIVE_URLS = True``` is necessary for the links on the site to work and for the _css_ and _javascript_ files run on github pages. When I initially set ```RELATIVE_URLS = False```, the site looked terrible, had no formatting or css and none of the links worked. Setting ```RELATIVE_URLS = True``` fixed the problem.

<br>

### Create a published version of the site

Up to this point, we used the ```make html``` command to build a demo version of the site. Now we are ready to _publish_ the site. We publish the site by running the command:

```text
(staticsite) $ pelican content -s publishconf.py
```

This creates a published version of the site with relative url's in the **output** directory. 

<br>

### Add, commit, push to the master branch on github

Before we can put the published version of the site up on github pages, we need to push the current version of the site up to the master branch.

```text
(staticsite) $ git add .
(staticsite) $ git commit -m "first published version"
(staticsite) $ git push origin master
```

<br>

### Create a **gh-pages** branch in our staticsite repo on github

Up to this point, we saved our work to the **master** branch of the staticsite repository on github. To host the site on github pages, we need to create a new branch in the **staticsite** repo called **gh-pages**. The **master** branch still houses the code,settings, markup files, notebooks, images, etc. to build the site. However, in the **gh-pages** branch of the **staticsite** repo any html, css and javascript files  will be served like a regular website. To create the new branch, go the main **staticsite** repository page on github and click the [Branch: Master] drop down menu on the upper left hand side. Enter the name of the new branch: **gh-pages**

<br>

### Use ```ghp-import``` to post the contents of the **output** directory to the **gh-pages** branch

As shown in the [Pelican documentation](http://docs.getpelican.com/en/stable/tips.html), you can use a Python package called ```ghp-import``` to help posting the contents of the output directory to the gh-pages branch of our repo on github. If ```ghp-import``` isn't installed yet, use ```pip```. Make sure you are in the ```(staticsite)``` virtual environment when you run ```pip```.

```text
(staticsite) $ pip install ghp-import
```

Now we'll use the ghp-import package to help us post the site. The command ```ghp-import output``` will assign the contents of the **output** directory to the **gh-pages** branch of our local git repository. The we ```push``` the contents of the local **gh-pages** branch up to the remote **gh-pages** branch on github.

```text
(staticsite) $ ghp-import output
(staticsite) $ git push origin gh-pages
```

I had trouble with this set of commands. Depending on which computer I was using, I would get the following error:

```text
 ! [rejected]        gh-pages -> gh-pages (fetch first)
error: failed to push some refs to 'https://github.com/professorkazarinoff/staticsite.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

I tried ```git stash``` and that didn't work.  I also tried ```git pull origin gh-pages``` but this ended up putting everything from the **output** directory into my root **staticsite** directory which made a big old mess. 

The way I got around it was to use the ```-f``` (force) flag. I don't think this is the most elegant or preferred way to get the contents of the **output** directory up to the **gh-pages** branch. I just don't really understand how ```git``` works well enough to know how to get around the problem without a _forced_ commit. If you get the error above try:

```text
(staticsite) $ pelican content -s publishconf.py

(staticsite) $ git add .
(staticsite) $ git commit -m "published"
(staticsite) $ git push origin master

(staticsite) $ghp-import output
(staticsite) $ git push -f origin gh-pages
```

That has worked so far for me.

<br>

### View the site on github pages.

Awesome! The site is now hosted for everyone to see on GitHub pages! Pretty cool right? Point a browser to the github pages url and take a look:

https://username.github.io/staticsite

Change _username_ to your GitHub user name. My site (the one that you are reading) is hosted here: 

[https://professorkazarinoff.github.io/staticsite](https://professorkazarinoff.github.io/staticsite)

Thanks for reading to the end! It was quite a bit of work to get the site up and running, but I am pleased with the results. Now I need to read up on git . . . 
