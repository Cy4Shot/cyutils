# CyUtils
 
 CyUtils is an all purpose package library for python. It currently adds Colored Text, Message Boxes, Extra List Functions, Ciphers.
 CyUtils will soon have support for Vector2 and Vector3s.

## Installation

You can install CyUtils with <a href="https://pip.pypa.io/en/stable/installing/">pip</a>! Once you have installed pip, open Command Prompt or Powershell and type:
```
pip install cyutils
```

Now at the top of your python library add:
```python
import cyutils
```

## Colored Text
To print colored text, you first need to import the colored text module:
```python
from cyutils.tools import colored_text
```
You can then use the `clrprint()` function to print colored text:
```python
from cyutils.tools import colored_text

colored_text.clrprint("<Text goes here>", "red")
```

The colored text module supports a wide range of colors:
- standard
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
