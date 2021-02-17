Title: Writing Tests in Scientific Code
Date: 2021-02-17 08:11
Modified: 2021-02-17 08:11
Status: draft
Category: Python
Tags: engineering,testing
Slug: writing-tests-in-scientific-code
Authors: Peter D. Kazarinoff

![science lab]({static}/posts/testing_science_code/images/lab.jpg)

In a previous blog post, I wrote about to incorporate a few software design principals into the code written by scientists. This post is a follow up on one specific software design principal: **testing**

Below are some practical ideas about how to incorporate software testing in science data analysis. Keep in mind the steps and tests below don't correspond to every piece of scientific code. My ideas are not designed to revoultionize the ways scientists write code, or fix repoducibility problems in published scientific research, or a strict TDD (test-driven development) framework for scientific code. The ideas below are some things I came up with that I wanted to share and my hope is that it is helpful and starts a few conversations.

**OK - with that disclaimer out of the way, let's get started.**

### A sample script

Below is a sample Python script that reads in an excel file of data, plots the data, and then outputs two calculated values. In this case, the data is from a mechanical test frame (a piece of equipment that tests the strength of materials), but the same testing ideas could be applied to a script that analyzes data from another subject area.

Very often scientific code includes a couple of common steps:

 * Read in data
 * Clean or reorganize the data
 * Run calculations on the data
 * Create a figure or plot

The code below is one long script. In the rest of this post, we are going work on adding tests to this script.

```python
# code raw
```

![cup cakes]({static}/posts/testing_science_code/images/cupcakes.jpg)

## Idea 1. Testing in Scientific Software is about Reproducibiliy

The first idea isn't code or a specific test, it's the idea that **testing scientists code is about ensuring reproducibility**. It's my understanding that testing software in general (not scientist's code) is about ensuring the system runs error-free and accomplishes what the programmer intends. In scientists code, my argument is that testing should be more about making sure the code is reproducible by other rearchers (or more likely useable by the scientist 6 months later or by a new grad student), than ensuring it runs error-free or produces the desired result. *All scientists what their research to be repoducible, right?*

![code]({static}/posts/testing_science_code/images/python_code.png)

## Idea 2. Use a .py-file instead of a Jupyter notebook

The second idea is to write scientific code in a .py-file instead of in a Jupyter notebook. Now, I love Jupyter notebooks. Jupyter notebooks are great for data exploration, plot creation and presentation. But... after the initial exploration, move the code from the Jupyter notebook into a .py-file. Within the Jupyter notebook interface you can select File --> Save As and select .py as the file type. 

After the Jupyter notebook is saved as a .py file, run the .py-file from the command line and see if the same output is produced by the .py and the Jupyternoteboom. Jupyter notebook cells can be run in any order and the execution order of a Jupyter notebook sometimes effects the output of the code. When the code is in a .py-file, the execution order of the lines of Python code are set by your programming logic. So idealy, each time your run the .py-file the output is the same.

![pack mule]({static}/posts/testing_science_code/images/pack_mule.jpg)

## Idea 2. Define Package Dependancies and Python Version

Create a ```requirements.txt``` file that contains the specific versions of the packages your script is run with. These packages just need to be the high-level dependancies that are imported by your script. The contents of a sample ```requirements.txt``` file are below:

```text
matplotib==3.3.2
numpy==1.19.2
pandas==1.1.3
pytest==6.1.1
```

If you don't know what version of matplotlib you are using, open the Python REPL and type:

```
>>> import matplotlib
>>> matplotlib.__version__
3.3.2
```

The ```.__version__``` attribute is commonly defined for widely used Python packages. 

In addition to the packages used by your script, you can also define which version of Python you are using. The Python version can be stored in a file called ```runtime.txt```. The contents of an example ```runtime.txt``` file are below:

```text
python-3.8.3
```

The python version you are using is shown when you enter the Python REPL. In a termial type ```python``` and the version is printed out above the REPL prompt.

