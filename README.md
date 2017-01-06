# msgBoxPy
Simple Cross-platform Python Message and Dialog Boxes Using the Tkinter Standard Library

## Purpose and Background
I just needed a simple, small, and easy way to display information, warnings, get input, select a file or directory, or ask a simple response question in a GUI format for my Python scripts. Sure there are many great third party modules I could use that are much more sophisticated, but I prefer to stay as close to the standard Python library as possible and only needed some basic GUI options. That's why I pieced together msgBoxPy's examples to use [Tkinter](https://wiki.python.org/moin/TkInter), included in the standard Python library, to show cross-platform message, input, and dialog boxes.

**The message boxes available are:**
* Information
* Warning
* Error
* Yes/No (which returns an answer of 'yes' or 'no')
* Ok/Cancel (which returns True or False)
* Retry/Cancel (which returns True or False)

**The input boxes available are:**
* String Input Box (returns the string if entered, otherwise returns 'empty' or 'cancel')
* Integer Input Box (returns a validated integer, otherwise returns 'cancel')

**The dialog boxes available are:**
* Select Filename (returns full path to file selected)
* Save As Filename (returns full path to file and name for saving)
* Select Directory (returns full path to directory selected)

![alt text](https://github.com/lotspaih/msgBoxPy/blob/master/ex_msgBoxPyU.png "Example Image")

## Requirements
* [ ] Python 3.4 or higher (*with Tkinter in Standard Library*)

Tested with Windows 7 SP1 x64, Ubuntu 16.04 x64, and OSX 10.11.6

## Installation
No install required. Just copy the msgBoxPy.py file to the same directory as your Python script and import it, or copy and paste the examples from within the msgBoxPy.py file directly into your own script and modify as needed.

## Example Use
Copy msgBoxPy.py into the same directory as your Python script and import it into your script:
```python
import msgBoxPy

msgBoxPy.infobox('Title', 'Here is my info message.') # Displays an information box with OK button
msgBoxPy.warningbox('Title', 'Here is my warning message!') # Displays a warning box with OK button
msgBoxPy.errorbox('Title', 'Here is my error message!') # Displays an error box with OK button

answer = msgBoxPy.integerbox(title='Your Age?', prompt='Enter your age: ') # Displays Integer Input
if answer == 'cancel': # Cancel button was selected
    msgBoxPy.errorbox(title='Error', message='Cancelled!')
else: # Integer was input and returned
    msgBoxPy.infobox(title='Your Age?', message='Your age is: ' + str(answer))

answer = msgBoxPy.retrycancelbox(title='Title', message='Empty') # Displays Retry/Cancel box
if not answer: # Answer was False (Cancel button was selected)
    msgBoxPy.warningbox('Retry?', 'You have cancelled the retry!')
else: # Answer was True (Retry was selected)
    retryAgain()
    
# Displays Select Directory dialog starting at the initial directory "/etc"
myDirectory = msgBoxPy.selectdirectorybox(initialdir='/etc', mustexist=True)
if not myDirectory: # Cancel button was selected
    msgBoxPy.errorbox(title='Error', message='Cancelled!')
else: # Directory was selected and is returned 
    msgBoxPy.infobox(title='Your Directory', message=myDirectory)
```

Copy and paste the examples from within the msgBoxPy.py file directly into your script and call the function passing the required or optional parameters:
```python
from tkinter import Tk
import tkinter.messagebox as box

def yesnobox(title='Title', message='Empty'):
    '''Show Yes/No messagebox GUI and return answer'''
    Tk().withdraw()
    answer = box.askquestion(title, message)
    return answer  # Returns 'yes' or 'no'
    
response = yesnobox('Title', 'Do you want to continue?') # Call function and pass title and message
print(response) # Shows a 'yes' or 'no' response
```

## TODO
* Clean up script (*make it more "[Pythonic](http://docs.python-guide.org/en/latest/writing/style/)"*)
* Add multiple selection type boxes??? (e.g. lists, checkboxes, radio buttons)

## License
MIT License for msgBoxPy
