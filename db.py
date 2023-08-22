import psycopg2


db_params = {
    'host': '51.250.68.42',
    'database': 'postgres',
    'user': 'curator',
    'password': '4oumQk'
}


try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Ваш код выполнения запросов

    cursor.execute(f"Select role from chats join userschats uc on uc.chatid = "
                f"chats.chatid join users on users.userid = uc.userid where truechatid = '{7656}' and isAlive = true")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()

except Exception as e:
    print("Ошибка:", e)
