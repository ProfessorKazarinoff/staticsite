Title: Thoughts on How to Test Science Code
Date: 2020-02-21 08:11
Modified: 2020-02-21 08:11
Status: draft
Category: Python
Tags: engineering,testing
Slug: how-to-test-science-code
Authors: Peter D. Kazarinoff

![fishing net]({static}/posts/testing_science_code/images/fishing-net.jpg)

I have been at a couple meetups (at PyData PDX) and heard a few podcasts (TalkPython) that had a theme of:

 > **"How do we bring software design princpals into science?"**

This got me thinking... There are a couple ways software design could be incorporated into science. The science I'm thinking about deals with the collection and analysis of data (that's almost all science right?). A few practices that could be incorporated into computer programs that analyze science data are below.

## Version Control

![fishing net]({static}/posts/testing_science_code/images/notebooks.jpg)

Instead of ```myscript-final.xlsx``` and ```myscript-final2.xlsx``` and ```myscript-final_v2_reviewed.xlsx```, use a version control system like **git** and Github.com. If this practice is adopted, scientists need to ensure that meaningful commit messages are incorporated with each code change. Version control could also be used as part of the peer-reviewed paper writing process. 

## Code Review

![fishing net]({static}/posts/testing_science_code/images/map.jpg)

When an analysis is completed, review it with a partner. Have someone else review your code, have some one else run the same code on their computer and give you structured feed-back about it. Scientists have practice reviewing paper drafts, use that experience to help review analysis that includes code.


## Break code up into modules and functions

![fishing net]({static}/posts/testing_science_code/images/package.jpg)

Some scientific code is written in one or two long scripts. Another software design principal to bring to this code is break code up into functions and modules (different files). A long 2000 line script can be broken up into different functions and these functions can be pulled out into different modules, or put into different files. Two rough guidlines:

 * Each file should be able to fit on one screen
 * Each function should be 10 lines or less

These are not hard rules, but something to aim for if you don't know where to start.

The last software design principal we'll talk about in this post is testing. It's a big topic. Here we go.

## Testing

![fishing net]({static}/posts/testing_science_code/images/lab.jpg)

So this is the main reason I wanted to write this post. How to incorporate software testing in science data analysis. I have a couple ideas.

### A sample script

Below is a sample Python script that reads in an excel file of data, plots the data, and then outputs two calculated values. In this case, the data is from a mechanical test frame (a piece of equipment that tests the strength of materials), but the same testing ideas could be applied to a script that analyzes data from another subject area.

Very often scientific code comes down to a couple steps:

 * Read in raw data from a file or many files
 * Clean or reorganize the data
 * Run calculations on the data
 * Create a figure that demonstrates the results

The code below is one long script. In the rest of this post, we are going work on adding tests to this script.

```python
# code raw
```

 ### Idea 1. Break the script up into functions

 ![holding hands]({static}/posts/testing_science_code/images/kids-holding-hands.jpg)

The first thing to do is break the script up into functions. If you don't know where to start, use the four bullet points above to help guide where to break up the one long script into 3 or 4 pieces. Don't worry if all that happens is that you have four sections, each section is a function and each function has no inputs and no outputs. End the script with a main function.

 ```python
 # code with functions
```

### Idea 2. Remove all hard-coded file names

 ![holding hands]({static}/posts/testing_science_code/images/concrete.jpg)

Next, let's try to remove all hard-coded file names. If you renamed your data file ```my-data_v2.csv```, would your script still work? If not, break the file name into a variable first. Next, make the file name be included as a parsed argument when the file is called.

 ```python
 # code with argparse
```

Now the script is run using the command below.

```text
# python analysis.py -i my-data.csv
```

### Idea 3. Your code should not modify the data

![holding hands]({static}/posts/testing_science_code/images/ice.jpeg)

When your code runs, it should not modify, rename, rewrite or otherwise change the originol data. If that happens as a result of your script, take it out.

```python
# code that doesn't modify the data
```

### Idea 4. Consider inputs and outputs of your functions

![holding hands]({static}/posts/testing_science_code/images/pipe.jpeg)

Now that we removed all hard-coded file names and made sure that the data wasn't modified by the code, is it any clearer what the input and output of our functions should be? At the very least, modify your functions tp return ```True``` at the end. For a function that produces a plot, assign the outputs as Matplotlib ```fig``` and ```ax``` objects.

```python
# code that have function inputs and outputs
```

### Idea 5. Test each function

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

### Idea 6. Test the main() function

### Idea 7. Set the version of Python your script works with, ensure that version of Python is used to run it

#### Sub Idea 7a. Set the operating system your script runs on, ensure that operating system is running the script

### Idea 8. Test the fig and ax objects

### Idea 9. Test the code against two different data files

## Conclusion

To wrap up. Some scientific code is difficult to test. But there are things we can do to make the code more portable and incorporate the ideas of software design into scientific code.

To help make a scientific script testable, consider trying the following:

 * break a long script into functions and seperate files
 * include one main fuction
 * assign functions inputs and outputs. If no output makes sense, return ```True```
 * functions which produce plots should output ```fig``` and ```ax``` objects.
