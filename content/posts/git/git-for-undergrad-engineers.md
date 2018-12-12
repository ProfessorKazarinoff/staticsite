Title: Git and GitHub for Undergrad Engineers
Date: 2018-10-30 12:40
Modified: 2018-10-30 12:40
Status: draft
Category: git
Tags: git, python, version control
Slug: git-for-undergrad-engineers
Authors: Peter D. Kazarinoff
Summary: This post is for first-time users of git. Git is command-line version control system that allows programers to manage file versions and share code. Git can be tricky to use. This post contains solutions to some of the most common use cases.

## What is git?

## How do I install **git**?

Git is installed with the Anaconda distribution of Python. Once Anaconda is installed, you can run git from the Anaconda Prompt.

## What is GitHub?

## How do I copy the contents of a repo on GitHub?

A common task is to copy a repo from GitHub.com onto your local computer. Go to this link on Github: 

 > https://github.com/ProfessorKazarinoff/piston_motion

You will see the Piston Motion repo. The repo contains a couple of files:

 * LICENSE
 * README.md
 * piston_motion.md
 * piston_motion.mp4
 * piston_motion.py

You could click on ```piston_motion.py``` and copy all of the code into a new file and then save the file. Then click on ```README.md``` and copy all of the code into a new file and then save the file. Then click on ```piston_motion.md``` and copy all the code into a new file and then save the file.... 

But an easier way to accomplish the same thing is to use the ```git clone``` command.

```text
git clone https://github.com/ProfessorKazarinoff/piston_motion
```

## What is .gitignore and why do I need it?

## How do I synch a repo on GitHub with a folder on my laptop?

## How do I update the folder on my laptop with the contents stored on GitHub?

## How do I save the contents of a folder on my laptop to GitHub?

## What if git push doesn't work?