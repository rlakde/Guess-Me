import sys
from Tkinter import *
import Tkinter as tk
from PIL import Image, ImageTk
def abc():
        root.destroy()
def effect():
        global i,z
        mtext = ment.get()
        i=z
        if mtext.lower()==n[i]:
                print i
                i=i+1
                z=i
                ex(i)
def finish():
        global aaa
        aaa.destroy()
def ex(i):
        global panel1,ss,mEntry
        panel1.destroy()
        print i
        if i==10:
                root.destroy()
                aaa=tk.Tk()
                global aaa
                aaa.geometry('500x500+0+0')
                image5 = ImageTk.PhotoImage(Image.open('winner.gif'))
                panel5 = tk.Label(aaa, image=image5)
                panel5.pack(side='top', fill='both', expand='yes')
                buttonnz=tk.Button(panel5,text='finish',fg='red',bg='yellow',command=finish,width=10,height=1)
                buttonnz.place(x=215,y=430)
                aaa.mainloop()
        else:
            image1 = ImageTk.PhotoImage(Image.open(l[i]))
            panel1 = tk.Label(root, image=image1)
            q = i*100
            ss.set(q)
            mlabel1 = Label(root, textvariable=ss,font=("Helvetica", 12)).place(x=450,y=10)
            panel1.place(x=0,y=40)
            root.mainloop()
root = tk.Tk()
ment = StringVar()
s = StringVar()
ss = StringVar()
ss.set(00)
s.set('Score:')
i,z=0,0
root.title('Guess me??')
l= ["bus.gif","karnafinal.gif","moto.gif","raghufinal.gif","car.gif","da.gif","dada.gif","ubuntu.gif","china.gif","cutting.gif"]
n= ["left","karna","motorola","raghuram rajan","neelam","leonardo da vinci","sourav ganguly","ubuntu","china","north street"]
image1 = ImageTk.PhotoImage(Image.open(l[i]))
root.geometry("500x500+0+0")
panel1 = tk.Label(root, image=image1)
panel1.place(x=0,y=40)
button = tk.Button(root, text='quit',width=8,command = abc)
button.place(x=240,y=450)
mlabel = Label(root, textvariable=s,font=("Helvetica", 12)).place(x=400,y=10)
mlabel2 = Label(root, textvariable=ss,font=("Helvetica", 12)).place(x=450,y=10)
button2 = tk.Button(root, text='submit',width=8,command = effect)
button2.place(x=180,y=450)
mEntry = Entry(root,textvariable=ment,width=15).place(x=195,y=420)
root.mainloop()
