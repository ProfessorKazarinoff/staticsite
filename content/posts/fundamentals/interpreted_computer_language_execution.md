Title: Execution of an interpreted computer language
Date: 2017-11-21 10:20
Modified: 2017-11-21 10:21
Status: Draft
Category: Orientation
Tags: python, programming language
Slug: executing-interpreted-computer-language
Authors: Peter D. Kazarinoff
Summary: Execution of an interpreted computer language can be described as opperating in three steps. A source file is created, the source is converted into bytecode by an interperater, then the bytecode is run


Running a script of an interpreted computer language like Python happens in three steps:

1. A source text file is created

2. the source text file is converted into bytecode by an interpreter

3. The bytecode is run. 

### 1. Create the source text file

First the source file is created in human-readable text using a text editor. If this file is a Python script, it is appended with the **_.py_** extension. The text file can be created in any text editor, this could be idle, spyder, gedit, notepad, Windows Code Editor or another text editing program.  The source file contains Python statements and Python sytax and can reference other Python modules and **_.py_** files. 

### 2. Load text **_.py_** file into a Python interpreter.

To the user, this happens automatically when you push **run** in idle or spyder or type ```python myscript.py``` at the command prompt, where ```myscript.py``` is the source text file. The Python interpreter converts the text-based **_.py_** file into _byte code_. Byte code is a low level, more machine-readable version of the text **_.py_** file created by the Python interpreter.  The byte code files are typically stored is a directory called **_\__pycache\___**" and saved as **_.pyc_** files. If you open up these **_.pyc_** file or collection of **_.pyc_**, **_.pyo_** and  **_.pyd_** files. If you open any of these files, they will look kind of like nonsense, but remember they are bytecode and not meant to be read or editied by people.


### 3. Run the interpreted code

After the byte code is created, the code is run. Speaking generally, the code is run line by line until the script completes or runs into an error. If only half of the script will run before an error, that part of the script will run.  The second part of the script will not. If there are no errors, the entire script runs. The creation of the bytecode and running of the bytecode are two separate steps. These two steps happen seamlessly to the user.  You can confirm these are two different steps by writing a script with an error in the first line. When "run" this script will create a **_.pyc_** file in the \__pycache\__ directory, even though no lines of the script are executed and only an error is produced as output.
 
 