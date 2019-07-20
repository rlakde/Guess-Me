import sys
from tkinter import *
root = Tk()
root.title('pylab4')
canvas = Canvas(root,height=300,width=500)
canvas.create_oval(50,50,250,150, fill ="Yellow")
canvas.create_oval(200,70,270,290, fill ="black")
canvas.create_oval(100,50,150,250, fill ="purple")
canvas.pack()
