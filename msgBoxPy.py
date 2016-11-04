#! python3
#! /usr/bin/python3
#! /usr/bin/env python3

# Copyright (c) 2016 Mark Lotspaih
# MIT License - https://opensource.org/licenses/MIT

# msgBoxPy - Quick import or reference for making simple GUI message boxes.
# USAGE: "import msgBoxPy" or copy the examples below. Two variables, "title"
#   and "message" must be submitted to the funtion or replaced if the example
#   is copied directly into a script.

from tkinter import *
import tkinter.messagebox as box


def infobox(title='Title', message='Empty'):
    Tk().withdraw()
    box.showinfo(title, message)


def warningbox(title='Title', message='Empty'):
    Tk().withdraw()
    box.showwarning(title, message)


def errorbox(title='Title', message='Empty'):
    Tk().withdraw()
    box.showerror(title, message)


def yesnobox(title='Title', message='Empty'):
    Tk().withdraw()
    answer = box.askquestion(title, message)
    return answer  # Returns 'yes' or 'no'
