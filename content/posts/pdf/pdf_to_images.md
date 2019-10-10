Title: Convert a PDF to Multiple Images with Python
Date: 2019-10-10 09:03
Modified: 2019-10-10 09:03
Status: Draft
Category: Python
Tags: python, pdf, images
Slug: pdf-to-multiple-images
Authors: Peter D. Kazarinoff

![pdf to dir]({static}/posts/pdf/images/pdf_to_dir.png)

I had one of those "[Automate the Boring Stuff](https://automatetheboringstuff.com/)" problems this week. **How do you convert a multi-page PDF into a folder of images?** One image for each page in the PDF? Read on to see how to solve this problem with Python.

[TOC]

## The Problem

So here is the basic problem:

 > Convert a multi-page PDF into a directory of images

We're going to solve this problem with Python. 

## Install Python

If you don't have Python installed yet, I suggest you install the [Anaconda](https://anaconda.com/distribution) distribution of Python. See [this post](https://pythonforundergradengineers.com/installing-anaconda-on-windows.html) to learn how to install Anaconda on your computer. Alternatively, you can download Python form [Python.org](https://python.org) or download Python the Microsoft Store.

## Create and virtual environment and install pdf2image

Before we start writing code, it is a good idea to create a new virtual environment when you start a new Python project. A virtual environment is an isolated installation of Python that is separate from other Python installations running on your computer. See [this post](https://pythonforundergradengineers.com/new-virtual-environment-with-conda.html) to learn how to create a virtual environment with the **Anaconda Prompt**.

To create a new Python virtual environment, open the **Anaconda Prompt** and type the following commands. Note the prompt character (the greater than sign ```>```) does not need to be typed. It is included to indicate the prompt. The ```-n pdf``` portion of the command denotes the name of the virtual environment. ```python=3.7``` ensures Python Version 3.7 is installed into the ```pdf``` virtual environment.

```text
> conda create -n pdf python=3.7
```

Type ```y``` for yes when prompted. Before we install any packages into the ```pdf``` environment it needs to be activated. Activate the ```pdf``` virtual environment with the command below. Note that when the ```pdf``` virtual environment is active, ```(pdf)``` is shown in parenthesis before the prompt.

```text
> conda activate pdf
(pdf)>
```

## Install img2pdf

Next we need to install the ```poppler``` package using conda and the ```pdf2image``` package using ```pip```

```text
(pdf)> conda install -c conda-forge poppler
(pdf)> pip install pdf2image
```

## Imports

Use a code editor like [VS Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) to create a new file called ```pdf.py```.

At the top of the file, import the ```confert_from_path``` function from the ```pdf2image``` package and the ```pdf2image``` exceptions.

```python
from pdf2image import convert_from_path

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
```

## The code

Below is the code to convert a PDF named ```myfile.pdf``` to multiple ```.png``` images. Save this code below the import lines.

```python
images = convert_from_path('myfile.pdf')

for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")
```

## Run the code

Put a PDF file in the same folder as the code. Make sure the PDF file has the same name as used in the code above. I called my PDF file ```myfile.pdf```.

```text
├───pdf
│   ├───pdf.py
│   └───myfile.pdf
```

The code can be run from the **Anaconda Prompt**. Make sure the ```(pdf)``` environment is active before the script is run.

```text
(pdf)> python pdf.py
```

After the code completes, you should see images in the same folder as your ```pdf.py``` Python script and ```myfile.pdf``` PDF file. 

![pdf to dir]({static}/posts/pdf/images/images_in_dir.png)

## Summary

In this post, we used a Python package called ```pdf2image``` to convert a PDF file into a directory full of images. Big thanks to the maintainers of ```pdf2image``` for making such a useful package.

The complete Python script is below:

```python
# pdf.py

"""
A Python script to convert a multi-page PDF to a directory of images
Uses the pdf2image package
"""

from pdf2image import convert_from_path

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path('myfile.pdf')

for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")

```
