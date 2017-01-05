# msgBoxPy
Simple Cross-platform Python Message Boxes Using the Tkinter Standard Library

## Purpose and Background
I just needed a simple, small, and quick way to display information, warnings, or ask a simple yes or no question in a GUI format for my Python scripts. Sure there are many great third party modules I could use (e.g. [pyautogui](https://github.com/asweigart/pyautogui)), but I prefer to stay as close to the standard Python library as possible for most of my scripts. That's why msgBoxPy uses the [Tkinter](https://wiki.python.org/moin/TkInter) standard library to show cross-platform message boxes.

The message boxes available are:
* Information
* Warning
* Error
* Yes/No (which returns an answer of 'yes' or 'no')
* Ok/Cancel (which returns True or False)
* Retry/Cancel (which returns True or False)

The input boxes available are:
* String Input Box (returns the string if entered, otherwise returns 'empty' or 'cancel')
* Integer Input Box (returns an integer)

The dialog boxes available are:
* Select Filename (returns full path to file selected)
* Save As Filename (returns full path to file for saving)
* Select Directory (returns full path to directory selected)

![alt text](https://github.com/lotspaih/msgBoxPy/blob/master/ex_msgBoxPyU.png "Example Image")

## Requirements
* [ ] Python 3.4 or higher (*with Tkinter in Standard Library*)

Tested with Windows 7 SP1 x64, Ubuntu 16.04 x64, and OSX 10.11.6

## Installation
No install required. Just copy the msgBoxPy.py file to the same directory as your Python script and import it, or copy and paste the examples from within the msgBoxPy.py file directly into your own script.

## Example Use
Copy msgBoxPy.py into the same directory as your Python script and import it into your script:
```python
import msgBoxPy

msgBoxPy.infobox('Title', 'Here is my info message.') # Displays an information box with OK button
msgBoxPy.warningbox('Title', 'Here is my warning message!') # Displays a warning box with OK button
msgBoxPy.errorbox('Title', 'Here is my error message!') # Displays an error box with OK button

answer = msgBoxPy.retrycancelbox(title='Title', message='Empty')
if not answer:
    msgBoxPy.warningbox('Retry?', 'You have cancelled the retry!')
else:
    retryAgain()
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
* Add simple string and integer input options
* Add file select and file save dialog options
* Clean up script (*make it more "[Pythonic](http://docs.python-guide.org/en/latest/writing/style/)"*)

## License
MIT License for msgBoxPy
