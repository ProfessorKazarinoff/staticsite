Title: Add a CNAME file to a Pelican blog 
Date: 2020-02-27 19:36
Modified: 2020-02-27 19:50
Status: Draft
Category: Python
Tags: python, pelican, blog, github 
Slug: add-nojekyll-file-to-pelican
Authors: Peter D. Kazarinoff

This blog is built with Python and a package called Pelican. Pelican is a Python package used to create blogs.  This blog is deployed on GitHub pages. When Pelican runs, it produces .html files that make up the blog in an output directory. The output directory is saved to a gh-pages branch of the main GitHub repo. When the gh-pages branch is updated with new content (a new blog post), the blog webpages are re-deployed.

## The Problem

The problem I had was that each time I pushed a new blog post to GitHub pages, I had to manually add my Domain Name in GitHub under the settings tab of the repository. This wasn't a deal-breaker, but it was annoying. Then by chance, I typed in the wrong domain name into the GitHub settings page and GitHub displayed something like

```text
* Failed the CNAME specified is already in use on GitHub Pages:

For more information, see https://help.github.com/en/github/working-with-github-pages/troubleshooting-custom-domains-and-github-pages#cname-already-taken.
```

I though, "Crap, someone stole my domain name!" But it turned out that I typed in the wrong domain name (a domain name for another one of my projects). Trying to find the solution to the ```CNAME already taken``` problem led me down a rabbit hole of trying to figure out what the ```CNAME``` file does, and where it has to be included. I ended up fixing two problems:

 1. I realized I typed in the wrong domain name
 2. I figured out how to add a CNAME file to a Pelican static site

## The Cause

The reason I had the domain name wrong is that I didn't get enough sleep or I was rushing to publish a blog post or both. 

The reason I had to enter the domain name manually in the settings tab for the GitHub repo where my static site resides is that I did not create a ```CNAME``` file when I built my site.

## The Solution

**The solution is to have Pelican copy a CNAME file to the main project directory when the site is built.** 

The solution I found is to add a ```CNAME``` file to root directory of the site. This ```CNAME``` file needs to have an upper-case file name and no file extension. One one line of text needs to be in the file, just a domain name with no ```https``` or ```www```. Something like ```mydomain.org```. 

## Copying a source file with Pelican

Pelican has the ability to copy static files when the site is built. First the static file needs to be added to the content of the site. 

### Add a ```CNAME``` file to the main project directory

My directory structure looks like below. I added the ```CNAME``` file to the ```extra/``` directory. Note the file name is ```CNAME``` all CAPS and no extension.

```text
project_root/
    content/
        code/
        css/
        extra/
            CNAME
            custom.css
            custom.js
            nojekyl
```

Inside the ```CNAME``` file, add one line with your domain.

```text
mydomain.org
```

### Modify ```pelican_conf.py```

Next, the Pelican configuration file, ```pelicanconf.py``` needs to be modified. Add the ```extra``` directory to the list of ```STATIC_PATHS``` and add a key:value pair to the ```EXTRA_PATH_METADATA``` dictionary. Note that the key is ```'extra/CNAME'``` and the value is ```{'path': 'CNAME'}```. The file comes from the ```extra``` directory and ends up in the main project directory

```text
# pelicanconf.py

STATIC_PATHS = [ ...
                'extra',
                ... ]

EXTRA_PATH_METADATA = {
    ...
    'extra/CNAME': {'path': 'CNAME'},
    ...
}

```

### Build the site and confirm 

Now build the site using Pelican and look in the output directory for a ```CNAME``` file.

```text
> invoke build
```

## Upload to GitHub on gh-pages branch

Build and deploy the site to GitHub Pages. The commands I use are below. 

```text
pelican content -o output -s publishconf.py
ghp-import output -b gh-pages
ghp-import -m "publishing site" -p -f output
```

### View the site

Now you can browse to your domain name and see the live static site in all it's glory!

### Summary

In this post, I reviewed how to add a CNAME file and a custom domain name to a static site built with Pelican. Making the CNAME file is easy, but figuring out where to put it and how to make Pelican copy when the site was built took a little trouble-shooting. But now that it's done, once and my ```pelicanconf.py``` is saved, I shouldn't have to manually add a domain name into the GitHub settings tab each time I depoly the site. 
