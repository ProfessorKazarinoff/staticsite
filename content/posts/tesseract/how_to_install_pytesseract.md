Title: How to install pytesseract
Date: 2021-03-12 11:00
Modified: 2021-03-12 11:00
Status: draft
Category: python
Tags: python, tesseract, pytesseract, ocr
Slug: how-to-install-pytesseract
Authors: Peter D. Kazarinoff

[![tesseract and python]({static}/posts/tesseract/images/tesseract_plus_python.png)]({filename}/posts/tesseract/how_to_install_pytesseract.md)

In this post, I'll show you how to install pytesseract. Pytesseract is a Python package that allows you to work with tesseract which is a command-line OCR (optical character recognician) program. You can use pytesseract to convert images with writing on them into text. It's a super cool package. Let's get to it.

## Prerequisites

Before you can install pytesseract, you need to have a couple things in place:

 * computer with an internet connection
 * Anaconda distribution of Python

You are going to need a computer with an internet connection. If you are reading this post, there is a good chance there is one in front of you right now. As far as I know you can't install pytesseract on a phone, tablet or chromebook. You are also going to need the Anaconda distribution of Python. Why Anaconda?

### Why Anaconda?

You might be wondering, why do I need Anaconda to install Pytesseract. Well you don't have to use the Anaconda distribution of Python when you install Pytesseract, but I think it's a lot easier than other installation methods. You can install Python packages, but also non-python packages with the Anacdonda Prompt. Since a non-python package is need to use Pytesseract, I think the Anaconda distribution of Python and the conda package manager is the way to go.

## What is pytesseract?

Pytesseract is a Python package that allows you to extract text from images. If you have a picture that has some text in it, pytessearct can be used to pull out that text into a python program. That's pretty cool. Pytesseract is a wrapper around a program from google called tesseract. It's tesseract that extracts the text from pictures. Pytesseract is there to help you use tesseract in your Python programs.

### What is tesseract?

Tesseract is a command-line application created by Google that can be used to pull text out of pictures. It is an example of an OCR application, which stands for optical character recognition. Which is just a fancy way of saying using a computer to read text.

## Create a virtual environment


```text
> conda create -y -n tesseract python=3.8
```



```text
> conda activate tesseract
(tesseract) >
```


## Install pytesseract

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

## Install tesseract

```text
> conda install -c conda-forge tesseract
```


You can confirm that tesseract is installed in your virtual enviroment by running the comand below. Make sure you are in the active environment that tesseract was installed into.

```text
> tesseract -h
```

## Determine the location of your tesseract executable

```text
> where tesseract
C:\Users\Peter\Anaconda3\envs\tesseract\Library\bin\tesseract.exe
```

## Point pytesseract at your tesseract installation

Create a Python script, or start up a Jupyter notebook. At the top of the file, import pytesseract and then point pytesseract at the tesseract installation you discovered in the previous step.

```python
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Peter\Anaconda3\envs\tesseract\Library\bin\tesseract.exe'

```

## Use pytesseract

```python
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Peter\Anaconda3\envs\tesseract\Library\bin\tesseract.exe'

text_from_image = pytesseract.image_to_string(Image.open('test.png'))
print(text_from_image)
```

Run the program or Jupyter notebook code cell and see the output.


## Conclusion
