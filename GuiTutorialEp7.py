from tkinter import *
#left click, middle click, right click
base = Tk()

def leftClick(event):
    print("left")

def middleClick(event):
    print("middle")

def rightClick(event):
    print("right")

frame = Frame(base, width=300, height=250)
#adjusts size of window but there is indeed an invisible frame there
frame.bind("<Button-1>", leftClick) #left button
frame.bind("<Button-2>", middleClick) #scroll wheel
frame.bind("<Button-3>", rightClick) #right button
frame.pack()

base.mainloop()