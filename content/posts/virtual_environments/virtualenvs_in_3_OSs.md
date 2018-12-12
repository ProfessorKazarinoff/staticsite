Title: Python Virtual Environments in OS X, Linux and Windows 10
Date: 2017-12-22 14:36
Modified: 2017-12-22 14:36
Status: published
Category: Orientation
Tags: python, Windows 10, virtualenv, OSX, Linux, Ubuntu, pip, conda, virtualenv, anaconda, anaconda prompt
Slug: virtualenv-in-osx-linux-windows
Authors: Peter D. Kazarinoff
Summary: In this post, I'll review creating virtual environments on three different operating systems: Windows 10, Linux and Mac OSX. Using virtual environments is good programming practice when using Python. A virtual environment will separate the Python interpreter and installed modules from the main Python installation.

In this post, I'll review creating virtual environments on three different operating systems: Windows 10, Linux and Mac OSX. Using virtual environments is good programming practice when using Python. A virtual environment will separate the Python interpreter and installed modules from the main Python installation.

I use three different operating systems on three different computers:

* Work: Windows 10 (no admin access)
* Home Office: Ubuntu 16.04 LTS
* Laptop: Mac OSX

Setting up a Python virtual environment is different on each one of these operating systems. Let's see at what happens when we try and create a new virtual environment in each.

### Ubuntu 16.04
Linux should be the easiest to get a new virtualenv up and running. In Ubuntu 16.04, I have a terminal and admin access (can use sudo). But look what happens when I try to set up a new virtualenv without any flags or customization:

```bash
$ mkvirtualenv webscrape
$ source activate webscrape
(webscrape)$ which python
$ 2.7.1 
```

The default installation is legacy Python!? I don't want the legacy 2.7 version, I want at least Python 3.2 and would prefer Python 3.6. Let's delete that legacy Python environment. Make sure the virtual environment is ```deactivate```d first.

```bash
(webscrape)$ source deactivate
$ rmvirtualenv webscrape
```

Let's try to specify Python 3 with the ```-p python3``` flag

```bash
$ mkvirtualenv -p python3 webscrape
$ error
```

Now what? Path is too long? How is that possible? What happens when we see which Python version is the default python3?

```bash
$ which python3
$ bin/usr/anaconda/python3
```

So that's the flag we need to use when the ```viruatlenv``` is created. The ```--python='which python3'``` flag will point **virtualenvwrapper** to the correct Python version. The new virtualenv is initiated with the full file path to our new environment ```~/.virtualenvs/webscrape```

```bash
$ mkvirtualenv --python='which python3' ~/.virtualenvs/webscrape
(webscrape)$ python
Python 3.6.2
```

Nice. Now we can ```pip install``` away. So what about creating a new virtual environment on a MacBook Air with OSX?

### Mac OSX
Mac OSX has a terminal too. I get to it by going to the finder and clicking the search in the upper right or using [command] + [space] to bring up the spotlight search bar. Type ```terminal``` into the search bar. Setting up a virtualenv should be pretty easy right?

```bash
$ mkvirtualenv webscrape
$ source activate webscrape
(webscrape)$ which python
python 2.7
```

Again!? More legacy Python?! Stop it already with the legacy Python. We want Python! Preferably 3.6. Gotta make sure that Python 3 is installed some where. ```rmvirtualenv``` that thing.

```bash
(webscrape)$ source deactivate
$ rmvirtualenv webscrape
$ which python3
$ usr/bin/python
$ virtualenv -p python3 webscrape
$ source activate webscrape
(webscrape)$ python
python 3.6.2
```

OK. Two down and one to go. Is this any easier on Windows 10? Especially with no admin access? Can't be right? Let's see.

### Windows 10 (no admin access)

I have a Windows 10 machine at work with no admin access. I can't install any programs on my work computer that use the Windows active directory (which is most programs). The Python distribution that has worked out the best has been **Anaconda**. Besides coming with Python 3, and having a bunch of packages already installed, it also comes with a command line client call the **Anaconda Prompt**. The **Anaconda Prompt** operates a little like the terminal on Linux and Mac OSX, but some of the commands are a little different. To make a new virtual environment from the **Anaconda Prompt** type:

```
$ conda create -n webscrape python=3.6
$ proceed ([y]/n)?
$ conda activate webscrape
(webscrape)$ python --version
python 3.6.3 :: Anaconda, Inc.
```

Rockin' right? Turns out that the Windows 10 virtual environment was one of the easiest to set up. Who would have guessed that? That's one piece of magic from the **Anaconda** distribution. If you are using Windows, I think **Anaconda** is the way to go.

</br>
</br>

End Note:

Maybe it's best to use **conda** on both OSX and Linux too...  You don't have to mess around with **_~/.bash_profile_** or pointing virtualenv wrapper to the proper directory.