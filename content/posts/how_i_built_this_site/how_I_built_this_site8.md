Title: How I Build This Site - Part 5
Date: 2017-11-20 12:40
Modified: 2017-11-20 12:40
Status: Draft
Category: This site
Tags: python, pelican, blog
Slug: how-built-site-5
Authors: Peter D. Kazarinoff
Series: How I built this site
Series_index: 5
Summary: This is the fifth part of a multi-part series on how I built this site. In last post, we customized the site and added the ability to use jupyter notebooks in posts.  In this post we are going to deploy the site to Digital Ocean Spaces. Digital Ocean Spaces is a cloud service provider like Amazon S3. We will use the command line tool **s3cmd** to upload the site.

This is the fifth part in a multi-part series on how I built this site. In last post, we customized the site and added the ability to use jupyter notebooks in posts.  In this post we are going to deploy the site to Digital Ocean Spaces. Digital Ocean Spaces is a cloud service provider like Amazon S3. We will use the command line tool **s3cmd** to upload the site.

### Steps in this post

By the end of the post we are going to have a working website on Digital Ocean Spaces. To accomplish we will go through the following steps.

1. Run pelican's ```make html``` command to build the site and preview it with ```make serve```
2. Sign up for a Digital Ocean account
3. Create a new Digital Ocean Space called pythonforundergradengineers
4. Install the ```s3cmd``` command line tool
5. Use ```s3cmd``` to push the contents of pelican's ```output``` folder to Digital Ocean Spaces
6. View the freshly published site! 


OK, let's start small.


### Run pelican's ```make html``` command to build the site and preview it with ```make serve```

Open a terminal and ```cd``` to the ```staticsite``` folder. Then we need to activate our ```(staticsite)``` virtual environment with ```conda activate staticsite```. Once in the ```(staticsite)``` environment, we can call the ```make html``` or ```fab build``` command to build our static site. 

On MacOS and Linux:

```text
(staticsite) $ make html
```

On Windows:

```text
(staticsite) $ fab build
```

This will place the contents of our site in the ```output``` folder.  We can preview the site with ```make serve``` or ```fab build```.

On MacOS and Linux:

```text
(staticsite) $ make serve
```


On Windows:

```text
(staticsite) $ fab serve
```

We can now look at our staticsite by pointing a browser to:

**_localhost:8000_**

we can press ```ctr-c``` to stop the server.

### Sign up for a Digital Ocean account

One hosting option for the site is **Digital Ocean Spaces**. Digital Ocean Spaces is sort of like Amazon S3. It is a cloud service provider for static assests like html files, images, video files etc.  There is no server and no database to run on Digital Ocean Spaces. It is just a place to park static files that other people can view.
 
### Install the ```s3cmd``` command line tool

```text
(staticsite) $ pip install s3cmd
```

### Use ```s3cmd``` to push the contents of pelican's ```output``` folder to Digital Ocean Spaces

To use the ```s3cmd``` command line utility, ensure that you are in the ```output``` folder. We want to copy all of the output folder, so we use the ```--recursive``` flag. To change the permissions of all the files to public, so that they can be viewed on the internet, the ```--acl-public``` flag is added. The combined relevant command is:

```text
(staticsite) $ s3cmd put * s3://pythonforundergradengineers/ --acl-public --recursive
```

### 6. View the freshly published site! 

Point a web browser to the site at:

https://pythonforundergradengineers.nyc3.digitaloceanspaces.com/index.html

In the [next post]({filename}how_I_built_this_site5.md) we will upload the contest of the site to GitHub pages. Then view the site with a web browser or phone.
