Title: Adding an "assignments" directory to each user on a Jupyter Hub server
Date: 2018-06-03 12:40
Modified: 2018-06-03 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: assignments-dir-and-custom-login-page-to-jupyterhub
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 7
Summary: This is the seventh part of a multi-part series that shows how to set up Jupyter Hub for a college class. In this post, we will build a pre-spawn hook that will create an "assignments" directory which contains the assignments for the quarter for each **jupyterhub** user. We will also build a custom login pages that looks much more like our college login page and contains help links. 

This is the seventh part of a multi-part series that shows how to set up Jupyter Hub for a college class. In this post, we will build a pre-spawn hook that will create an "assignments" directory which contains the assignments for the quarter for each **jupyterhub** user. We will also build a custom login pages that looks much more like our college login page and contains help links. 

### Posts in this series

1. [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 
2. [Create ssh key, save to documents/ssh-keys]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md)
3. [Create a new Digital Ocean Droplet with a non-root sudo user]({filename}/posts/jupyterhub/new_DO_droplet.md)
4. [Install Jupyter Hub on the server]({filename}/posts/jupyterhub/installing_jupyterhub.md)
5. [Apply SSL, link a domain name to the server and configure nginx]({filename}/posts/jupyterhub/SSL_and_nginx_with_jupyterhub.md)
6. [Connect OAuth to Jupyter Hub]({filename}/posts/jupyterhub/authentication_and_jupyterhub_as_a_system_service.md)
7. **Pre-populate each new user's directory tree to include three notebook assignments** (this post)

### Last time

In the last post, we set **jupyterhub** to run as a system service in the background. Then we added tried two different login systems: github and google. The github authentication system allowed user logins using github usernames and passwords. The google authentication system allowed user loings using our college usernames and passwords. Then we modified the authentication system to use google user names and passwords even if the usernames contained a dot. 

### Steps in this post:

1. Create a repo on github.com with the assignments
2. Add a pre-spawn hook in jupyterhub_config.py
3. Modify the default login page

<br>

### 1. Create a repo on github.com with the assignments

On github.com, I created a new repo with the notes and assignments for the quarter. 

![new repo]()

![repo details]()

Clone the github repo locally and add notebooks that are the assignments for the quarter

```
$ mkdir ENGR101
$ cd ENGR101
$ git init
$ git clone https://github.com/ProfessorKazarinoff/ENGR101.git
$ git pull origin master
```

Locally, build the assignment for the quarter. I did this using jupyter notebooks locally. Then push the changes up to github

```
$ git add .
$ commit -m "added assignments"
$ git push origin master
```

### 2. Add a pre-spawn hook in jupyterhub_config.py

Now we can go to the server and have the notebooks we created and pushed up to github. We are going to use a Python package called **gitpython** to help with pulling the notebooks down from github.com to each of the users home directory when they log into **jupyterhub**. Log into the server and install **gitpython** using **conda**

```
$ sudo apt-get update
$ conda install -c conda-forge gitpython
```

Now we need to modify the jupyterhub_config.py file to do a couple things. We need to add a pre-spawn hook that gets called every time a user logs into jupyterhub.  This pre-spawn hook will run before the users jupyter notebook server is created. In the pre-spawn hook, we want to check to see if the user has the assignments already loaded. If the user doesn't have the assignments, then we want to pull the assignments down from github. The basic function we want to add is:

```
import git, os, shutil

DIR_NAME = "assignments"
REMOTE_URL = "https://github.com/ProfessorKazarinoff/ENGR101.git"
 
if os.path.isdir(DIR_NAME):
    shutil.rmtree(DIR_NAME)
 
os.mkdir(DIR_NAME)
 
repo = git.Repo.init(DIR_NAME)
origin = repo.create_remote('origin',REMOTE_URL)
origin.fetch()
origin.pull(origin.refs[0].remote_head)
```

In our jupyterjub_config.py file we build a pre-spawn hook function that will run when the spawner starts:

make sure the following imports are present:

```
import git, os, shutil
```

The pre-spawn hook function

```
def create_dir_hook(spawner)
    username = spawner.user.name
    DIR_NAME = os.path.join("/home","username","assignments")
    REMOTE_URL = "https://github.com/ProfessorKazarinoff/ENGR101.git"
    if not os.path.isdir(DIR_NAME):
        os.mkdir(DIR_NAME)
        repo = git.Repo.init(DIR_NAME)
        origin = repo.create_remote('origin',REMOTE_URL)
        origin.fetch()
        origin.pull(origin.refs[0].remote_head)
```

Then we need to add a pre-spawn hook function to the spawner in the form of

```
c.Spawner.pre_spawn_hook = create_dir_hook
```

<br>

### 3. Modify the default login page

The jupyterhub login page looks like this:

But our college login page looks liek this:

For users to feel comfortable with login into the server, we'll make the jupyterhub login page look more like the college login page.

<br>

### Summary
In this post, we will build a pre-spawn hook that will create an "assignments" directory which contains the assignments for the quarter for each **jupyterhub** user. We will also build a custom login pages that looks much more like our college login page and contains help links.  

<br>

### Conclusion
This concludes the Jupyter Hub series. We accomplished a lot to get a working version of jupyterhub running on a Digital Ocean server that has the following features.
