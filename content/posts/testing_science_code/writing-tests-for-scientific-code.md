Title: Writing Tests for Scientific Code
Date: 2021-02-19 08:11
Modified: 2021-02-19 08:11
Status: draft
Category: Python
Tags: engineering,testing
Slug: writing-tests-for-scientific-code
Authors: Peter D. Kazarinoff

![science lab]({static}/posts/testing_science_code/images/lab.jpg)

In a [previous blog post]({filename}/posts/testing_science_code/thoughts-on-software-design-in-science.md), I wrote about how to incorporate a few software design principals into the code written by scientists. This post is a follow up on one specific software design principal that can be used by scientists: **testing**

Below are some practical ideas about how to incorporate software testing in science data analysis. Keep in mind the steps and tests below don't correspond to every piece of scientific code. My ideas are not designed to revoultionize the ways scientists write code, or fix repoducibility problems in published scientific research, or be a strict TDD (Test-Driven Development) framework for scientific code. The ideas below are some things I came up with that I wanted to share and my hope is that it is helpful and starts a few conversations.

**OK - with that disclaimer out of the way, let's get started.**

### A sample notebook

The example scientific code we will be working with is made up of one long script. In the rest of this post, we are going work on adding tests to this scientific script.

Very often, scientific code includes a couple of common steps:

 * Read in the data
 * Clean or reorganize the data
 * Run calculations on the data
 * Create a figure or plot

