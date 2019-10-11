Title: Add a .nojekyll file to a Pelican blog 
Date: 2019-10-11 19:36
Modified: 2019-11-10 19:50
Status: Draft
Category: Python
Tags: python, pelican, blog, github 
Slug: add-nojekyll-file-to-pelican
Authors: Peter D. Kazarinoff

This blog is build with Python and a package called Pelican. Pelican is a Python package used to create blogs.  This blog is deployed on GitHub pages. When Pelican runs, it produces .html files that make up the blog in an output directory. The output directory is saved to a gh-pages branch of the main GitHub repo. When the gh-pages branch is updated with new content (a new blog post).

## The Problem

The problem I had was that the changes to the blog would not show up after the gh-pages branch was updated. Github gave a cryptic message about not being able to build the site. 

```text
The page build failed for the `gh-pages` branch with the following error:

Page build failed. For more information, see https://help.github.com/articles/troubleshooting-github-pages-builds/.
```

But Pelican already built the site. Why is GitHub trying to build something? Why isn't the blog updating?

## The Cause

I think the cause of the problem is **GitHub thinks my blog is built with Jekyll**. GitHub is trying to build a Jekyll site with the files in the gh-pages branch. Since I built my site with Pelican and Python (not Jekyll), the build is failing. Why does GitHub think that my site is made with Jekyll? I don't know, but for some reason it does. 

## The Solution

So if the problem is GitHub thinks my site is a Jekyll site, **the solution is to tell GitHub the site isn't a Jekyll site**. 

The [GitHub page on Jekyll build errors](https://help.github.com/en/articles/troubleshooting-jekyll-build-errors-for-github-pages-sites) has a lot of information on how to fix _Jekyll build errors_, but I couldn't find any information on how to tell GitHub that **I don't want a Jekyll site at all**.

The solution I found is to add a ```.nojekyll``` file to root directory of the site. This means I need to come up with a way to make Pelican copy a ```.nojekyll``` file from the source files that make up the blog and dump the ```.nojekyll``` file into the output directory when Pelican builds the site. 

## Copying a source file with Pelican

Pelican has a method to copy static files when the site is built. First the static file needs to be added to the content of the site. 

### Add a ```nojekyll``` file to blog content

My directory structure looks like below. I added the ```nojekyll``` file to the ```extra/``` directory. Note the file name is ```nojekyll``` not ```.nojekyll```. There is no dot ```.``` at the start of the filename. I don't know why, but for some reason, Pelican or Windows wouldn't copy over a ```.nojekyll``` file but will copy over a ```nojekyll``` file.

```text
dir structure
```

After the ```nojekyll``` file is added

```text
dir structure with nojekyll
```

### Modify ```pelican_conf.py```

Next, the Pelican configuration file, ```pelicanconf.py``` needs to be modified. Add the ```extra``` directory to the list of ```STATIC_PATHS``` and add a key:value pair to the ```EXTRA_PATH_METADATA``` dictionary. Note that the key is ```'extra/nojekyll'``` (no dot), and the value is ```{'path': '.nojekyll'}``` (with a dot).

```text
# pelicanconf.py

STATIC_PATHS = [ ...
                'extra',
                ... ]

EXTRA_PATH_METADATA = {
    ...
    'extra/nojekyll': {'path': '.nojekyll'},
    ...
}

```

### Build the site and confirm 

Now build the site using Pelican and look in the output directory for a ```.nojekyll``` file.

```
> invoke build
```

## Upload to GitHub on gh-pages branch

### Re-add the domain name

### View the site

### Summary
