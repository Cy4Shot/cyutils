# CyUtils
 
 CyUtils is an all purpose package library for python. It currently adds Colored Text, Message Boxes, Extra List Functions, Ciphers.
 CyUtils will soon have support for Vector2 and Vector3s.

# Main menu:
- <a href="https://github.com/Cy4Shot/cyutils#installation">Installation</a>
- <a href="https://github.com/Cy4Shot/cyutils#colored-text-module">Colored Text Module</a>
- <a href="https://github.com/Cy4Shot/cyutils#message-boxes-module">Message Boxes Module</a>
- <a href="https://github.com/Cy4Shot/cyutils#custom-error-module">Custom Error Module</a>
- <a href="https://github.com/Cy4Shot/cyutils#vector2-module">Vector2 Module</a>
- <a href="https://github.com/Cy4Shot/cyutils#lists-module">Lists Module</a>

## Installation

You can install CyUtils with <a href="https://pip.pypa.io/en/stable/installing/">pip</a>! Once you have installed pip, open Command Prompt or Powershell and type:
```
pip install cyutils
```

Now at the top of your python library add:
```python
import cyutils
```

## Colored Text Module
To print colored text, you first need to import the colored text module:
```python
from cyutils.io import colored_text
```
You can then use the `clrprint()` function to print colored text:
```python
from cyutils.io import colored_text

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

## Message Boxes Module
The Message Boxes module allows you to create a windows message box using VB overloads! It creates a temporary vbscript and executes it to create a message box.
To begin, you need to import the message boxes module:
```python
from cyutils.io import message_boxes as mb
```
This package will allow you to create a message box with a simple `message_box()` function.
> **NOTE: THIS FUNCTION WILL ONLY WORK ON WINDOWS OPERATING SYSTEMS**

```python
from cyutils.io import message_boxes as mb

mb.message_box("<Window Title>", "<Box Contents>", "< (OPTIONAL) VB Overloads>")
```

For the VB Overload you can either add text overloads:
> e.g. "vbOkOnly+vbCritical"

Or get the sum of the overloads that you want from the table below:

Constant | Value | Description
--- | --- | ---
vbOKOnly | 0 | Display OK button only.
vbOKCancel | 1 | Display OK and Cancel buttons.
vbAbortRetryIgnore | 2 | Display Abort, Retry, and Ignore buttons.
vbYesNoCancel | 3 | Display Yes, No, and Cancel buttons.
vbYesNo | 4 | Display Yes and No buttons.
vbRetryCancel | 5 | Display Retry and Cancel buttons.
vbCritical | 16 | Display Critical Message icon.
vbQuestion | 32 | Display Warning Query icon.
vbExclamation | 48 | Display Warning Message icon.
vbInformation | 64 | Display Information Message icon.
vbDefaultButton2 | 256 | Second button is default.
vbDefaultButton3 | 512 | Third button is default.
vbDefaultButton4 | 768 | Fourth button is default.
vbSystemModal | 4096 | System modal; all applications are suspended until the user responds to the message box.
vbMsgBoxHelpButton | 16384 | Adds Help button to the message box.
vbMsgBoxSetForeground | 65536 | Specifies the message box window as the foreground window.
vbMsgBoxRight | 524288 | Text is right-aligned.
vbMsgBoxRtlReading | 1048576 | Specifies text should appear as right-to-left reading on Hebrew and Arabic systems.

## Custom Error Module
The Custom Error module allows you to create an error without using `raise` or showing the lines of code that the error occured in. To begin, import the Custom Error module:
```python
from cyutils.io.custom_error import CustomError
```
The title of an error is the name of the error you want to throw. This is not restricted to default python error names, it can be anything! You can throw a basic error like this:
```python
from cyutils.io.custom_error import CustomError

CustomError("<Title of Error>").throw("<Error Message>")
```
The custom error can also be stored as a variable and thrown later:
```python
from cyutils.io.custom_error import CustomError

myError = CustomError("<Title of Error>")

#SOME CODE HERE

myError.throw("<Error Message>")
```
You can also configure the error so that it doesn't exit after sending the message to the console:
```python
from cyutils.io.custom_error import CustomError