Below is a sample Jupyter notebook (that we'll use in the rest of this post) with Python code that reads in an excel file of data, cleans up the data, runs a calculation, then plots the data. The data in this example is from a mechanical test frame (a piece of equipment that tests the strength of materials), but the same testing ideas in this post could be applied to a script that analyzes data in another subject area. You can find the notebook here: [analysis.ipynb](https://github.com/ProfessorKazarinoff/testing-scientific-code/blob/master/analysis.ipynb) and the raw data here: [raw_data.csv](https://github.com/ProfessorKazarinoff/testing-scientific-code/blob/master/data/raw_data.csv)


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

raw_data_df = pd.read_csv('data/raw_data.csv')

raw_data_array = np.array(raw_data_df)
cleaned_data_array = raw_data_array[1:,:]

d = 0.506
A0 = np.pi*(d/2)**2
F = cleaned_data_array[:,4]
stress = F/A0
strain = cleaned_data_array[:,5]*0.01
ts = np.max(stress)
te = np.max(strain)-np.min(strain)
print(f'Tensile Strength={ts}')
print(f'Total Extension={te}')

fig, ax = plt.subplots()
ax.plot(strain,stress)
ax.set_xlabel("Strain (mm/mm)")
ax.set_ylabel("Stress (MPa)")
plt.savefig("output/plot.png")
plt.show()
```

When the code is run, the plot produced looks like the plot below:

![plot]({static}/posts/testing_science_code/images/plot.png)

Notice how in the code above the .csv data file isn't in the same directory as the script. The .csv file is in a sub-directory called ```data/```. In addition, the plot that's produced by the script is saved in a directory called ```output/```. In scientific code, it's a good idea to keep the data seperate from the script that analyzes the data. It's also a good idea to keep the output of the script (the plot) separate from the script itself.

*How can we possibly write software tests for this script?*

![cup cakes]({static}/posts/testing_science_code/images/cupcakes.jpg)

## Testing in Scientific Software is about Reproducibiliy

The first idea isn't code or a specific test, it's the idea that **testing scientific code is about ensuring reproducibility**. It's my understanding that testing software in general (not scientist's code) is about ensuring the system runs error-free and accomplishes what the programmer intends. In scientist's code, my argument is that testing should be more about making sure the code is reproducible by other rearchers (or more likely useable to the scientist 6 months later or a new grad student), than ensuring the code runs error-free or produces the desired result. 

*All scientists what their research to be repoducible, right?*

![code]({static}/posts/testing_science_code/images/python_code.png)

## Use a .py-file instead of a Jupyter notebook

The second idea is to write scientific code in a **.py-file** instead of writing the code in a Jupyter notebook. Now, I love Jupyter notebooks as much as the next Engineer. Jupyter notebooks are great for data exploration, plot creation and presentation. But... Jupyter notebook cells can be run in any order. The execution order of a Jupyter notebook sometimes effects the output of the code. When the code is in a .py-file, the execution order of the lines of Python code are set by your programming logic. So idealy, each time your run the .py-file, the output is the same. Therefor after initial data exploration, move code from a Jupyter notebook into a .py-file. 

Within the Jupyter notebook interface, you can select File --> Download As and select .py as the file type. 

![Download As in Jupyter notebook]({static}/posts/testing_science_code/images/jupyter_notebook_download_as.jpg)

After the Jupyter notebook is saved as a .py-file, run the .py-file from the command line. 

```
> python analysis.py
```

See if the same output is produced by the .py-file and the Jupyter notebook. In the next section, we'll deal with Python versions and dependancies.

![pack mule]({static}/posts/testing_science_code/images/pack_mule.jpg)

## Define Package Dependancies and Python Version

After the scientific script is saved in a .py-file, the next step is to define the Python version and dependancies needed to run the script. This can be accomplished by creating a ```requirements.txt``` file that contains the specific versions of the packages your script is run with. These packages just need to be the high-level dependancies that are imported by your script. The contents of a sample ```requirements.txt``` file are below. Note that **pytest** is also included as a dependancy. We are going to use pytests a little later to test the script.

```text
matplotib==3.3.2
numpy==1.19.2
pandas==1.1.3
pytest==6.1.1
```

If you don't know what version of matplotlib you are using, open the Python REPL and type:

```text
>>> import matplotlib
>>> matplotlib.__version__
3.3.2
```

The ```.__version__``` attribute is commonly defined for popular Python packages. 

In addition to the packages used by your script, you can also define which version of Python you are using. The Python version can be stored in a file called ```runtime.txt```. The contents of a ```runtime.txt``` file is below:

```text
python-3.8.3
```

If you don't know what version of Python you are using, it's easy to figure out. The Python version is shown when you enter the Python REPL. In a termial type ```python``` and the version is printed out above the REPL prompt.

```text
> python
Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

At this point, we have converted an originol Jupyter notebook into a Python script. We have also included a ```requirements.txt``` file and a ```runtime.txt``` file along side our script. The directory structure of our growing project is shown below.

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

Our dependanies and Python version defined, let's write our first tests.

## Test the Dependancy Versions and the Python Version

Now that we defined our package versions and Python version, we can write tests to confirm these are the same versions that run our script. If another researcher wants to run our script, they can confirm through our tests that they are using the same dependancy versions we we are.

Create a new directory called ```tests``` and inside the ```tests``` directory, create a new file called ```test_dependancies.py```. In addition, create a blank ```__init__.py``` file along side the ```test_dependancies.py``` file. This defines the ```tests/``` directory as a package.

The directory structure of our project now looks like:

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

### Test Dependancies

Inside the ```test_dependancies.py``` file, we can write tests that confirm the versions of the packages we say are necessary in our ```requirements.txt``` file. Examples of these tests are below. The tests are written using [pytest](https://docs.pytest.org/en/stable/contents.html), an excellent testing framework that is pretty easy to use.

```python
# tests/test_dependancies.py

import pytest

import numpy as np
import pandas as pd
import matplotlib as mpl

def test_numpy_version():
    expected = "1.18.5"
    actual = np.__version__
    assert actual == expected


def test_pandas_version():
    expected = "1.0.5"
    actual = pd.__version__
    assert actual == expected


def test_matplotlib_version():
    expected = "3.2.2"
    actual = mpl.__version__
    assert actual == expected

```

We can run these tests from the command line as long as pytest is installed. If it isn't installed, pytest can be installed with **pip**

```text
> pip install pytest
```

The command below runs the tests we defined in ```test_dependancies.py``` with pytest

```text
> python -m pytest tests/test_dependancies.py
```

The output should be something like below:

```text
======================== test session starts =========================
platform linux -- Python 3.8.3, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/peter/Documents/testing-scientific-code
collected 3 items                                                    

tests/test_dependancies.py .....                               [100%]

```

If we want more information about the tests, we can use the ```-v``` flag when we run the tests.

```text
> python -m pytest -v tests/test_dependancies.py
```

Additional information is shown in the output:

```text
collected 3 items

tests/test_dependancies.py::test_numpy_version PASSED                 [ 33%]
tests/test_dependancies.py::test_pandas_version PASSED                  [ 66%]
tests/test_dependancies.py::test_matplotlib_version PASSED                 [100%]

```

### Test Python Version

We can also write a test for the version of Python we're using. Let's add another test in ```test_dependancies.py```. The test below ensures Python verison 3.8.3 is used. Make sure to import the ```platform``` module from the Python Standard Library at the top of ```test_dependancies.py``` or the test won't work.

```python
import platorm

def test_python_version():
    expected = "3.8.3"
    actual = platform.python_version()
    assert actual == expected

```

All four tests can be run on the command line with pytest.

```text
> python -m pytest tests/test_dependancies.py
```

The output should look something like below:

```text
collected 4 items                                                    

tests/test_dependancies.py .....                               [100%]

```

This means all four tests passed.

### Test Character Encoding

One more test we can write is test what character encoding is used. On most computers, the character encodeing is **utf-8**. We can check for the character encoding by writing another test. This character encoding test uses the ```sys``` module. Make sure to add the ```sys``` module import at the top of the ```test_dependancies.py``` file.

```python
import sys

def test_system_encoding():
    expected = "utf-8"
    actual = sys.getfilesystemencoding()
    assert actual == expected

```

We can run all the tests with pytest. They should all pass. If they don't, that means some trouble shooting.

*Are you sure those are the package versions you are using?*

```text
> python -m pytest tests/test_dependancies.py

collected 5 items                                                    

tests/test_dependancies.py .....                               [100%]

```

**Our 5 tests are great right?** Yes, yes they are great. But...

*How can we test the scientific code in the script ```analysis.py``` itself?* 

Before we can test the script, we need to break the script up into functions.

## Break the script up into functions

![holding hands]({static}/posts/testing_science_code/images/kids-holding-hands.jpg)

Next, we are going to break the script ```analysis.py``` up into functions. Let's use the four bullet points below to help guide us through how to break up our long ```analysis.py``` script into 3 or 4 pieces. 

 * Read in data
 * Clean or reorganize the data
 * Run calculations on the data
 * Create a figure or plot

The code below shows how each one of the steps can be encapsulated in a function. 

```python
# analysis.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def import_data():
    raw_data_df = pd.read_csv('data/raw_data.csv')
    raw_data_array = np.array(raw_data_df)
    return raw_np_array

def clean_data(raw_np_array):
    cleaned_data_array = raw_data_array[1:,:]
    return cleaned_data_array

def get_stress_and_strain(cleaned_data_array):
    d = 0.506
    A0 = np.pi * (d / 2) ** 2
    F = cleaned_data_array[:, 4]
    stress = F / A0
    strain = cleaned_data_array[:, 5] * 0.01
    return stress, strain

def get_tensile_strength(stress, strain):
    return np.max(stress).round(3)

def get_total_extension(stress, strain):
    return np.max(strain) - np.min(strain)

def plot(x,y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel("Strain (mm/mm)")
    ax.set_ylabel("Stress (MPa)")
    plt.show()

```

Let's end the script by defining a ```main()``` function that calls the functions defined above in the proper order. Then we can call the ```main()``` function with an ```if __name__ == "__main__":``` line.

```python

def main():
    raw_data_array = import_data()
    clean_data_array = clean_data(raw_data_array)
    stress, strain = get_stress_and_strain(clean_data_array)
    plot(strain, stress)
    ts = get_tensile_strength(stress, strain)
    te = get_total_extension(stress, strain)
    print(f"Tensile Strength: {ts}, Total Extension: {te}")


if __name__ == "__main__":
    main()

```

Run the script from the command line. 

```text
> python analysis.py
```

A plot should be produced and the output should be the same as when the script didn't contain any user-defined fuctions.

Now that we've divided our script up into functions, we can make sure our script doesn't modify our raw data by writing another test.

## Test if the code modifies the data

![ice]({static}/posts/testing_science_code/images/ice.jpeg)

When our code runs, it should not modify, rename, rewrite or otherwise change our originol data. Let's create a new test file in the ```tests/``` directory called ```test_data_unchanged.py```. The directory structure should now look like:

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
        test_data_unchanged.py
```

The test to make sure our script doesn't change the raw data file is below. All the the attributes listed in the test from the ```os.stat``` object should be the same before the script is run and after the script is run.

```python
# test_data_unchanged.py

from pathlib import Path

import pytest

import analysis


def test_data_is_unchanged():
    fp1 = Path("data/raw_data.csv")
    d1 = os.stat(fp1)
    analysis.main()
    fp2 = Path("data/raw_data.csv")
    d2 = os.stat(fp2)
    assert (
        d1.st_mode == d2.st_mode
        and d1.st_ino == d2.st_ino
        and d1.st_dev == d2.st_dev
        and d1.st_nlink == d2.st_nlink
        and d1.st_uid == d2.st_uid
        and d1.st_gid == d2.st_gid
        and d1.st_size == d2.st_size
        and d1.st_mtime == d2.st_mtime
        and d1.st_ctime == d2.st_ctime
    )
```

Run the ```data_is_unchanged()``` test from the command line. If the test passes, that mean the data file ```raw_data.csv``` is not modified by our script.

```text
python -m pytest tests/test_data_unchanged.py

collected 1 item                                                     

tests/test_data_unchanged.py .                                 [100%]

==================== 1 passed in 3.53s ====================

```

In order to test the functions of script itself, it is helpful for each function in the script accept input and produce output. Therefore, next we'll modify the functions of our script and make sure each function includes inputs and outputs.

## Ensure each accepts input and produces output

![pipe]({static}/posts/testing_science_code/images/pipe.jpeg)

Now that we know our script doesn't modify the data it uses, we are going to modify the functions of our script to be more testable. To make these functions more testable, we'll add inputs and output where possible.

Is clear what the input and output of our functions should be? For a function that produces a plot, assign the outputs as Matplotlib ```fig``` and ```ax``` objects. The code below includes modifications to ```analysis.py```.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def import_data(f_name):
    df = pd.read_csv(f_name)
    np_raw_array = np.array(df)
    np_array = np_raw_array[1:, :]
    return np_array


def get_stress_and_strain(cleaned_data_array):
    d = 0.506
    A0 = np.pi * (d / 2) ** 2
    F = cleaned_data_array[:, 4]
    stress = F / A0
    strain = cleaned_data_array[:, 5] * 0.01
    return stress, strain


def plot(x, y, title, x_label, y_label):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()
    return fig, ax

def save_fig(fig,fname):
    out = plt.savefig(fig, fname)
    return out

def get_tensile_strength(stress, strain):
    return np.max(stress).round(3)


def get_total_extension(stress, strain):
    return np.max(strain) - np.min(strain)
```

No we can modify the ```main()``` function and include a file path for our raw data and saved figure.

```python

def main():
    raw_data = Path("data/raw_data.csv")
    raw_data_array = import_data()
    clean_data_array = clean_data(raw_data_array)
    stress, strain = get_stress_and_strain(clean_data_array)
    plot(strain, stress)
    ts = get_tensile_strength(stress, strain)
    te = get_total_extension(stress, strain)
    print(f"Tensile Strength: {ts}, Total Extension: {te}")

if __name__ == "__main__":
    main()

```

OK - our functions have inputs and outputs. Let's get to testing them with pytest.

## Test each function

 ![pin wheel]({static}/posts/testing_science_code/images/pin_wheel.jpg)

Now we are going to use **pytest** to test each function in our ```analysis.py``` script. Creat a new file called ```test_analysis.py``` in the ```tests/``` directory. The directory strucuture now looks like:

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
        test_analysis.py
        test_dependancies.py
        test_data_unchanged.py
```

### Create some sample data

At the top of ```test_analysis.py``` let's add our imports and some sample data to test our functions with. 

```python
import os
from pathlib import Path

import pytest
import numpy as np

import analysis

x = np.array([1, 2, 3])
y = np.array([6, 7, 10])
```

### Test the analysis functions

```python
def test_get_stress_and_strain():
    expected = 
    actual = analysis.get_stress_and_strain(x,y)
    assert expected == actual

def test_tensile_strength():
    expected = 10.0
    actual = analysis.get_tensile_strength(y, x)
    assert round(expected, 3) == round(actual, 3)

def test_total_extension():
    expected = 3 - 1
    actual = analysis.get_total_extension(y, x)
    assert round(expected, 3) == round(actual, 3)

```

Run these tests with pytest

```
> pytest tests/test_analysis.py
```


## Test the plot

We'll test the plot in a new test file called ```test_plot.py```

```python
# tests/test_plot.py

import pyest

import analysis

x = np.array([1, 2, 3])
y = np.array([6, 7, 10])
fig, ax = analysis.plot(x, y, "my_title", "my_x_axis_label", "my_y_axis_label")

def test_plot_x_axis_label():
    assert ax.xaxis.label.get_text() == "my_x_axis_label"


def test_plot_y_axis_label():
    assert ax.yaxis.label.get_text() == "my_y_axis_label"


def test_plot_title_label():
    assert ax.title.get_text() == "my_title"


def test_axis_object():
    assert type(ax) == maplotlib.axes.ax


def test_figure_object():
    assert type(fig) == matplotlib.axes.ax
```

Run the tests with pytest

```text
> pytest tests/test_plot.py
```

The output should look something like below:

```text
collected 5 items                                                     

tests/test_plot.py .                                 [100%]

==================== 5 passed in 3.58s ====================

```

## Run all the tests

We can run all the tests by passing the whole ```tests/``` directory to pytest

```text
> python -m pytest tests/
```

The output should look something like below:

```text

```

## Wrap-Up

In this post we tested a scientific script using pytest. We did this in a couple of steps. 

 * convert Jupyter notebook to a .py-file
 * divide .py-file up into functions
 * test Python version and dependancies
 * test the script doesn't change the data
 * test the analysis functions
 * test the plot

Tests like the one's shown in this post could be written for scripts written by scientists that follow the same basic steps of data injest and cleaning, analysis, and plotting.
