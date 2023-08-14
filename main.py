from getdataWindow import *
from updateWindow import *
from reportWindow import *


def main():
    root = Tk()
    root.title("Основное меню")
    root.geometry("300x250")

    updatesB = ttk.Button(text="Актуализация данных", command=update_window)
    getdataB = ttk.Button(text="Получить данные", command=getdata_window)
    reportB = ttk.Button(text="Сформировать отчет", command=report_window)

    updatesB.pack(anchor=CENTER, fill=X, ipadx=10, ipady=10, pady=[20, 0])
    getdataB.pack(anchor=CENTER, fill=X, ipadx=10, ipady=10, pady=[20, 0])
    reportB.pack(anchor=CENTER, fill=X, ipadx=10, ipady=10, pady=[20, 0])

    root.mainloop()


if __name__ == '__main__':
    main()
