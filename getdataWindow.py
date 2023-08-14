from tkinter import *
from tkinter import ttk
from db import *


def getdata_window():
    window = Tk()
    window.title("Получить данные")
    window.geometry("300x250")

    coach = ttk.Button(window, text="Тренеры", command=select_coach)
    student = ttk.Button(window, text="Ученики", command=select_student)
    team = ttk.Button(window, text="Команды", command=select_team)

    coach.pack(anchor=CENTER, fill=X, ipadx=10, ipady=10, pady=[20, 0])
    student.pack(anchor=CENTER, fill=X, ipadx=10, ipady=10, pady=[20, 0])
    team.pack(anchor=CENTER, fill=X, ipadx=10, ipady=10, pady=[20, 0])


def select_coach():
    window = Tk()
    window.title("Тренеры")
    window.geometry("300x250")

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM coach")
    coaches = cursor.fetchall()

    columns = ("id", "fio", "salary", "phone")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1)

    tree.heading("id", text="id")
    tree.heading("fio", text="ФИО")
    tree.heading("salary", text="Зарплата")
    tree.heading("phone", text="Телефон")

    for el in coaches:
        tree.insert("", END, values=el)

    cursor.close()
    connection.close()

def select_student():
    window = Tk()
    window.title("Ученики")
    window.geometry("300x250")

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("select student.id, student.fio, student.avg, team.name from team join student on student.teamid = team.id")
    coaches = cursor.fetchall()

    columns = ("id", "fio", "avg", "teamid")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1)

    tree.heading("id", text="id")
    tree.heading("fio", text="ФИО")
    tree.heading("avg", text="Средний балл")
    tree.heading("teamid", text="Команда")

    for el in coaches:
        tree.insert("", END, values=el)

    cursor.close()
    connection.close()

def select_team():
    window = Tk()
    window.title("Команды")
    window.geometry("300x250")

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("select team.id, team.name, coach.fio from team join coach on coach.CoachId = team.coachId")
    coaches = cursor.fetchall()

    columns = ("id", "name", "fio")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1)

    tree.heading("id", text="id")
    tree.heading("name", text="Название команды")
    tree.heading("fio", text="ФИО")

    for el in coaches:
        tree.insert("", END, values=el)

    cursor.close()
    connection.close()
