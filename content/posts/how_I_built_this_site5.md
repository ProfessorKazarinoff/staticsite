Title: How I build this Site - Part 5
Date: 2017-12-09 18:50
Modified: 2017-12-09 18:50
Status: draft
Category: This site
Tags: python, pelican, blog, jupyter
Slug: how-i-built-site-5
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 5
Summary: This is the fifth part in a multi-part series on how I built this site. In the [last post]({filename}how_I_built_this_site4.md), we installed a couple of plugins to add extra functionality to our site. These plugins will allow our site to have a series of posts and add embedded jupyter notebooks in posts. In this post we will customize the site. We'll add some css in order to make tables on the site look better and put a search bar at the top right of each page.

This is the fifth part in a multi-part series on how I built this site. In the [last post]({filename}how_I_built_this_site4.md), we installed a couple of plugins to add extra functionality to our site. These plugins will allow our site to have a series of posts and add embedded jupyter notebooks in posts. In this post we will customize the site. We'll add some css in order to make tables on the site look better and put a search bar at the top right of each page.


### Steps in this post

We are going to accomplish the following in this post. By the end of the post we are going to have a site with a working search bar and nice looking tables.

1. Activate our ```staticsite``` virtual environment
2. Pull the most recent version of our site from github
3. Modify the **_pelicanconf.py_** file to use the **'tipue_search'** pulugin
4. Add some custom css to make tables look better
5. Build and preview the site with Pelican
6. Add and commit the changes then push those changes to github


Let's get started.


### Activate our virtual environment and pull the most recent version of the site down from github


```
$ source activate staticsite
(staticsite) $ cd ~/Documents/staticsite
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
├── develop_server.sh
├── fabfile.py
├── output
├── pelican-plugins
│   ├── i18n_subsites
│   ├── liquid_tags
│   ├── pelican-ipynb
├── pelican-themes
│   ├── pelican-bootstrap3
├── pelican.pid
├── pelicanconf.py
├── publishconf.py
└── srv.pid
```

### Add the **'tipue_search'** plugin to the **_pelicanconf.py_** file

Now we need to modify the **_pelicanconf.py_** file to use the **'tipue_search'** plugin. This plugin will give us the ability to add a search bar to our site menu at the top right of each page. 


Add ```'tipue_search'``` to the ```PLUGINS = [ ]``` list in the **_pelicanconf.py_** file. Make sure each plugin is separated them with commas and surrounded by quotes .

```
#pelicanconf.py

PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup',
    'tipue_search' ] 
```

To use the **'tipue_search'** plugin, we also add the following line to the **_pelicanconf.py_** file:

```
#pelicanconf.py

# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')
```


### Add some custom css to make tables look good.

Now we'll add some custom css to make tables in posts look better. 


Let's make a new post in the **content/posts** directory. This post will contain a markdown table using the ``` | ``` (pipe) character and a header row.

**_fourth_post.md_**
```
Title: Fourth Post - Part 4
Date: 2017-11-30 12:40
Modified: 2017-11-30 12:40
Status: published
Category: example posts
Tags: python, pelican, blog, tables
Slug: fourth-post
Authors: Peter D. Kazarinoff
Series: example-post-series
Series_index: 4
Summary: This is the fourth post of a series of posts. It will demonstrate tables.

This is the fourth post of a series of posts. It will demonstrate tables.

| Column Header | Column Header |
| --- | ---| 
| Row 1 | Data 1 |
| Row 2 | Data 2 |
```

After the post is saved, our **staticsite directory** should look something like this:

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
│       ├── fourth_post.md
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



### Build and preview the site with Pelican

With a new plugin configured and a new posts written containing a table, let's preview our site again.  We build the site and view it with a web browser with the commands:

```
make html
make serve
```

To view the site, point a browser to _localhost:8000_

[localhost:8000](localhost:8000)

use ```ctrl-c``` to stop the server.

### Add and commit the changes then push them to github

When we are done editing the the site, we add **all of the changes** to our local git repo using ```git add .```. Then we commit those changes with ```git commit``` and add the ``` -m "added plugins" ``` flag to give supply a commit message (make sure to use double quotes "commit message"). To push those changes up to github use ```git push origin master```

```
git add .
git commit -m "added search and tables"
git push origin master
```

In the next post we will publish the site live to github pages. Actually publish the real live static site!






