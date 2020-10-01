# CyUtils
 
 CyUtils is an all purpose package library for python. It currently adds Colored Text, Message Boxes, Extra List Functions, Ciphers.
 CyUtils will soon have support for Vector2 and Vector3s.

# Main menu:
- <a href="https://github.com/Cy4Shot/cyutils#installation">Installation</a>
- <a href="https://github.com/Cy4Shot/cyutils#colored-text-module">Colored Text Module</a>
- <a href="https://github.com/Cy4Shot/cyutils#message-boxes-module">Message Boxes Module</a>

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
vbDefaultButton1 | 0 | First button is default.
vbDefaultButton2 | 256 | Second button is default.
vbDefaultButton3 | 512 | Third button is default.
vbDefaultButton4 | 768 | Fourth button is default.
vbSystemModal | 4096 | System modal; all applications are suspended until the user responds to the message box.
vbMsgBoxHelpButton | 16384 | Adds Help button to the message box.
vbMsgBoxSetForeground | 65536 | Specifies the message box window as the foreground window.
vbMsgBoxRight | 524288 | Text is right-aligned.
vbMsgBoxRtlReading | 1048576 | Specifies text should appear as right-to-left reading on Hebrew and Arabic systems.