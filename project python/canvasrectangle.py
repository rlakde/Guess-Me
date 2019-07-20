from Tkinter import *

top = Tk()
canvas = Canvas(top, width=300, height=200)
canvas.pack()
canvas.create_rectangle(0,0,150,150, fill ="Yellow")
top.mainloop()
