Title: Adding an "assignments" directory to each user on a Jupyter Hub server
Date: 2018-06-12 12:40
Modified: 2018-06-12 12:40
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
7. **Pre-populate each new user's directory tree to include an assignments directorry and build a custom login page** (this post)

### Last time

In the last post, we set **jupyterhub** to run as a system service in the background. Then we added tried two different login systems: github and google. The github authentication system allowed user logins using github usernames and passwords. The google authentication system allowed user logins using our college usernames and passwords. Then we modified the authentication system to use google user names and passwords even if the usernames contained a dot. 

### Steps in this post:

1. Create a repo on github.com with the assignments and notes
2. Add a pre-spawn hook in jupyterhub_config.py
3. Modify the default login page

<br>

### 1. Create a repo on github.com with the assignments

On github.com, I created a new repo with the notes and assignments for the quarter. 

![new repo]()

![repo details]()

On a local computer, note the server, clone the github repo and add notebooks that are the assignments for the quarter.

```
$ mkdir ENGR101
$ cd ENGR101
$ git init
$ git remote add origin https://github.com/ProfessorKazarinoff/ENGR101.git
$ git pull origin master
```

On the local computer, not the server, build the assignment for the quarter. I did this using jupyter notebooks. Then push the changes up to github.

```
$ git add .
$ commit -m "added assignments"
$ git push origin master
```

### 2. Add a pre-spawn hook in jupyterhub_config.py

Now we can go to the server and have the notebooks we created (and pushed up to github) pre-populate each users directory tree. We are going to use a Python package called **gitpython** to help with pulling the notebooks down from github.com to each of the users directory tree when they log into **jupyterhub**. Log into the server and install **gitpython** using **conda**:

```
# on the server
$ sudo apt-get update
$ conda install -c conda-forge gitpython
```

Now we need to modify the jupyterhub_config.py file to do a couple things. We need to add a pre-spawn hook that gets called every time a user logs into jupyterhub.  This pre-spawn hook will run before the user's jupyter notebook server is created. In the pre-spawn hook, we want to check to see if the user has the assignments already loaded. If the user doesn't have the assignments, then we want to pull the assignments down from github. 

So first we need a function that will pull the repo down from github. Note the line ```uid = getpwnam(user).pw_uid``` and ```gid = getpwnam(user).pw_gid```. These lines of code get the user's numerical user id and group id. We need these so that we can assign the proper permissions to the files we pull down from github. When I first built the function, changing file permissions was note included. I could log onto jupterhub and see the notebooks, but I couldn't run or edit them. The problem was that the notebooks were pulled down from github by a sudo user and the jupyterhub user didn't have the permissions to write or execute any of the files. Building in the permissions to the function with ```shutil.chown``` solved the problem. 

```
def clone_repo(user, git_url, repo_dir):
    """
    A function to clone a github repo into a specific directory of a user.
    """
    Repo.clone_from(git_url, repo_dir)
    uid = getpwnam(user).pw_uid
    gid = getpwnam(user).pw_gid
    for root, dirs, files in os.walk(repo_dir):
        for d in dirs:
            shutil.chown(os.path.join(root, d), user=uid, group=gid)
        for f in files:
            shutil.chown(os.path.join(root, f), user=uid, group=gid)
```

Now we'll build a pre-spawn hook function that will run when the spawner starts. The function will call the ```clone_repo()``` function and pull down the assignments from the github repo the first time a user logs into jupyterhub.  After the assignments are initially created, each subsequent time the user logs into jupyterhub a new fresh set of assignments are pulled down if ```ERASE_DIR``` is set to ```True```. If ```ERASE_DIR``` is set to false, once the assignments are downloaded, they will not be over-written.  

To run the pre-spawn hook function and the pull repo function, we need to make sure the following imports are present in our jupyterhub_config.py file:

```
import git, os, shutil
```

The complete pre-spawn hook function is below:

```
def create_dir_hook(spawner):
    """
    A function to clone a github repo into a specific directory of a 
   jupyterhub user when the server spawns a new notebook instance.
    """
    username = spawner.user.name
    DIR_NAME = os.path.join("/home", username)
    git_url = "https://github.com/ProfessorKazarinoff/ENGR101.git"
    repo_dir = os.path.join(DIR_NAME, 'notebooks')

    if ERASE_DIR == True:
        if os.path.isdir(repo_dir):
            shutil.rmtree(repo_dir)
        os.mkdir(repo_dir)
        clone_repo(username, git_url, repo_dir)

    if ERASE_DIR == False and not (os.path.isdir(repo_dir)):
        os.mkdir(repo_dir)
        clone_repo(username, git_url, repo_dir)

    if ERASE_DIR == False and os.path.isdir(repo_dir):
        pass
```

The two functions need to be pasted into the jupyterhub_config.py file. Make sure the imports are present as well as an ```ERASE_DIR = True``` or ```ERASE_DIR = False``` line.

Next we need to add a pre-spawn hook function to the spawner in the form of

```
c.Spawner.pre_spawn_hook = create_dir_hook
```

With these changes made, we can restart jupyterhub using:

```
$ sudo systemctl stop jupyterhub
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
```

TO exit the status screen use [Ctrl] + [c]

<br>

### 3. Modify the default login page

The jupyterhub login page looks like this:

But our college login page looks lik this:

For users to feel comfortable with login into the server, we'll make the jupyterhub login page look more like the college login page.

<br>

This was a time consuming and fussy task. It involved messing around a lot with css and html.

First a set of custom jinja templates need to be created. 

Next the jupyterhub_config.py file needs to be modified so that the set of custom jinja tempates are used instead of the default jinja templates.

Finally the style.min.css file needs to be modified so that the login page styling looks a little more like the college login page.

Let's see how it looks. With the changes complete, we can restart jupyterhub using:

```
$ sudo systemctl stop jupyterhub
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
```

![login page image](login page image)

### Summary
In this post, we will build a pre-spawn hook that will create an "assignments" directory which contains the assignments for the quarter for each **jupyterhub** user. We will also build a custom login pages that looks much more like our college login page and contains help links.  

<br>

### Conclusion
This concludes the Jupyter Hub series. We accomplished a lot to get a working version of jupyterhub running on a Digital Ocean server that has the following features.

 * Users don't need to install anything to use python. They just need a web browser and an internet connect.
 * A custom domain is hooked to jupyterhub instead of just an IP address
 * jupyterhub runs on https and has SSL security
 * users can log into jupyterhub using their college usernames and passwords
 * users directory trees are prepopulated with assignments
 * all users have the same set of installed packages and don't need to install any extra
 * pre-populated assignments can be run and modified by users.