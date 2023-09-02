import psycopg2
from config import db_params
# TODO: убрать обработку ошибок отсюда и перенести в app.py

connection = psycopg2.connect(**db_params)  # запускаем один раз


# TODO: убрать говнокод и написать нормальный запрос
# TODO: научиться формировать запросы сразу на список пользователей, так будет быстрее
def user_add(tui, tci, curs):
    try:
        curs.execute(
            f"""SELECT ChatID FROM Chats WHERE TrueChatId='{tci}'"""
        )
        chat_id = curs.fetchone()[0]
        curs.execute(
            f"""INSERT into public.Users(TrueUserID, role, isAlive) values ({tui}, 0, false) RETURNING UserID"""
        )
        user_id = curs.fetchone()[0]
        connection.commit()
        curs.execute(
            f"""INSERT into public.UsersChats(UserID, ChatID) values ({user_id}, {chat_id})"""
        )
    except Exception as e:
        print("Ошибка:", e)


def chat_add(tci, curs):
    try:
        curs.execute(
            f"""INSERT into public.Chats(TrueChatID, StateID) values ({tci}, 0)""")
        connection.commit()
    except Exception as e:
        print("Ошибка:", e)


def close(cur):
    cur.close()
