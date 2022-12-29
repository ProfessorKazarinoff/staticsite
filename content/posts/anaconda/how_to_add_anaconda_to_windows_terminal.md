Title: How to add Anaconda to the Windows Terminal
Date: 2022-12-29 08:11
Modified: 2022-12-29 08:11
Status: draft
Category: tools
Tags: ssh, anaconda, github
Slug: how-to-add-anaconda-to-windows-terminal
Authors: Peter D. Kazarinoff
Summary: [![Top 5 Python Tools]({static}/posts/top_five/images/five_tools_logos_composition.png)]({filename}/posts/top_five/top_five_python_tools.md) In this post, you'll learn how to add Anaconda to the Windows terminal. I prefer using the new Windows Terminal, compared to using the old Windows Command Prompt. This post shows how to create an Anaconda profile in your Windows Terminal and set the Anaconda profile as the default.

[![Top 5 Python Tools]({static}/posts/top_five/images/five_tools_logos_composition.png)]({filename}/posts/top_five/top_five_python_tools.md) I prefer using the new Windows Terminal, compared to using the old Windows Command Prompt. This post shows how to create an Anaconda profile in your Windows Terminal and set the Anaconda profile as the default.

## Prerequisits

1. A Windows computer
2. The Anaconda distribution of Python
3. Windows Terminal Installed

## Why create an Anaconda profile in Windows Terminal

![anaconda logo]({static}/posts/top_five/images/anaconda_logo.png)

An SSH Key is ...

Anaconda comes with the most commonly used Python packages for Engineers and scientists. Anaconda includes the Anaconda Prompt and the **conda** command-line tool. If you want a smaller install (Anaconda is a pretty big download), you can download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) instead. Miniconda comes with just the Anaconda Prompt, the conda package manager, and a base Python environment, but no pre-installed packages. 

## How to create an Anaconda profile in Windows Terminal

[![Jupyter notebook screenshot]({static}/posts/top_five/images/jupyter_logo.png)](https://jupyter.org/)

Open the Anaconda Prompt from the Windows start menu. In the Anaconda Prompt, type the command below:

```text
ssh-keygen -t ed25519 -C "your_email@example.com"
```

[![Jupyter notebook screenshot]({static}/posts/top_five/images/jupyter_notebook_screenshot.png)](https://jupyter.org/)

This will create a new SSH key in your .ssh directory. 

## Summary

This post showed how to create an Anaconda Profile in the Windows Terminal. Now when you open Windows Terminal, the Anaconda Profile opens by default. This means that the Windows Terminal now effectivly acts like the Anaconda Prompt, but with all the Windows Terminal goodness included.

## Support

Interested in using the Anaconda Distribution of Python? Check out my book:
