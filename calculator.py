from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("python calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font=('arial',35,'bold'))
screen.pack(fill=X, ipadx=8,pady=10)

f = Frame(root,bg='blue')
b = Button(f, text="9",padx=25,pady=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=12)


b = Button(f, text="8",padx=25,pady=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=12)


b = Button(f, text="7",padx=25,pady=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=10,pady=12)


#b = Button(f, text="+",padx=25,pady=22,font="lucida 35 bold")
#b.pack(side=LEFT,padx=10,pady=12)

               
root.mainloop()