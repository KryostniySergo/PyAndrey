from tkinter import *
from tkinter import ttk
from db import *
from tkinter.messagebox import showerror, showinfo

def update_window():
    window = Tk()
    window.title("Актуализация данных")
    window.geometry("460x150")

    #Тренер
    coachL = ttk.Label(window, text="Тренеры")
    textbox = ttk.Entry(window)
    addB = ttk.Button(window, text="Добавить", command=coach_blank)
    deletB = ttk.Button(window, text="Удалить", command=lambda: delete("coach", textbox))
    updateB = ttk.Button(window, text="Изменить", command=lambda: coach_blank_update(textbox.get()))

    coachL.grid(row=0, column=0, padx=[20, 0])
    textbox.grid(row=1, column=0, padx=[20, 0])

    addB.grid(row=2, column=0, ipadx=25, padx=[20, 0])
    deletB.grid(row=3, column=0, ipadx=25, padx=[20, 0])
    updateB.grid(row=4, column=0, ipadx=25, padx=[20, 0])
    #-----------------------

    #Студент
    StudentL = ttk.Label(window, text="Ученик")
    textboxS = ttk.Entry(window)
    addBS = ttk.Button(window, text="Добавить", command=student_blank)
    deletBS = ttk.Button(window, text="Удалить", command=lambda: delete("student", textboxS))
    updateBS = ttk.Button(window, text="Изменить", command=lambda: student_blank_update(textboxS.get()))

    StudentL.grid(row=0, column=1, padx=[20, 0])
    textboxS.grid(row=1, column=1, padx=[20, 0])

    addBS.grid(row=2, column=1, ipadx=25, padx=[20, 0])
    deletBS.grid(row=3, column=1, ipadx=25, padx=[20, 0])
    updateBS.grid(row=4, column=1, ipadx=25, padx=[20, 0])
    #---------------------

    #Команда
    teamL = ttk.Label(window, text="Команда")
    textboxT = ttk.Entry(window)
    addBT = ttk.Button(window, text="Добавить", command=team_blank)
    deletBT = ttk.Button(window, text="Удалить", command=lambda: delete("team", textboxT))
    updateBT = ttk.Button(window, text="Изменить", command=lambda: team_blank_update(textboxT.get()))

    teamL.grid(row=0, column=2, padx=[20, 0])
    textboxT.grid(row=1, column=2, padx=[20, 0])

    addBT.grid(row=2, column=2, ipadx=25, padx=[20, 0])
    deletBT.grid(row=3, column=2, ipadx=25, padx=[20, 0])
    updateBT.grid(row=4, column=2, ipadx=25, padx=[20, 0])


    # newb = ttk.Button(window, text="Dest", command=window.destroy)
    # newb.pack(anchor=CENTER, expand=1)
    #
    # window.bind("<Destroy>", dest)

def delete(dbname, textbox):
    connection = create_connection()
    if dbname == "coach":
        execute_query(connection, f"DELETE FROM {dbname} WHERE coachid = {textbox.get()}")
    else:
        execute_query(connection, f"DELETE FROM {dbname} WHERE id = {textbox.get()}")
    showinfo(title="Уведомление", message="Данные успешно удалены")
    connection.close()

def coach_blank():
    window = Tk()
    window.title("Актуализация данных")
    window.geometry("175x150")

    fioL = ttk.Label(window, text="ФИО")
    fio = ttk.Entry(window)
    salaryL = ttk.Label(window, text="Зарплата")
    salary = ttk.Entry(window)
    phoneL = ttk.Label(window, text="Телефон")
    phone = ttk.Entry(window)
    button = ttk.Button(window, text="Добавить", command=lambda: add_coach(fio.get(), salary.get(), phone.get()))

    fioL.grid(row=0, column=0, padx=[20, 0])
    fio.grid(row=1, column=0, padx=[20, 0])
    salaryL.grid(row=2, column=0, padx=[20, 0])
    salary.grid(row=3, column=0, padx=[20, 0])
    phoneL.grid(row=4, column=0, padx=[20, 0])
    phone.grid(row=5, column=0, padx=[20, 0])
    button.grid(row=6, column=0, padx=[20, 0])

