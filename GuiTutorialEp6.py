from tkinter import *
#binding a function to a widget, using events
base = Tk()

#pass an event as a parameter
#event can be mouse movement, scroll, click etc

def printName(event):
    print("Hello my name is Joelle!")

button_1 = Button(base, text="Print my name")
#"<Button-1>" is the name for left click event
button_1.bind("<Button-1>", printName)
button_1.pack()

base.mainloop()