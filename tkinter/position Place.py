from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("title")
root.geometry("250x200")
 
btn = ttk.Button(text="Click me")
#btn.place(x=20, y=30)
#btn.place(relx=0.8, rely=0.8) 
#btn.place(relx=.5, rely=.5, anchor="c", width=80, height=40)
btn.place(relx=0.5, rely=0.5, anchor="c", relwidth=0.33, relheight=0.25)

root.mainloop()