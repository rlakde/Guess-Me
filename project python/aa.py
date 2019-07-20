import sys
from Tkinter import *
import Tkinter as tk
from PIL import Image, ImageTk

def start():
        aa.destroy()
        import imgg.py

aa=tk.Tk()
aa.geometry('500x500+0+0')
image2 = ImageTk.PhotoImage(Image.open('title.gif'))
panel3 = tk.Label(aa, image=image2)
panel3.pack(side='top', fill='both', expand='yes')
buttonn=tk.Button(panel3,text='start',fg='red',bg='yellow',command=start,width=10,height=1)
buttonn.place(x=215,y=430)
aa.mainloop()
