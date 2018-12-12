Title: Automating Black with Pre-Commit
Date: 2018-12-06 14:36
Modified: 2018-12-06 14:36
Status: draft
Category: git
Tags: git, version control, pre-commit, automation
Slug: automating-black-with-pre-commit
Authors: Peter D. Kazarinoff
Summary: In this post, I'll show you how I automated code cleanup with a package called [Black](https://github.com/ambv/black) and another package called [pre-commit](https://pre-commit.com/#intro). Black automatically reformats code for you, and pre-commit automatically runs black for you. It's a great combination! Every time I commit code with git, pre-commit runs black and cleans up the code for me. 

In this post, I'll show you how I automated code cleanup with a package called [Black](https://github.com/ambv/black) and another package called [pre-commit](https://pre-commit.com/#intro). Black automatically reformats code for you, and pre-commit automatically runs black for you. It's a great combination! Every time I commit code with git, pre-commit runs black and cleans up the code for me.

The packages and tools used in this post are:

* **git** - a version control system run form the command line. **git** is used to push code up to GitHub (and other cloud-based code repositories) so that the code is consistant across different computers. 
* **Black** - a Python package that re-formats code. It is sort of like a code linter, but **Black** actually modifies code, not just checks code. I love it.
* **pre-commit** - a Python package that helps with _pre-commit hooks_. Pre-commit hooks are scripts that run, checks that are made, or processes completed before a commit is made. We can have **pre-commit** make a pre-commit hook that runs **Black** every time we commit code.

Setting up **Black** to run automatically with **pre-commit** is pretty easy. There are only a couple of steps:

[TOC]

### Install pre-commit

Activate whichever virtual environment is used for the project. In this example I have a project called notebook-conversion in the ```notebook-conversion``` directory. My virtual environment for the project is called ```(convenv)```. I use **conda** to create and manage virtual environments. Activate the virtual environment and install pre-commit.

```text
$ cd notebook-conversion
$ pwd
~/notebook-conversion
$ conda activate convenv
(convenv)$ pip install pre-commit
```

### Add pre-commit to requirements-dev.txt

Now that pre-commit is installed, we'll create a ```requirements-dev.txt``` file that contains the package we just installed. 

```text
(convenv)$ pip freeze requirements-dev.txt
```

### Create a ```.pre-commit-config.yaml``` file

Next we need to create a file called ```.pre-commit-config.yaml``` in our main project directory. Inside this file, we'll include the configuration to run **Black** every time we run ```git commit -m "commit message"``` on our code. 

Copy the contents to below into ```.pre-commit-config.yaml```:

```text
repos:
 - repo: https://github.com/ambv/black
   rev: stable
   hooks:
    - id: black
      language_version: python3.6
```

### Run ```pre-commit install``` to install the hook with git

Once the pre-commit configuration file is complete, the next step is to run ```pre-commit install``` to install the a pre-commit hook inside our .git directory.

```text
(convenv)$ pre-commit install
```

### Commit a change and watch **pre-commit** and **Black** work their magic

Finally, let's make a commit with **git** and see **Black** run and change our code.

```text
(convenv)$ git add .
(convenv)$ git commit -m "added .pre-commit-config.yaml"

black....................................................................Passed
[master aec9dd2] added .pre-commit-config.yaml
 2 files changed, 32 insertions(+), 22 deletions(-)

```

### Summary

In this post we automated running the code cleanup tool **Black** using **pre-commit**. We installed **pre-commit** with pip. Then we created a ```.pre-commit-config.yaml``` file that contained information on how to run **Black**. Next, we installed the pre-commit hook into our .git folder. Finally, we ran ```git commit``` and watched our code get cleaned up by **Black** automatically. 