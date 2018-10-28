Title: Installing Jupyter on a Chromebook
Date: 2018-10-28 10:30
Modified: 2018-10-28 10:30
Status: draft
Category: chromebook
Tags: python, chromebook, installation, jupyter
Slug: installing-jupyter-on-a-chromebook
Authors: Peter D. Kazarinoff

## Why Jupyter notebooks on a Chromebook?

## Open Termux

## Install Numpy, matplotlib, and pandas

We'll start off installing numpy first. This is going to take a while. It took my little chromebook over 10 minutes and I wasn't sure that it was still working during the process. For me numpy 1.12 did not install, but numpy 1.15 (the current version as of writing this post) did install.

```text
$ LDFLAGS="-lm -lcompiler_rt" pip install numpy==1.15
```

```text
$ LDFLAGS="-lm -lcompiler_rt" pip install matplotlib
```

need to also install xlrd library for excel to import .xls and .xlsx data files.

## Install Jupyter

## Open a Jupyter notebook
