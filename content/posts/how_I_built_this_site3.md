Title: How I Build This Site - Part 3
Date: 2017-11-24 12:40
Modified: 2017-11-24 12:40
Status: Draft
Category: This site
Tags: python, pelican, blog
Slug: how-built-site-3
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 3
Summary: This is the third part in a multi-part series on how I built this site. In last post, we used ```pelican-quickstart``` to build the framework of the site and wrote a short first post, then viewed a demo version of the site. In this post we are to add a custom theme to the site called pelican_bootstrap3, then add some custom css.

This is the third part in a multi-part series on how I built this site. In last post, we used ```pelican-quickstart``` to build the framework of the site and wrote a short first post, then viewed a demo version of the site. In this post we are to add a custom theme to the site called pelican_bootstrap3, then add some custom css.

### Steps in this post

We are going to accomplish the following in this post. By the end of the post we are going to have a a static site with a great looking bootstrap3 theme which is mobile responsive and looks great on desktops, tablets and phones.

1. Activate our ```staticsite``` virtual environment
2. Pull the most recent version of our site from github
3. Add a git submodule to our staticsite folder and bring in pelican-themes from github
4. Modify the pelicanconf.py file to utilize the new theme
5. Build and preview the site with Pelican
6. Add custom css to modify the look of the site
7. Add and commit the changes we made and push those changes to github

Big steps, it's really going to look like a website when we are done.


### Activate our virtual environment and pull from github

Open the Anaconda Prompt and activate the ```(staticsite)``` virtual environment

```
$ source activate staticsite
```

Then cd into the staticsite directory and bring in the most up to date version of the site stored on github

```
(staticsite) $ cd ~
(staticsite) $ cd Documents/staticsite
(staticsite) $ git pull origin master
```

There are a bunch of different themes available for static site built with pelican. The three I was most interested in were:

* material

* voidy_bootstrap

* pelican-bootstrap3

We can bring in all of the Pelican themes stored on github by making a git submodule. A git submodule is a sub repository within a git repository that is linked to another repository. It is a way to bring in something else from github within a local repository and not have to keep a local copy up to date. Each time we "pull" from the submodule, we get the newest version of the pelican-themes repo on github. We don't have to manually track any changes to these themes and incorporate them to our local version. 

To create the folder for our pelican-themes git submodule, ensure you are in the staticsite folder, then call:

```
$ git add submodule.....
```

When we are done editing the the site. We add **all of the changes** to our local git repo using ```git add .```. Then we commit theose changes with ```git commit``` and add the ```-m "created pelcian static site``` flag to give supply a commit message. (make sure to use double quotes "commit message") To  push those changes up to github use ```git push origin master```

```
git add .
git commit -m "created pelican static site"
git push origin master
```