def add_coach(fio, salary, phone):
    conn = create_connection()
    cursor = conn.cursor()
    coach = (fio, salary, phone)
    try:
        cursor.execute("INSERT INTO Coach (fio, salary, phone) VALUES (%s, %s, %s)", coach)
        conn.commit()
        showinfo(title="Уведомление", message="Тренер успешно добавлен")
    except Exception as e:
        showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
        print(e)
    cursor.close()
    conn.close()

def student_blank():
    window = Tk()
    window.title("Актуализация данных")
    window.geometry("175x150")

    fioL = ttk.Label(window, text="ФИО")
    fio = ttk.Entry(window)
    avgL = ttk.Label(window, text="Средний балл")
    avg = ttk.Entry(window)
    teamidL = ttk.Label(window, text="Id команды")
    teamid = ttk.Entry(window)
    button = ttk.Button(window, text="Добавить", command=lambda: add_student(fio.get(), avg.get(), teamid.get()))

    fioL.grid(row=0, column=0, padx=[20, 0])
    fio.grid(row=1, column=0, padx=[20, 0])
    avgL.grid(row=2, column=0, padx=[20, 0])
    avg.grid(row=3, column=0, padx=[20, 0])
    teamidL.grid(row=4, column=0, padx=[20, 0])
    teamid.grid(row=5, column=0, padx=[20, 0])
    button.grid(row=6, column=0, padx=[20, 0])

def add_student(fio, avg, teamid):
    conn = create_connection()
    cursor = conn.cursor()
    student = (fio, avg, teamid)
    try:
        cursor.execute("INSERT INTO student (fio, avg, teamid) VALUES (%s, %s, %s)", student)
        conn.commit()
        showinfo(title="Уведомление", message="Ученик успешно добавлен")
    except Exception as e:
        showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
        print(e)
    cursor.close()
    conn.close()

def team_blank():
    window = Tk()
    window.title("Актуализация данных")
    window.geometry("175x120")

    nameL = ttk.Label(window, text="Название команды")
    name = ttk.Entry(window)

    coachidL = ttk.Label(window, text="Id тренера")
    coachid = ttk.Entry(window)
    button = ttk.Button(window, text="Добавить", command=lambda: add_team(name.get(), coachid.get()))

    nameL.grid(row=0, column=0, padx=[20, 0])
    name.grid(row=1, column=0, padx=[20, 0])
    coachidL.grid(row=2, column=0, padx=[20, 0])
    coachid.grid(row=3, column=0, padx=[20, 0])
    button.grid(row=6, column=0, padx=[20, 0])

def add_team(name, coachid):
    conn = create_connection()
    cursor = conn.cursor()
    team = (name, coachid)
    try:
        cursor.execute("INSERT INTO team (name, coachid) VALUES (%s, %s)", team)
        conn.commit()
        showinfo(title="Уведомление", message="Команда успешно добавлена")
    except Exception as e:
        showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
        print(e)
    cursor.close()
    conn.close()


def coach_blank_update(textbox):
    window = Tk()
    window.title("Актуализация данных")
    window.geometry("175x150")

    fioL = ttk.Label(window, text="ФИО")
    fio = ttk.Entry(window)
    salaryL = ttk.Label(window, text="Зарплата")
    salary = ttk.Entry(window)
    phoneL = ttk.Label(window, text="Телефон")
    phone = ttk.Entry(window)
    button = ttk.Button(window, text="Изменить", command=lambda: update_coach(fio.get(), salary.get(), phone.get(), textbox))

    fioL.grid(row=0, column=0, padx=[20, 0])
    fio.grid(row=1, column=0, padx=[20, 0])
    salaryL.grid(row=2, column=0, padx=[20, 0])
    salary.grid(row=3, column=0, padx=[20, 0])
    phoneL.grid(row=4, column=0, padx=[20, 0])
    phone.grid(row=5, column=0, padx=[20, 0])
    button.grid(row=6, column=0, padx=[20, 0])

