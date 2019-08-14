from tkinter import *

base = Tk() #start of main body
#Creating frame objects
#frame = invisible rectangle/container you can put things in
topFrame = Frame(base) #making an invisible container and its gonna go in the main window base
topFrame.pack() #.pack() = place somewhere in main frame
bottomFrame = Frame(base)
bottomFrame.pack(side=BOTTOM) #can put parameter telling exactly where you want the frame to be "packed" into the window

#Creating button objects
#button objects contain various parameters:  1st where, 2nd what you want to show up on button, 3rd colour
# 'fg' means foreground, therefore the colour of the text on the button will be red, not the actual button
button1 = Button(topFrame, text= "Button 1", fg="red")
button2 = Button(topFrame, text= "Button 2", fg="blue")
button3 = Button(topFrame, text= "Button 3", fg="green")
button4 = Button(bottomFrame, text= "Button 4", fg="purple")

#need pack statement to display the buttons on the frame (without the pack statement the buttons wont show up
button1.pack(side=LEFT)
#side=LEFT in the .pack() tells the computer that when it is packing, place the button as far left as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
#buttons will be aligned in a row now instead of being stacked when the .pack() parameter was blank
button4.pack()
#play around with positions of side=______ to find different layouts!
base.mainloop() #end of main body