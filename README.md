# msgBoxPy
Simple Cross-platform Python Message Boxes Using the Tkinter Standard Library

## Purpose and Background


## Requirements
* [ ] Python 3.4 or higher (*with Standard Library*)

Tested with Windows 7 SP1 x64 and Ubuntu 16.04 x64, but it should work on other operating systems that support Python 3.4 or higher.

## Installation
No install required. Just copy the msgBoxPy.py file to the same directory as your Python script and import it, or copy and paste the examples from within the msgBoxPy.py file directly into your own script.

## Example Use
Copy msgBoxPy.py into the same directory as your Python script and import it into your script:
```python
import msgBoxPy

msgBoxPy.infobox('Title', 'Here is my info message.') # Displays an information box with OK button
msgBoxPy.warningbox('Title, 'Here is my warning message!') # Displays a warning box with OK button
msgBoxPy.errorbox('Title, 'Here is my error message!') # Displays an error box with OK button
```

Copy and paste the examples from within the msgBoxPy.py file directly into your script and call the function passing the required title and message fields:
```python
def yesnobox(title='Title', message='Empty'):
    Tk().withdraw()
    answer = box.askquestion(title, message)
    return answer  # Returns 'yes' or 'no'
    
response = yesnobox('Title', 'Do you want to continue?') # Call function and pass title and message
print(response) # Shows a 'yes' or 'no' response
```

## License
MIT License for msgBoxPy
