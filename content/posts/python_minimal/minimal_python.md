Title: Add a CNAME file to a Pelican blog
Date: 2020-06-26 19:36
Modified: 2020-06-26 19:50
Status: Draft
Category: Python
Tags: python, minimal, web assembly, wasm
Slug: minimal-python
Authors: Peter D. Kazarinoff

This post contains my thoughts on building a minimal Python distribution. A minimal Python distribution could be used by other tools to compile a Python program down to webassembly or just be a vary small and contained Python installation for other purposes. 

## A Minimal Python Interpreter

A minimal Python Interpreter has to be able to do the following

 * run a Python program (a .py file) from the command line
 * install python packages from GitHub

That's it. Nothing more

## What's not Included

The following things are not included in the minimal Python Interpreter

## Pip

Pip will need to be the first thing installed so other things can be installed. Pip is intalled from Github and pulled in somehow. 

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Pip expects all of the imports below to work:

```
import os.path
import pkgutil
import shutil
import sys
import struct
import tempfile
```

So built into the Python minimal distribution would need to be all of these packages. It would also need the functionality without any additional pip install downloads to run the pip install .py script. So maybe including pip with the minimal interpreter makes sense because you will always have to use it. On the other had, not including pip means this is closer to a "True" minimum Python Interpreter and if users have to pip install and import all sorts of built in or standard library stuff, downloading pip and running the pip install script isn't too bad. So that sort of means that the keywords used in the pip install script need to work:

import, as, from, with, open, if, for, and, def, etc

and the built in types are needed: dict, int, set, list


### No Standard Library Modules

None of the modules from the Standard Library are included. This means no math, pathlib, statistics, json or any other standard library module. All of these could be installed using pip install wasm-math, pip install wasm-pathlib, pip install wasm-json. Slowly the Standard Library modules would be added to PyPI. Some older, less useful modules will probably never be added.

### No REPL

The Python REPL is not included. It could be added with pip using pip install wasm-repl

### No Built-in Functions

None of the Built-in Functions are part of the minimal interpreter. Each of these functions need to be installed on their own. For exampel pip install wasm-abs or pip install wasm-min

abs()
delattr()
hash()
memoryview()
set()
all()
dict()
help()
min()
setattr()
any()
dir()
hex()
next()
slice()
ascii()
divmod()
id()
object()
sorted()
bin()
enumerate()
input()
oct()
staticmethod()
bool()
eval()
int()
open()
str()
breakpoint()
exec()
isinstance()
ord()
sum()
bytearray()
filter()
issubclass()
pow()
super()
bytes()
float()
iter()
print()
tuple()
callable()
format()
len()
property()
type()
chr()
frozenset()
list()
range()
vars()
classmethod()
getattr()
locals()
repr()
zip()
compile()
globals()
map()
reversed()
__import__()
complex()
hasattr()
max()
round()

No Built-in Classes

None of the built-in classes are installed by default in the minimal Python Interpreter. These classes can be installed with pip install wasm-Int and pip install wasm-Dict pip install wasm-List. 

Could be that When the type is installed, the associated function is installed at the same time. So pip install wasm-int installs the int type as well as the int() function. 

Or could be pip install wasm-Int for the int type and pip install wasm-int for the int() funciton.

Set Types - frozenset, set
Mapping Types - dict
Immutable Sequence Types - string, tuple, bytes
Mutable Sequence Types - list
Number Types - integer, float, complex
Boolean Types - bool (True, False), None, NotImplemented


Operational Kind of Types
functions - def
classes - class
contextmanager - used when a with statement is called: with open('file.txt','r') as f:
range
Ellipsis - used for slicing like a[1:5]

## Key Words

Almost none of the Python Key Words work without being imported. These can be imported with pip install wasm-import or pip install wasm-for. Exceptions are: import, from, as. These keywords are needed to import the others.

and
as - needed in minimal
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from - needed in minimal
global
if
import - needed in minimal
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield

## No Import This and import antigravity

No import this or import antigravity. Can pip install them with pip install wasm-this, pip install wasm-antigravity

## No character sets are included

No character sets are included. If you want to use letters or numbers you need to pip install wasm-ascii, pip install wasm-utf8. This means you can't even write a = 2 without an import first. Maybe from wasm-ascii import a,=,2. Maybe the ascii character set is included by default.

## There is a web assemly complier

You can install a module called wasm-complier using pip install wasm-complier. The complier bundles up the Python minimal interpreter and all of the pip installed modules. Can use it:

```
from wasm-complier import Complier
from wasm-with import with
from wasm-open import open

c = Complier(**kwargs)
with open('main.py','r') as f:
    wasm = c.compile(f)
with open('run.wasm','rb') as f:
    wasm.output_binary(f)
```

## There is an idea of a minimal standard requirements.txt file