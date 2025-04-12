import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Многострочное текстовое поле с прокруткой")
root.geometry("400x300")

# Создаем многострочное текстовое поле
textbox = tk.Text(root, font=("Arial", 14), width=30, height=5)
textbox.pack(side=tk.LEFT, padx=10, pady=10)

# Создаем полосу прокрутки
scrollbar = tk.Scrollbar(root, command=textbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Привязываем полосу прокрутки к текстовому полю
textbox.config(yscrollcommand=scrollbar.set)

# Добавляем кнопку для получения текста из поля
def get_text():
    content = textbox.get("1.0", tk.END)  # Получаем текст из текстового поля
    print(f"Вы ввели:\n{content}")

button = tk.Button(root, text="Получить текст", font=("Arial", 12), command=get_text)
button.pack(pady=10)

root.mainloop()