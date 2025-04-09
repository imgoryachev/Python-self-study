import tkinter as tk
import random

# Создаем главное окно
root = tk.Tk()
root.title("Убегающая кнопка")
root.geometry("500x400")

# Функция для перемещения кнопки
def move_button(event=None):
    # Генерируем случайные координаты relx и rely
    new_relx = random.uniform(0.1, 0.9)  # От 10% до 90% ширины окна
    new_rely = random.uniform(0.1, 0.9)  # От 10% до 90% высоты окна
    
    # Перемещаем кнопку
    button.place(relx=new_relx, rely=new_rely, anchor="center")

# Создаем кнопку
button = tk.Button(
    root,
    text="Поймай меня!",
    font=("Arial", 16),
    fg="white",
    bg="red",
    command=lambda: print("Это невозможно! :)")
)

# Размещаем кнопку по центру
button.place(relx=0.5, rely=0.5, anchor="center")

# Привязываем событие <Enter> к функции move_button
button.bind("<Enter>", move_button)

root.mainloop()