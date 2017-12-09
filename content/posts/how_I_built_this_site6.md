Title: How I build this site - Part 6
Date: 2017-11-27 12:40
Modified: 2017-11-27 12:40
Status: draft
Category: This site
Tags: python, pelican, blog, git, github
Slug: how-i-built-this-site-6
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 6
Summary: This is the sixth part of a multi-part series on how I built this site. In last post, we customized the site and added the ability to use jupyter notebooks in posts.  In this post we are going to deploy the site to [github pages](https://pages.github.com/). Github pages is a place on github were documentation and static sites can be hosted. It was tricky for me to set this up, but after a lot trial and error, I was able to get it to work.

This is the sixth part of a multi-part series on how I built this site. In last post, we customized the site and added the ability to use jupyter notebooks in posts.  In this post we are going to deploy the site to [github pages](https://pages.github.com/). Github pages is a place on github were documentation and static sites can be hosted. It was tricky for me to set this up, but after a lot of trial and error, I was able to get it to work.

### Steps in this post

By the end of the post we are going to have a working static website hosted on github pages. To accomplish we will complete the following steps:

1. Pull the most recient version of the site from gitub
2. Run pelican's ```make html``` command to build the site and preview it with ```make serve```
3. Modify the **_publishconf.py_** file to include our github pages url
4. Use ```pelican content -s publishconf.py``` to create a published version of the site in the output directory
5. Add, commit and push the published contents to github
6. Make a gh-pages branch in our staticsite repo on github
7. Use ```git subtree push --prefix output origin gh-pages``` to push the output directory to the gh-pages branch
8. View the freshly published site! 


OK, let's get started. Can't wait to see the published site live on github pages.


### Pull to the most recent version of the site from github

Open a terminal and ```cd``` to the ```staticsite``` folder. Then we need to activate our ```(staticsite)``` virtual environment with ```source activate staticsite```. Once in the ```(staticsite)``` environment, we can call ```git pull origin master``` to pull the most recent version of the site down from github.

```
cd ~/Documents/staticsite
source activate staticsite
(staticsite) $ git pull origin master
```

Now we use the ```make html``` command to build a demo version of the site. This will place the static files (html, css, javascript) that forms the static site in the **output** folder.  We can preview the site with ```make serve```

```
(staticsite) $ make html
(staticsite) $ make serve
```

The demo version of our static site can now be viewed by pointing a browser to:

[localhost:8000](localhost:8000)

Press ```ctr-c``` to stop the server.

### Modify the **_publishconf.py_** file to use the github pages url

The staticsite directory should look something like this:
```
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
 
we need to edit the **_publishconf.py_** file to add our github pages url to ```SITEURL``` and set ```RELATIVE_URLS``` to True. The lines to change are:

```
#publishconf.py
SITEURL = 'https://username.github.io/staticsite'
RELATIVE_URLS = True
```

Make sure to set ```username``` to your github user name. Setting ```RELATIVE_URLS = True``` is necessary for the links on the site to work and for the css and javascript files run on github pages. When I initially set ```RELATIVE_URLS = False```, the site looked terrible, had no formatting or css and none of the links worked. Setting ```RELATIVE_URLS = True``` fixed the problem.

### Create a published version of the site

Up to this point, we used the ```make html``` command to build a demo version of the site. Now we are ready to _publish_ the site. We publish the site by running the command:

```
pelican content -s publishconf.py
```

This creates a published version of the site with relative url's in the **output** directory. 

### Add, commit, push to the master branch on github

Before we can put the published version of the site up on github pages, we need to push the current version of the site up to the master branch.

```
git add .
git commit -m "first published version"
git push origin master
```

### Create a **gh-pages** branch in our staticsite repo on github

Up to this point, we saved our work to the **master** branch of the staticsite repository on github. To host the site on github pages, we need to create a new branch in the staticsite repo called **gh-pages**. The **master** branch still houses the code,settings, markup files, notebooks, images, etc. to build the site. Any html, css and javascript files in the **gh-pages** branch of the staticsite repo on github will be served like a regular website. To create the new branch, go the main staticsite repository page on github and click the **Branch: Master** drop down menu on the upper left hand side. Enter the name of the new branch: **gh-pages**

### Use **git subtree** to push the contents of the **output** directory to the **gh-pages** branch

I tried a bunch of different ways to send the contents of the **output** directory up to github pages. First I tried multiple times to use ```ghp-import``` shown in the [Pelican documentation](http://docs.getpelican.com/en/stable/tips.html), but I never got it to work right. I also tried using git submodules, but had trouble with that as well. I kept getting commit error messages. The way that finally worked was the ```git subtree``` command. 

```
git subtree push --prefix output origin gh-pages
```

Note the subtree we are pushing is the **output** directory. We are pushing this subtree to the **gh-pages** branch. 

### View the site on github pages.

Awesome! The site is now hosted for everyone to see on github pages! Pretty cool right? Point a browser to the github pages url and take a look:

https://username.github.io/staticsite

Change _username_ to your github user name. My site (the one that you are reading) is hosted here: 

[https://professorkazarinoff.github.io/staticsite](https://professorkazarinoff.github.io/staticsite)
