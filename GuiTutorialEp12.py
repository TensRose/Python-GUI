from tkinter import *
import tkinter.messagebox
#you have to import messagebox because it is a submodule and submodules arent automatically imported

base = Tk()

#first parameter allows you to change window title
tkinter.messagebox.showinfo("Joelle's Program", "Soy un ouevo")

answer = tkinter.messagebox.askquestion("Question 1", "Do you like chili flakes?")

if answer == "yes":
    print("You added 20 chili flakes to your inventory!")

base.mainloop()