from tkinter import *

# Добавление при нажатии Enter
def add_to_list(event):
    text = entry.get()
    if text:
        listbox.insert(END, text)
        entry.delete(0, END)

#Копирование
def copy(event):
    selected_item_index = listbox.curselection()
    if selected_item_index:
        text = listbox.get(selected_item_index)
        entry.delete(0, END)
        entry.insert(0, text)

root = Tk()
root.title("Tinker 7")

#Однострочное текстовое поле
entry = Entry(root, width=40)
entry.pack(padx=10, pady=10)


entry.bind('<Return>', add_to_list)

# Listbox
listbox = Listbox(root, width=40, height=10)
listbox.pack(padx=10, pady=10)

# Копирование при двойном клике
listbox.bind('<Double-Button-1>', copy)

root.mainloop()
