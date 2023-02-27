from tkinter import *

def finish():
    root.destroy()
    print("CLose app")

root = Tk()
root.title('Application')
root.geometry("300x250")

label = Label(text="Hello World")
label.pack()

root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()