def update_coach(fio, salary, phone, textbox):
    conn = create_connection()
    cursor = conn.cursor()

    if fio:
        try:
            cursor.execute("UPDATE coach SET fio =%s WHERE coachid=%s", (fio, textbox))
            conn.commit()
            showinfo(title="Уведомление", message="Данные изменены")
        except Exception as e:
            showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
            print(e)
        cursor.close()
        conn.close()
        return
    if salary:
        try:
            cursor.execute("UPDATE coach SET salary =%s WHERE coachid=%s", (salary, textbox))
            conn.commit()
            showinfo(title="Уведомление", message="Данные изменены")
        except Exception as e:
            showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
            print(e)
        cursor.close()
        conn.close()
        return
    if phone:
        try:
            cursor.execute("UPDATE coach SET phone =%s WHERE coachid=%s", (phone, textbox))
            conn.commit()
            showinfo(title="Уведомление", message="Данные изменены")
        except Exception as e:
            showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
            print(e)
        cursor.close()
        conn.close()
        return

def team_blank_update(textbox):
    window = Tk()
    window.title("Актуализация данных")
    window.geometry("175x120")

    nameL = ttk.Label(window, text="Название команды")
    name = ttk.Entry(window)

    coachidL = ttk.Label(window, text="Id тренера")
    coachid = ttk.Entry(window)
    button = ttk.Button(window, text="Изменить", command=lambda: update_team(name.get(), coachid.get(), textbox))

    nameL.grid(row=0, column=0, padx=[20, 0])
    name.grid(row=1, column=0, padx=[20, 0])
    coachidL.grid(row=2, column=0, padx=[20, 0])
    coachid.grid(row=3, column=0, padx=[20, 0])
    button.grid(row=6, column=0, padx=[20, 0])

def update_team(name, coachid, textbox):
    conn = create_connection()
    cursor = conn.cursor()

    if name:
        try:
            cursor.execute("UPDATE team SET name =%s WHERE id=%s", (name, textbox))
            conn.commit()
            showinfo(title="Уведомление", message="Данные изменены")
        except Exception as e:
            showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
            print(e)
        cursor.close()
        conn.close()
        return
    if coachid:
        try:
            cursor.execute("UPDATE team SET coachid =%s WHERE id=%s", (coachid, textbox))
            conn.commit()
            showinfo(title="Уведомление", message="Данные изменены")
        except Exception as e:
            showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
            print(e)
        cursor.close()
        conn.close()
        return

def student_blank_update(textbox):
    window = Tk()
    window.title("Актуализация данных")
    window.geometry("175x150")

    fioL = ttk.Label(window, text="ФИО")
    fio = ttk.Entry(window)
    avgL = ttk.Label(window, text="Средний балл")
    avg = ttk.Entry(window)
    teamidL = ttk.Label(window, text="Id команды")
    teamid = ttk.Entry(window)
    button = ttk.Button(window, text="Изменить", command=lambda: update_student(fio.get(), avg.get(), teamid.get(), textbox))

    fioL.grid(row=0, column=0, padx=[20, 0])
    fio.grid(row=1, column=0, padx=[20, 0])
    avgL.grid(row=2, column=0, padx=[20, 0])
    avg.grid(row=3, column=0, padx=[20, 0])
    teamidL.grid(row=4, column=0, padx=[20, 0])
    teamid.grid(row=5, column=0, padx=[20, 0])
    button.grid(row=6, column=0, padx=[20, 0])

def update_student(fio, avg, teamid, textbox):
    conn = create_connection()
    cursor = conn.cursor()

    if fio:
        try:
            cursor.execute("UPDATE student SET fio =%s WHERE id=%s", (fio, textbox))
            conn.commit()
            showinfo(title="Уведомление", message="Данные изменены")
        except Exception as e:
            showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
            print(e)
        cursor.close()
        conn.close()
        return
    if avg:
        try:
            cursor.execute("UPDATE student SET avg =%s WHERE id=%s", (avg, textbox))
            conn.commit()
            showinfo(title="Уведомление", message="Данные изменены")
        except Exception as e:
            showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
            print(e)
        cursor.close()
        conn.close()
        return
    if teamid:
        try:
            cursor.execute("UPDATE student SET teamid =%s WHERE id=%s", (teamid, textbox))
            conn.commit()
            showinfo(title="Уведомление", message="Данные изменены")
        except Exception as e:
            showerror(title="Ошибка", message="Вы ввели неверные данные ил вовсе оставили поля пустыми")
            print(e)
        cursor.close()
        conn.close()
        return