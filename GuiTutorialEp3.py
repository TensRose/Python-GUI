from tkinter import *

base = Tk()

one = Label(base, text="One", bg="red", fg="white")
one.pack()
two = Label(base, text="Two", bg= "green", fg="black")
two.pack(fill=X) #grows horizontal
#fill=X means that the label is going to grow in size according to how much you stretch out the window
#   (fill widget as wide as the parent is)
three = Label(base, text="Three", bg= "blue", fg="white")
three.pack(side=LEFT,fill=Y) #grows vertical
# bg means background
# fg means foreground aka, font

base.mainloop()