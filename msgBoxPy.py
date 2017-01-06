#! python3
#! /usr/bin/python3
#! /usr/bin/env python3

# Copyright (c) 2016 Mark Lotspaih
# MIT License - https://opensource.org/licenses/MIT

# msgBoxPy - Quick import or reference for making simple GUI messages, input,
#    and dialog boxes.
# USAGE: "import msgBoxPy" or copy the examples (including imports) below.
# VERSION: 01/06/2017

from tkinter import Tk
import tkinter.messagebox as box
from tkinter import filedialog
from tkinter import simpledialog


def infobox(title='Title', message='Empty'):
    '''Show information messagebox GUI'''
    Tk().withdraw()
    box.showinfo(title, message)
    return None


def warningbox(title='Title', message='Empty'):
    '''Show warning messagebox GUI'''
    Tk().withdraw()
    box.showwarning(title, message)
    return None


def errorbox(title='Title', message='Empty'):
    '''Show error messagebox GUI'''
    Tk().withdraw()
    box.showerror(title, message)
    return None


def yesnobox(title='Title', message='Empty'):
    '''Show Yes/No messagebox GUI and return yes or no answer'''
    Tk().withdraw()
    answer = box.askquestion(title, message)
    return answer


def okcancelbox(title='Title', message='Empty'):
    '''Show Ok/Cancel messagebox GUI and returns True for Ok and False for
    Cancel'''
    Tk().withdraw()
    answer = box.askokcancel(title, message)
    return answer


def retrycancelbox(title='Title', message='Empty'):
    '''Show Retry/Cancel messagebox GUI and returns True for Retry and False
    for Cancel'''
    Tk().withdraw()
    answer = box.askretrycancel(title, message)
    return answer


def inputbox(title='Title', prompt='Prompt text:'):
    '''Creates a simple string input box with Ok/Cancel buttons. Ok returns
    the string entered unless the string is empty then "empty" is returned.
    Cancel returns "cancel".'''
    Tk().withdraw()
    enteredString = simpledialog.askstring(title, prompt)
    if enteredString == None:
        return 'cancel'
    elif enteredString == '':
        return 'empty'
    else:
        return enteredString


def integerbox(title='Title', prompt='Prompt text:'):
    '''Creates a simple integer input box with Ok/Cancel buttons. Ok returns
    the integer entered. Cancel returns "cancel".'''
    Tk().withdraw()
    enteredInteger = simpledialog.askinteger(title, prompt)
    if enteredInteger == None:
        return 'cancel'
    else:
        return enteredInteger


def selectfilenamebox(**kwargs):
    '''Creates a select file dialog box and returns path to the file
    selected or returns empty if Cancel was selected.
    Example keyword options are "title" and "initialdir".'''
    Tk().withdraw()
    filePath = filedialog.askopenfilename(**kwargs)
    return filePath


def savefilenamebox(**kwargs):
    '''Creates a save file dialog box and returns path to the file
    selected or name entered. Returns empty if Cancel was selected.
    Example keyword options are "title" and "initialdir".'''
    Tk().withdraw()
    filePath = filedialog.asksaveasfilename(**kwargs)
    return filePath


def selectdirectorybox(**kwargs):
    '''Creates a select directory dialog box and returns path to the directory
    selected or returns empty if Cancel was selected.
    Example keyword options are "title", "initialdir", and "mustexist".'''
    Tk().withdraw()
    filePath = filedialog.askdirectory(**kwargs)
    return filePath
