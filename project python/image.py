from Tkinter import *
from PIL import ImageTk, Image

def effect():
    mtext = ment.get()
    if mtext.lower()=="karna":
        mlabel = Label(panel1,text="Correct")
        mlabel.place(x=265,y=590)
        panel1.destroy()
        mEntry.destroy()
        nlabel = Label(root,text="Correct")
        nlabel.place(x=250,y=450)
    else :
        mlabel = Label(root,text="Wrong")
        mlabel.place(x=265,y=590)
root = Tk()
ment = StringVar()
root.title("Who I am?")
root.geometry('600x620')
img = ImageTk.PhotoImage(Image.open("C:\Users\Dell\Desktop\python\raghufinal.gif"))
panel1 = Label(root, image = img)
panel1.pack(side='top', fill='both', expand='yes')
mEntry = Entry(panel1,textvariable=ment,width=15).place(x=250,y=515)
mbutton = Button(panel1,text="submit",command = effect,width=10,height=1).place(x=265,y=550)
root.mainloop()
