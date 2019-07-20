import sys
from tkinter import *
root = Tk()
root.title('pylab3')
canvas = Canvas(root,height=300,width=500)
canvas.create_rectangle(60,60,300,300, fill ="black")
canvas.create_rectangle(40,40,250,250, fill ="purple")
canvas.create_rectangle(0,0,150,150, fill ="red")
canvas.pack()
