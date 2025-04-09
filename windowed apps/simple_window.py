import tkinter as tk
from screeninfo import get_monitors
import random

# Create main window
root = tk.Tk()
root.title("Title Name")

# Get info about all monitors and find main monitor
monitors = get_monitors()

primary_monitor = None
for monitor in monitors:
    if monitor.is_primary:
        primary_monitor = monitor
        break

if primary_monitor is None:
    raise Exception("Main monitor not found")

# Get display resolution
screen_width = primary_monitor.width
screen_height = primary_monitor.height

# Set window size as half of display
window_widht = int(screen_width * 0.5)
window_height = int(screen_height * 0.5)

# Set start position
x_position = (screen_width - window_widht) // 2
y_position = (screen_height - window_height) // 2

# Set size and position
root.geometry(f"{window_widht}x{window_height}+{x_position}+{y_position}")

# Prohibit to change window size
root.resizable(True, True)

# Find font button size relatively display resolution
font_size = int(screen_height * 0.0075)

# Add buttons function
def on_button_click():
    print('Button has been pressed')

def close_window():
    root.destroy()

# Add buttons
button = tk.Button(
    root,
    text="Нажми меня",
    font=("Arial", font_size, "bold"),  # Шрифт и размер текста
    fg="black",                         # Цвет текста
    bg="white",                         # Цвет фона кнопки
    activeforeground="yellow",          # Цвет текста при наведении
    activebackground="green",           # Цвет фона при наведении
    borderwidth=3,                      # Толщина рамки
    relief="raised"                     # Стиль рамки (raised, flat, sunken и т.д.)
)
button.pack(pady=10)

button2 = tk.Button(
    root, 
    text="Закрыть", 
    command=close_window,
    font=(font_size)
)
button2.place(relx=0.9, rely=0.9, relwidth=0.1, relheight=0.05, anchor="center")

# Add dodging button
def move_button(event=None):
    new_relx = random.uniform(0.1, 0.9)
    new_rely = random.uniform(0.1, 0.9)
    dodge_button.place(relx=new_relx, rely=new_rely, relwidth=0.2, relheight=0.1, anchor="center")

dodge_button = tk.Button(
    root,
    text="Catch me!",
    command=lambda: print("THATS IMPOSSIBLE!"),
    font=(font_size)
)
dodge_button.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor="center")
dodge_button.bind("<Enter>", move_button)

# Create lable
label = tk.Label(root, text=font_size)
label1 = tk.Label(root, text=window_widht)
label.pack()
label1.pack()

# Run window
root.mainloop()