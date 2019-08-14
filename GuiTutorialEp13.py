from tkinter import *

base = Tk()
#need canvas to draw on, cant draw directly on frame
canvas = Canvas(base, width=200, height=100)
canvas.pack()
# starts at 0,0 and goes to 200,50
blackLine = canvas.create_line(0, 0, 200, 50) #starts top left
redLine = canvas.create_line(0, 100, 200, 50, fill="red") #starts bottom left
#parameter 1 is where the coordnates of top left of rectangle are
# 130 is the width and 60 is the height
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

# use canvas.delete(redLine) if the user wants to delete the line
# use canva.delete(ALL) to delete all graphics

base.mainloop()