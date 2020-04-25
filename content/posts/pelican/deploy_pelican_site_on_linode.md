Title: Deploy as Static Site Built with Pelican on Linode
Date: 2020-04-24 19:36
Modified: 2020-04-24 19:50
Status: Draft
Category: blog
Tags: python, pelican, blog, deployment, linode
Slug: deploy-pelican-static-site-on-linode
Authors: Peter D. Kazarinoff

This blog is built with Python and a package called [Pelican](https://docs.getpelican.com/en/stable/index.html). Pelican is a Python package used to create static web sites, like a blog, a documentation site, or a simple site that doesn't require a back-end server or a database.

This blog is deployed on GitHub pages. But static sites can be deployed in other places too, such as on Amazon's S3 cloud infrastructure or on Digital Ocean. In this post, we are going to discuss how to deploy a static site built with Python and Pelican on Linode. Right now, Linode is offering free object storage. So it's a great and free time to deploy a static site

## Build the static site locally with Python and Pelican

Before we can deploy the site, we need to first build the site. Pelican makes it pretty easy to build static sites. We will save the code and source files that make up our site on GitHub.com. After GitHub is set up, there are a couple steps: Install Python, create a virtual environment and install pelican, write some content, customize, and build/preview the site. We will run over each of these steps in a little more detail.

### Create a new GitHub repo

### Install Python

Before you can use Pelican to build the site, you need to install Python on your computer. Python can be installed in a couple of ways, but the way I recommend is to install the Anaconda distribution of Python. A link to download Anaconda is below.

 > [https://anaconda.com/distribution](https://anaconda.com/distribution)


### Link our local project folder to the GitHub repo

Open the **Anaconda Prompt** from the Windows start menu, or open a terminal if you are using MacOS or Linux. Type the following commands to create a project folder and link the project folder to your repo on Github. Make sure to change ```<username>``` and ```<reponame>``` to your GitHub username and your newly created GitHub repo name. The greater than, less than characters do not need to be included, but the ```.git``` extension should be included at the end of the url.

```text
mkdir staticsite
cd staticsite
git init
git remote add origin https://github.com/<useranme>/<reponame>.git
git pull origin master
```

### Create a Virtual Environment

While inside the ```staticsite``` directory, type the commands below into the Anaconda Prompt (or terminal) to create a new virtual environment called ```venv```.

```text
python -m venv venv
```

If you look in the staticsite directory, you should now see the ```README.md```, ```LICENSE``` and ```venv``` directory.

### Activate the virtual environment and install Pelican

Next, while still in the ```staticsite``` directory, activate the virtual environment we just created. When the virtual environment is active, you should see ```(venv)``` defore the prompt. Then use **pip** to install Pelican from PyPI. Note the activate command is different for Windows 10 users and MacOS/Linux users.

In Windows 10:

```text
venv\Scripts\activate.bat
pip install pelican
```

In MacOS/Linux:

```text
source venv/bin/activate
pip install pelican[Markdown]
pip install invoke
```

Now that pelican is installed, you can open the Python REPL (the Python prompt), import Pelican and call Pelican's ```.__version__``` atribute. If this works, it mean the virtual environment creation, activation and pip install steps were completed and you are ready to move on to the next steps. Note the triple chevron ```>>>``` is not ment to be typed. It is included to indicate the Python REPL, not a command for you to enter.

```text
python
>>> import pelican
>>> pelican.__version__
>>> exit()
```

### Run the Pelican Qickstart Command

Next we will create our static site with Pelican and write one blog post.

Using the **Anaconda Prompt** or a terminal, make sure the virtual environment where pelican was just installed is activate and your are in the ```staticsite``` main project directory.

```text
pelican-quickstart
```

The answers I included to the quickstart questions are below:

```text
Welcome to pelican-quickstart v4.2.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

> Where do you want to create your new web site? [.] .
> What will be the title of this web site? pelican-linode
> Who will be the author of this web site? Peter Kazarinoff
> What will be the default language of this web site? [English] en
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10] 5
> What is your time zone? [Europe/Paris] America/Los_Angeles
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) N
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
> Do you want to upload your website using Rackspace Cloud Files? (y/N) N
> Do you want to upload your website using GitHub Pages? (y/N) N
Done. Your new project is available at C:\Users\student\Desktop\pelican-linode
```

When you complete the quickstart, Pelican will create a couple files in your main project folder. There should already be some files in the project folder that came from Github too.

```text
staticsite/
├── content/
├── output
├── tasks.py
├── LICENSE
├── Makefile
├── pelicanconf.py
├── publishconf.py
├── README.md
└── venv
```

### Write a post

Next, we'll write a blog post in markdown format. I prefer to write in markdown format (as compared to restructured text), because GitHub uses markdown and I have more familiarity with it. Use a code editor to create, write and save your file (I like [VS Code](https://linktovscode.html)). I created a file ```first_post.md``` in the ```staticsite/content/posts/``` directory. The directory structure after the file was created is below:

```text
staticsite/
├── content/
    └── posts/
        └── first_post.md
├── output
├── tasks.py
├── LICENSE
├── Makefile
├── pelicanconf.py
├── publishconf.py
├── README.md
└── venv
```

In the ```first_post.md``` file, include the text below:

```text
Title: My First Post
Date: 2020-04-24 10:20
Modified: 2020-04-24 19:30
Category: Python
Tags: pelican, publishing
Slug: my-first-post
Authors: My Name
Summary: Short version of the post for the main page

My super blog post content.

```

## Build the site locally

Save you first blog post and go back to the **Anaconda Prompt** or terminal. Run the command below to build the site. Make sure the ```(venv)``` virtual environment is activate when the command is entered.

```text
invoke build
```

### See the site

To see the site we just built, run the command below:

```text
invoke serve
```

Next up in deployment on Linode

## Deploy the static site on Lindoe

Linode's documentation about how to host a static site on their object storage platorm is below.

 > [https://www.linode.com/docs/platform/object-storage/host-static-site-object-storage/](https://www.linode.com/docs/platform/object-storage/host-static-site-object-storage/)

Object storage is Linode's version of Amazon S3 or Digital Ocean's Spaces. It's sort of just like having a thumb drive up in the cloud where your files are stored. We simply need to move our static site up to Linode's object storage and make sure our object storage settings are correct for other people to view our site.

### Install the s4cmd command line tool

I had trouble getting the s3cmd package to work with the Anaconda Prompt on Windows 10. For some reason the s3cmd executable in the ```venv\Scripts``` directory has to be specified exactly and ```s3cmd``` is not added to the **Anaconda Prompt** terminal path. 

```text
python -m pip install s3cmd
python venv\Scripts\s3cmd --version
```

### Create a new object storage bucket

This is equivalent to creating a new thumb drive or installing a new hard disk into your computer. Except we will create this place to store files up in Linode's cloud storage architecture.

```text
python venv\Scripts\s3cmd --configure
```
