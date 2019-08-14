from tkinter import *

base = Tk()

label_1 = Label(base, text="Name:")
label_2 = Label(base, text="Password:")
#must create an "entry" for user to input data
#Entry() creates space for user to type in data
entry_1 = Entry(base)
entry_2 = Entry(base)
#.grid allows for rows and columns rather than using pack
# sticky parameter allows the label to be "attached"
# to the entry point (allows name to be right aligned instead of centred)
# sticky uses values N,E,S, and W for north east south and west
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
#label 2 will be right under label 1

# we want the entry inputs to the right of the labels
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

#adding a widget that takes up two columns
#Checkbutton gives the box you can check or uncheck
c = Checkbutton(base, text="Keep Me Signed In")
c.grid(columnspan=2) #allows text to span over two cells

base.mainloop()