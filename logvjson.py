import sqlite3
import tkinter as tk
from tkinter import ttk


def filter_data():
    keyword = entry_filter.get().strip()

    tree.delete(*tree.get_children())

    connection = sqlite3.connect("fail.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM logs WHERE ip_address LIKE ?", ('%' + keyword + '%',))
    
    for row in cursor:
        tree.insert("", tk.END, text="", values=row)

    connection.close()


root = tk.Tk()
root.title("Fail Data")
root.geometry("400x400")

frame_filter = tk.Frame(root)
frame_filter.pack(pady=10)

label_filter = tk.Label(frame_filter, text="Filter:")
label_filter.pack(side=tk.LEFT)

entry_filter = tk.Entry(frame_filter)
entry_filter.pack(side=tk.LEFT, padx=5)

button_filter = tk.Button(frame_filter, text="Apply Filter", command=filter_data)
button_filter.pack(side=tk.LEFT)

tree = ttk.Treeview(root)
tree["columns"] = ("ip_address", "request_time", "status_code", "user_agent")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("ip_address", anchor=tk.CENTER, width=120)
tree.column("request_time", anchor=tk.CENTER, width=120)
tree.column("status_code", anchor=tk.CENTER, width=80)
tree.column("user_agent", anchor=tk.CENTER, width=180)

tree.heading("#0", text="")
tree.heading("ip_address", text="IP Address")
tree.heading("request_time", text="Request Time")
tree.heading("status_code", text="Status Code")
tree.heading("user_agent", text="User Agent")

tree.pack(fill=tk.BOTH, expand=True)

connection = sqlite3.connect("fail.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM logs")

for row in cursor:
    tree.insert("", tk.END, text="", values=row)

connection.close()

root.mainloop()