import tkinter as tk


def add_task():
    task = ttextbox.get()
    if task:
        listbox.insert(tk.END, task)
        ttextbox.delete(0, tk.END)


def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)


def clear_list():
    listbox.delete(0, tk.END)


root = tk.Tk()
root.title("TODO-лист")
root.geometry("700x500")




ttextbox = tk.Entry(root, width=30)
ttextbox.pack(pady=5)


add_button = tk.Button(root, text="Добавить", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)


delete_button = tk.Button(root, text="Удалить", command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Очистить всё", command=clear_list)
clear_button.pack(pady=5)


root.mainloop()
