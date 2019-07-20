import Tkinter
import tkMessageBox

top= Tkinter.Tk()

c= Tkinter.Canvas(top, bg="blue", height=250, width=300)

coord= 10,50,240,210
arc=c.create_arc(coord, start=0, extent=150, fill="red")

c.pack(padx=100)
top.mainloop()


