from Tkinter import *

root= Tk()
canvas= Canvas(root,width=300, height=200)
canvas.pack()
canvas.create_oval(50,50,250,150,fill="yellow")
canvas.create_polygon(50,30,150,50,250,30,150,10, fill="green")
canvas.create_line(50,50,250,150,fill="red", width=5)
canvas.create_text(150,100,text="Amazing!", fill="purple", font="Helvetica 26 bold underline")
canvas.create_text(200,50,text="Carpe Diem!", fill="orange", font="Helvetica 16 bold underline")
root.mainloop()
