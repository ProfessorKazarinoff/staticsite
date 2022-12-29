Title: How to create an SSH key on Windows
Date: 2022-12-29 08:11
Modified: 2022-12-29 08:11
Status: draft
Category: tools
Tags: ssh, anaconda, github
Slug: how-to-create-an-ssh-key-on-windows
Authors: Peter D. Kazarinoff
Summary: [![Top 5 Python Tools]({static}/posts/top_five/images/five_tools_logos_composition.png)]({filename}/posts/top_five/top_five_python_tools.md) In this quick post, you'll learn how to add an SSH key on Windows. SSH keys are useful when you are working with GitHub.com. An SSH key is also useful when working with virtual machines using programs like PuTTY and FileZilla.

[![Top 5 Python Tools]({static}/posts/top_five/images/five_tools_logos_composition.png)]({filename}/posts/top_five/top_five_python_tools.md) This post contains my top 5 Python tools. These 5 tools are the ones I use the most and recommend for Python programmers. These tools help me write, run and revise code and they make me a more productive programmer.

## Prerequisits

1. A Windows computer
2. The Anaconda distribution of Python

## What is an SSH Key

![anaconda logo]({static}/posts/top_five/images/anaconda_logo.png)

An SSH Key is ...

Anaconda comes with the most commonly used Python packages for Engineers and scientists. Anaconda includes the Anaconda Prompt and the **conda** command-line tool. If you want a smaller install (Anaconda is a pretty big download), you can download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) instead. Miniconda comes with just the Anaconda Prompt, the conda package manager, and a base Python environment, but no pre-installed packages. 

## How to create a new SSH key

[![Jupyter notebook screenshot]({static}/posts/top_five/images/jupyter_logo.png)](https://jupyter.org/)

Open the Anaconda Prompt from the Windows start menu. In the Anaconda Prompt, type the command below:

```text
ssh-keygen -t ed25519 -C "your_email@example.com"
```

[![Jupyter notebook screenshot]({static}/posts/top_five/images/jupyter_notebook_screenshot.png)](https://jupyter.org/)

This will create a new SSH key in your .ssh directory. 

## Summary

This quick post showed how to create a new SSH key on Windows using the Anaconda distribution of Windows and the Anaconda prompt.

## Support

SSH keys are great to use with GitHub.com. If you use GitHub.com and find this post helpful, consider becoming one of my GitHub sponsors.