```text
> python
Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

At this point, we have now converted an originol Jupyter notebook into a Python script. We have also included a ```requirements.txt``` file and a ```runtime.txt``` file. The directory structure of our growing project is shown below.

```text
project/
    analysis.ipynb
    analysis.py
    requirements.txt
    runtime.txt
    data/
        raw_data.csv
    output/
        plot.png
```

## Idea 3. Test the Dependancy Package Versions and the Python Version

Now that we defined our package versions and Python runtime version, we can write tests to confirm these are the same versions that are used when our script is run. If another researcher wants to run our script, they can confirm through our tests that they are using the same dependancy versions. Create a new directory called ```tests``` and inside create a new file called ```test_dependancies.py```.

The directory structure of our project should now look like:

```text
project/
    analysis.ipynb
    analysis.py
    requirements.txt
    runtime.txt
    data/
        raw_data.csv
    output/
        plot.png
    tests/
        __init__.py
        test_dependancies.py
```

Inside the ```test_dependancies.py``` file, we can write tests that confirm the versions of the packages we say are necessary in our ```requirements.txt``` file. Examples of these tests are below.

```python
# test_dependancies.py


```

The Python version can be tested with another test. 

```python
def test_python_version():

```

Now these tests can be run on the command line with pytest

```text
> python -m pytest tests/test_dependancies.py
```

The output should look something like below:

```text
pytest output
```

## Idea 2. Break the script up into functions

![holding hands]({static}/posts/testing_science_code/images/kids-holding-hands.jpg)

The first thing to do is break the script up into functions. If you don't know where to start, use the four bullet points above to help guide where to break up the one long script into 3 or 4 pieces. Don't worry if all that happens is that you have four sections, each section is a function and each function has no inputs and no outputs. End the script with a main function.

 ```python
 # code with functions
```

## Idea 3. Remove all hard-coded file names

 ![holding hands]({static}/posts/testing_science_code/images/concrete.jpg)

Next, let's try to remove all hard-coded file names. If you renamed your data file ```my-data_v2.csv```, would your script still work? If not, break the file name into a variable first. Next, make the file name be included as a parsed argument when the file is called.

 ```python
 # code with argparse
```

Now the script is run using the command below.

```text
# python analysis.py -i my-data.csv
```

## Idea 4. Your code should not modify the data

![holding hands]({static}/posts/testing_science_code/images/ice.jpeg)

When your code runs, it should not modify, rename, rewrite or otherwise change the originol data. If that happens as a result of your script, take it out.

```python
# code that doesn't modify the data
```

## Idea 5. Consider the inputs and outputs of your functions

![holding hands]({static}/posts/testing_science_code/images/pipe.jpeg)

Now that we removed all hard-coded file names and made sure that the data wasn't modified by the code, is it any clearer what the input and output of our functions should be? At the very least, modify your functions to return ```True``` at the end. For a function that produces a plot, assign the outputs as Matplotlib ```fig``` and ```ax``` objects.

```python
# code that have function inputs and outputs
```

## Idea 5. Test each function

 ![holding hands]({static}/posts/testing_science_code/images/pin_wheel.jpg)

Now we are going to use **pytest** to test each function. Some of the functions can have expected input and output. Some functions may need an example file passed to them.

Before pytest can be used, pytest needs to be installed. You can install pytest using **pip**, Python's package manager

```text
$ pip install pytest
```

I set up my directory structure as shown below. The file which contains the tests start with the filename ```test_ ...```.

```text
project_directory/
├── analysis.py
├── analysis_script.py
├── data
│   └── raw_data.csv
├── LICENSE
├── README.md
└── tests
    └── test_plot.py
```

## Idea 6. Test the main() function

## Idea 7. Set the version of Python your script works with, ensure that version of Python is used to run it

### Sub Idea 7a. Set the operating system your script runs on, ensure that operating system is running the script

### Sub Idea 7b. Set the version of packages your script runs on, ensure that version of the package is used to run it.

## Idea 8. To test plots, test the fig and ax objects
