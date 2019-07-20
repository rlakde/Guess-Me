import Tkinter
import tkMessageBox

top= Tkinter.Tk()

def helloCallBack():
	tkMessageBox.showinfo("Hello Python","Hello World")

B= Tkinter.Button(top, bg="red",text="hello" ,height=10 ,width=10 , command=helloCallBack)

#B.pack(padx=0, pady=110)
B.pack()
top.mainloop()
