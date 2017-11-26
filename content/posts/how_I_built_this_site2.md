Title: How I Build This Site - Part 2
Date: 2017-10-13 12:40
Modified: 2017-10-13 12:40
Status: Draft
Category: This site
Tags: python, pelican, blog
Slug: how-built-site-2
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 2
Summary: This is the second part in a multi-part series on how I built this site. In last post, we set up our development environment including python, a new virtual environment, installing the pelican and markdown modules and setting up git. In this post we are going to use the ```pelican-quickstart``` to get the blog off the ground. I'm also going to add a new post page and serve up the website locally so I can take a look at it.

This is the second part in a multi-part series on how I built this site. In last post, we set up our development environment including python, a new virtual environment, installing the pelican and markdown modules and setting up git. In this post we are going to use the ```pelican-quickstart``` to get the blog off the ground. I'm also going to add a new post page and serve up the website locally so I can take a look at it.

### Steps in this post

We are going to accomplish the following in this post. By the end of the post we are going to have a working website served locally to view and an updated github repo with all of the changes saved.

1. Activate our ```pelicanenv``` virtual environment
2. Pull the most recent version of our site from github
3. Use the ```pelican-quickstart``` command to make a first version of the site
4. Write a first post in markup language (.md)
5. Build the site using pelican
6. Serve the site locally using pelican and view with a web browser
7. Shut down the server
8. Add and commit the changes we made and push those changes to github

That's a lot to do, so let's get started.


### Activating our virtual environment

I highly recommend installing the Anaconda distribution of python. If you followed along with the previous post, you will have installed Anaconda and can pull up the Anaconda prompt. Open the Anaconda Prompt and see which virtual environments are available.

```
$ conda info --envs
```

You should see a list of all the virtual environments conda has created on your machine. It should look something like:

```
staticsite                  C:\Users\user.name\AppData\Local\Continuum\Anaconda3\envs\pelican
root                     *  C:\Users\user.name\AppData\Local\Continuum\Anaconda3
```

The ```staticsite``` virtual environment is the one we set up to run our site. To activate it:

```
$ source activate staticsite
```

You should now see ```(staticsite)``` before the command prompt. This means we are operating in the ```staticsite``` virtual environment. 

### View installed packages

We installed pelican, markdown and fabric in the last post. Let's make sure they are install in our ```(staticsite)``` virtual environment.

```
(staticsite)$ pip freeze
```

Make sure that you see the following modules: ```beautifulsoup4==4.6.0```, ```Jinja2==2.9.6```, ```Fabric==1.14.0```, ```Markdown==2.6.9```,```pelican==3.7.1``` and ```Pygments==2.2.0```.

### Pelican Quickstart - make the site!

We are now going to build the site! Exciting stuff. With the virtual environment and packages in place we just need to make sure we are in a directory where we want our site to live.

```
(staticsite)$ cd ~
(staticsite)$ cd Documents
(staticsite)$ cd staticsite
```

You can confirm you are working in the staticsite directory by typing ```pwd``` which stands for print working directory:

```(staticsite)$ pwd```

No we can spin up the settings and structure of our pelican build. Start the process with the command:

```
(staticsite)$ pelican quickstart
```

Pelican will ask us a bunch of questions at the start. 


When we are done editing the posts and the site. We add **all of the changes** to our local git repo using ```git add .```. Then we commit theose changes with ```git commit``` and add the ```-m "created pelcian static site``` flag to give supply a commit message. (make sure to use double quotes "commit message") To  push those changes up to github use ```git push origin master```

```angular2html
git add .
git commit -m "created pelican static site"
git push origin master
```



