from tkinter import *


def doNothing():
    print("ok ok I won't...")

# ------------ Main Menu ------------- #

base = Tk()

myMenu = Menu(base)
base.config(menu=myMenu)
# .config configures menu for you
# parameter name is menu

subMenu = Menu(myMenu)  # subMenu goes INSIDE of menu
myMenu.add_cascade(label="File", menu=subMenu)  # cascade is a drop down menu
subMenu.add_command(label="New Project...", command=doNothing)  # adds elements to click under the drop down menu
subMenu.add_command(label="New ...", command=doNothing)
subMenu.add_separator()  # just for user to see what menu items are related and what are not
# separator looks like a faint line that separates topics
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(myMenu)
# create another item in main menu
myMenu.add_cascade(label="Edit", menu=editMenu)
# add it as drop down functionality
editMenu.add_command(label="Redo", command=doNothing)

# ***************** Toolbar **************** #

toolbar = Frame(base)
#button(location, text, command)
InsertButt = Button(toolbar, text="Insert Image", command=doNothing)
#padding (pad) adds space between buttons
InsertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)
#.pack() allows things to be displayed
toolbar.pack(side=TOP, fill=X)
#use fill X so that the toolbar is across the top no matter how large you create the window

# //////////////// Status Bar //////////////// #

status = Label(base, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
#bd stands for boarder


base.mainloop()