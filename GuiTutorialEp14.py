from tkinter import *

base = Tk()

photo = PhotoImage(file="Beyond.png")
# must assign image to label
label = Label(base, image=photo)
label.pack()

base.mainloop()
