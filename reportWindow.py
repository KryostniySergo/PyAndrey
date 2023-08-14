from tkinter import *
from tkinter import ttk
from db import *

def report_window():
    window = Tk()
    window.title("Сформировать отчет")
    window.geometry("300x250")

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("select fio, salary from coach order by salary desc")
    coaches = cursor.fetchall()

    columns = ("fio", "salary")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1)

    tree.heading("fio", text="ФИО")
    tree.heading("salary", text="Зарплата")

    for el in coaches:
        tree.insert("", END, values=el)

    cursor.close()
    connection.close()