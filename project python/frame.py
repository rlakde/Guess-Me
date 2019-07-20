from Tkinter import *

root=Tk()
frame= Frame(root)
frame.pack()

bottomframe= Frame(root)
bottomframe.pack(side= BOTTOM)

redbutton= Button(frame,text="Red", fg="red")
redbutton.pack(side= RIGHT)

brownbutton= Button(frame,text="Brown", fg="Brown")
brownbutton.pack(side= LEFT)


bluebutton= Button(frame,text="Blue", fg="Blue")
bluebutton.pack(side= LEFT)

blackbutton= Button(bottomframe,text="Black", fg="Black")
blackbutton.pack(side= BOTTOM)
root.mainloop()

#change side and see

