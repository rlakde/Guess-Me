from Tkinter import *

root= Tk()

labelframe= LabelFrame(root,text="This is a Labelframe")
labelframe.pack(fill="both", expand="yes")

left= Label(labelframe,text="Inside the LabelFrame")
left.pack()

root.mainloop()

#also try expand="no" and see
