from tkinter import *
from tkinter import ttk

clicks = 0
def click_button():
    global clicks
    clicks += 1
    btn["text"] = f"{clicks}"

root = Tk()
root.title("Title")
root.geometry("250x150")

btn = ttk.Button(text="Click Me", command=click_button)
btn1 = ttk.Button(text="haha cant press", state=["disabled"])
btn.pack()
btn1.pack()

root.mainloop()