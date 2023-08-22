import psycopg2


db_params = {
    'host': '51.250.68.42',
    'database': 'postgres',
    'user': 'curator',
    'password': '4oumQk'
}


connection = psycopg2.connect(**db_params)  # запускаем один раз


def query_ins_user(tui, curs):
    try:
        # Запрос добавления пользователя
        curs.execute(
            f"""INSERT into public.Users(TrueUserID, role, isAlive) values ({tui}, 0)""")
        connection.commit()
    except Exception as e:
        print("Ошибка:", e)


def query_ins_chat(tci, curs):
    try:  # Запрос добавления чата
        curs.execute(
            f"""INSERT into public.Chats(TrueChatID, StateID) values ({tci}, 0)""")
        connection.commit()
    except Exception as e:
        print("Ошибка:", e)


def query_sel(query, curs):
    try:
        # Запрос вывода из БД
        curs.execute("SELECT * FROM chats")
        rows = curs.fetchall()

        # for row in rows:
        #     print(row)

    except Exception as e:
        print("Ошибка:", e)


def query_change(x):
    # Написать выдачу резов по ролям
    pass


def close(cur):
    cur.close()

