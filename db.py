import psycopg2


def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="12345", host="127.0.0.1", port="5432")
        print("Подключение установлено")
    except Exception as e:
        print(f"Обнаружена ошибка: {e}")

    return conn


def delete_connection(connection):
    connection.close()


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Query {query} executed")
    except Exception as e:
        print(f"Обнаружена ошибка: {e}")


def create_tables(connection):

    execute_query(connection, """
       CREATE TABLE IF NOT EXISTS Coach (
           CoachId SERIAL PRIMARY KEY,
           fio VARCHAR(50),
           salary INTEGER,
           phone VARCHAR(50))
       """)

    execute_query(connection, """
        CREATE TABLE IF NOT EXISTS Team (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            CoachId INTEGER unique references Coach(CoachId) ON DELETE CASCADE
            )
        """)

    execute_query(connection, """
    CREATE TABLE IF NOT EXISTS Student (
        id SERIAL PRIMARY KEY,
        fio VARCHAR(50),
        avg NUMERIC,
        TeamId INTEGER REFERENCES Team(Id) ON DELETE CASCADE
        )
    """)

def createData(connection):
    cursor = connection.cursor()
    coaches = [("Зыков Овидий Дамирович", 20000, "79372182120"),
               ("Лапин Арсен Митрофанович", 25000, "79372193064"),
               ("Щербаков Евгений Ярославович", 20000, "79377819686"),
               ("Миронов Гордей Лукьевич", 30000, "79371941585")]
    cursor.executemany("INSERT INTO Coach (fio, salary, phone) VALUES (%s, %s, %s)", coaches)

    teams = [("Палладий", 1), ("Каракал", 3), ("Лисица", 2), ("Гепард", 4)]
    cursor.executemany("INSERT INTO Team (name, CoachId) VALUES (%s, %s)", teams)

    students = [("Зимин Исак Дмитриевич", 3.5, 2),
                ("Шубин Варлам Филиппович", 4.3, 2),
                ("Алексеев Власий Владленович", 3.3, 3),
                ("Журавлёв Власий Мэлсович", 3.1, 3),
                ("Белозёров Ибрагил Робертович", 4.4, 4),
                ("Дроздов Панкратий Степанович", 4.6, 4),
                ("Сазонов Осип Эдуардович", 4.8, 1),
                ("Пономарёв Терентий Михаилович", 3.8, 1)]
    cursor.executemany("INSERT INTO Student (fio, avg, TeamId) VALUES (%s, %s, %s)", students)

    connection.commit()