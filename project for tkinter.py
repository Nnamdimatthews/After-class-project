from tkinter import *

window = Tk()

def hanle_keypress(event):
    """print the character associated to the key pressed"""
    print(event.char)

window.bind("<key>")

window.mainloop