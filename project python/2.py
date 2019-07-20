import sys
from tkinter import *
def ramo():
        ment1=ment.get()
        nlabel=Label(abc,text=ment1).pack()

abc = Tk()
ment = StringVar()
abc.geometry('400x500+200+100')
mlabel = Label(abc,text="My Label",fg='red',bg='yellow').pack()
mbutton = Button(abc,text="OK",command=ramo,fg='black',bg='purple').pack()
mentry = Entry(abc,textvariable=ment).pack()
