Title: How I Build This Site - Part 5
Date: 2017-12-09 18:50
Modified: 2017-12-09 18:50
Status: published
Category: This site
Tags: python, pelican, blog, css, javascript
Slug: how-i-built-this-site-5
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 5
Summary: This is the fifth part in a multi-part series on how I built this site. In the [last post]({filename}how_I_built_this_site4.md), we installed a couple of plugins to add extra functionality to the site. These plugins enabled embedded jupyter notebooks and posts in a series. In this post we'll put a search bar at the top right of each page and add some css and javascript in order to make tables on the site look better.

This is the fifth part in a multi-part series on how I built this site. In the [last post]({filename}how_I_built_this_site4.md), we installed a couple of plugins to add extra functionality to the site. These plugins enabled embedded jupyter notebooks and posts in a series. In this post we'll put a search bar at the top right of each page and add some css and javascript in order to make tables on the site look better.


### Steps in this post

We are going to accomplish the following in this post. By the end of the post we are going to have a site with a working search bar and nice looking tables.

1. Activate our ```staticsite``` virtual environment
2. Pull the most recent version of our site from github
3. Modify the **_pelicanconf.py_** file to use the **'tipue_search'** plugin
4. Add custom css and javascript to make tables look better
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
├── pelican-themes
│   ├── pelican-bootstrap3
├── pelican.pid
├── pelicanconf.py
├── publishconf.py
└── srv.pid
```

### Add the **'tipue_search'** plugin to the **_pelicanconf.py_** file

Now we need to modify the **_pelicanconf.py_** file to use the **'tipue_search'** plugin. This plugin will give us the ability to add a search bar to our site menu at the top right of each page. 


Add ```'tipue_search'``` to the ```PLUGINS = [ ]``` list in the **_pelicanconf.py_** file. Make sure each plugin is separated with commas and surrounded by quotes .

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

To use the **'tipue_search'** plugin, we also need to add the following line to the **_pelicanconf.py_** file:

```
#pelicanconf.py

# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')
```


### Add some custom css and javascript to make tables look good.

Even with a great theme like pelican-bootstrap3, there are some changes to make to the look of the site. One of these changes is to make tables look better, like the tables on github readme pages look. 


Let's make a new post in the **content/posts** directory. This post will contain a markdown table using the ``` | ``` (pipe) character and a header row with pipes separated by three dashes ``` --- ```.

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

To change the way that tables are rendered, we will add some custom css and javascript that is not included with the pelican-bootstrap3 theme. First create a new folder in the **staticsite/content** directory called **extra**.

```
cd ~/Dcouments/staticsite/content
mkdir extra && cd extra
```

Inside the **extra** folder, create a new **_.css_** file called **_custom.css_**. Insert the following style changes in **_custom.css_**:

```
.table {

    width: inherit;
    max-width: 100%;
    margin-bottom: 21px;
    padding: 6px 13px;    

}
```

Now create a new javascript file in the **content/extra** directory called **_custom.js_**. This file contains extra javascript that will be injected into pages when the _.html_ is generated by Pelican.

```
var tables, i;
tables = document.getElementsByTagName('table');
for (i=0;i<tables.length;i++) {
  tables[i].className = 'table table-bordered table-hover table-striped table-responsive';
}
```

With the addition of these two new files, the contents of the **staticsite** directory will look something like:

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
│   ├── code
│       ├── sample_notebook.ipynb
│   ├── extra
│       ├── custom.css
│       ├── custom.js
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


Pelican needs to know about the two new "custom" files. Modify the **_pelicanconf.py_** file to include the lines:

```
#pelicanconf.py

CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

STATIC_PATHS = [ 'extra' ]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}
```

When the site is built, Pelican will read in **_custom.css_** and **_custom.js_** siting in the **extra** folder. Pelican will then copy these two files in the appropriate places in the **output** directory (static/css/custom.css and static/css/custom.js) for the theme to use. Then the code from the css and javascript files will be used by the _.html_ pages in the output directory along with the other css and javascript from the bootstrap3 theme. This will make tables look more like tables in github readme pages. 

### Build and preview the site with Pelican

With the search plugin configured, a new posts containing a table written, plus our **_custom.js_** and **_custom.css_** in place, let's preview the site again.  We build the site and serve up the contents in the **output** folder with:

```
make html
make serve
```

To view the site, point a browser to _localhost:8000_

[localhost:8000](localhost:8000)

use ```ctrl-c``` to stop the server.

### Add and commit the changes then push them to github

When we are done editing the the site, we add **all of the changes** to our local git repo using ```git add .```. Commit those changes with ```git commit``` and add the ``` -m "added search and tables" ``` flag to supply a commit message (make sure to use double quotes "commit message"). Push the changes up to github with ```git push origin master```

```
git add .
git commit -m "added search and tables"
git push origin master
```

In the next post we will add two new menu items across the top of our site. These new menu items will link to an [About] page and a [Book] page.






