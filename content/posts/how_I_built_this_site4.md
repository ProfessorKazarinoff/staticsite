Title: How I build this Site - Part 4
Date: 2017-11-30 12:40
Modified: 2017-10-30 12:40
Status: Draft
Category: This site
Tags: python, pelican, blog
Slug: how-built-site-2
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 4
Summary: This is the fourth part in a multi-part series on how I built this site. In the last post, we installed the pelican_bootstrap3 theme and made our site mobile responsive and look good on all devices.  In this post we are going to install a couple of plugins to add extra functionality to our site. These plugins will allow our site to have a series of post that are linked together, create a working search bar, add youtube videos to posts, and view LaTeX math output in posts.

This is the fourth part in a multi-part series on how I built this site. In the last post, we installed the pelican_bootstrap3 theme and made our site mobile responsive and look good on all devices.  In this post we are going to install a couple of plugins to add extra functionality to our site. These plugins will allow our site to have a series of post that are linked together, create a working search bar, add youtube videos to posts, and view LaTeX math output in posts.


### Steps in this post

We are going to accomplish the following in this post. By the end of the post we are going to have a great looking  website that contains a two-part series, a search bar, a post with an embedded youtube video and these changes pushed up to github

1. Activate our ```pelicanenv``` virtual environment
2. Pull the most recient version of our site from github
3. Use the ```git submodule``` to pull down the pelican-plugins repo
4. Modify **_pelicanconf.py_** to include our new plugins
5. Build a couple new posts that use the plugin functionality
6. Serve the site locally and view with a web browser
7. Add and commit the changes we made then push those changes to github

Seems like a lot to do, so let's get started.


### Activate our virtual environment and pull the most recent version of the site down from github


```
$ source activate staticsite
(staticsite) $ cd ~/Documents/staticsite
(staticsite) $ pwd
(staticsite) $ git pull origin master
```

Now we are going to download the pelican-themes repo from github. Just like we did with the pelican-themes in the previous post, we are going to use git submodules. We need to make sure to specify the ```--recursive``` flag to ensure that all of the submodules with the pelican-themes repo are pulled down to our local machine.
```
(staticsite) $ git add submodule https://github.com/pelican-themes.git
(staticsite) $ git submodule init
(staticsite) $ git suumodule pull --recursive
```

After the submodule pull the contents of the **static_site** folder should look something like this:




You should see a list of all the virtual environments conda has created on your machine. It should look something like:

```
pelican                  C:\Users\user.name\AppData\Local\Continuum\Anaconda3\envs\pelican
root                  *  C:\Users\user.name\AppData\Local\Continuum\Anaconda3
```

The ```pelican``` virtual environment is the one we set up to run our site. To activate it:

```
$ activate pelican
```

You should now see ```(pelican)``` before the command prompt. This means we are opperating in the ```pelican``` virtual environment. 

### View install packages

We installed pelican and markdown in the last post. Let's make sure they are install in our ```(pelican)``` virtual environment.

```
(pelican)$ pip freeze
```

Make sure that you see the following modules: ```beautifulsoup4==4.6.0```, ```Jinja2==2.9.6```, ```Markdown==2.6.9```,```pelican==3.7.1``` and ```Pygments==2.2.0```.

### Pelican Quickstart - make the site!

We are now going to build the site! Exciting stuff. With the virtual environement and packages in place we just need to make sure we are in a directory where we want our site to live.

```
(pelican)$ mkdir staticsite
(pelican)$ cd staticsite
```






