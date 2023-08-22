import psycopg2


db_params = {
    'host': '51.250.68.42',
    'database': 'test',
    'user': 'curator',
    'password': '4oumQk'
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()

def query_ins_user(str x, curs = cursor):
    try:
        # Запрос добавления пользователя
        curs.execute(f"""INSERT into public.Users(TrueUserID, role, isAlive) values ({x}, 0)""")
        curs.commit()
    except Exception as e:
        print("Ошибка:", e)
    

def query_ins_chat(str x, curs = cursor):
    try: # Запрос добавления чата
        curs.execute(f"""INSERT into public.Chats(TrueChatID, StateID) values ({x}, 0)""")
        curs.commit()
    except Exception as e:
        print("Ошибка:", e)
    


def query_sel(str x, curs = cursor):
    try:
        # Запрос вывода из БД
        curs.execute("SELECT * FROM chats")
        rows = curs.fetchall()

        # for row in rows:
        #     print(row)

    except Exception as e:
        print("Ошибка:", e)

def query_change(str x):
    # Написать выдачу резов по ролям
    


def close(cur = cursor, conn = connection):
    cursor.close()
    connection.close()