myError = CustomError("<Title of Error>", exitOnError=False)
myError.throw("<Error Message>")

print("HELLO WORLD") # HELLO WORLD
```

## Vector2 Module
The Vector2 Module allows the creation and manipulation of 2 dimensional vectors in python. To begin, import the Vector2 module:
```python
from cyutils.tools.math import Vector2
```
You can now create a vector with a simple command. The following code creates the vector (2, 3) and assigns it to a variable, `x`:
```python
from cyutils.tools.math import Vector2

x = Vector2(2, 3)
```
You can now manipulate this with standard operators, such as `+`, `-`, `*`, `/`, `//` and check if vectors are equal with `==`.
> Using a standard operator between two vector will do the operation to their X and Y values, whereas doing a standard operation between a vector and an int or float will apply the operation to both X and Y values with the said int or float.
The Vector2 Module also contains some functions. You can see them below:
### Vector2 Module: Functions
A menu of all the functions is listed below:
- <a href="https://github.com/Cy4Shot/cyutils#magnitude">Magnitude</a>
- <a href="https://github.com/Cy4Shot/cyutils#normalize">Normalize</a>
- <a href="https://github.com/Cy4Shot/cyutils#distance">Distance</a>
- <a href="https://github.com/Cy4Shot/cyutils#lerp">Lerp</a>
- <a href="https://github.com/Cy4Shot/cyutils#up">Up</a>
- <a href="https://github.com/Cy4Shot/cyutils#down">Down</a>
- <a href="https://github.com/Cy4Shot/cyutils#left">Left</a>
- <a href="https://github.com/Cy4Shot/cyutils#right">Right</a>
- <a href="https://github.com/Cy4Shot/cyutils#one">One</a>
- <a href="https://github.com/Cy4Shot/cyutils#zero">Zero</a>
- <a href="https://github.com/Cy4Shot/cyutils#positive-infinity">Positive Infinity</a>
- <a href="https://github.com/Cy4Shot/cyutils#negative-infinity">Negative Infinity</a>
#### Magnitude
You can use the `magnitude` function to get the magnitude of a vector. You can see an implementation below:
```python
from cyutils.tools.math import Vector2

myVector = Vector2(2, 3)
print(myVector) # Vector2: (2, 3)

magnitude = myVector.magnitude()
print(magnitude) # 3.605551275463989
```
You can also get the square magnitude of a vector by using the `sqrMagnitude` function. This is useful if you want to compare two vectors as this function is faster than the `magnitude` function. You can see an implementation below:
```python
from cyutils.tools.math import Vector2

myVector = Vector2(2, 3)
print(myVector) # Vector2: (2, 3)

magnitude = myVector.sqrMagnitude()
print(magnitude) # 13
```
#### Normalize
You can use the `normalize` function to get the normalized Vector. That is a Vector where all the values are between 0 and 1. You can see an implementation below:
```python
from cyutils.tools.math import Vector2

myVector = Vector2(2, 3)
print(myVector) # Vector2: (2, 3)

myVector.normalize()
print(myVector) # Vector2: (0.5547001962252291, 0.8320502943378437)
```
You can also use the `normalized` function which returns a new vector instead of changing the old one. You can see an implementation below:
```python
from cyutils.tools.math import Vector2

myVector = Vector2(2, 3)
print(myVector) # Vector2: (2, 3)

normalizedVec = myVector.normalized()
print(normalizedVec) # Vector2: (0.5547001962252291, 0.8320502943378437)
```
#### Distance
You can use the `distance` function to calculate the distance between two Vector2s. You can see an implementation below:
```python
from cyutils.tools.math import Vector2

myFirstVector = Vector2(2, 3)
print(myFirstVector) # Vector2: (2, 3)

mySecondVector = Vector2(8, 10)
print(mySecondVector) # Vector2: (8, 10)

distance = Vector2.distance(myFirstVector, mySecondVector)
print(distance) # 9.219544457292887
```
You can also use the non-static `distanceTo` function to calculate the distance between itself and another Vector2. You can see an implementation below:
```python
from cyutils.tools.math import Vector2

myFirstVector = Vector2(2, 3)
print(myFirstVector) # Vector2: (2, 3)

mySecondVector = Vector2(8, 10)
print(mySecondVector) # Vector2: (8, 10)

distance = myFirstVector.distanceTo(mySecondVector)
print(distance) # 9.219544457292887
```
#### Lerp
You can use the `lerp` function to lerp on the line between two different vectors. You can see an implementation below:
```python
from cyutils.tools.math import Vector2

myFirstVector = Vector2(2, 3)
print(myFirstVector) # Vector2: (2, 3)

mySecondVector = Vector2(8, 10)
print(mySecondVector) # Vector2: (8, 10)

lerped = Vector2.lerp(myFirstVector, mySecondVector, 0.8)
print(lerped) # Vector2: (3.1999999999999997, 4.4)
```
#### Up
The `up` function returns the Vector (0, 1):
```python
from cyutils.tools.math import Vector2

vector = Vector2.up()
print(vector) # Vector2: (0, 1)
```
#### Down
The `down` function returns the Vector (0, -1):
```python
from cyutils.tools.math import Vector2

vector = Vector2.down()
print(vector) # Vector2: (0, -1)
``` 
#### Left
The `left` function returns the Vector (-1, 0):
```python
from cyutils.tools.math import Vector2

vector = Vector2.left()
print(vector) # Vector2: (-1, 0)
``` 
#### Right
The `right` function returns the Vector (1, 0):
```python
from cyutils.tools.math import Vector2

vector = Vector2.right()
print(vector) # Vector2: (1, 0)
``` 
#### One
The `one` function returns the Vector (1, 1):
```python
from cyutils.tools.math import Vector2

vector = Vector2.one()
print(vector) # Vector2: (1, 1)
``` 
#### Zero
The `zero` function returns the Vector (0, 0):
```python
from cyutils.tools.math import Vector2

vector = Vector2.zero()
print(vector) # Vector2: (0, 0)
```
#### Positive Infinity
The `positiveInfinity` function returns the Vector (infinity, infinity):
```python
from cyutils.tools.math import Vector2

vector = Vector2.positiveInfinity()
print(vector) # Vector2: (inf, inf)
``` 
#### Negative Infinity
The `negativeInfinity` function returns the Vector (-infinity, -infinity):
```python
from cyutils.tools.math import Vector2

vector = Vector2.negativeInfinity()
print(vector) # Vector2: (-inf, -inf)
```

