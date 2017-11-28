Title: How I build this Site - Part 6
Date: 2017-11-27 12:40
Modified: 2017-11-27 12:40
Status: Published
Category: This site
Tags: python, pelican, blog, git, gitjub
Slug: how-built-site-6
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 6
Summary: This is the sixth part of a multi-part series on how I built this site. In last post, we customized the site and added the ability to use jupyter notebooks in posts.  In this post we are going to deploy the site to github pages. Github pages is a place on github were documentation and static sites can be hosted. It was tricky for me to set this up, but after a lot of different trial and error, I was able to get it to work.

This is the sixth part of a multi-part series on how I built this site. In last post, we customized the site and added the ability to use jupyter notebooks in posts.  In this post we are going to deploy the site to github pages. Github pages is a place on github were documentation and static sites can be hosted. It was tricky for me to set this up, but after a lot of different trial and error, I was able to get it to work.

### Steps in this post

By the end of the post we are going to have a working website on github pages. To accomplish we will go through the following steps.

1. Pull the most recient version of the site from gitub
2. Run pelican's ```make html``` command to build the site and preview it with ```make serve```
3. Modify the publishconf.py file with our github pages url
4. Use ```pelican content -s publishconf.py``` to make a published version of the site in the output directory
5. Add, commit, push the published contents to github
6. make a gh-pages branch in our staticsite repo on github
7. Use ```git subtree push --prefix output origin gh-pages``` to push the output directory to the gh-pages branch
8. View the freshly published site! 


OK, let's get started. Can't wait to see the published site live up on github pages.


### Pull to the most recent version of the site from github

Open a terminal and ```cd``` to the ```staticsite``` folder. Then we need to activate our ```(staticsite)``` virtual environment with ```source activate staticsite```. Once in the ```(staticsite)``` environment, we can call ```git pull origin master``` to pull the most recent version of the site down from github.

```
cd ~/Documents/staticsite
source activate staticsite
(staticsite) $ git pull origin master
```

This will place the contents of our site in the ```output``` folder.  We can preview the site with ```make serve```

```
(staticsite) $ make html
(staticsite) $ make serve
```

We can now look at our staticsite by pointing a browser to:

[localhost:8000](localhost:8000)

we can press ```ctr-c``` to stop the server.

### Modify the _publishconf.py_ file to use the github pages url

The static site folder should look something like this:
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
 
we need to edit the **_publishconf.py_** file to use our github pages url and set relative url's to True. The lines to change are:

```
#publishconf.py
SITEURL = 'https://username.github.io/staticsite'
RELATIVE_URLS = True
```

Make sure to set ```username``` to your github user name. Setting ```RELATIVE_URLS = True``` is necessary to get the links in the site to work and have the css and javascript files run on github pages.

### Make a published version of the site

Up to this point, we have been using the ```make html``` command to build a demo version of the site. Now we are ready to **publish** the site. We do this by running the command:

```
pelican content -s publishconf.py
```

This creates a published version of the site with relative url's in the output directory. 

### Add, commit, push to the master branch on github

Before we can put the published version of the site up on github pages, we need to push the current version of the site up to the master branch.

```
git add .
git commit -m "first published version"
git push origin master
```

### Create a gh-pages branch in our staticsite repo on github

On github, we have so far only been saving our work in the **master** branch of the staticsite repository. To have the site hosted on githubpages we need to create a new branch in the staticsite repo called **gh-pages**. Any html, css and javascript files in the **gh-pages** branch will be served like a regular website. To create a new branch, go the repo on github and click the **Branch: Master** drop down menu on the upper left hand site. Enter the name of the new branch: **gh-pages**

### Use the git subtree command to push the contents of the output directory to the gh-pages branch

I tried a bunch of different ways to get the contents of the output directory up to github pages. I tried multiple times to use the **ghp-import** command shown in the Pelican documentation, but I never got it to work right. I also tried to use git submodules, but had trouble with that as well. The way that finally worked was to use the ```git subtree``` command. 

```
git subtree push --prefix output origin gh-pages
```

Note the subtree we are pushing is the contents of the **output** directory. We are pushing this subtree to the **gh-pages** branch. 

### View the site on github pages.

Awesome! The site is now on github pages. Point a browser to the githubpages url:

https://username.github.io/staticsite

Change _username_ to your github user name. My site (the one that you are reading) is hosted here: 

[https://professorkazarinoff.github.io/staticsite](https://professorkazarinoff.github.io/staticsite)