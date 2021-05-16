Title: Git and GitHub for Undergrad Engineers
Date: 2021-05-15 12:40
Modified: 2021-05-15 12:40
Status: published
Category: git
Tags: git, python, version control
Slug: git-and-github-for-undergrad-engineers
Authors: Peter D. Kazarinoff

[![Git and GitHub Logo]({static}/posts/git/images/git_and_github_logo.png)]({filename}/posts/git/git-for-undergrad-engineers.md)

This post is for first-time users of git. Git is a command-line version control system that allows programmers and engineers to manage file versions and share code. Git can be tricky to use. This post contains solutions to some of the most common problems you may encounter when using Git.

## What is **git**?

![git scm window]({static}/posts/git/images/git_scm_window.jpg)

**Git** is one of the standard _version-control_ systems used by programmers to save code and work on code collaboratively as a team. **Git** is a program run on the command line or **Anaconda Prompt**. If you use Windows, you can download the **gitbash** program at [git-scm.com/downloads](https://git-scm.com/downloads). **gitbash** on Windows allows you to use the same git commands as MacOS and Linux users. **Git** was created by Linus Torvalds, who also designed the Linux operating system.

## How do I install **git**?

Git is installed with the Anaconda distribution of Python. Once Anaconda is installed [Anaconda.com/downloads](https://anaconda.com/downloads), you can run git from the Anaconda Prompt. Git can also be run on Windows using the **gitbash** program. Gitbash can be downloaded from [git-scm.com/downloads](https://git-scm.com/downloads).

![git scm window]({static}/posts/git/images/git_scm_download_page.jpg)

## What is GitHub?

![GitHub Profile Page]({static}/posts/git/images/github_profile_page.png)

[GitHub.com](https://github.com/) (now owned by Microsoft) is a website and service used by programmers and open source projects to share code and allow contributors to propose changes to existing code. GitHub is free if you are willing to share your code publicly. 

## git and GitHub terminology

![GitHub Profile Page]({static}/posts/git/images/dictionary_icon.png)

Before using **git** and GitHub.com, it is helpful to understand a couple of terms:

 * **git** - a command-line program used to track file changes and collaborate on code with others.
 * **Command Line** a programming terminal where commands are entered as text. 
 * **repo** - short name for "repository". A repo is a directory and its contents that **git** knows about.
 * **local repo** -  a directory and its contents on your computer that **git** knows about. Local repos are folders and the contents in those folders.
 * **remote repo** - a directory and its contents stored in the cloud that **git** knows about. GitHub.com is a site where remote repos are stored.
 
## Common git commands
 
A selection of useful **git** commands are summarized below:

 * ```git clone https://github.com/user/repo.git``` copy a remote repo from GitHub.com into a local directory
 
 * ```git init``` create a new local repo in the current folder
 
 * ```git remote add origin https://github.com/user/repo.git``` link a local repo to a remote repo on GitHub.com
 
 * ```git add .``` add all files and changes to the local repo
 
 * ```git commit -m "commit message"``` commit the changes in the local repo with the message ```"commit message"```
 
 * ```git push origin main``` push local changes up to the remote repo*
 
 * ```git pull origin main``` pull down the version in the remote repo into the local repo*

 > GitHub, as part of their move to use more inclusive language, re-named the default branch to **main** for any new repo. You can read about the change [here](https://www.theserverside.com/feature/Why-GitHub-renamed-its-master-branch-to-main)

## How do I copy the contents of a repo on GitHub?

A common task is to accomplish with git is to copy a repo from GitHub.com onto your local computer. In this example, we are going to copy all the files in the ```piston_motion``` repo on GitHub.com onto our local computer.
 
 Go to this link on Github: 

 > https://github.com/ProfessorKazarinoff/piston_motion

You see the Piston Motion repo on GitHub.com. The Piston Motion repo contains a couple of files:

 * LICENSE
 * README.md
 * piston_motion.md
 * piston_motion.mp4
 * piston_motion.py

If you want to use the code in Piston Motion remote repo stored on GitHub.com, you can click on ```piston_motion.py``` and copy all of the code into a new file and then save the file. You could also click on ```README.md``` and copy all of the code into a new file and then save the file. Then click on ```piston_motion.md``` and copy all the code into a new file and then save the file... That is a lot of copying and pasting. Kind of a pain.

An easier way to accomplish the same task is to use the ```git clone``` command. Open the Anaconda Prompt, or **gitbash** and type the following command, then press [Enter].

```text
git clone https://github.com/ProfessorKazarinoff/piston_motion
```

This command copies the repo named ```piston_motion``` to your local computer. Now you have a new ```piston_motion``` folder on your computer. If you open the ```piston_motion``` folder in a file browser, you will see the following files.

```text
piston_motion/
├── LICENSE
├── README.md
├── piston_motion.md
├── piston_motion.mp4
└── piston_motion.py
```

## How do I clone a repo into a specific folder?

What if you want all the code from the ```piston_motion``` repo, but you don't want that code to end up in a folder called ```piston_motion```? Running ```git clone``` creates a new folder with the repo contents inside it. ```git clone``` does not copy the contents of the repo into the current folder (it creates a new folder that contains the repo contents). But, you can make the folder that the repo contents get copied into any name you want. Say you want to copy the ```piston_motion``` repo into a folder called ```github_examples```. 

The command below copies the contents of the ```piston_motion``` repo on GitHub.com into a folder on your local computer called ```github_examples```.

```text
git clone https://github.com/ProfessorKazarinoff/piston_motion.git github_examples
```

If you open the folder ```github_examples```, you see the same code you downloaded into the ```piston_motion``` folder.

```text
github_examples/
├── LICENSE
├── README.md
├── piston_motion.md
├── piston_motion.mp4
└── piston_motion.py
```

## Creating and synching a remote repo on GitHub.com with a local repo

Another common task to complete with **git** is to synch a remote repo on GitHub.com with a local repo on your local computer. This is useful when you want to keep the files in a particular project synced across multiple computers. Synched remote and local repos are also useful for a group of problem solvers working on the same project. Each team member has access to the same remote repo on GitHub.com and each team member has the same local repo on their computer.

#### Create a remote repo on GitHub.com

First, go to [GitHub.com/join](https://github.com/join) and create a new account. Log in and create a new repo. It is a good idea to include a license and a **_.gitignore_** file. For a Python project, the **_.gitignore_** file for Python is a good start. Two common licenses for open source projects (projects you are willing to share with others) are the _GNU General Public License v3.0_ and the _MIT License_.

#### Make a new local repo and link the local repo to the remote repo on GitHub.com

Second, create a local directory and ```cd``` into it. Initialize a git repo locally in that directory. Then sync the local folder with the remote repo on GitHub.com.

```text
$ mkdir newproject
$ cd newproject
$ git init
$ git remote add origin https://github.com/user/repo.git
$ git checkout main
$ git pull origin main
```

#### Add, commit and push changes up to Github.com

Third, work on the project locally. For example, you could edit one of the files in the directory ```newproject``` or create a new file in the directory ```newproject```.

Finally, save your work and commit the changes you made with **git**. Push those changes up to the remote repo on GitHub.com

```text
$ git add .
$ git commit -m "commit message"
$ git push origin main
```

#### Pull the most recent version from GitHub.com before each work session

If using **git** and GitHub.com, remember to pull the most recent version of the repo down from GitHub.com before you make any changes locally. If changes are made locally before the version of the repo on GitHub.com is synched, the local repo and remote repo will be out of synch.

```text
$ git pull origin main
```

After local changes are made, save the changes and push them to GitHub.com

```text
$ git add .
$ git commit -m "commit message"
$ git push origin main
```

## What is .gitignore and why do I need it?

The ```.gitignore``` file contains a list of files and folders that git will "ignore". This means the files and folders specified in the ```.gitignore``` files will not be copied up to GitHub.com. This is useful for a couple of reasons. One reason is that Python creates some files automatically when a program runs. These files don't need to be saved as part of the GitHub.com repo. Another reason to add a fit to the ```.gitignore``` file is that you might have files in your local git repo that you don't want to share publicly. A file that contains usernames, passwords, or API keys should never be stored on GitHub.com. You can add a file that contains private information to ```.gitignore``` then the file won't be saved up on GitHub where anyone on the internet can see it.

## Support

Thanks for reading! If you want to support the open source work I do (like this blog), consider becoming one of my GitHub sponsors:

<iframe src="https://github.com/sponsors/ProfessorKazarinoff/button" title="Sponsor ProfessorKazarinoff" height="35" width="116" style="border: 0;"></iframe>
