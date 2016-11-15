#! python3
#! /usr/bin/python3
#! /usr/bin/env python3

# Copyright (c) 2016 Mark Lotspaih
# MIT License - https://opensource.org/licenses/MIT

# msgBoxPy - Quick import or reference for making simple GUI message boxes.
# USAGE: "import msgBoxPy" or copy the examples below. Two variables, "title"
#   and "message" must be submitted to the function or replaced if the example
#   is copied directly into a script.

from tkinter import Tk
import tkinter.messagebox as box


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
    '''Show Yes/No messagebox GUI and return answer'''
    Tk().withdraw()
    answer = box.askquestion(title, message)
    return answer  # Returns 'yes' or 'no'
