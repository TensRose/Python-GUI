from tkinter import *
#binding a function to a widget
base = Tk()

#pass an event as a parameter
#event can be mouse movement, scroll, click etc

def printName():
    print("Hello my name is Joelle!")

#new parameter command allows for the button to perform a task once the button is clicked
button_1=Button(base, text="Print my name", command=printName)
button_1.pack()

base.mainloop()