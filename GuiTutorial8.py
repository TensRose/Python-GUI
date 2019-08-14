from tkinter import *


# using classes


class JoellesButtons:
    # creating objects within the class
    # init stands for initialize, function will occur when you create something
    # master means base, root, or main window
    # pass base data as "master" parameter
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow this actually worked!")


base = Tk()
# created class JoellesButtons and created "master" as a parameter so we are passing base,
# the window, as a parameter
b = JoellesButtons(base)
base.mainloop()