## Lists Module
The lists module allows for easier manipulation and creation of lists in python. You can import the module like this:
```python
from cyutils.tools import lists
```
The lists module comes with a few functions:
- <a href="https://github.com/Cy4Shot/cyutils#empty-list">Empty List</a>
- <a href="https://github.com/Cy4Shot/cyutils#flatten-list">Flatten List</a>
- <a href="https://github.com/Cy4Shot/cyutils#list-total">List Total</a>
#### Empty List
The `empty list` function allows you to create a multi-dimensional square list, filled with zeros with a single line of code. You can see an implementation below:
```python
from cyutils.tools import lists

list1 = lists.empty_list(5, dimensions=1)
print(list1) # [0.0, 0.0, 0.0, 0.0, 0.0]

list2 = lists.empty_list(3, dimensions=2)
print(list2) # [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

list3 = lists.empty_list(2, dimensions=3)
print(list3) # [[[0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0]]]
```
#### Flatten List
The `flatten list` function allows you to flatten a multidimensional list into a one dimensional list. You can see an implementation below:
```python
from cyutils.tools import lists

multidimensional_list = lists.empty_list(2, dimensions=3)
print(multidimensional_list) # [[[0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0]]]

onedimensional_list = lists.flatten_list(multidimensional_list)
print(onedimensional_list) # [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```
#### List Total
The `list total` function allows you to get the sum of all the ints or floats in a multidimensional list. You can see an implementation below:
```python
from cyutils.tools import lists

myList = lists.empty_list(2, dimensions=3)
myList[0][1][1] = 4
myList[1][0][1] = 3
print(myList) # [[[0.0, 0.0], [0.0, 4]], [[0.0, 3], [0.0, 0.0]]]

total = lists.list_total(myList)
print(total) # 7.0
```