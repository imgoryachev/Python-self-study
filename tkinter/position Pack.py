from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("Title")
root.geometry("250x200")
 
btn = ttk.Button(text="Click me")
# expand
#btn.pack(expand=True)
#btn.pack(expand=True, ipadx=10, ipady=10)
# anchor
#btn.pack(anchor=N)
# fill
#btn.pack(fill=X)
# indent
#btn.pack(anchor=NW, padx=20, pady=30)
# btn.pack(fill=X, padx=20, pady=30)

btn1 = ttk.Button(text="BOTTOM")
btn1.pack(side=BOTTOM)
 
btn2 = ttk.Button(text="RIGHT")
btn2.pack(side=RIGHT)
 
btn3 = ttk.Button(text="LEFT")
btn3.pack(side=LEFT)
 
btn4 = ttk.Button(text="TOP")
btn4.pack(side=TOP)
root.mainloop()