Title: Python Virtual Environments (virtualenv's) in OS X, Linux and Windows 10)
Date: 2017-12-06 19:36
Modified: 2017-12-06 19:50
Status: draft
Category: Orientation
Tags: python, Windows 10, virtualenv, OS X, Linux, Ubuntu, pip, conda, virtualenv, anaconda, anaconda prompt
Slug: virtualenv-in-osx-linux-windows
Authors: Peter D. Kazarinoff
Summary:


I use three different operating systems on three different computers:

Work: Windows 10 (no admin access)
Home Office: Ubuntu 16.04 LTS
Laptop: Mac OS X

Setting up a Python virtual environment is different on each one of these operating systems. Let's see at what happens when we try and create a new virtual environment in each.

### Ubuntu 16.04
Linux should be the easiest to get a new virtualenv up and running. In Ubuntu 16.04, we have a terminal, admin access (can use sudo). But look what happens when I try to set up a new virtualenv without any flags or customization:

```
$ mkvirtualenv webscrape
$ (webscrape) which pyton
$ 2.7.1 
```

So the default installation is going to legacy Python!? I don't want the legacy 2.7 version, I want at least Python 3.2 and would prefer Python 3.6. Let's delete that legacy Python environment. Make sure the virtual environment is ```deactivate```d first.

```
(webscrape) deactivate
rmvirtualenv webscrape
```

Let's try to specify python3 with the ```-p python3``` flag

```
$ mkvirtualenv -p python3 webscrape
$ error
```

Now what? Path is too long? How is that possible? What happens when we see which Python version is the default python3?

```
which python3
bin/usr/anaconda/python3
```

So that's what we need to use when the ```viruatlenv``` is created. The ```--python='which python3'``` flag will point virtualenvwrapper to the correct python version. The new virtualenv is initiated with the full file path to our new environment ```~/.virtualenvs/webscrape```

```
$ mkvirtualenv --python='which python3' ~/.virtualenvs/webscrape
(webscrape)$ python
Python 3.6.2
```

Nice. Now we can ```pip install``` away. So what about on a MacBook Air with OSX?

### Mac OSX
Mac OSX has a terminal too. I get to it by going to the finder and clicking the search in the upper right or using . Type in terminal. Setting up a virtualenv should be pretty easy right?

```
$ mkvirtualenv webscrape
(webscrape)$ which python
python 2.7
```

Again!? More legacy Python?! Stop it already with the legacy Python. We want Python! Preferably 3.6. Gotta make sure that Python 3 is installed some where. ```rmvirtualenv``` that thing.

```
(webscrape)$ deactivate
$ rmvirtualenv webscrape
$ which python3
$ usr/bin/python
$ virtualenv -p python3 webscrape
(webscrape)$ python
python 3.6.2
```

OK. Two down and one to go. Is this any easier on Windows 10? Especially with no admin access? Can't be right? Let's see.

### Windows 10 (no admin access)

At work, I have a windows 10 machine with no admin access. I can't install any programs my work computer. The Python distribution that has worked out the best has been **Anaconda**. Besides coming with Python 3, having a bunch of packages already installed, it also comes with a command line client call the **Anaconda Prompt***. The **Anaconda Prompt** operates a little like the terminal on Linux and OSX, but some of the commands are a little different. To make a new virtual environment from the **Anaconda Prompt** type:

```
$ conda create -n webscrape python=3.6
$ proceed ([y]/n)?
(webscrape)$ which python
python 3.6
```

Rockin' right? Turns out that the Windows 10 virtual env was one of the easiest. Who would have guessed that? That's one piece of magic from the **Anaconda** distribution. If you are using Windows, I think **Anaconda** is the way to go.

End Note:

Maybe it's best to use **conda** on both OSX and Linux too...  You don't have to mess around with **_~/.bash_profile_** or pointing virtualenv wrapper to the proper directory.  
