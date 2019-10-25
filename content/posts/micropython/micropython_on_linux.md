Title: Building Micropython for Linux
Date: 2019-10-24 09:01
Modified: 2019-10-24 09:01
Status: Draft
Category: micropython
Tags: python, micropython, linux
Slug: building-mircopython-for-linux
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 9
Summary: This is the nineth part of a multipart series on Micropython. In this post of the series, we will build micropython for Linux and run micropython on linux

This is the nineth part of a multipart series on Micropython. 

## Summary of Steps:

1. Go to the den and use the Linux Desktop running Ubuntu 16.04
2. Install dependancies
3. Build the Micropython firmware
4. Upload the firmware to the ESP-01
5. Test out the Micropython REPL
6. A neat buried function in the Micropython firmware


### 1. Go to the den and use the Linux Desktop running Ubuntu 19.04

The computer I used to build MicroPython for Linux and run MicroPython for Linux is an Ubuntu 19.04 desktop. I recently build this desktop using a Ryzen 5 processor and 16 GB of RAM. 

### 2. Install the ESP Open SDK

In order to build the Micropython for Linux, a couple of dependancies are required. The dependancies can be instaled with **apt**, the Ubuntu/Debian package manager. According the the [GitHub page for MicroPython](https://github.com/micropython/micropython#external-dependencies)

 > Building MicroPython ports may require some dependencies installed.
   
   For Unix port, libffi library and pkg-config tool are required. On Debian/Ubuntu/Mint derivative Linux distros, install build-essential (includes toolchain and make), libffi-dev, and pkg-config packages.

```text
sudo apt-get install build-essential libffi-dev pkg-config
```

