from Tkinter import *
import tkMessageBox
import Tkinter

top=Tk()

c1= Checkbutton(top,text="Music",onvalue=1, offvalue=0,height=5, width=20)
c2= Checkbutton(top,text="Video",onvalue=1, offvalue=0,height=5, width=20)

c1.pack()
c2.pack()
top.mainloop()
