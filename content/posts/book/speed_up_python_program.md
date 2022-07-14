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

## Change import statements

## Loop to list comprehension

## Summary
