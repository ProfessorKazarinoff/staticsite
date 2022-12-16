Title: Opening a Jupyter Notebook on Windows
Date: 2022-12-16 09:20
Modified: 2022-12-16 09:21
Status: draft
Category: jupyter
Tags: jupyter, python, anaconda, windows, jupyter notebook
Slug: how-to-double-click-to-open-a-jupyter-notebook
Authors: Peter D. Kazarinoff
Summary: In this post, we will run through how you can double-click a Jupyter notebook to open it.  **Jupyter notebooks** are one way engineers can write and execute **Python** code. But when you double click a Jupyter notebook on your computer, it probably doesn't open right. Learn how to open Jupyter notebooks by double clicking using the steps in this post.

This is a set of optional steps to open ```.ipynb``` files by double clicking them. This set of steps may introduce other problems on your system, but the process is reversible. This only works on Windows using the Anaconda distribution of Python.

## Prerequisits

In order to double click to open Jupyter notebooks using the steps below you need to:

 * Use a Windows computer
 * Install the Anaconda Distribution of Python

## There are three general steps:

1. Find and copy the location of Anaconda on your computer

2. Create a .bat file with some custom commands in it

3. Set the .bat file as the "program" to use when opening .ipynb files.

Details for each step is below:

### 1. Find and copy the location of Anaconda on your computer

The first thing to do in order to double click to open ```.ipynb``` files is to find the location of Anaconda on your computer.

Open the Anaconda Prompt using the Windows Start Menu. In the Anaconda prompt type:

```text
conda info
```

![anaconda prompt conda info]({static}/posts/jupyter/images/conda-info.png)

Look for the entry:

```text
active env location : C:\Users\peter.kazarinoff\AppData\Local\Continuum\Anaconda3
```

![anaconda prompt see active env location]({static}/posts/jupyter/images/active-env-location.png)

Your active env location may be different. Copy the active env location (from the ```C:\ to the \Anaconda3```)

### 2. Create a .bat file with some custom commands in it

Create a new text file. I recommend creating the file in the Documents folder inside a folder called ```open_ipynb_files```.

![anaconda prompt see active env location]({static}/posts/jupyter/images/make-new-text-file.png)

Inside the text file, copy the commands below. On the second line, replace the path after set ANACONDAPATH= to the file path you copied in step 1 which is location of Anaconda on your computer.

```text
@echo off
set ANACONDAPATH=C:\Users\Peter\Anaconda3
%ANACONDAPATH%\python.exe %ANACONDAPATH%\cwp.py %ANACONDAPATH%^ %ANACONDAPATH%\python.exe %ANACONDAPATH%\Scripts\jupyter-notebook-script.py %1
```

![anaconda prompt see active env location]({static}/posts/jupyter/images/dot-bat-file-text.png)

Save the text file as ```open_ipynb_files.bat```   It's important that the file ends in the ```.bat``` file extension.

![anaconda prompt see active env location]({static}/posts/jupyter/images/accept-name-change.png)

### 3. Set the .bat file as the "program" to use when opening ```.ipynb``` files.

Open a Windows file explorer window and navigate to a folder that contains an ```.ipynb file```. It doesn't matter what's in the ```.ipynb``` file. Any Jupyter notebook will do.

Right-click on on the .ipynb file and choose Open with --> Choose Another App

![anaconda prompt see active env location]({static}/posts/jupyter/images/choose-another-program.png)

Scroll down to the bottom of the list of Apps and click [Look for another app on this PC].

At the top of the window, in the [How do you want to open this file?] Section, click [More Apps].

![anaconda prompt see active env location]({static}/posts/jupyter/images/choose-more-apps.png)

At the bottom of the window, check the box [Always use this app to open .ipynb files]

![anaconda prompt see active env location]({static}/posts/jupyter/images/always-use-this-program-radio-box.png)

In the pop out window, navigate to the .bat file you created in step 2. I recommended that the ```.bat``` file is in Documents --> open_ipynb_files --> open_ipynb_files.bat. Select the .bat file and click [Open].

![anaconda prompt see active env location]({static}posts/jupyter/images/open-button.png)

The result should be a new web browser tab running the Jupyter notebook.

![anaconda prompt see active env location]({static}/posts/jupyter/images/jupyter-notebook-open.png)

From now on, if you double click an ```.ipynb``` file, a web browser tab should open with the running Jupyter notebook.

![anaconda prompt see active env location]({static}/posts/jupyter/images/double-click-ipynb.png)

<br/>

#### Congratulations! Now you can open Jupyter notebooks by double clicking them. Now go write some Python code to solve some problems!

<br/>
