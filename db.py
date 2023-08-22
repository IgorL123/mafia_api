import psycopg2


db_params = {
    'host': '51.250.68.42',
    'database': 'test',
    'user': 'curator',
    'password': '4oumQk'
}


try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Ваш код выполнения запросов

    cursor.execute("SELECT * FROM chats")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()

except Exception as e:
    print("Ошибка:", e)