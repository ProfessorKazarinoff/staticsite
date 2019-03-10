Title: Building a Jupyter Notebook Conversion App with PyInstaller, nbconvert and Gooey
Date: 2019-03-10 09:20
Modified: 2019-03-10 09:21
Status: draft
Category: jupyter
Tags: jupyter, python, jupyter notebook, nbconvert, gooey
Slug: building-a-jupyter-notebook-conversion-app-pyinstaller
Authors: Peter D. Kazarinoff

In this post, we will run through how to build a Jupyter Notebook conversion App with PyInstaller, nbconvert and Gooey. The reason I wanted to build this App is that I write and save the lab instructional materials for one of my courses in Jupyter Notebooks. But I need to post .pdf's for students to read, not .ipynb notebook files. Therefore, I need to be able to convert the Jupyter notebooks into .pdf's. Jupyter created an nbconvert utility which converts Jupyter notebooks to .pdf's, but the template used by default does not produce course materials in the proper format.

I built a GUI app with a Python package called Gooey to assist with the process, but each time I need to convert a Jupyter notebook to a .pdf, I have to:
 
  * open the Anaconda Prompt
  * activate a virtual environment
  * run the proper Python file

It would be more convenient to click on a .exe file and run the notebook converted in one step. This post details the process I used to create a Windows app (a .exe file) that converts Jupyter notebook .ipynb files into .tex files.

[TOC]

## Converting .ipynb files to .tex files using nbconvert

## A Gui App built with Gooey to convert .ipynb file to .tex

## Summary

In this post...