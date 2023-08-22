import psycopg2


db_params = {
    'host': '51.250.68.42',
    'database': 'test',
    'user': 'curator',
    'password': '4oumQk'
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()

def query_ins_user(str x):
    try:
        # Запрос добавления пользователя
        cursor.execute(f"""INSERT into public.Users(TrueUserID, role, isAlive) values ({x}, 0)""")
        cursor.commit()
    except Exception as e:
        print("Ошибка:", e)
    

def query_ins_chat(str x):
    try: # Запрос добавления чата
        cursor.execute(f"""INSERT into public.Chats(TrueChatID, StateID) values ({x}, 0)""")
        cursor.commit()
    except Exception as e:
        print("Ошибка:", e)
    


def query_sel(str x):
    try:
        # Запрос вывода из БД
        cursor.execute("SELECT * FROM chats")
        rows = cursor.fetchall()

        # for row in rows:
        #     print(row)

    except Exception as e:
        print("Ошибка:", e)

def close(cur = cursor, conn = connection):
    cursor.close()
    connection.close()

