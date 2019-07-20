import sys
from tkinter import *
def funct():
    mlabel = Label(text='u just entered Ok',fg='purple').pack()
abc = Tk()
abc.title('pylab1')
abc.geometry('500x300+50+50')
mbutton = Button(text='ok',command=funct,fg='red',bg='yellow').pack()
