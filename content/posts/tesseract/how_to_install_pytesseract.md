Title: How to install pytesseract
Date: 2021-03-12 11:00
Modified: 2021-03-12 11:00
Status: draft
Category: python
Tags: python, tesseract, pytesseract, ocr
Slug: how-to-install-pytesseract
Authors: Peter D. Kazarinoff

[![tesseract and python]({static}/posts/tesseract/images/tesseract_plus_python.png)]({filename}/posts/tesseract/how_to_install_pytesseract.md)

In this post, I'll show you how to install pytesseract. Pytesseract is a Python package that allows you to work with tesseract which is a command-line OCR (optical character recognician) program. You can use pytesseract to convert images into text. It's a super cool package. Let's get to it.

## Prerequisites

![briefcase]({static}/posts/tesseract/images/briefcase.jpg)

Before you can install pytesseract, you need to have a couple things in place:

 * computer with an internet connection
 * Anaconda distribution of Python

You are going to need a computer with an internet connection. If you are reading this post, there is a good chance there is one in front of you right now. As far as I know you can't install pytesseract on a phone, tablet or chromebook. You are also going to need the Anaconda distribution of Python. Why Anaconda?

### Why Anaconda?

![anaconda icon]({static}/posts/tesseract/images/anaconda_icon.png)

You might be wondering, why do I need Anaconda to install Pytesseract. Well you don't have to use the Anaconda distribution of Python when you install Pytesseract, but I think it's a lot easier than other installation methods. You can install Python packages, but also non-python packages with the Anacdonda Prompt. Since a non-python package is need to use Pytesseract, I think the Anaconda distribution of Python and the conda package manager is the way to go.

## What is pytesseract?

![anaconda icon]({static}/posts/tesseract/images/pytesseract_at_pypi.png)

Pytesseract is a Python package that allows you to extract text from images. If you have a picture that has some text in it, pytessearct can be used to pull out that text into a python program. That's pretty cool. Pytesseract is a wrapper around a program from google called tesseract. It's tesseract that extracts the text from pictures. Pytesseract is there to help you use tesseract in your Python programs.

### What is tesseract?

![anaconda icon]({static}/posts/tesseract/images/tesseract_icon.png)

Tesseract is a command-line application created by Google that can be used to pull text out of pictures. It is an example of an OCR application, which stands for optical character recognition. Which is just a fancy way of saying using a computer to read text.

## Create a virtual environment

![anaconda icon]({static}/posts/tesseract/images/container_ships.jpg)

Next, we are going to create a virtual environment to install pytesseract into. It's a good idea to create a new virtual environment for each Python project.

Open up the Anaconda Prompt from the windows start menu and type the command below.

```text
> conda create -y -n tesseract python=3.8
```

You now have a new virtual environment called ```(tesseract)```. Before you can install packages into this environment, it needs to be activated. Activate the ```(tesseract)``` environment with the command below:

```text
> conda activate tesseract
(tesseract) >
```

You know the ```(tesseract)``` environment is active when you see the environment name ```(tesseract)``` before the prompt. In the next few steps we are going to install packages into our ```(tesseract)``` environment. Make sure the environment is active when you run any ```conda install``` commands.

## Install pytesseract

Now we are going to install pytesseract into our virtual environment. Make sure the ```(tesseract)``` environment is activated. You can install pytesseract from PyPI, the Python package index using **pip**. But I suggest installing pytesseract with **conda**. Conda can manage non-python dependancies and we want to be sure that pytesseract plays well with the other packages we install. Use the command below to install pytesseract. Note the ```-c conda-forge``` portion of the command. This means we are installing pytesseract from the **conda-forge** channel. If you don't specifiy the channel, the installation will fail.

```text
> conda install -c conda-forge pytesseract
```

You can confirm that pytesseract is installed in your virtual enviroment by hopping into the Python REPL and trying to import it.

```text
> python
>>> import pytesseract
>>> help(pytesseract)

Help on package pytesseract:

NAME
    pytesseract - # flake8: noqa: F401
...

>>> exit()
```

pytesseract is installed. Great! But before we can use it, we need to install the tesseract application.

## Install tesseract

Now that pytesseract is installed, there are two more things we need to do before we can use it.

 * install tesseract
 * figure out where the tesseract executable is located

We can install tesseract using conda at the Ancaconda Prompt, just like we installed pytesseract. Again, make sure the ```(tesseract)``` virtual environment is active before you run the ```conda install``` command. Type the command below to install tesseract.

```text
> conda install -c conda-forge tesseract
```

You can confirm that tesseract is installed in your virtual enviroment by running the comand below. The command calls up the tesseract help screen.

```text
> tesseract -h
```

OK - one more step before we can use pytesseract, we need to figure out where our tesseract executable was installed. The tesseract executable location is needed for pytesseract won't work properly.

## Determine the location of your tesseract executable

![island]({static}/posts/tesseract/images/island.jpg)

The next step is to determine where the tesseract program is located on our computer. We need this location when we use pytesseract in a python program. Typing the ```where <executable>``` command into the Anaconda Prompt shows the location of that ```<exectable>```. ```where``` on Windows is sort of like the ```which``` command in MacOS and Linux.

```text
> where tesseract
C:\Users\Peter\Anaconda3\envs\tesseract\Library\bin\tesseract.exe
```

Make note of this file path. We need the file path to use pytesseract in a Python program.

## Point pytesseract at your tesseract installation

![map.jpg]({static}/posts/tesseract/images/map.jpg)

Create a Python script (a .py-file), or start up a Jupyter notebook. At the top of the file, import ```pytesseract``` , then point pytesseract at the tesseract installation you discovered in the previous step.

```python
# test_pytesseract.py

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Peter\Anaconda3\envs\tesseract\Library\bin\tesseract.exe'

```

Now we can use pytesseract to extract some text from a picture.

## Use pytesseract

OK! Now it's time to pull text out of a picture. You are going to need a picture to pull text out of. The picture I'm using can be found [here](https://github.com/ProfessorKazarinoff/staticsite/blob/master/content/posts/tesseract/images/tesseract_plus_python.png) and is shown below.

![map.jpg]({static}/posts/tesseract/images/test_image.png)

Make sure the ```test_image.png``` is in the same folder as your Python program.

```python
# test_pytesseract.py

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Peter\Anaconda3\envs\tesseract\Library\bin\tesseract.exe'

text_from_image = pytesseract.image_to_string(Image.open('test_image.png'))
print(text_from_image)
```

Run the Python program or Jupyter notebook code cell and see the output.

The output produced should look something like below:

```text
This is a lot of 12 point text to test the
ocr code and see if it works on all types
of file format.

The quick brown dog jumped over the
lazy fox. The quick brown dog jumped
over the lazy fox. The quick brown dog
jumped over the lazy fox. The quick
brown dog jumped over the lazy fox.
♀
```

## Going Further

![map.jpg]({static}/posts/tesseract/images/bricks.jpg)

Now that pytesseract is installed what are you going to build? There are so many possibilities for projects:

 * Run pytesseract on a stack of pdf's from work
 * Try to see if pytesseract can read your handwriting
 * See if pytesseract can read junkmail
 * Incorporate pytesseract into a web application

**Happy coding!**
