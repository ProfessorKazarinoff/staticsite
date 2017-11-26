Title: Unicode characters for engineers in Python
Date: 2017-10-10 10:01
Modified: 2017-10-11 10:01
Status: Draft
Category: python
Tags: python, engineering, statistics
Slug: unicode-characters-in-python
Authors: Peter Kazarinoff
JavaScripts: table.js
Stylesheets: table.css



Unicode characters are very useful for engineers. A couple commonly used symbols in engineers include Omega and Delta. We can print these in python using unicode characters. From the Python interperater we can type:

```
>>> print('Omega: \u03A9')
Omega: Ω
>>> print('Delta: \u0394')
Delta: Δ
>>> print('sigma: \u03C3')
sigma: σ
>>> print('mu: \u03BC')
mu: μ
>>> print('epsilon: \u03B5')
epsilon: ε
>>> print('degree: \u00B0')
degree: °
>>> print('6i\u0302 + 4j\u0302-2k\u0302')
6î + 4ĵ-2k̂
```

All of these are unicode characters. Python has support for unicode characters built in. You can check if your system supports it by importing the ```sys``` module and calling the ```sys.getdefaultencoding()``` function

```
>>> import sys
>>> sys.getdefaulencoding()
'utf-8'
```

If you see utf-8, then your system supports unicode characters. To print any chacacter in the Python interpereter, use a ```\u``` to denote a unicode character and then follow this with the character code.  For instance, the code for β is 03B2, so to print β the command is ```print('\u03B2')```. There are a couple of special characters that will combine symbols. A usefull one in engineering is the ```^``` symbol. This is typically used with unit vectors. We can add a hat ```^``` (also called a circumflex) by putting the unicode excape after the letter you want to add a hat to. For example to add a hat to ```i``` the command is ```print('i\u0302'). 

Below is a list of symbols and greek letters and the corresponding unicode escape to produce the character in python. 

### Useful unicode symbols in engineering
|unicode|character|description|
|---|:--:|---|
\u0394 | Δ | GREEK CAPITAL LETTER DELTA
\u03A9 | Ω | GREEK CAPITAL LETTER OMEGA
\u03C0 | π | GREEK SMALL LETTER PI
\u03F4 | ϴ | GREEK CAPITAL THETA SYMBOL
\u03BB | λ | GREEK SMALL LETTER LAMDA
\u03B8 | θ | GREEK SMALL LETTER THETA
\u03B1 | ° | DEGREE SYMBOL
i\u0302	| î | i HAT
j\u0302	| ĵ	| j HAT
k\u0302	| k̂	| k HAT
u\u0302	| û	| u HAT


### Greek lower case letters
|unicode|character|description|
|---|:--:|---|
\u03B1 | α | GREEK SMALL LETTER ALPHA
\u03B2 | β | GREEK SMALL LETTER BETA
\u03B3 | γ | GREEK SMALL LETTER GAMMA
\u03B4 | δ | GREEK SMALL LETTER DELTA
\u03B5 | ε | GREEK SMALL LETTER EPSILON
\u03B6 | ζ | GREEK SMALL LETTER ZETA
\u03B7 | η | GREEK SMALL LETTER ETA
\u03B8 | θ | GREEK SMALL LETTER THETA
\u03B9 | ι | GREEK SMALL LETTER IOTA
\u03BA | κ | GREEK SMALL LETTER KAPPA
\u03BB | λ | GREEK SMALL LETTER LAMDA
\u03BC | μ | GREEK SMALL LETTER MU
\u03BD | ν | GREEK SMALL LETTER NU
\u03BE | ξ | GREEK SMALL LETTER XI
\u03BF | ο | GREEK SMALL LETTER OMICRON
\u03C0 | π | GREEK SMALL LETTER PI
\u03C1 | ρ | GREEK SMALL LETTER RHO
\u03C2 | ς | GREEK SMALL LETTER FINAL SIGMA
\u03C3 | σ | GREEK SMALL LETTER SIGMA
\u03C4 | τ | GREEK SMALL LETTER TAU
\u03C5 | υ | GREEK SMALL LETTER UPSILON
\u03C6 | φ | GREEK SMALL LETTER PHI
\u03C7 | χ | GREEK SMALL LETTER CHI
\u03C8 | ψ | GREEK SMALL LETTER PSI
\u03C9 | ω | GREEK SMALL LETTER OMEGA

### Greek upper case letters
|unicode|character|description|
|---|:--:|---|
\u0391 | Α | GREEK CAPITAL LETTER ALPHA
\u0392 | Β | GREEK CAPITAL LETTER BETA
\u0393 | Γ | GREEK CAPITAL LETTER GAMMA
\u0394 | Δ | GREEK CAPITAL LETTER DELTA
\u0395 | Ε | GREEK CAPITAL LETTER EPSILON
\u0396 | Ζ | GREEK CAPITAL LETTER ZETA
\u0397 | Η | GREEK CAPITAL LETTER ETA
\u0398 | Θ | GREEK CAPITAL LETTER THETA
\u0399 | Ι | GREEK CAPITAL LETTER IOTA
\u039A | Κ | GREEK CAPITAL LETTER KAPPA
\u039B | Λ | GREEK CAPITAL LETTER LAMDA
\u039C | Μ | GREEK CAPITAL LETTER MU
\u039D | Ν | GREEK CAPITAL LETTER NU
\u039E | Ξ | GREEK CAPITAL LETTER XI
\u039F | Ο | GREEK CAPITAL LETTER OMICRON
\u03A0 | Π | GREEK CAPITAL LETTER PI
\u03A1 | Ρ | GREEK CAPITAL LETTER RHO
\u03A3 | Σ | GREEK CAPITAL LETTER SIGMA
\u03A4 | Τ | GREEK CAPITAL LETTER TAU
\u03A5 | Υ | GREEK CAPITAL LETTER UPSILON
\u03A6 | Φ | GREEK CAPITAL LETTER PHI
\u03A7 | Χ | GREEK CAPITAL LETTER CHI
\u03A8 | Ψ	| GREEK CAPITAL LETTER PSI
\u03A9 | Ω | GREEK CAPITAL LETTER OMEGA
\u03F4 | ϴ | GREEK CAPITAL THETA SYMBOL
