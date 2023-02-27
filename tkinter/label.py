from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Title")
root.geometry("550x400")

logo = PhotoImage(file="any.png")

label = ttk.Label(image=logo, text="LOGO", compound="top")
#label = ttk.Label(text="Hello Tkinter", background="#FFCDD2", foreground="#B71C1C", padding=8)
#label = ttk.Label(text="Hello Tkinter", borderwidth=2, relief="ridge", padding=8)
#label = ttk.Label(text="Hello World", font=("Arial", 14))
label.pack()

root.mainloop()