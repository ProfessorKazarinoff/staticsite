Title: Thoughts on How to Test Science Code
Date: 2020-02-21 08:11
Modified: 2020-02-21 08:11
Status: dract
Category: Python
Tags: engineering,testing
Slug: how-to-test-science-code
Authors: Peter D. Kazarinoff

![fishing net]({static}/posts/testing_science_code/images/fishing-net.jpg)

I have been at a couple meetups (at PyData PDX) and heard a few podcasts (TalkPython) that had a theme of:

 > **"How do we bring software design princpals into science?"**

This got me thinking. There are a couple ways software design could be incorporated into science. The science I'm thinking about deals with the collection and analysis of data (that's almost all science right?). A few practices that could be incorporated are below.

## Version Control

Instead of -final.xlsx and -final2.xlsx and -final_v2_reviewed.xlsx, use a version control system like git and make meaningful commit messages. 

## Code Review

When an analysis is completed, review it with a partner. Have someone else review your code, have some one else run the same code on their computer and give you structured feed-back about it. Scientists have practice reviewing paper drafts, use that experience to help review analysis that includes code.

## Portability and Packaging



## Break code up into modules and functions


## Testing

So this is the main reason I wanted to write this post. How to incorporate software testing in science data analysis. I have a couple ideas.

### A sample script

Below is a sample Python script that reads in an excel file of data, plots the data and then outputs two calculated values. In this case the data is from Field Effect Transistors made from semiconducting polymers, but the same ideas with testing could be applied to a script that does something different. Very often science analysis comes down to a couple steps:

 * reading in raw data from a file or many files
 * cleaning or reorganizing the data in some way
 * running calculations on the data
 * creating a figure that demonstrates the results

```python
# code raw
```

 ### Idea 1. Break the script up into functions

 ![streamlit bokeh heroku]({static}/posts/testing_science_code/images/kids-holding-hands.jpg)

The first thing to do is break the script up into functions. If you don't know where to start, use the four bullet points above to help guide where to break up the one long script into 3 or 4 pieces. Don't worry if all that happens is that you have four sections, each section is a function and each function has no inputs and no outputs. End the script with a main function.

 ```python
 # code with functions
```

### Idea 2. Remove all hard-coded file names

Next, try to remove all hard-coded file names. If you renamed your data file my-data_v2.csv, would your script still work? If not, break the file name into a variable first, and then make the file name be included as a parsed argument when the file is called.

 ```python
 # code with argparse
```

### Idea 3. Your code should not modify the data

When your code runs, it should not modify, rename, rewrite or otherwise change the originol data. If that happens as a result of your script, take it out.

```python
# code that doesn't modify the data
```

### Idea 4. Consider inputs and outputs of your functions

Now that we removed all hard-coded file names and make sure that the data wasn't modified by the code, is it any clearer what the input and output of our functions are? At the very least, have your functions return ```True``` at the end. For a function that produces a plot, make the output be ```fig``` and ```ax``` objects.

```python
# code that have function inputs and outputs
```

### Idea 5. Test each function

Now we are going to use pytest to test each function. Some of the functions can have expected input and output. Some functions may need an example file passed to them.

### Idea 6. Test the main() function

### Idea 7. Set the version of Python your script works with, ensure that version of Python is used to run it

#### Sub Idea 7a. Set the operating system your script runs on, ensure that operating system is running the script

### Idea 8. Test the fig and ax objects

### Idea 9. Test the code against two different data files

## Conclusion



