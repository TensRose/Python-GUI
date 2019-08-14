from tkinter import *
#import tkinter library

base = Tk()
#created blank window object, thats what base is equal to
theLabel = Label(base, text="This is too easy")
#creates label object with first parameter as the blank window and the 2nd parameter as text
theLabel.pack()
#pack means put the label in the first place you can put it (sort of just throws the label into the
#blank window
base.mainloop()
#GUI app, must have window coninuously on screen until it you decide to close it
#mainloop allows program to coninuously run rather than computer popping up and closing almost instantly