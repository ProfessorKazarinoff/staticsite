Title: How to speed up a Python program
Date: 2022-06-14 10:30
Modified: 2022-06-14 10:30
Status: draft
Category: book
Tags: python, book, speed
Slug: how-to-speed-up-a-python-program
Authors: Peter D. Kazarinoff
Summary: In this post, I'll discuss how I went about speeding up a Python program. The results come from my investigation of ways to make my book Problem Solving with Python 3.9 Edition build faster from source. The basic Python program takes a directory of Jupyter notebooks and converts them into a .tex file. See how the changes I made effected the speed of the Python program.

## Application 

This post is an investigation of how to speed up a Python program. The methods described here are only applicable to the specific program I'm running. I would not take these results to correspond to any Python program. This is about speeding up my specific program. However, the methods I tried could be replicated on other Python programs in order to speed them up.

The program I'm trying to speed up is my book building program. The basic Python program takes a directory of Jupyter notebooks and converts them into a .tex file. The main part of the program converts a list of Jupyter notebooks into one big Jupyter notebook and then converts this big Jupyter notebook into a .tex file.

## Baseline

Before we make any speed improvements, let's take a baseline. All timing runs were tested on a MacBook M1 Pro running Below is an average of 5 runs of the Python program.

MacBook M1 Pro
10 Cores (8 performance and 2 efficiency)
16 GB Memory
MacOS Monterey 12.4
Python 3.9.4

Baseline: 

45.411109 seconds
44.798712 seconds
44.590597 seconds
45.154676 seconds
46.116601 seconds

Mean: 45.214339 seconds

## Anthony Shaw's anti-pattern tester

To figure out how to speed up this Python program, I used Anthony Shaw's **perflint** tool. This tool was presented at PyCon US 2022 and I enjoyed the talk on performance anit-patterns. **perflint** isn't a speed test. What **perflint** does is analyze your code for performance anti-pattersn (things that slow down your program) and highlight them.

You can install **perflint** with **pip**:

```text
$ pip install perflint
```

Once installed, you can call **perflint** from the command line and pass it a Python file or directory. Since I am testing my book building program, I ran **perflint** against my ```tasks.py``` file that uses **invoke** to create a very simple command-line interface to build the book.

```text
perflint tasks.py
```

**perflint** outputs a list of lines / structures in the code that could be rewritten to speed up the program's execution. My list of potential speed-ups is below:

```text
************* Module tasks
tasks.py:134:17: W8205: Importing the "getcwd" name directly is more efficient in this loop. (dotted-import-in-loop)
tasks.py:135:17: W8205: Importing the "getcwd" name directly is more efficient in this loop. (dotted-import-in-loop)
tasks.py:131:14: W8301: Use tuple instead of list for a non-mutated sequence (use-tuple-over-list)
tasks.py:148:36: W8301: Use tuple instead of list for a non-mutated sequence (use-tuple-over-list)
tasks.py:149:36: W8301: Use tuple instead of list for a non-mutated sequence (use-tuple-over-list)
tasks.py:244:15: W8205: Importing the "exists" name directly is more efficient in this loop. (dotted-import-in-loop)
tasks.py:244:15: W8205: Importing the "path" name directly is more efficient in this loop. (dotted-import-in-loop)
tasks.py:244:30: W8205: Importing the "join" name directly is more efficient in this loop. (dotted-import-in-loop)
tasks.py:244:30: W8205: Importing the "path" name directly is more efficient in this loop. (dotted-import-in-loop)
tasks.py:246:25: W8205: Importing the "listdir" name directly is more efficient in this loop. (dotted-import-in-loop)
tasks.py:247:20: R8203: Try..except blocks have an overhead. Avoid using them inside a loop unless you're using them for control-flow. (loop-try-except-usage)
tasks.py:257:51: W8205: Importing the "exc_info" name directly is more efficient in this loop. (dotted-import-in-loop)
tasks.py:255:24: W8201: Consider moving this expression outside of the loop. (loop-invariant-statement)
tasks.py:258:24: W8201: Consider moving this expression outside of the loop. (loop-invariant-statement)
tasks.py:291:21: W8205: Importing the "listdir" name directly is more efficient in this loop. (dotted-import-in-loop)
tasks.py:291:12: W8401: Use a list comprehension instead of a for-loop (use-list-comprehension)

------------------------------------------------------------------
Your code has been rated at 9.08/10 (previous run: 9.75/10, -0.67)
```

I think these suggestions fit into a couple of buckets

Bucket 1: Imports and calling functions

**perflint** called out a number of import / calling function optimizations. For example, one is ```mporting the "getcwd" name directly is more efficient in this loop.```. This means that I called ```os.getcwd()``` in the body of the program. Instead, I can import ```getcwd()``` from Python's ```os``` module and then just call ```getcwd()```. There are couple more items from **perflint** like this such as: ```os.path```, ```os.path.join``` and ```os.listdir```.

Bucket 2: Use a tuple instead of a list

**perflint** listed a couple of mutable sequenes (lists) that could be converted to tuples. This is pretty easy change if the lists are not ever modified.

Bucket 3: Use a list comprehension instead of a loop

**perflint** found a for loop that adds an item to a list. If this for loop is converted to a list comprehension, that could speed up the code. I expect this change will be the hardest one to implement.

## Change import / function call statements

The first change I'll try is to convert function calls from something like ```os.path.join()``` into just a fuction call of ```join()``` with the addition of an import statement at the top of the program ```from os.path import join```.

After this change, the program speed was:

45.158873 seconds
45.777669 seconds
45.541985 seconds
44.966410 seconds
45.516561 seconds

mean: 45.3922996 seconds

The mean is higher than before the function call replacements, but given the spread of the data compared to the difference in mean, I don't think the function call reassignments helped speed up the program in any measureable way.

## Use tuples instead of lists

Next, I'm going to try replacing lists with tuples. For example, there is a list of all the extra .tex files that need to be copied when the book is built. This list can be converted into a tuple. The list of .tex files that need to be copied don't change when the program runs, so converting the list to a tuple shouldn't be a problem.

## Loop to list comprehension

## Summary
